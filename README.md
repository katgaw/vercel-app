# 🍽️ AI Diet Recipe Generator

A beautiful and simple FastAPI application that generates personalized dinner recipes using OpenAI's GPT-4o model. Users can select their dietary preferences (vegetarian, vegan, or no restrictions) and get instant recipe suggestions.

## ✨ Features

- 🎨 Modern, gradient UI with smooth animations
- 🥗 Three diet options: Vegetarian, Vegan, No Restrictions
- 🔐 Secure API key input (user provides their own OpenAI key)
- ⚡ Fast recipe generation using GPT-4o
- 📱 Responsive design for all devices
- 🐍 Compatible with Python 3.13

## 🚀 Setup Instructions

### Prerequisites

- Python 3.13
- OpenAI API Key ([Get one here](https://platform.openai.com/api-keys))

### Installation

1. Install the required dependencies:

```bash
pip install -r requirements.txt
```

2. Run the application:

```bash
python main.py
```

Or alternatively:

```bash
uvicorn main:app --reload
```

3. Open your browser and navigate to:

```
http://localhost:8000
```

## 🎯 How to Use

1. Enter your OpenAI API key in the provided field
2. Select your dietary preference:
   - 🥗 **Vegetarian**: No meat, but dairy and eggs are okay
   - 🌱 **Vegan**: No animal products at all
   - 🍖 **No Restrictions**: All ingredients allowed
3. Click "Generate Recipe ✨"
4. Wait a few seconds for your personalized dinner recipe!

## 📦 Dependencies

- `fastapi==0.115.0` - Modern web framework
- `uvicorn==0.32.0` - ASGI server
- `openai==1.51.0` - OpenAI API client
- `python-multipart==0.0.12` - Form data parsing
- `pydantic==2.9.2` - Data validation

## 🔒 Security Note

Your OpenAI API key is only used for the current request and is never stored or logged by the application. The key is sent directly from your browser to the OpenAI API through the FastAPI backend.

## 🛠️ Tech Stack

- **Backend**: FastAPI (Python 3.13)
- **AI**: OpenAI GPT-4o
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Styling**: Custom CSS with gradients and animations

## 📝 License

MIT License - feel free to use this project however you'd like!

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

---

Enjoy cooking! 👨‍🍳👩‍🍳

