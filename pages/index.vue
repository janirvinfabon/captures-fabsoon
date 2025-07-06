<template>
  <div class="min-h-screen relative">
    <!-- Video Background -->
    <video
      v-if="!showCamera"
      autoplay
      muted
      loop
      playsinline
      preload="auto"
      class="video-background"
    >
      <source src="/wedding-background.mp4" type="video/mp4">
    </video>
    
    <!-- Landing Page -->
    <div v-if="!showCamera" class="flex flex-col items-center justify-center min-h-screen text-black text-center p-4">
      <h1 class="text-4xl md:text-6xl font-bold mb-4">Fabsoon Captures</h1>
      <p class="text-lg md:text-xl mb-8">Create your wedding souvenir</p>
      <button
        @click="openCamera"
        class="bg-orange-500 hover:bg-orange-600 text-black font-bold py-3 px-6 rounded-lg text-lg"
      >
        Open Camera
      </button>
    </div>

    <!-- Camera View -->
    <div v-if="showCamera" class="min-h-screen bg-black">
      <div class="p-4">
        <button
          @click="closeCamera"
          class="text-white mb-4"
        >
          ← Back
        </button>
      </div>
      
      <div class="relative flex justify-center">
        <video
          ref="videoElement"
          autoplay
          playsinline
          class="max-w-full h-auto"
        ></video>
        <canvas
          ref="canvasElement"
          class="overlay-canvas"
        ></canvas>
      </div>
      
      <div class="text-center p-4">
        <button
          @click="capturePhoto"
          class="bg-red-500 hover:bg-red-600 text-white font-bold py-3 px-6 rounded-full text-lg"
        >
          📷 Capture
        </button>
      </div>
    </div>

    <!-- Background Selection -->
    <div v-if="capturedImage" class="min-h-screen bg-gray-100 p-4">
      <div class="max-w-4xl mx-auto">
        <h2 class="text-2xl font-bold text-center mb-6">Choose Your Wedding Background</h2>
        
        <div class="relative mb-6">
          <canvas
            ref="previewCanvas"
            class="w-full max-w-md mx-auto border rounded-lg"
          ></canvas>
        </div>
        
        <div class="grid grid-cols-2 md:grid-cols-4 gap-4 mb-6">
          <div
            v-for="(bg, index) in weddingBackgrounds"
            :key="index"
            @click="selectBackground(bg)"
            class="cursor-pointer border-2 rounded-lg overflow-hidden"
            :class="selectedBackground === bg ? 'border-pink-500' : 'border-gray-300'"
          >
            <img 
              :src="bg" 
              :alt="`Background ${index + 1}`" 
              class="w-full h-20 min-h-20 object-cover"
              @error="handleImageError($event, index)"
              @load="handleImageLoad(index)"
            >
          </div>
        </div>
        
        <div class="text-center space-x-4">
          <button
            @click="retakePhoto"
            class="bg-gray-500 hover:bg-gray-600 text-white font-bold py-3 px-6 rounded-lg text-lg"
          >
            📷 Retake
          </button>
          <button
            @click="uploadFinalImage"
            :disabled="uploading"
            class="bg-green-500 hover:bg-green-600 disabled:bg-gray-400 text-white font-bold py-3 px-6 rounded-lg text-lg"
          >
            {{ uploading ? 'Uploading...' : '✨ Create Souvenir' }}
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
const showCamera = ref(false)
const capturedImage = ref(null)
const selectedBackground = ref(null)
const uploading = ref(false)

const videoElement = ref(null)
const canvasElement = ref(null)
const previewCanvas = ref(null)

const weddingBackgrounds = [
  '/backgrounds/wedding-bg-1.jpg',
  '/backgrounds/wedding-bg-2.jpg',
  '/backgrounds/wedding-bg-3.jpg',
  '/backgrounds/wedding-bg-4.jpg'
]

const { $config } = useNuxtApp()

const openCamera = async () => {
  showCamera.value = true
  await nextTick()
  
  try {
    const stream = await navigator.mediaDevices.getUserMedia({ 
      video: { facingMode: 'user' } 
    })
    videoElement.value.srcObject = stream
  } catch (error) {
    console.error('Camera access denied:', error)
    alert('Camera access is required for this feature')
    closeCamera()
  }
}

const closeCamera = () => {
  if (videoElement.value?.srcObject) {
    videoElement.value.srcObject.getTracks().forEach(track => track.stop())
  }
  showCamera.value = false
}

const capturePhoto = async () => {
  const video = videoElement.value
  const canvas = canvasElement.value
  const ctx = canvas.getContext('2d')
  
  canvas.width = video.videoWidth
  canvas.height = video.videoHeight
  ctx.drawImage(video, 0, 0)
  
  capturedImage.value = canvas.toDataURL('image/jpeg', 0.8)
  closeCamera()
  selectedBackground.value = weddingBackgrounds[0]
  updatePreview()
  
  // Auto scroll to background selection
  await nextTick()
  window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' })
}

const selectBackground = (background) => {
  selectedBackground.value = background
  updatePreview()
}

const updatePreview = async () => {
  await nextTick()
  if (!previewCanvas.value || !capturedImage.value || !selectedBackground.value) {
    return
  }
  
  const canvas = previewCanvas.value
  const ctx = canvas.getContext('2d')
  
  canvas.width = 400
  canvas.height = 600
  
  // Load background
  const bgImg = new Image()
  bgImg.crossOrigin = 'anonymous'
  bgImg.onload = () => {
    console.log('Background loaded, drawing...')
    ctx.drawImage(bgImg, 0, 0, canvas.width, canvas.height)
    
    // Load captured image
    const userImg = new Image()
    userImg.onload = () => {
      console.log('User image loaded, compositing...')
      const size = Math.min(canvas.width * 0.6, canvas.height * 0.4)
      const x = (canvas.width - size) / 2
      const y = canvas.height * 0.1
      ctx.drawImage(userImg, x, y, size, size)
      console.log('Preview updated successfully')
    }
    userImg.onerror = (e) => console.error('User image load error:', e)
    userImg.src = capturedImage.value
  }
  bgImg.onerror = (e) => console.error('Background image load error:', e)
  bgImg.src = selectedBackground.value
}

const handleImageError = (event, index) => {
  console.error(`Background image ${index + 1} failed to load:`, event.target.src)
}

const handleImageLoad = (index) => {
  console.log(`Background image ${index + 1} loaded successfully`)
}

const retakePhoto = () => {
  capturedImage.value = null
  selectedBackground.value = null
  openCamera()
}

const uploadFinalImage = async () => {
  uploading.value = true
  
  try {
    const finalImageData = previewCanvas.value.toDataURL('image/jpeg', 0.9)
    
    const response = await $fetch(`${$config.public.apiBaseUrl}/upload`, {
      method: 'POST',
      body: {
        image: finalImageData,
        timestamp: new Date().toISOString()
      }
    })
    
    alert('Your wedding souvenir has been created successfully! 🎉')
    
    // Reset
    capturedImage.value = null
    selectedBackground.value = null
    
  } catch (error) {
    console.error('Upload failed:', error)
    alert('Upload failed. Please try again.')
  } finally {
    uploading.value = false
  }
}
</script>

<style scoped>
.video-background {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  z-index: -1;
}

.overlay-canvas {
  position: absolute;
  top: 0;
  left: 0;
  pointer-events: none;
}
</style>