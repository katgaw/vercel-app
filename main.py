from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from openai import OpenAI
import os
from pathlib import Path
import httpx

app = FastAPI(title="Diet Recipe Generator")

# Verify httpx is properly imported (helps with Vercel deployment)
print(f"httpx version: {httpx.__version__}")

class RecipeRequest(BaseModel):
    diet_type: str
    api_key: str

@app.get("/", response_class=HTMLResponse)
async def read_root():
    # Handle both local and Vercel deployment paths
    html_path = Path(__file__).parent / "static" / "index.html"
    with open(html_path, "r") as f:
        return f.read()

@app.post("/api/generate-recipe")
async def generate_recipe(request: RecipeRequest):
    try:
        # Initialize OpenAI client with user's API key
        # Set timeout and max_retries for Vercel serverless environment
        client = OpenAI(
            api_key=request.api_key,
            timeout=60.0,
            max_retries=2
        )
        
        # Create prompt based on diet type
        diet_prompts = {
            "vegetarian": "vegetarian (no meat, but dairy and eggs are okay)",
            "vegan": "vegan (no animal products at all)",
            "no_restrictions": "with no dietary restrictions"
        }
        
        diet_description = diet_prompts.get(request.diet_type, "with no dietary restrictions")
        
        prompt = f"""Create a simple, delicious dinner recipe that is {diet_description}. 
        
Please format the response as follows:
- Recipe Name: [name]
- Prep Time: [time]
- Servings: [number]
- Ingredients: [list them]
- Instructions: [numbered steps]

Keep it simple and easy to make!"""
        
        # Call OpenAI API
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful cooking assistant who provides simple, tasty recipes."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=800
        )
        
        recipe = response.choices[0].message.content
        
        return {
            "success": True,
            "recipe": recipe,
            "diet_type": request.diet_type
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating recipe: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

