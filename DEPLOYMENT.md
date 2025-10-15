# 🚀 Vercel Deployment Guide

This guide will help you deploy your AI Diet Recipe Generator to Vercel.

## 📋 Prerequisites

- A [Vercel account](https://vercel.com/signup) (free tier works fine)
- [Vercel CLI](https://vercel.com/cli) installed (optional, but recommended)

## 🔧 Deployment Steps

### Option 1: Deploy via Vercel CLI (Recommended)

1. **Install Vercel CLI** (if not already installed):
```bash
npm install -g vercel
```

2. **Login to Vercel**:
```bash
vercel login
```

3. **Deploy from the project directory**:
```bash
vercel
```

4. Follow the prompts:
   - Set up and deploy? **Y**
   - Which scope? Select your account
   - Link to existing project? **N** (for first deployment)
   - What's your project's name? **vercel-app** (or your preferred name)
   - In which directory is your code located? **./**
   - Want to override the settings? **N**

5. Your app will be deployed! You'll get a URL like: `https://your-app.vercel.app`

### Option 2: Deploy via GitHub (Alternative)

1. **Push your code to GitHub**:
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/yourusername/your-repo.git
git push -u origin main
```

2. **Connect to Vercel**:
   - Go to [vercel.com](https://vercel.com)
   - Click "New Project"
   - Import your GitHub repository
   - Vercel will auto-detect the FastAPI app
   - Click "Deploy"

## ⚙️ Configuration Files

The following files are configured for Vercel deployment:

- **`vercel.json`** - Vercel configuration for routing and builds
- **`runtime.txt`** - Specifies Python 3.12 runtime
- **`.vercelignore`** - Files to exclude from deployment
- **`requirements.txt`** - Python dependencies with pinned versions to avoid conflicts

## 🔧 Important Notes

### httpx Dependency Conflict Fix

The `requirements.txt` file includes pinned versions of `httpx` and `httpcore` to prevent dependency conflicts with the OpenAI library on Vercel:

```txt
httpx==0.27.2
httpcore==1.0.6
```

This ensures compatibility between OpenAI SDK and Vercel's serverless environment.

### Python Version

Vercel supports Python 3.9 and 3.12. We're using **Python 3.12** as specified in `runtime.txt` (closest to your Python 3.13 requirement).

## 🌐 After Deployment

Once deployed, your app will be available at your Vercel URL. Users can:

1. Visit the URL
2. Enter their OpenAI API key
3. Select their diet preference
4. Generate recipes instantly!

## 🐛 Troubleshooting

### Deployment Fails

- Check the build logs in Vercel dashboard
- Ensure all files are committed
- Verify `vercel.json` configuration

### Import Errors

- Make sure all dependencies are in `requirements.txt`
- Check that httpx versions are pinned correctly

### Static Files Not Loading

- Verify the `static` directory is included in your deployment
- Check the path resolution in `main.py`

## 📊 Monitoring

- View logs: `vercel logs <deployment-url>`
- Check analytics in Vercel dashboard
- Monitor function execution times

## 🔄 Redeployment

To redeploy after making changes:

```bash
vercel --prod
```

Or simply push to your GitHub main branch if you're using GitHub integration.

## 💰 Pricing

The free Vercel tier includes:
- Unlimited deployments
- 100GB bandwidth per month
- Serverless function execution

This should be more than enough for personal use and testing!

---

Happy deploying! 🎉

