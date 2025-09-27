export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: ['@nuxtjs/tailwindcss'],
  css: ['~/assets/css/main.css'],
  app: {
    head: {
      title: 'Jan & Muriel Wedding Invitation',
      meta: [
        { name: 'description', content: 'You are invited to celebrate our wedding.' },
        { property: 'image', content: 'https://fabsoon.com/backgrounds/seo.jpg' },
        { property: 'url', content: 'https://fabsoon.com' },
        { property: 'og:title', content: 'Jan & Muriel Wedding Invitation' },
        { property: 'og:description', content: 'You are invited to celebrate our wedding.' },
        { property: 'og:image', content: 'https://fabsoon.com/backgrounds/seo.jpg' },
        { property: 'og:url', content: 'https://fabsoon.com' },
        { property: 'og:type', content: 'website' },
        { property: 'og:site_name', content: 'Jan & Muriel Wedding' },
        { property: 'og:image:width', content: '1200' },
        { property: 'og:image:height', content: '630' },
        { name: 'twitter:card', content: 'summary_large_image' },
        { name: 'twitter:title', content: 'Jan & Muriel Wedding Invitation' },
        { name: 'twitter:description', content: 'You are invited to celebrate our wedding.' },
        { name: 'twitter:image', content: 'https://fabsoon.com/backgrounds/seo.jpg' }
      ]
    }
  },
  runtimeConfig: {
    public: {
      apiBaseUrl: process.env.API_BASE_URL || 'https://your-api-gateway-url.amazonaws.com/dev'
    }
  }
})