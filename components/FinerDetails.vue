<template>
  <section class="mb-16">
    <h2 class="font-cormorant text-4xl text-center mb-8">Finer Details</h2>
    <div class="mb-8">
      <h3 class="font-cormorant text-2xl text-center mb-6">Dress Code</h3>
      <div class="grid md:grid-cols-3 gap-6">
        <div class="bg-white shadow-lg rounded-lg p-6 text-center">
          <img src="/dress-code/code-1.png" alt="Principal Sponsors" class="w-full h-48 object-contain rounded-lg mb-4">
          <p class="font-cormorant text-lg font-semibold mb-2">Principal Sponsors</p>
          <p class="text-gray-600">Filipiñana Dress / Polo Barong</p>
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
      
      <div class="flex justify-center gap-2 md:gap-4 mb-6">
        <div @click="copyColor('#3d1d11')" class="w-10 h-10 md:w-16 md:h-16 rounded-full cursor-pointer hover:scale-110 transition-transform shadow-lg flex-shrink-0" style="background-color: #3d1d11" title="#3d1d11"></div>
        <div @click="copyColor('#6c462f')" class="w-10 h-10 md:w-16 md:h-16 rounded-full cursor-pointer hover:scale-110 transition-transform shadow-lg flex-shrink-0" style="background-color: #6c462f" title="#6c462f"></div>
        <div @click="copyColor('#536150')" class="w-10 h-10 md:w-16 md:h-16 rounded-full cursor-pointer hover:scale-110 transition-transform shadow-lg flex-shrink-0" style="background-color: #536150" title="#536150"></div>
        <div @click="copyColor('#cd7b49')" class="w-10 h-10 md:w-16 md:h-16 rounded-full cursor-pointer hover:scale-110 transition-transform shadow-lg flex-shrink-0" style="background-color: #cd7b49" title="#cd7b49"></div>
        <div @click="copyColor('#cfb795')" class="w-10 h-10 md:w-16 md:h-16 rounded-full cursor-pointer hover:scale-110 transition-transform shadow-lg flex-shrink-0" style="background-color: #cfb795" title="#cfb795"></div>
        <div @click="copyColor('#977969')" class="w-10 h-10 md:w-16 md:h-16 rounded-full cursor-pointer hover:scale-110 transition-transform shadow-lg flex-shrink-0" style="background-color: #977969" title="#977969"></div>
      </div>
      
      <p class="text-center text-sm font-medium" style="color: #cd7b49">Note: Please avoid wearing White.</p>
    </div>
  </section>
</template>

<script setup>
const copyColor = async (color) => {
  if (process.client) {
    try {
      await navigator.clipboard.writeText(color)
    } catch (err) {
      console.error('Failed to copy color:', err)
    }
  }
}
</script>