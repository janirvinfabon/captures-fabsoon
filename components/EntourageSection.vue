<template>
  <section class="mb-16 relative overflow-hidden" id="entourage">
    <h2 class="font-cormorant text-4xl text-center mb-12">Our Entourage</h2>

    <!-- Parents -->
    <div v-if="entourage.groomParents" class="mb-16">
      <div class="text-center mb-8">
        <div class="w-24 h-px mx-auto mb-2" style="background-color: #cfb795"></div>
        <h3 class="font-script text-2xl" style="color: #cd7b49">Parents</h3>
        <div class="w-24 h-px mx-auto mt-2" style="background-color: #cfb795"></div>
      </div>
      <div class="grid grid-cols-2 max-w-md mx-auto gap-x-8 gap-y-2">
        <div class="text-right">
          <h4 class="font-script text-lg mb-2 text-gray-700">Groom's Parents</h4>
          <div v-for="person in entourage.groomParents" :key="person.name" class="mb-2 md:mb-2 text-right">
            <p class="font-alegreya md:text-lg sm:text-md" style="color: #3d1d11">{{ person.name }}</p>
          </div>
        </div>
        <div class="text-left">
          <h4 class="font-script text-lg md:text-xl mb-2 text-gray-700">Bride's Parents</h4>
          <div v-for="person in entourage.brideParents" :key="person.name" class="mb-2 md:mb-2 text-left">
            <p class="font-alegreya md:text-lg sm:text-md" style="color: #3d1d11">{{ person.name }}</p>
          </div>
        </div>
      </div>
    </div>

    <!-- Principal Sponsors -->
    <div v-if="entourage.principalSponsors" class="mb-16" id="entourage-principal-sponsors">
      <div class="text-center mb-8">
        <div class="w-24 h-px mx-auto mb-2" style="background-color: #cfb795"></div>
        <h3 class="font-script text-2xl" style="color: #cd7b49">Principal Sponsors</h3>
        <div class="w-24 h-px mx-auto mt-2" style="background-color: #cfb795"></div>
      </div>
      <div class="grid grid-cols-2 max-w-md mx-auto gap-x-8 gap-y-2">
        <div v-for="(person, index) in entourage.principalSponsors" :key="person.name" class="mb-2 md:mb-3" :class="index % 2 === 0 ? 'text-right' : 'text-left'">
          <p class="font-alegreya md:text-lg sm:text-md" style="color: #3d1d11">{{ person.name }}</p>
        </div>
      </div>
    </div>

    <!-- Best Man & Maid of Honor -->
    <div class="w-2/5 h-px mx-auto mb-8" style="background-color: #cfb795"></div>
    <div v-if="entourage.bestMan" class="grid grid-cols-2 text-center max-w-md mx-auto mb-8 gap-x-8 gap-y-2">
      <div class="text-center">
        <h3 class="font-script text-xl mb-4" style="color: #cd7b49">Best Man</h3>
        <div v-for="person in entourage.bestMan" :key="person.name" class="mb-3">
          <p class="font-alegreya md:text-lg sm:text-md" style="color: #3d1d11">{{ person.name }}</p>
        </div>
      </div>
      
      <div class="text-center">
        <h3 class="font-script text-xl mb-4" style="color: #cd7b49">Maid of Honor</h3>
        <div v-for="person in entourage.maidOfHonor" :key="person.name" class="mb-3">
          <p class="font-alegreya md:text-lg sm:text-md" style="color: #3d1d11">{{ person.name }}</p>
        </div>
      </div>
    </div>

    <!-- Secondary Sponsors -->
    <div v-if="entourage.secondarySponsors" class="mb-8" id="entourage-secondary-sponsor">
      <div class="text-center mb-6">
        <div class="w-24 h-px mx-auto mb-2" style="background-color: #cfb795"></div>
        <h3 class="font-script text-2xl" style="color: #cd7b49">Secondary Sponsors</h3>
        <div class="w-24 h-px mx-auto mt-2" style="background-color: #cfb795"></div>
      </div>
      <div class="space-y-8">
        <div v-for="(sponsors, role) in groupedSecondarySponsors" :key="role" class="text-center">
          <h3 class="font-script text-xl mb-2" style="color: #cd7b49">{{ role }}</h3>
          <div class="text-center">
            <div v-for="person in sponsors" :key="person.name" class="mb-1 md:mb-2">
              <p class="font-alegreya md:text-lg sm:text-md" style="color: #3d1d11">{{ person.name }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Bridesmaids & Groomsmen -->
    <div v-if="entourage.groomsmen" class="grid grid-cols-2 text-center max-w-md mx-auto mb-16">
      <div class="text-center">
        <h3 class="font-script text-xl mb-4" style="color: #cd7b49">Groom Squad</h3>
        <div v-for="person in entourage.groomsmen" :key="person.name" class="mb-3">
          <p class="font-alegreya md:text-lg sm:text-md" style="color: #3d1d11">{{ person.name }}</p>
        </div>
      </div>
      
      <div class="text-center">
        <h3 class="font-script text-xl mb-4" style="color: #cd7b49">Bride Squad</h3>
        <div v-for="person in entourage.bridesmaids" :key="person.name" class="mb-3">
          <p class="font-alegreya md:text-lg sm:text-md" style="color: #3d1d11">{{ person.name }}</p>
        </div>
      </div>
    </div>

    <!-- Special Roles -->
    <div v-if="entourage.specialRoles">
      <div class="space-y-6">
        <div v-for="roleGroup in entourage.specialRoles" :key="roleGroup.role" class="text-center">
          <h4 class="font-script text-xl mb-2" style="color: #cd7b49">{{ roleGroup.role }}</h4>
          <div v-for="name in roleGroup.names" :key="name">
            <p class="font-alegreya md:text-lg sm:text-md" style="color: #3d1d11">{{ name }}</p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
const entourage = ref({})

const groupedSecondarySponsors = computed(() => {
  if (!entourage.value.secondarySponsors) return {}
  
  return entourage.value.secondarySponsors.reduce((groups, person) => {
    const role = person.role
    if (!groups[role]) {
      groups[role] = []
    }
    groups[role].push(person)
    return groups
  }, {})
})

onMounted(async () => {
  try {
    entourage.value = await $fetch('/entourage.json')
    console.log('Loaded entourage data:', entourage.value)
    console.log('Special roles:', entourage.value.specialRoles)
  } catch (error) {
    console.error('Failed to load entourage data:', error)
  }
})
</script>