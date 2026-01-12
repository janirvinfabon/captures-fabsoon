<template>
  <!-- Login Form -->
  <div v-if="!isAuthenticated" class="min-h-screen bg-gray-50 flex items-center justify-center p-4">
    <div class="bg-white rounded-lg shadow p-8 w-full max-w-md">
      <h1 class="text-2xl font-bold text-center mb-6">Admin Login</h1>
      <form @submit.prevent="login">
        <input v-model="password" type="password" placeholder="Password" class="w-full p-3 border rounded mb-4" required>
        <button type="submit" class="w-full bg-blue-500 text-white p-3 rounded hover:bg-blue-600">Login</button>
      </form>
      <p v-if="loginError" class="text-red-500 text-sm mt-2">{{ loginError }}</p>
    </div>
  </div>

  <!-- RSVP Admin -->
  <div v-else class="min-h-screen bg-gray-50 p-4">
    <div class="max-w-6xl mx-auto">
      <div class="flex justify-between items-center mb-8">
        <h1 class="text-3xl font-bold">RSVP ({{ attendingRsvps.length + notAttendingRsvps.length }})</h1>
        <div class="flex gap-2">
          <button @click="logout" class="px-4 py-2 bg-red-500 text-white rounded hover:bg-red-600">Logout</button>
          <button @click="refreshData" :disabled="loading" class="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 disabled:opacity-50">
            {{ loading ? 'Loading...' : 'Refresh' }}
          </button>
        </div>
      </div>
      
      <div class="grid md:grid-cols-2 gap-8">
        <!-- Attending -->
        <div class="bg-white rounded-lg shadow p-6">
          <h2 class="text-xl font-semibold text-green-600 mb-4">
            Attending ({{ attendingRsvps.length }})
          </h2>
          <div class="space-y-3">
            <div v-if="loading" class="text-center py-8 text-gray-500">Loading...</div>
            <div v-else-if="attendingRsvps.length === 0" class="text-center py-8 text-gray-500">No RSVPs yet</div>
            <div v-else v-for="rsvp in paginatedAttending" :key="rsvp.email" class="border-b pb-2">
              <p class="font-medium">{{ rsvp.name }}</p>
              <p class="text-sm text-gray-600">{{ rsvp.email }}</p>
              <p v-if="rsvp.message" class="text-sm text-gray-700 mt-1">{{ rsvp.message }}</p>
              <p class="text-xs text-gray-500">{{ formatDate(rsvp.datetime) }}</p>
            </div>
          </div>
          <div class="flex justify-between items-center mt-4" v-if="attendingPages > 1">
            <button @click="attendingPage = Math.max(1, attendingPage - 1)" :disabled="attendingPage === 1" class="px-3 py-1 bg-gray-200 rounded disabled:opacity-50">Prev</button>
            <span class="text-sm">{{ attendingPage }} / {{ attendingPages }}</span>
            <button @click="attendingPage = Math.min(attendingPages, attendingPage + 1)" :disabled="attendingPage === attendingPages" class="px-3 py-1 bg-gray-200 rounded disabled:opacity-50">Next</button>
          </div>
        </div>

        <!-- Not Attending -->
        <div class="bg-white rounded-lg shadow p-6">
          <h2 class="text-xl font-semibold text-red-600 mb-4">
            Not Attending ({{ notAttendingRsvps.length }})
          </h2>
          <div class="space-y-3">
            <div v-if="loading" class="text-center py-8 text-gray-500">Loading...</div>
            <div v-else-if="notAttendingRsvps.length === 0" class="text-center py-8 text-gray-500">No RSVPs yet</div>
            <div v-else v-for="rsvp in paginatedNotAttending" :key="rsvp.email" class="border-b pb-2">
              <p class="font-medium">{{ rsvp.name }}</p>
              <p class="text-sm text-gray-600">{{ rsvp.email }}</p>
              <p v-if="rsvp.message" class="text-sm text-gray-700 mt-1">{{ rsvp.message }}</p>
              <p class="text-xs text-gray-500">{{ formatDate(rsvp.datetime) }}</p>
            </div>
          </div>
          <div class="flex justify-between items-center mt-4" v-if="notAttendingPages > 1">
            <button @click="notAttendingPage = Math.max(1, notAttendingPage - 1)" :disabled="notAttendingPage === 1" class="px-3 py-1 bg-gray-200 rounded disabled:opacity-50">Prev</button>
            <span class="text-sm">{{ notAttendingPage }} / {{ notAttendingPages }}</span>
            <button @click="notAttendingPage = Math.min(notAttendingPages, notAttendingPage + 1)" :disabled="notAttendingPage === notAttendingPages" class="px-3 py-1 bg-gray-200 rounded disabled:opacity-50">Next</button>
          </div>
        </div>
      </div>


    </div>
  </div>
</template>

<script setup>
const config = useRuntimeConfig()
const attendingRsvps = ref([])
const notAttendingRsvps = ref([])
const attendingPage = ref(1)
const notAttendingPage = ref(1)
const itemsPerPage = 10
const loading = ref(false)
const isAuthenticated = ref(false)
const password = ref('')
const loginError = ref('')

const login = async () => {
  try {
    loginError.value = ''
    const response = await $fetch(`${config.public.apiBaseUrl}/admin/login`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-API-Key': config.public.apiKey
      },
      body: JSON.stringify({ password: password.value })
    })
    
    if (response.success) {
      isAuthenticated.value = true
      nextTick(() => refreshData())
    } else {
      loginError.value = 'Unauthorized user.'
    }
  } catch (error) {
    loginError.value = 'Unauthorized user.'
  }
}

const logout = () => {
  isAuthenticated.value = false
  password.value = ''
}

const attendingPages = computed(() => Math.ceil(attendingRsvps.value.length / itemsPerPage))
const notAttendingPages = computed(() => Math.ceil(notAttendingRsvps.value.length / itemsPerPage))

const paginatedAttending = computed(() => {
  const start = (attendingPage.value - 1) * itemsPerPage
  return attendingRsvps.value.slice(start, start + itemsPerPage)
})

const paginatedNotAttending = computed(() => {
  const start = (notAttendingPage.value - 1) * itemsPerPage
  return notAttendingRsvps.value.slice(start, start + itemsPerPage)
})

const fetchRsvps = async (status) => {
  try {
    const response = await $fetch(`${config.public.apiBaseUrl}/rsvp/${status}`, {
      headers: {
        'X-API-Key': config.public.apiKey
      }
    })
    return response.rsvps || []
  } catch (error) {
    console.error(`Error fetching ${status} RSVPs:`, error)
    return []
  }
}

const formatDate = (dateString) => {
  return new Date(dateString).toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'short',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  })
}

const refreshData = async () => {
  loading.value = true
  attendingRsvps.value = await fetchRsvps('yes')
  notAttendingRsvps.value = await fetchRsvps('no')
  loading.value = false
}


</script>