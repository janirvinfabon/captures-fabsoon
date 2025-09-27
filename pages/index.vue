<template>
  <!-- Splash Screen -->
  <Transition name="fade" appear>
    <div v-if="loading" class="fixed inset-0 z-50 flex items-center justify-center bg-white">
      <div class="relative">
        <div class="w-48 h-48 md:w-64 md:h-64 border-4 md:border-6 border-t-transparent rounded-full animate-spin" style="border-color: #cd7b49; border-top-color: transparent;"></div>
        <div class="absolute inset-0 flex items-center justify-center">
          <h1 class="font-script text-3xl md:text-5xl text-center" style="color: #cd7b49;">Jan &<br>Muriel</h1>
        </div>
      </div>
    </div>
  </Transition>

  <Transition name="slide-up" appear>
    <div v-if="!loading" class="min-h-screen bg-gradient-to-b from-amber-50 to-white">
      <HeroSection />
      
      <div class="max-w-4xl mx-auto px-4 py-16">
        <SaveTheDate />
        <OurLoveStory />
        <FinerDetails />
        <EntourageSection />
        <RsvpSection @showToast="showToast" />
        <FooterSection />
      </div>

      <!-- Toast Notification -->
      <div v-if="toast.show" class="fixed top-4 right-4 z-50 p-4 rounded-lg shadow-lg transition-all duration-300 text-white" :style="{ backgroundColor: toast.type === 'success' ? '#536150' : '#6c462f' }">
        <p class="font-cormorant">{{ toast.message }}</p>
      </div>
    </div>
  </Transition>
</template>

<script setup>
  const loading = ref(true)
  const toast = ref({ show: false, message: '', type: 'success' })

  const showToast = (message, type = 'success') => {
    toast.value = { show: true, message, type }
    setTimeout(() => {
      toast.value.show = false
    }, 5000)
  }
  
  onMounted(() => {
    if (process.client) {
      setTimeout(() => {
        loading.value = false
      }, 2000)
    }
  })
</script>

