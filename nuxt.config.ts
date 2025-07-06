export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: ['@nuxtjs/tailwindcss'],
  css: ['~/assets/css/main.css'],
  runtimeConfig: {
    public: {
      apiBaseUrl: process.env.API_BASE_URL || 'https://your-api-gateway-url.amazonaws.com/dev'
    }
  }
})