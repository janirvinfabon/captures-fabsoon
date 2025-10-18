<template>
  <section class="mb-16 relative overflow-hidden" id="gift-guide">
    <h2 class="font-cormorant text-4xl text-center mb-8">Gift Guide</h2>
    <p class="font-alegreya text-center text-lg mb-12 max-w-2xl mx-auto" style="color: #3d1d11">
      We are deeply grateful for all the blessings God has bestowed upon us and could not ask for more. Your presence and prayers are the greatest gifts we could ever receive. However, if you wish to honor us with a token of love, a monetary gift toward our future together would be sincerely appreciated.
    </p>

    <!-- QR Code Carousel -->
    <div class="relative">
      <div class="overflow-hidden rounded-lg">
        <div class="flex transition-transform duration-300 ease-in-out" :style="{ transform: `translateX(-${currentSlide * 100}%)` }">
          <div v-for="(payment, index) in paymentMethods" :key="index" class="w-full flex-shrink-0">
            <div class="p-4 rounded-lg mb-4 flex justify-center">
              <img :src="payment.qrCode" :alt="`${payment.name} QR Code`" class="w-auto lg:w-2/4 object-contain">
            </div>
          </div>
        </div>
      </div>

      <!-- Navigation Dots -->
      <div class="flex justify-center space-x-2">
        <button
          v-for="(_, index) in paymentMethods"
          :key="index"
          @click="currentSlide = index"
          class="w-3 h-3 rounded-full transition-colors duration-200"
          :style="{ backgroundColor: currentSlide === index ? '#cd7b49' : '#cfb795' }"
        ></button>
      </div>


    </div>
  </section>
</template>

<script setup>
const currentSlide = ref(0)

const paymentMethods = ref([
  {
    name: 'BDO',
    qrCode: '/qr-codes/bdo-qr.png',
    accountInfo: 'Account Name: Jan & Muriel Wedding'
  },
  {
    name: 'GCash',
    qrCode: '/qr-codes/gcash-qr.png',
    accountInfo: 'Account Name: Jan & Muriel Wedding'
  },
  {
    name: 'Maya',
    qrCode: '/qr-codes/maya-qr.png',
    accountInfo: 'Account Name: Jan & Muriel Wedding'
  }
])

const nextSlide = () => {
  currentSlide.value = (currentSlide.value + 1) % paymentMethods.value.length
}

const previousSlide = () => {
  currentSlide.value = currentSlide.value === 0 ? paymentMethods.value.length - 1 : currentSlide.value - 1
}

// Auto-advance carousel
onMounted(() => {
  setInterval(() => {
    nextSlide()
  }, 7500)
})
</script>