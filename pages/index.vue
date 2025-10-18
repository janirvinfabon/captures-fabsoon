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
        <FaqSection />
        <RemindersSection />
        <!-- Page Breaker -->
        <div class="my-16 flex items-center justify-center">
          <div class="w-full h-px" style="background-color: #cfb795"></div>
          <div class="absolute px-6" style="background-color: #fffefa">
            <svg class="w-6 h-6" style="color: #cd7b49" fill="currentColor" viewBox="0 0 24 24">
              <!-- Gift box -->
              <rect x="4" y="8" width="16" height="12" rx="1" fill="currentColor"/>
              <!-- Ribbon vertical -->
              <rect x="11" y="6" width="2" height="16" fill="#cfb795"/>
              <!-- Ribbon horizontal -->
              <rect x="2" y="11" width="20" height="2" fill="#cfb795"/>
              <!-- Bow -->
              <path d="M10 6c0-1 1-2 2-2s2 1 2 2c0 1-1 2-2 2s-2-1-2-2z" fill="#cfb795"/>
              <path d="M9 5c-1 0-2 1-2 2s1 2 2 2 2-1 2-2-1-2-2-2z" fill="#cfb795"/>
              <path d="M15 5c1 0 2 1 2 2s-1 2-2 2-2-1-2-2 1-2 2-2z" fill="#cfb795"/>
            </svg>
          </div>
        </div>
        
        <GiftGuideSection />
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

