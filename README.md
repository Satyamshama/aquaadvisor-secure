# 🌊 AquaAdvisor - AI Water Quality Expert

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Netlify-00C7B7?style=for-the-badge&logo=netlify)](https://dapper-beijinho-83f760.netlify.app/)
[![Backend API](https://img.shields.io/badge/Backend%20API-Render-46E3B7?style=for-the-badge&logo=render)](https://aquaadvisor-ai.onrender.com)
[![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)

## 📖 Overview

**AquaAdvisor** is an AI-powered conversational agent that serves as your personal water quality expert. Built with modern web technologies and powered by advanced AI, it provides instant, reliable guidance on water quality parameters, purification methods, and safety standards.

### 🎯 What AquaAdvisor Does

- **pH Level Analysis** - Understand ideal pH ranges (6.5-8.5) and get recommendations for adjustments
- **TDS Interpretation** - Learn about Total Dissolved Solids and when to be concerned (>500 ppm)  
- **Purification Guidance** - Compare RO, UV, boiling, and carbon filtration methods
- **Safety Standards** - Get advice based on WHO and Indian water quality standards
- **Professional Testing** - Know when to seek professional water analysis

## 🚀 Live Application

### 🌐 Frontend (User Interface)
**Try it now:** [https://dapper-beijinho-83f760.netlify.app/](https://dapper-beijinho-83f760.netlify.app/)

### 🔧 Backend API
**API Endpoint:** [https://aquaadvisor-ai.onrender.com](https://aquaadvisor-ai.onrender.com)

**API Documentation:**
- Health Check: `GET /health`
- Chat Endpoint: `POST /chat`
- API Docs: `/docs` (coming soon)

## 🏗️ Architecture

┌─────────────────┐ HTTP/HTTPS ┌──────────────────┐ Groq API ┌─────────────┐
│ Frontend │ ─────────────────▶│ Backend API │ ─────────────▶│ AI Model │
│ (Netlify) │ │ (Render.com) │ │ (Llama3-8B) │
│ │◀───────────────── │ │◀─────────────── │ │
│ - HTML/CSS/JS │ JSON │ - Flask │ Response │ Groq │
│ - UI/UX │ │ - CORS Enabled │ │ │
│ - Responsive │ │ - Secure Keys │ │ │
└─────────────────┘ └──────────────────┘ └─────────────┘



## 🛠️ Technology Stack

### Frontend
- **HTML5** - Semantic markup and structure
- **CSS3** - Modern styling with gradients and animations
- **Vanilla JavaScript** - API communication and DOM manipulation
- **Responsive Design** - Mobile-first approach

### Backend
- **Python 3.12** - Core programming language
- **Flask** - Lightweight web framework
- **Flask-CORS** - Cross-origin resource sharing
- **Requests** - HTTP library for API calls
- **Gunicorn** - WSGI HTTP Server

### AI & External Services
- **Groq API** - Fast inference with Llama3-8B-8192 model
- **Environment Variables** - Secure API key management

### Deployment & Hosting
- **Frontend:** Netlify (Static hosting with CDN)
- **Backend:** Render.com (Container-based deployment)
- **Version Control:** Git with GitHub

## 📁 Project Structure

aquaadvisor/
├── frontend/
│ └── index.html # Complete web interface
├── backend/
│ ├── app.py # Flask application
│ ├── requirements.txt # Python dependencies
│ └── .gitignore # Git ignore rules
├── docs/
│ └── README.md # This file
└── .env.example # Environment variables template

text

## 🚀 Local Development

### Prerequisites
- Python 3.10+ installed
- Git installed
- Code editor (VS Code recommended)

### Backend Setup

1. **Clone the repository:**
git clone https://github.com/Satyamshama/aquaadvisor-secure.git
cd aquaadvisor-secure

text

2. **Create virtual environment:**
python -m venv aqua_env
source aqua_env/bin/activate # On Windows: aqua_env\Scripts\activate

text

3. **Install dependencies:**
pip install -r requirements.txt

text

4. **Set environment variables:**
export GROQ_API_KEY="your-groq-api-key-here"

On Windows: set GROQ_API_KEY=your-groq-api-key-here
text

5. **Run the application:**
python app.py

text

The backend will be available at `http://localhost:8000`

### Frontend Setup

1. **Open `index.html` in your browser** or serve it using:
Using Python's built-in server
python -m http.server 3000

Using Node.js (if installed)
npx serve .

text

2. **Update API URL** in `index.html` for local development:
const API_URL = 'http://localhost:8000'; // For local backend

text

## 📡 API Reference

### Chat Endpoint

**POST** `/chat`

Send a water quality question and receive AI-powered advice.

**Request Body:**
{
"message": "What is the ideal pH for drinking water?",
"session_id": "unique-session-id"
}

text

**Response:**
{
"response": "The ideal pH for drinking water is between 6.5 and 8.5 according to WHO standards...",
"session_id": "unique-session-id"
}

text

**cURL Example:**
curl -X POST "https://aquaadvisor-ai.onrender.com/chat"
-H "Content-Type: application/json"
-d '{"message":"My TDS reading is 650 ppm, is it safe?","session_id":"demo"}'

text

### Health Check

**GET** `/health`

Check if the API is running and healthy.

**Response:**
{
"status": "healthy",
"agent": "AquaAdvisor",
"timestamp": "2025-08-25",
"api_key_configured": true
}

text

## 🎯 Example Queries

Try these questions with AquaAdvisor:

### Basic Water Quality
- "What is the ideal pH level for drinking water?"
- "Is 500 ppm TDS safe for consumption?"
- "How do I remove chlorine taste from water?"

### Advanced Analysis
- "My water pH is 9.2 and tastes bitter, what should I do?"
- "Compare RO vs UV water purification methods"
- "When should I get professional water testing?"

### Troubleshooting
- "My water has a metallic taste, what could be wrong?"
- "Is cloudy water safe to drink?"
- "How often should I test my private well water?"

## 🔒 Security Features

- **🔐 Environment Variables** - API keys stored securely, never in code
- **🛡️ CORS Protection** - Controlled cross-origin resource sharing
- **🔍 Input Validation** - Sanitized user inputs and API responses
- **📝 Error Handling** - Graceful degradation with meaningful error messages
- **🌐 HTTPS** - Encrypted communication in production

## 🚀 Deployment

### Backend Deployment (Render.com)

1. **Connect GitHub repository** to Render
2. **Configure build settings:**
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python app.py`
3. **Set environment variables:**
   - `GROQ_API_KEY`: Your Groq API key
4. **Deploy** and get your API URL

### Frontend Deployment (Netlify)

1. **Drag and drop** `index.html` to Netlify
2. **Or connect GitHub** repository for auto-deployment
3. **Update API URL** in code to point to your backend
4. **Deploy** and get your frontend URL

## 🧪 Testing

### Manual Testing
1. Visit the [live demo](https://dapper-beijinho-83f760.netlify.app/)
2. Try various water quality questions
3. Check browser console for any errors

### API Testing
Test health endpoint
curl https://aquaadvisor-ai.onrender.com/health

Test chat endpoint
curl -X POST "https://aquaadvisor-ai.onrender.com/chat"
-H "Content-Type: application/json"
-d '{"message":"Test question","session_id":"test"}'



## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch:** `git checkout -b feature/amazing-feature`
3. **Commit your changes:** `git commit -m 'Add amazing feature'`
4. **Push to the branch:** `git push origin feature/amazing-feature`
5. **Open a Pull Request**

### Development Guidelines
- Follow PEP 8 for Python code
- Use semantic commit messages
- Add comments for complex logic
- Test your changes locally before submitting

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Satyam Sharma**
- 🎓 BTech Computer Science, IIT Jodhpur (4th Year)
- 💼 Specializing in AI/ML 
- 📧 Contact: [satyampvsharma@gmail.com]
- 🐙 GitHub: [@Satyamshama](https://github.com/Satyamshama)

## 🙏 Acknowledgments

- **Groq** for providing fast AI inference capabilities
- **Open Source Community** for the amazing tools and libraries
- **Water Quality Research** community for domain expertise

## 📈 Project Stats

- **Language:** Python, JavaScript, HTML, CSS
- **AI Model:** Llama3-8B-8192 via Groq API
- **Response Time:** < 2 seconds average
- **Availability:** 99.9% uptime target
- **Mobile Responsive:** ✅ Yes

## 🔮 Future Enhancements

- [ ] **Water Quality Calculator** - Interactive parameter calculator
- [ ] **Location-based Advice** - Regional water quality recommendations
- [ ] **Image Analysis** - Upload water test results for analysis
- [ ] **Multilingual Support** - Hindi and other Indian languages
- [ ] **Mobile App** - Native iOS and Android applications
- [ ] **Water Testing Labs** - Integration with local testing facilities

---

<div align="center">

**⭐ Star this repository if you found it helpful!**

[Live Demo](https://dapper-beijinho-83f760.netlify.app/) • [API Docs](https://aquaadvisor-ai.onrender.com) • [Report Bug](https://github.com/Satyamshama/aquaadvisor-secure/issues) • [Request Feature](https://github.com/Satyamshama/aquaadvisor-secure/issues)

</div>
