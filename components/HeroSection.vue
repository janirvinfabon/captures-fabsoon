<template>
  <section class="relative h-screen flex items-center justify-center bg-cover bg-center" style="background-image: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.3)), url('/backgrounds/invitation-1.jpg'); opacity: 0.9">
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
  </section>
</template>

<script setup>
const scrollToSaveTheDate = () => {
  document.getElementById('save-the-date')?.scrollIntoView({ behavior: 'smooth' })
}
</script>