<template>
  <section id="rsvp" class="mb-16">
    <div class="rounded-lg p-8" style="background-color: rgba(207, 183, 149, 0.2)">
      <h2 class="font-cormorant text-4xl text-center mb-8">RSVP</h2>
      <p class="text-center text-gray-700 mb-4 font-cormorant text-lg">
        Your presence would make our day even more special. Please let us know if you can join us!
      </p>
      
      <p class="text-center text-sm mb-6 font-medium" style="color: #cd7b49;">
        Please respond by November 15, 2025
      </p>
      
      <form @submit.prevent="submitRSVP" class="max-w-md mx-auto space-y-6" autocomplete="off">
        <div>
          <input 
            v-model="rsvpForm.name" 
            type="text" 
            placeholder="Full Name" 
            required 
            autocomplete="off"
            class="w-full p-4 border rounded-lg focus:outline-none font-cormorant" 
            style="border-color: #cfb795"
          >
        </div>
        <div>
          <input 
            v-model="rsvpForm.email" 
            type="text" 
            placeholder="Email Address" 
            required 
            autocomplete="new-password"
            class="w-full p-4 border rounded-lg focus:outline-none font-cormorant" 
            style="border-color: #cfb795"
          >
        </div>
        <div>
          <p class="text-gray-700 mb-3 font-cormorant text-lg">Will you attend?</p>
          <div class="space-y-3">
            <label class="flex items-center cursor-pointer">
              <input v-model="rsvpForm.attendance" type="radio" name="attendance" value="yes" required class="mr-3" style="accent-color: #cd7b49">
              <span class="font-cormorant text-lg">Yes, I'll be there!</span>
            </label>
            <label class="flex items-center cursor-pointer">
              <input v-model="rsvpForm.attendance" type="radio" name="attendance" value="no" required class="mr-3" style="accent-color: #cd7b49">
              <span class="font-cormorant text-lg">Sorry, I can't make it</span>
            </label>
          </div>
        </div>
        <div>
          <textarea 
            v-model="rsvpForm.message" 
            placeholder="Special message for the couple (optional)" 
            rows="3"
            autocomplete="new-password"
            class="w-full p-4 border rounded-lg focus:outline-none font-cormorant" 
            style="border-color: #cfb795"
          ></textarea>
        </div>
        <button 
          type="submit" 
          :disabled="submitting || isRsvpExpired" 
          class="w-full disabled:bg-gray-400 text-white font-cormorant text-lg py-4 rounded-lg transition-colors" style="background-color: #3d1d11"
        >
          {{ submitting ? 'Sending...' : isRsvpExpired ? 'RSVP Deadline Passed' : 'Send RSVP' }}
        </button>
      </form>
    </div>
  </section>
</template>

<script setup>
const emit = defineEmits(['showToast'])

const rsvpForm = ref({
  name: '',
  email: '',
  attendance: '',
  message: ''
})

const submitting = ref(false)

const isRsvpExpired = computed(() => {
  const deadline = new Date('2025-11-15T23:59:59')
  return new Date() > deadline
})

const createGoogleCalendarUrl = () => {
  const eventDetails = {
    title: 'Jan & Muriel Wedding',
    startDate: '20251220T060000Z', // December 20, 2025 2:00 PM UTC
    endDate: '20251220T100000Z',   // December 20, 2025 6:00 PM UTC
    description: 'Join us for our special day!',
    location: 'Coron Westown Resort'
  }
  
  const params = new URLSearchParams({
    action: 'TEMPLATE',
    text: eventDetails.title,
    dates: `${eventDetails.startDate}/${eventDetails.endDate}`,
    details: eventDetails.description,
    location: eventDetails.location
  })
  
  return `https://calendar.google.com/calendar/render?${params.toString()}`
}

const submitRSVP = async () => {
  submitting.value = true
  
  try {
    const { $config } = useNuxtApp()
    
    if ($config?.public?.apiBaseUrl) {
      await $fetch(`${$config.public.apiBaseUrl}/rsvp`, {
        method: 'POST',
        headers: {
          'X-API-Key': $config.public.apiKey
        },
        body: {
          name: rsvpForm.value.name,
          email: rsvpForm.value.email,
          attendance: rsvpForm.value.attendance,
          message: rsvpForm.value.message,
          timestamp: new Date().toISOString()
        }
      })
    }
    
    emit('showToast', 'Thank you for your RSVP! We look forward to celebrating with you!');
    if (rsvpForm.value.attendance === 'yes') {
      setTimeout(() => {
        const googleCalendarUrl = createGoogleCalendarUrl()
        window.open(googleCalendarUrl, '_blank')
      }, 1500);
    }
    
    rsvpForm.value = {
      name: '',
      email: '',
      attendance: '',
      message: ''
    }
    
  } catch (error) {
    if (error?.data?.error) {
      emit('showToast', error.data.error, 'error')
    } else {
      emit('showToast', 'RSVP submission failed. Please try again.', 'error')
    }
  } finally {
    submitting.value = false
  }
}
</script>