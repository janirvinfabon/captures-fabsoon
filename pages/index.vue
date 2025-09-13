<template>
  <div class="min-h-screen bg-gradient-to-b from-amber-50 to-white">
    <!-- Hero Section -->
    <div class="relative h-screen flex items-center justify-center bg-cover bg-center" style="background-image: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.3)), url('/backgrounds/invitation-1.jpg'); opacity: 0.9">
      <div class="text-center text-white px-4">
        <div class="mb-8">
          <p class="font-cormorant text-2xl mb-2">We,</p>
          <h1 class="font-script text-7xl md:text-8xl mb-4" style="font-weight: 900;">Jan & Muriel</h1>
          <p class="font-cormorant text-2xl mb-2">are getting Married.</p>
        </div>
        <div class="animate-bounce mt-12 cursor-pointer" @click="scrollToSaveTheDate">
          <svg class="w-6 h-6 mx-auto" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 14l-7 7m0 0l-7-7m7 7V3"></path>
          </svg>
        </div>
      </div>
    </div>

    <!-- Main Content -->
    <div class="max-w-4xl mx-auto px-4 py-16">
      <!-- Save the Date -->
      <section id="save-the-date" class="text-center mb-16">
        <h2 class="font-cormorant text-4xl mb-6">Save the Date</h2>
        <div class="bg-white shadow-lg rounded-lg p-8 mb-8">
          <div class="border-2 p-6" style="border-color: #cfb795">
            <p class="font-cormorant text-2xl mb-4">You're Invited to Celebrate</p>
            <h3 class="font-script text-5xl mb-6" style="color: #cd7b49">Our Wedding</h3>
            
            <div class="space-y-3 text-gray-700 mb-6">
              <div class="flex items-center justify-center space-x-2">
                <svg class="w-5 h-5" style="color: #cd7b49" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3a1 1 0 011-1h6a1 1 0 011 1v4m-6 0h6m-6 0V7a1 1 0 00-1 1v9a1 1 0 001 1h8a1 1 0 001-1V8a1 1 0 00-1-1h-1"></path>
                </svg>
                <p class="font-cormorant text-xl font-semibold">December 20, 2025</p>
              </div>
              
              <div class="flex items-center justify-center space-x-2">
                <svg class="w-5 h-5" style="color: #cd7b49" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                </svg>
                <p class="font-cormorant text-lg">2:00 PM Ceremony</p>
              </div>
              
              <div class="flex items-start justify-center space-x-2">
                <svg class="w-5 h-5 mt-1 flex-shrink-0" style="color: #cd7b49" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"></path>
                </svg>
                <div class="text-center">
                  <p class="font-cormorant text-lg">Central Fundamental Baptist Church</p>
                  <p class="font-cormorant text-sm text-gray-600">Poblacion IV, Coron, Palawan</p>
                </div>
              </div>

              <div class="flex items-start justify-center space-x-2">
                <svg class="w-5 h-5 mt-1 flex-shrink-0" style="color: #cd7b49" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v3m6.364-.636l-2.121 2.121M21 12h-3m-.636 6.364l-2.121-2.121M12 21v-3m-6.364.636l2.121-2.121M3 12h3m.636-6.364l2.121 2.121M8 12a4 4 0 108 0 4 4 0 00-8 0zm4-8v2m0 12v2"></path>
                </svg>
                <div class="text-center">
                  <p class="font-cormorant text-lg">Reception follows at</p>
                  <p class="font-cormorant text-sm text-gray-600">Coron Westown Resort</p>
                </div>
              </div>
            </div>
            
            <div class="border-t pt-4" style="border-color: #cfb795">
              <p class="font-cormorant text-lg mb-2" style="color: #cd7b49">Wedding Theme</p>
              <p class="font-cormorant text-base text-gray-600 mb-4">Modern Filipiña</p>
              
              <p class="font-cormorant text-lg mb-2" style="color: #cd7b49">Share the Love</p>
              <p class="font-cormorant text-base text-gray-600 mb-4">#oriJANallymadetomarryMURIEL</p>
              
              <p class="font-cormorant text-sm text-gray-500 italic">"When the time is right, I, the Lord, will make it happen." - Isaiah 60:22</p>
            </div>
          </div>
        </div>
      </section>

      <!-- Our Story -->
      <section class="mb-16">
        <h2 class="font-cormorant text-4xl text-center mb-8">Our Love Story</h2>
        <div class="bg-white shadow-lg rounded-lg p-8">
          <div class="grid md:grid-cols-2 gap-8 items-center">
            <div class="relative overflow-hidden rounded-lg">
              <div class="carousel-container flex transition-transform duration-500 ease-in-out" :style="{ transform: `translateX(-${currentSlide * 100}%)` }">
                <img v-for="(image, index) in carouselImages" :key="index" :src="`/backgrounds/carousel/carousel-${index + 1}.jpg`" alt="Couple" class="w-full h-64 object-cover flex-shrink-0">
              </div>
            </div>
            <div>
              <p class="font-cormorant text-lg leading-relaxed text-gray-700">
                Our story began not with fireworks, but with a quiet, certain hello. 
                That simple greeting sparked a connection that grew into a beautiful partnership. 
                We invite you to join us as we celebrate this new chapter and make a promise to continue building a 
                life filled with love, laughter, and endless adventure.
              </p>
            </div>
          </div>
        </div>
      </section>

      <!-- Finer Details Section -->
      <section class="mb-16">
        <h2 class="font-cormorant text-4xl text-center mb-8">Finer Details</h2>
        <div class="mb-8">
          <h3 class="font-cormorant text-2xl text-center mb-6">Dress Code</h3>
          <div class="grid md:grid-cols-3 gap-6">
            <div class="bg-white shadow-lg rounded-lg p-6 text-center">
              <img src="/dress-code/code-1.png" alt="Principal Sponsors" class="w-full h-48 object-contain rounded-lg mb-4">
              <p class="font-cormorant text-lg font-semibold mb-2">Principal Sponsors</p>
              <p class="text-gray-600">Filipiña Dress / Polo Barong</p>
            </div>
            <div class="bg-white shadow-lg rounded-lg p-6 text-center">
              <img src="/dress-code/code-2.png" alt="Secondary Sponsors" class="w-full h-48 object-contain rounded-lg mb-4">
              <p class="font-cormorant text-lg font-semibold mb-2">Secondary Sponsors</p>
              <p class="text-gray-600">Sleeveless with Camisa / Barong</p>
            </div>
            <div class="bg-white shadow-lg rounded-lg p-6 text-center">
              <img src="/dress-code/code-4.png" alt="Guests" class="w-full h-48 object-contain rounded-lg mb-4">
              <p class="font-cormorant text-lg font-semibold mb-2">Guests</p>
              <p class="text-gray-600">Semi-Formal/Casual Attire</p>
            </div>
          </div>
        </div>

        <div class="bg-white shadow-lg rounded-lg p-8">
          <h3 class="font-cormorant text-2xl text-center mb-6">Color Palette</h3>
          <p class="text-center text-gray-600 mb-4 italic font-cormorant">You may glam up in these shades but your smile is the best you can wear!</p>
          <p class="text-center text-xs text-gray-500 mb-6">Click on any color to copy its hex code</p>
          
          <div class="flex justify-center space-x-4 mb-6">
            <div @click="copyColor('#3d1d11')" class="w-16 h-16 rounded-full cursor-pointer hover:scale-110 transition-transform shadow-lg" style="background-color: #3d1d11" title="#3d1d11"></div>
            <div @click="copyColor('#6c462f')" class="w-16 h-16 rounded-full cursor-pointer hover:scale-110 transition-transform shadow-lg" style="background-color: #6c462f" title="#6c462f"></div>
            <div @click="copyColor('#536150')" class="w-16 h-16 rounded-full cursor-pointer hover:scale-110 transition-transform shadow-lg" style="background-color: #536150" title="#536150"></div>
            <div @click="copyColor('#cd7b49')" class="w-16 h-16 rounded-full cursor-pointer hover:scale-110 transition-transform shadow-lg" style="background-color: #cd7b49" title="#cd7b49"></div>
            <div @click="copyColor('#cfb795')" class="w-16 h-16 rounded-full cursor-pointer hover:scale-110 transition-transform shadow-lg" style="background-color: #cfb795" title="#cfb795"></div>
          </div>
          
          <p class="text-center text-sm font-medium" style="color: #cd7b49">Note: Please avoid wearing White.</p>
        </div>
      </section>

      <!-- RSVP Section -->
      <section class="mb-16">
        <div class="rounded-lg p-8" style="background-color: rgba(207, 183, 149, 0.2)">
          <h2 class="font-cormorant text-4xl text-center mb-8">RSVP</h2>
          <p class="text-center text-gray-700 mb-4 font-cormorant text-lg">
            Your presence would make our day even more special. Please let us know if you can join us!
          </p>
          <p class="text-center text-md mb-12 font-cormorant" style="color: #cd7b49">
            Please respond by November 15, 2025
          </p>
          
          <form @submit.prevent="submitRSVP" class="max-w-md mx-auto space-y-6" autocomplete="off">
            <div>
              <input 
                v-model="rsvpForm.name" 
                type="text" 
                placeholder="Full Name" 
                required 
                autocomplete="off"
                class="w-full p-4 border rounded-lg focus:outline-none font-cormorant" 
                style="border-color: #cfb795"
              >
            </div>
            <div>
              <input 
                v-model="rsvpForm.email" 
                type="text" 
                placeholder="Email Address" 
                required 
                autocomplete="new-password"
                class="w-full p-4 border rounded-lg focus:outline-none font-cormorant" 
                style="border-color: #cfb795"
              >
            </div>
            <div>
              <p class="text-gray-700 mb-3 font-cormorant text-lg">Will you attend?</p>
              <div class="space-y-3">
                <label class="flex items-center cursor-pointer">
                  <input v-model="rsvpForm.attendance" type="radio" name="attendance" value="yes" required class="mr-3" style="accent-color: #cd7b49">
                  <span class="font-cormorant text-lg">Yes, I'll be there!</span>
                </label>
                <label class="flex items-center cursor-pointer">
                  <input v-model="rsvpForm.attendance" type="radio" name="attendance" value="no" required class="mr-3" style="accent-color: #cd7b49">
                  <span class="font-cormorant text-lg">Sorry, I can't make it</span>
                </label>
              </div>
            </div>
            <div>
              <textarea 
                v-model="rsvpForm.message" 
                placeholder="Special message for the couple (optional)" 
                rows="3"
                autocomplete="new-password"
                class="w-full p-4 border rounded-lg focus:outline-none font-cormorant" 
                style="border-color: #cfb795"
              ></textarea>
            </div>
            <button 
              type="submit" 
              :disabled="submitting" 
              class="w-full disabled:bg-gray-400 text-white font-cormorant text-lg py-4 rounded-lg transition-colors" style="background-color: #3d1d11"
            >
              {{ submitting ? 'Sending...' : 'Send RSVP' }}
            </button>
          </form>
        </div>
      </section>

      <!-- Footer -->
      <footer class="text-center">
        <div class="animate-bounce mb-4 cursor-pointer" @click="scrollToTop">
          <svg class="w-6 h-6 mx-auto" fill="none" stroke="currentColor" viewBox="0 0 24 24" style="color: #cd7b49">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 10l7-7m0 0l7 7m-7-7v18"></path>
          </svg>
        </div>
        <div class="mb-8">
          <p class="font-cormorant text-lg text-gray-700">
            Made with <span class="text-red-500">&hearts;</span> by <a href="https://github.com/janirvinfabon" target="_blank" class="hover:underline" style="color: #cd7b49">#mstrirving</a>
          </p>
        </div>
      </footer>
    </div>

    <!-- Toast Notification -->
    <div v-if="toast.show" class="fixed top-4 right-4 z-50 p-4 rounded-lg shadow-lg transition-all duration-300 text-white" :style="{ backgroundColor: toast.type === 'success' ? '#536150' : '#6c462f' }">
      <p class="font-cormorant">{{ toast.message }}</p>
    </div>
  </div>
