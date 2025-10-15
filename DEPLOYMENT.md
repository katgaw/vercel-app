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

### httpx Dependency Conflict & Proxy Error Fix ⚠️

The `requirements.txt` file includes **specifically tested versions** to prevent proxy errors and dependency conflicts with the OpenAI library on Vercel:

```txt
httpx==0.27.0        # Critical: This exact version prevents proxy errors
httpcore==1.0.5      # Must match httpx requirements
anyio==4.4.0         # Handles async operations in serverless
sniffio==1.3.1       # Required by anyio
h11==0.14.0          # HTTP/1.1 protocol support
certifi==2024.8.30   # SSL certificates (prevents SSL errors)
idna==3.10           # Internationalized domain name support
```

**DO NOT** change these versions unless testing thoroughly, as they are specifically tuned for Vercel's serverless environment.

### OpenAI Client Configuration

The OpenAI client includes timeout and retry settings optimized for serverless:
```python
client = OpenAI(
    api_key=request.api_key,
    timeout=60.0,      # Prevents timeout errors
    max_retries=2      # Automatic retry on transient failures
)
```

### Vercel Function Settings

The `vercel.json` configures optimal settings:
- **Memory**: 1024 MB (sufficient for OpenAI + dependencies)
- **Max Duration**: 60 seconds (handles longer API calls)
- **Max Lambda Size**: 15 MB (accommodates all packages)

### Python Version

Vercel supports Python 3.9 and 3.12. We're using **Python 3.12** as specified in `runtime.txt` (closest to your Python 3.13 requirement).

## 🌐 After Deployment

Once deployed, your app will be available at your Vercel URL. Users can:

1. Visit the URL
2. Enter their OpenAI API key
3. Select their diet preference
4. Generate recipes instantly!

## 🐛 Troubleshooting

### Proxy Errors ⚠️ (Most Common Issue)

If you see `httpx.ProxyError` or connection errors:

1. **Verify exact dependency versions** in `requirements.txt`:
   - httpx must be `0.27.0` (not 0.27.2 or newer)
   - httpcore must be `1.0.5`

2. **Redeploy with clean build**:
   ```bash
   vercel --prod --force
   ```

3. **Check Vercel logs**:
   ```bash
   vercel logs <your-deployment-url>
   ```

See [TROUBLESHOOTING.md](TROUBLESHOOTING.md) for detailed proxy error solutions.

### Deployment Fails

- Check the build logs in Vercel dashboard
- Ensure all files are committed
- Verify `vercel.json` configuration
- Make sure Python version is 3.12 (runtime.txt)

### Import Errors

- Make sure all dependencies are in `requirements.txt`
- Check that httpx versions are pinned correctly
- Verify no typos in package names

### Timeout Errors

- OpenAI timeout is set to 60 seconds
- Vercel max duration is 60 seconds
- If still timing out, check OpenAI API status

### Static Files Not Loading

- Verify the `static` directory is included in your deployment
- Check the path resolution in `main.py` uses `Path(__file__).parent`

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

