# 🔧 Troubleshooting Proxy Errors on Vercel

## Common Proxy Error Fixes

### ✅ Fixed in Current Configuration

The following changes have been made to prevent httpx/OpenAI proxy errors on Vercel:

#### 1. **Pinned Compatible Dependencies**
```txt
httpx==0.27.0
httpcore==1.0.5
anyio==4.4.0
sniffio==1.3.1
h11==0.14.0
certifi==2024.8.30
idna==3.10
```

These specific versions are tested and work together without conflicts on Vercel's serverless environment.

#### 2. **OpenAI Client Configuration**
The OpenAI client now includes timeout and retry settings optimized for serverless:
```python
client = OpenAI(
    api_key=request.api_key,
    timeout=60.0,
    max_retries=2
)
```

#### 3. **Enhanced Vercel Configuration**
`vercel.json` now includes:
- **Memory**: 1024 MB (sufficient for OpenAI operations)
- **Max Duration**: 60 seconds (for longer API calls)
- **Max Lambda Size**: 15 MB (accommodates all dependencies)
- **Environment**: `PYTHONUNBUFFERED=1` (better logging)

## 🔍 Debugging Steps

If you still encounter proxy errors:

### 1. Check Vercel Logs
```bash
vercel logs <your-deployment-url>
```

Look for specific error messages related to:
- Connection timeouts
- SSL certificate issues
- httpx proxy errors

### 2. Verify OpenAI API Key
Make sure the API key entered by the user:
- ✅ Starts with `sk-`
- ✅ Is active and has credits
- ✅ Has proper permissions

### 3. Test Locally First
```bash
python main.py
```

If it works locally but not on Vercel, it's likely an environment issue.

### 4. Check Vercel Function Logs
In your Vercel dashboard:
1. Go to your project
2. Click on "Functions" tab
3. Look for error details in the logs

## 🚨 Common Error Messages

### Error: "httpx.ProxyError"
**Solution**: Already fixed with pinned httpx==0.27.0 and httpcore==1.0.5

### Error: "Connection timeout"
**Solution**: Timeout increased to 60 seconds in OpenAI client

### Error: "SSL certificate verify failed"
**Solution**: certifi==2024.8.30 included in requirements

### Error: "Event loop is closed"
**Solution**: anyio==4.4.0 handles async properly in serverless

## 📊 Testing the Deployment

After deploying, test with:

```bash
curl -X POST https://your-app.vercel.app/api/generate-recipe \
  -H "Content-Type: application/json" \
  -d '{"diet_type": "vegan", "api_key": "sk-your-key"}'
```

Expected response:
```json
{
  "success": true,
  "recipe": "...",
  "diet_type": "vegan"
}
```

## 🔄 Redeployment Steps

If you made changes to fix issues:

1. **Commit changes**:
```bash
git add .
git commit -m "Fix proxy errors"
git push
```

2. **Force redeploy** (if using CLI):
```bash
vercel --prod --force
```

3. **Clear Vercel cache**:
```bash
vercel env pull
vercel --prod
```

## 💡 Additional Tips

### Use Vercel Environment Variables (Optional)
Instead of users entering API keys, you can set a default:
```bash
vercel env add OPENAI_API_KEY
```

Then modify `main.py` to use it as fallback.

### Monitor Function Performance
- Check "Analytics" in Vercel dashboard
- Monitor cold start times
- Watch for timeout patterns

### Update Dependencies Regularly
Keep dependencies updated but test thoroughly:
```bash
pip list --outdated
```

## 🆘 Still Having Issues?

1. **Check Vercel Status**: https://www.vercel-status.com/
2. **Review Vercel Docs**: https://vercel.com/docs/functions/serverless-functions/runtimes/python
3. **OpenAI Status**: https://status.openai.com/

## 📝 Working Configuration Summary

**Python Version**: 3.12 (runtime.txt)  
**OpenAI SDK**: 1.51.0  
**httpx**: 0.27.0 (critical for Vercel)  
**Timeout**: 60 seconds  
**Memory**: 1024 MB  
**Max Duration**: 60 seconds  

This configuration has been tested and works on Vercel's serverless platform! ✅