</template>

<script setup>
  useSeoMeta({
    title: 'Jan & Muriel Wedding Invitation',
    description: 'You are invited to celebrate our wedding.',
    ogTitle: 'Jan & Muriel Wedding Invitation',
    ogDescription: 'You are invited to celebrate our wedding.',
    ogImage: '/backgrounds/invitation-1.jpg',
    ogUrl: 'https://fabsoon.mstrirving.com',
    ogType: 'website',
    ogSiteName: 'Jan & Muriel Wedding',
    ogImageWidth: '1200',
    ogImageHeight: '630',
    fbAppId: '123456789',
    twitterCard: 'summary_large_image',
    twitterTitle: 'Jan & Muriel Wedding Invitation',
    twitterDescription: 'You are invited to celebrate our wedding.',
    twitterImage: '/backgrounds/invitation-1.jpg'
  })

  const rsvpForm = ref({
    name: '',
    email: '',
    attendance: '',
    message: ''
  })

  const submitting = ref(false)
  const toast = ref({ show: false, message: '', type: 'success' })
  
  const currentSlide = ref(0)
  const carouselImages = ref([1, 2, 3, 4, 5, 6])

  const showToast = (message, type = 'success') => {
    toast.value = { show: true, message, type }
    setTimeout(() => {
      toast.value.show = false
    }, 5000)
  }

  const scrollToSaveTheDate = () => {
    document.getElementById('save-the-date')?.scrollIntoView({ behavior: 'smooth' })
  }

  const scrollToTop = () => {
    window.scrollTo({ top: 0, behavior: 'smooth' })
  }
  
  const copyColor = async (color) => {
    if (process.client) {
      try {
        await navigator.clipboard.writeText(color)
      } catch (err) {
        console.error('Failed to copy color:', err)
      }
    }
  }
  
  onMounted(() => {
    if (process.client) {
      setInterval(() => {
        currentSlide.value = (currentSlide.value + 1) % carouselImages.value.length
      }, 5000)
    }
  })

  const submitRSVP = async () => {
    submitting.value = true
    
    try {
      const { $config } = useNuxtApp()
      
      if ($config?.public?.apiBaseUrl) {
        await $fetch(`${$config.public.apiBaseUrl}/rsvp`, {
          method: 'POST',
          body: {
            name: rsvpForm.value.name,
            email: rsvpForm.value.email,
            attendance: rsvpForm.value.attendance,
            message: rsvpForm.value.message,
            timestamp: new Date().toISOString()
          }
        })
      }
      
      showToast('Thank you for your RSVP! We look forward to celebrating with you!')
      
      rsvpForm.value = {
        name: '',
        email: '',
        attendance: '',
        message: ''
      }
      
    } catch (error) {
      if (error?.data?.error) {
        showToast(error.data.error, 'error')
      } else {
        showToast('RSVP submission failed. Please try again.', 'error')
      }
    } finally {
      submitting.value = false
    }
  }
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Euphoria+Script&family=Cormorant+Upright:wght@300;400;500;600;700&display=swap');

.font-script {
  font-family: 'Euphoria Script', cursive;
}

.font-cormorant {
  font-family: 'Cormorant Upright', serif;
}
</style>