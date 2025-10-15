# 🐛 Common Errors & Solutions

## Error: "Client.__init__() got an unexpected keyword argument 'proxies'"

### ❌ The Problem
```
Error generating recipe: Client.__init__() got an unexpected keyword argument 'proxies'
```

### 🔍 Root Cause
- **OpenAI SDK 1.x+** changed how proxies work
- The new SDK doesn't accept a `proxies` parameter in `OpenAI()` initialization
- Vercel's environment tries to auto-configure proxies from environment variables
- This causes a parameter mismatch error

### ✅ The Solution

The fix is to create a custom `httpx.Client` and pass it to OpenAI:

```python
# Create custom httpx client with proxies explicitly disabled
http_client = httpx.Client(
    timeout=60.0,
    follow_redirects=True,
    proxies=None  # This prevents the error!
)

# Pass the custom client to OpenAI
client = OpenAI(
    api_key=request.api_key,
    http_client=http_client,
    max_retries=2
)
```

### 📝 How It Works

1. **Old way (causes error)**:
   ```python
   # This fails on Vercel because it tries to pass proxies parameter
   client = OpenAI(api_key=request.api_key, proxies={...})  # ❌
   ```

2. **New way (works)**:
   ```python
   # Create httpx client with explicit proxy config
   http_client = httpx.Client(proxies=None)
   client = OpenAI(api_key=request.api_key, http_client=http_client)  # ✅
   ```

### 🔄 Already Fixed!

This fix is already implemented in `main.py`. The code now:
- ✅ Creates a custom httpx client
- ✅ Explicitly sets `proxies=None` 
- ✅ Passes the client to OpenAI
- ✅ Properly closes the client after use

---

## Error: "httpx.ProxyError" or "Connection timeout"

### ❌ The Problem
```
httpx.ProxyError: Cannot connect to proxy
```

### ✅ The Solution
This is fixed by:
1. Using `httpx==0.27.0` (exact version)
2. Custom httpx client with `proxies=None`
3. Timeout set to 60 seconds

See [PROXY_ERROR_FIX.md](PROXY_ERROR_FIX.md) for details.

---

## Error: "Module not found" or Import Errors

### ❌ The Problem
```
ModuleNotFoundError: No module named 'httpx'
```

### ✅ The Solution
All dependencies are listed in `requirements.txt`:

```txt
fastapi==0.115.0
uvicorn==0.32.0
openai==1.51.0
httpx==0.27.0
httpcore==1.0.5
anyio==4.4.0
sniffio==1.3.1
h11==0.14.0
certifi==2024.8.30
idna==3.10
python-multipart==0.0.12
pydantic==2.9.2
```

Make sure to redeploy:
```bash
vercel --prod --force
```

---

## Error: "Timeout" or "Request took too long"

### ❌ The Problem
```
OpenAI request timeout after 30 seconds
```

### ✅ The Solution
Timeout is now set to 60 seconds:
```python
http_client = httpx.Client(timeout=60.0)
```

And in `vercel.json`:
```json
{
  "functions": {
    "main.py": {
      "maxDuration": 60
    }
  }
}
```

---

## Error: "Invalid API Key"

### ❌ The Problem
```
Error: Incorrect API key provided
```

### ✅ The Solution
1. Get a valid API key from https://platform.openai.com/api-keys
2. Make sure it starts with `sk-`
3. Check your OpenAI account has credits
4. Verify the key hasn't expired

---

## Error: "Memory limit exceeded"

### ❌ The Problem
```
Function execution exceeded memory limit
```

### ✅ The Solution
Memory is set to 1024 MB in `vercel.json`:
```json
{
  "functions": {
    "main.py": {
      "memory": 1024
    }
  }
}
```

If still failing, consider optimizing the response or increasing memory.

---

## Error: "Static files not found"

### ❌ The Problem
```
FileNotFoundError: static/index.html
```

### ✅ The Solution
The path uses `Path(__file__).parent` for compatibility:
```python
html_path = Path(__file__).parent / "static" / "index.html"
```

Make sure `static/index.html` is committed to git.

---

## 🧪 Testing After Fixes

Test the API endpoint:
```bash
curl -X POST https://your-app.vercel.app/api/generate-recipe \
  -H "Content-Type: application/json" \
  -d '{
    "diet_type": "vegan",
    "api_key": "sk-your-openai-key"
  }'
```

Expected response:
```json
{
  "success": true,
  "recipe": "Recipe details...",
  "diet_type": "vegan"
}
```

---

## 🆘 Still Having Issues?

1. **Check Vercel logs**:
   ```bash
   vercel logs --follow
   ```

2. **Force clean build**:
   ```bash
   vercel --prod --force
   ```

3. **Verify dependencies**:
   - Ensure httpx is exactly 0.27.0
   - Check all packages installed correctly

4. **Review documentation**:
   - [PROXY_ERROR_FIX.md](PROXY_ERROR_FIX.md)
   - [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
   - [DEPLOYMENT.md](DEPLOYMENT.md)

---

**Last Updated**: October 15, 2025  
**All errors listed above are FIXED in current code** ✅

