<template>
  <section id="save-the-date" class="text-center mb-16">
    <h2 class="font-cormorant text-4xl mb-6">Save the Date</h2>
    <div class="bg-white shadow-lg rounded-lg p-8 mb-8">
      <div class="border-2 p-6" style="border-color: #cfb795">
        <p class="font-cormorant text-2xl mb-4">You're Invited to Celebrate</p>
        <h3 class="font-script text-5xl mb-6" style="color: #cd7b49">Our Wedding</h3>

        <!-- Countdown Timer -->
        <div class="mb-6">
          <div class="grid grid-cols-4 gap-4 max-w-md mx-auto">
            <div class="text-center">
              <div class="text-2xl font-bold" style="color: #cd7b49">{{ countdown.days }}</div>
              <div class="text-sm font-cormorant text-gray-600">Days</div>
            </div>
            <div class="text-center">
              <div class="text-2xl font-bold" style="color: #cd7b49">{{ countdown.hours }}</div>
              <div class="text-sm font-cormorant text-gray-600">Hours</div>
            </div>
            <div class="text-center">
              <div class="text-2xl font-bold" style="color: #cd7b49">{{ countdown.minutes }}</div>
              <div class="text-sm font-cormorant text-gray-600">Minutes</div>
            </div>
            <div class="text-center">
              <div class="text-2xl font-bold" style="color: #cd7b49">{{ countdown.seconds }}</div>
              <div class="text-sm font-cormorant text-gray-600">Seconds</div>
            </div>
          </div>
        </div>
        
        <div class="flex items-center justify-center mb-6">
          <div class="flex-1 h-px" style="background-color: #cfb795"></div>
        </div>
        
        <div class="space-y-3 text-gray-700 mb-6">
          <div class="flex items-center justify-center space-x-2">
            <svg class="w-5 h-5" style="color: #cd7b49" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"></path>
            </svg>
            <p class="font-cormorant text-base font-semibold">December 20, 2025</p>
          </div>
          
          <div class="flex items-center justify-center space-x-2">
            <svg class="w-5 h-5" style="color: #cd7b49" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>
            </svg>
            <p class="font-cormorant text-sm">2:00 PM Ceremony</p>
          </div>
          
          <div class="flex items-start justify-center space-x-2">
            <svg class="w-5 h-5 mt-1 flex-shrink-0" style="color: #cd7b49" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"></path>
            </svg>
            <div class="text-center">
              <p class="font-cormorant text-sm">Ceremony & Reception will be held at</p>
              <p class="font-cormorant text-sm text-gray-600">Coron Westown Resort</p>
            </div>
          </div>
        </div>
        
        <div class="border-t pt-4" style="border-color: #cfb795">
          <p class="font-cormorant text-lg mb-2" style="color: #cd7b49">Wedding Theme</p>
          <p class="font-cormorant text-base text-gray-600 mb-4">Modern Filipiñana</p>
          
          <p class="font-cormorant text-lg mb-2" style="color: #cd7b49">Share the Love</p>
          <p class="text-base text-gray-600 mb-4">#oriJANallymadetomarryMURIEL</p>
          
          <p class="text-base text-gray-500 italic">"When the time is right, I, the Lord, will make it happen." - Isaiah 60:22</p>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
const countdown = ref({ days: 0, hours: 0, minutes: 0, seconds: 0 })

const updateCountdown = () => {
  const weddingDate = new Date('2025-12-20T00:00:00')
  const now = new Date()
  const diff = weddingDate.getTime() - now.getTime()

  if (diff > 0) {
    countdown.value = {
      days: Math.floor(diff / (1000 * 60 * 60 * 24)).toString().padStart(2, '0'),
      hours: Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)).toString().padStart(2, '0'),
      minutes: Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60)).toString().padStart(2, '0'),
      seconds: Math.floor((diff % (1000 * 60)) / 1000).toString().padStart(2, '0')
    }
  }
}

onMounted(() => {
  if (process.client) {
    updateCountdown()
    setInterval(updateCountdown, 1000)
  }
})
</script>