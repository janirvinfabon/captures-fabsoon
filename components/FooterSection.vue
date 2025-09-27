<template>
  <footer class="text-center">        
    <div class="mb-8">
      <p class="font-cormorant text-lg text-gray-700">
        Made with <span class="text-red-500">&hearts;</span> by <a href="https://github.com/janirvinfabon" target="_blank" class="hover:underline" style="color: #cd7b49">#mstrirving</a>
      </p>
    </div>
    <div class="animate-bounce mb-4 cursor-pointer" @click="scrollToTop">
      <svg class="w-6 h-6 mx-auto" fill="none" stroke="currentColor" viewBox="0 0 24 24" style="color: #cd7b49">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 10l7-7m0 0l7 7m-7-7v18"></path>
      </svg>
    </div>
  </footer>
</template>

<script setup>
const scrollToTop = () => {
  window.scrollTo({ top: 0, behavior: 'smooth' })
}
</script>