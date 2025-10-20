<template>
  <div class="min-h-screen bg-gradient-to-b from-amber-50 to-white flex items-center justify-center p-4">
    <div class="text-center">
      <h1 class="font-script text-6xl mb-4" style="color: #cd7b49;">Oops!</h1>
      <h2 class="text-2xl font-semibold mb-4">Page Not Found</h2>
      <p class="text-gray-600 mb-8">The page you're looking for doesn't exist.</p>
      <NuxtLink to="/" class="inline-block px-6 py-3 text-white rounded-lg hover:opacity-90 transition-opacity" style="background-color: #cd7b49;">
        Back to Wedding Invitation
      </NuxtLink>
    </div>
  </div>
</template>

<script setup>
definePageMeta({
  layout: false
})
</script>