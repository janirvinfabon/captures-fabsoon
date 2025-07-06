# Captures Fabsoon Wedding

A wedding souvenir application that allows guests to capture photos with wedding backgrounds.

## Features

- Landing page with video background
- Mobile-friendly camera capture
- Wedding background selection
- S3 upload for final images
- DynamoDB metadata storage

## Setup

### Frontend (Nuxt.js)

```bash
npm install
npm run dev
```

### Backend (Serverless)

```bash
cd backend
npm install -g serverless
pip install -r requirements.txt
serverless deploy
```

### Required Assets

Add these files to `/public/`:
- `wedding-background.mp4` - Landing page video
- `backgrounds/wedding-bg-1.jpg` - Wedding background 1
- `backgrounds/wedding-bg-2.jpg` - Wedding background 2
- `backgrounds/wedding-bg-3.jpg` - Wedding background 3
- `backgrounds/wedding-bg-4.jpg` - Wedding background 4

### Environment Variables

Update `nuxt.config.ts` with your API Gateway URL after deployment:

```typescript
runtimeConfig: {
  public: {
    apiBaseUrl: 'https://your-api-gateway-url.amazonaws.com/dev'
  }
}
```

## Tech Stack

- **Frontend**: Nuxt.js 3, Tailwind CSS
- **Backend**: Python 3.11, Serverless Framework
- **AWS Services**: API Gateway, Lambda, S3, DynamoDB
