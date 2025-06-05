#!/bin/bash

# AI Platform Development Environment Setup Script
# Run this script to set up your development environment quickly

echo "🚀 Setting up AI Platform Development Environment..."

# Check if Docker is installed
if command -v docker &> /dev/null; then
    echo "✅ Docker is installed"
else
    echo "❌ Docker not found. Please install Docker first:"
    echo "   https://docs.docker.com/get-docker/"
    exit 1
fi

# Check if Node.js is installed
if command -v node &> /dev/null; then
    echo "✅ Node.js is installed ($(node --version))"
else
    echo "❌ Node.js not found. Please install Node.js first:"
    echo "   https://nodejs.org/"
    exit 1
fi

# Check if Python is installed
if command -v python3 &> /dev/null; then
    echo "✅ Python 3 is installed ($(python3 --version))"
else
    echo "❌ Python 3 not found. Please install Python 3 first"
    exit 1
fi

# Create Python virtual environment
echo "📦 Creating Python virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Create requirements.txt if it doesn't exist
if [ ! -f requirements.txt ]; then
    echo "📝 Creating requirements.txt..."
    cat > requirements.txt << EOL
# Langbase SDK for AI primitives
langbase

# FastAPI for backend development (Open WebUI compatible)
fastapi
uvicorn[standard]

# Database and ORM
sqlalchemy
alembic

# Development tools
pytest
black
flake8

# Playwright for browser automation
playwright

# Additional utilities
python-dotenv
requests
EOL
fi

# Install Python dependencies
echo "📦 Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Install Playwright browsers
echo "🎭 Installing Playwright browsers..."
playwright install

# Create package.json if it doesn't exist
if [ ! -f package.json ]; then
    echo "📝 Creating package.json..."
    cat > package.json << EOL
{
  "name": "ai-platform-development",
  "version": "1.0.0",
  "description": "Local AI platform with advanced capabilities",
  "scripts": {
    "dev": "npm run dev:backend & npm run dev:frontend",
    "dev:backend": "uvicorn src.main:app --reload --port 8000",
    "dev:frontend": "echo 'Frontend development server not yet configured'",
    "test": "pytest tests/",
    "lint": "black src/ && flake8 src/",
    "setup:openwebui": "docker run -d -p 3000:8080 -e OLLAMA_BASE_URL=http://host.docker.internal:11434 -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main"
  },
  "keywords": ["ai", "local", "platform", "open-webui", "langbase"],
  "author": "Alexander Stoffa",
  "license": "MIT",
  "devDependencies": {
    "@playwright/test": "^1.40.0"
  }
}
EOL
fi

# Install Node.js dependencies
echo "📦 Installing Node.js dependencies..."
npm install

# Create environment template
if [ ! -f .env.example ]; then
    echo "📝 Creating environment template..."
    cat > .env.example << EOL
# Langbase Configuration
LANGBASE_API_KEY=your_langbase_api_key_here

# Open WebUI Configuration
OLLAMA_BASE_URL=http://localhost:11434

# Development Configuration
DEBUG=true
LOG_LEVEL=info

# Playwright Configuration
PLAYWRIGHT_BROWSER=chromium
EOL
fi

echo ""
echo "🎉 Development environment setup complete!"
echo ""
echo "📋 Next steps:"
echo "1. Copy .env.example to .env and add your API keys"
echo "2. Choose your first adventure:"
echo "   • Run 'npm run setup:openwebui' to start Open WebUI"
echo "   • Visit https://chai.new to explore agent prototyping"
echo "   • Create a Langbase account at https://langbase.com"
echo ""
echo "3. Activate your Python environment:"
echo "   source venv/bin/activate"
echo ""
echo "Happy building! 🚀" 