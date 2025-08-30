```markdown
# 🇦🇪 First UAE AI – by OrionixLabs.com

> **Dubai’s First Branded AI Assistant**  
> A production-grade, Arabic-aware, FastAPI-powered AI platform built for the Middle East.

![First UAE AI Logo](frontend/assets/logo.svg)

**First UAE AI** is a sovereign, fully branded artificial intelligence assistant developed by **[OrionixLabs.com](https://orionixlabs.com)**, a Dubai-based AI and automation lab. Built on top of advanced LLM infrastructure (DeepSeek-V3), this platform operates as a standalone AI identity — never exposing its underlying model.

Engineered for **enterprises, government agencies, and service providers** across the GCC, First UAE AI enables secure, localized, and multilingual customer engagement with full data residency in the UAE.

---

## 🛠️ Getting Started

### 2. Configure Environment
```bash
cp .env.example .env
```

Edit `.env` with your credentials:
```env
DEEPSEEK_API_KEY=your_deepseek_api_key_here
SECRET_KEY=your_strong_jwt_secret
ADMIN_KEY=your_admin_password
TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_token
TWILIO_PHONE_NUMBER=+1234567890
DATABASE_URL=postgresql://orionix:orionpass@db:5432/first_uae_ai
REDIS_URL=redis://redis:6379
```

> 🔐 **Never commit `.env` to version control.**

---

### 3. Launch with Docker
```bash
docker-compose up --build -d
```

✅ The platform is now running in detached mode.

---

## 🌐 Access Endpoints

| Service | URL |
|-------|-----|
| **API Documentation** | `http://localhost:8000/docs` |
| **Chat Interface** | `http://localhost:8000/frontend/index.html` |
| **Admin Panel** | `http://localhost:8000/frontend/admin/index.html` |
| **WhatsApp Webhook** | `http://localhost:8000/whatsapp` |

---

## 🔐 User Authentication

### Register a New User
```bash
curl -X POST http://localhost:8000/register \
  -H "Content-Type: application/json" \
  -d '{"username": "user1", "password": "pass123"}'
```

### Log In & Retrieve JWT Token
```bash
curl -X POST http://localhost:8000/token \
  -H "Content-Type: application/json" \
  -d '{"username": "user1", "password": "pass123"}'
```

Use the returned token in subsequent requests:
```http
Authorization: Bearer <your-jwt-token>
```

---

## 👮 Admin Panel: Chat Log Management

Access the admin interface at:  
👉 `http://localhost:8000/frontend/admin/index.html`

🔐 Protected by `ADMIN_KEY` from `.env`.  
Displays:
- User ID
- Prompt history
- AI responses
- Timestamps

All logs are stored in PostgreSQL for compliance and analytics.

---

## 💬 WhatsApp Integration (Twilio)

Enable global AI engagement via WhatsApp:

1. Visit [Twilio Console](https://twilio.com)
2. Acquire a WhatsApp-enabled number
3. Set the webhook to:  
   `https://your-domain.com/whatsapp`
4. Start conversing in Arabic or English

> **Example (Arabic):**  
> *User:* ما هو الطقس في أبوظبي؟  
> *First UAE AI:* الطقس في أبوظبي اليوم صافٍ ودرجات الحرارة مرتفعة، تصل إلى 40 مئوية.

---

## 🛡️ Security & Compliance

- 🔒 **Model Identity Protection**: AI never discloses backend model
- 🔐 **JWT Authentication**: Secure session management
- 🚫 **Rate Limiting**: Redis-backed throttling (100 req/hour default)
- 🌐 **Data Residency**: All logs stored in UAE-hosted PostgreSQL
- 🔄 **Secure Deployment**: Dockerized, isolated services
- 🔒 **HTTPS Recommended**: Use Nginx/Certbot or cloud TLS

---

## ☁️ Deployment Options

### Option 1: DigitalOcean App Platform (Recommended)
1. Push to GitHub
2. Visit [DigitalOcean Apps](https://cloud.digitalocean.com/apps)
3. Connect repository
4. Set environment variables
5. Deploy with one click

### Option 2: AWS EC2 / On-Premise
```bash
git clone https://github.com/orionixlabs/first-uae-ai.git
cd first-uae-ai
nano .env  # Insert keys
docker-compose up --build -d
```

Open port `8000` in firewall/security group.

### Option 3: Railway / Render
Deploy via Docker with environment variables.

---

## 📁 Project Structure

```
first-uae-ai/
├── backend/
│   ├── main.py               # FastAPI core
│   ├── database.py           # DB connection
│   ├── models.py             # SQLAlchemy models
│   ├── schemas.py            # Pydantic schemas
│   ├── config.py             # Environment loader
│   ├── auth.py               # JWT authentication
│   └── whatsapp.py           # Twilio webhook handler
├── frontend/
│   ├── index.html            # Chat UI
│   ├── admin/index.html      # Admin panel
│   └── assets/logo.svg       # OrionixLabs-branded logo
├── docker-compose.yml        # Multi-service orchestration
├── Dockerfile                # Production image
├── .env.example              # Environment template
├── requirements.txt          # Python dependencies
├── README.md                 # This document
└── LICENSE                   # MIT License
```

---

## 📬 Contact & Support

For enterprise integration, custom AI solutions, or technical support in the UAE:

📧 **contact@orionixlabs.com**  
🌐 **[https://orionixlabs.com](https://orionixlabs.com)**  
📍 Dubai, United Arab Emirates

---

## 💡 About OrionixLabs

**[OrionixLabs.com](https://orionixlabs.com)** is a Dubai-based AI and automation software laboratory specializing in:
- Custom AI models & RAG systems
- Self-hosted, privacy-first platforms
- Predictive safety & smart surveillance
- Workflow automation & agent systems

We build intelligent, adaptive, and secure systems that empower organizations across the Middle East.

> **First UAE AI — Engineered in Dubai. Powered by the Future.** 🇦🇪🚀
```
