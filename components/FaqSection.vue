<template>
  <section id="faq" class="mb-16">
    <h2 class="font-cormorant text-4xl text-center mb-8">Frequently Asked Questions</h2>
    <div class="max-w-4xl mx-auto">
      <div class="border rounded-lg" style="border-color: rgba(207, 183, 149, 0.3);">
        <div v-for="(faq, index) in faqs" :key="index">
          <h2>
            <button @click="toggleAccordion(index)" type="button" class="flex items-center justify-between w-full py-5 px-6 font-medium text-left border-b gap-3 transition-colors hover:bg-gray-50" style="color: #3d1d11; border-color: rgba(207, 183, 149, 0.3);">
              <span class="flex items-center">
                <svg class="w-5 h-5 me-2 shrink-0" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                  <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-8-3a1 1 0 00-.867.5 1 1 0 11-1.731-1A3 3 0 0113 8a3.001 3.001 0 01-2 2.83V11a1 1 0 11-2 0v-1a1 1 0 011-1 1 1 0 100-2zm0 8a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd"></path>
                </svg>
                <span class="font-poppins text-base md:text-md">{{ faq.question }}</span>
              </span>
              <svg class="w-3 h-3 shrink-0 transition-transform duration-300" :class="{ 'rotate-180': openItem === index }" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 10 6">
                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5 5 1 1 5"/>
              </svg>
            </button>
          </h2>
          <div v-show="openItem === index" class="py-5 px-6 border-b" style="border-color: rgba(207, 183, 149, 0.3);">
            <div class="space-y-2">
              <p v-for="(answer, answerIndex) in faq.answer" :key="answerIndex" class="font-poppins text-base md:text-base text-gray-700 leading-relaxed" :class="{ 'font-bold': answer.bold }">
                <span v-if="answer.bulleted">• </span>{{ answer.text }}
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
const faqs = ref([])
const openItem = ref(null)

const toggleAccordion = (index) => {
  if (openItem.value === index) {
    openItem.value = null
  } else {
    openItem.value = index
  }
}

onMounted(async () => {
  try {
    const data = await $fetch('/faq.json')
    faqs.value = data.faqs
  } catch (error) {
    console.error('Failed to load FAQ data:', error)
  }
})
</script>