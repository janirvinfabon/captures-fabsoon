<template>
  <section id="our-love-story" class="mb-16">
    <h2 class="font-cormorant text-4xl text-center mb-8">Our Love Story</h2>
    <div class="bg-white shadow-lg rounded-lg p-8">
      <div class="grid md:grid-cols-[1.65fr_1fr] gap-8 items-center">
        <div class="relative overflow-hidden rounded-lg">
          <div class="carousel-container flex transition-transform duration-500 ease-in-out" :style="{ transform: `translateX(-${currentSlide * 100}%)` }">
            <img v-for="(_, index) in carouselImages" :key="index" :src="`/backgrounds/carousel/reduced/image-${index + 1}.jpg`" alt="Couple" class="w-full h-64 object-cover flex-shrink-0">
          </div>
        </div>
        <div>
          <p class="font-cormorant text-lg leading-relaxed text-gray-700 text-justify">
            Our story began not with fireworks, but with a quiet, certain hello. 
            That simple greeting sparked a connection that grew into a beautiful partnership. 
            We invite you to join us as we celebrate this new chapter and make a promise to continue building a 
            life filled with love, laughter, and endless adventure.
          </p>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
const currentSlide = ref(7)
const carouselImages = ref([1, 2, 3, 4, 5, 6, 7, 8])

onMounted(() => {
  if (process.client) {
    setInterval(() => {
      currentSlide.value = (currentSlide.value + 1) % carouselImages.value.length
    }, 5000)
  }
})
</script>