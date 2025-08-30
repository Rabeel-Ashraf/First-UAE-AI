#!/bin/bash
# first-uae-ai/scripts/deploy.sh
# OrionixLabs - First UAE AI
# Deployment script for DigitalOcean/Docker environments
# Usage: ./scripts/deploy.sh

set -euo pipefail

echo "🚀 Deploying First UAE AI - OrionixLabs Dubai"
echo "📦 Version: 1.0.0"
echo "📍 Deploying to: ${DEPLOY_ENV:-production}"

# Validate required environment variables
echo "🔍 Checking environment variables..."
if [[ -z "${DEEPSEEK_API_KEY:-}" ]]; then
    echo "❌ Error: DEEPSEEK_API_KEY is not set"
    exit 1
fi

if [[ -z "${SECRET_KEY:-}" ]]; then
    echo "❌ Error: SECRET_KEY is not set"
    exit 1
fi

if [[ -z "${ADMIN_KEY:-}" ]]; then
    echo "❌ Error: ADMIN_KEY is not set"
    exit 1
fi

# Create .env file from environment variables
echo "⚙️  Creating .env configuration..."
cat > .env << EOF
DEEPSEEK_API_KEY=$DEEPSEEK_API_KEY
SECRET_KEY=$SECRET_KEY
ADMIN_KEY=$ADMIN_KEY
DATABASE_URL=${DATABASE_URL:-postgresql://orionix:orionpass@db:5432/first_uae_ai}
REDIS_URL=${REDIS_URL:-redis://redis:6379}
RATE_LIMIT_REQUESTS=${RATE_LIMIT_REQUESTS:-100}
RATE_LIMIT_WINDOW=${RATE_LIMIT_WINDOW:-3600}
ALGORITHM=${ALGORITHM:-HS256}
ACCESS_TOKEN_EXPIRE_MINUTES=${ACCESS_TOKEN_EXPIRE_MINUTES:-1440}
TWILIO_ACCOUNT_SID=${TWILIO_ACCOUNT_SID:-}
TWILIO_AUTH_TOKEN=${TWILIO_AUTH_TOKEN:-}
TWILIO_PHONE_NUMBER=${TWILIO_PHONE_NUMBER:-}
EOF

echo "✅ .env file created"

# Build and deploy with Docker Compose
echo "🐳 Building Docker containers..."
docker-compose down --remove-orphans || true
docker-compose build --no-cache
docker-compose up -d

# Wait for services to be ready
echo "⏳ Waiting for services to start..."
sleep 10

# Verify deployment
echo "🔍 Verifying deployment..."
if docker-compose ps | grep -q "Up"; then
    echo "✅ First UAE AI deployed successfully!"
    echo "🌐 Access your AI at: http://localhost:8000"
    echo "💬 Chat: http://localhost:8000/frontend/src/index.html"
    echo "👮 Admin: http://localhost:8000/frontend/src/admin/index.html"
    echo "📄 API Docs: http://localhost:8000/docs"
else
    echo "❌ Deployment failed"
    docker-compose logs
    exit 1
fi

# Print health status
echo ""
echo "🏥 Service Status:"
docker-compose ps

echo ""
echo "✨ First UAE AI - Powered by OrionixLabs.com | Dubai, UAE"
echo "🚀 Your sovereign AI platform is now live!"
