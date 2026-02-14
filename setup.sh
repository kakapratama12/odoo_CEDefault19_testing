#!/bin/bash
# =====================================================
# Odoo 19 CE - Initial Setup Script
# =====================================================
# This script clones OCA addons and prepares the project

set -e

echo "🔧 Odoo 19 CE - Setup Script"
echo "============================="

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Create directories
echo -e "${YELLOW}📁 Creating directories...${NC}"
mkdir -p addons
mkdir -p oca-addons
mkdir -p config
mkdir -p nginx

# Clone OCA addons (19.0 branch)
echo -e "${YELLOW}📦 Cloning OCA account-financial-reporting (19.0)...${NC}"
if [ -d "oca-addons/account-financial-reporting" ]; then
    echo "  Already exists, pulling latest..."
    cd oca-addons/account-financial-reporting && git pull origin 19.0 && cd ../..
else
    git clone --depth 1 --branch 19.0 https://github.com/OCA/account-financial-reporting.git oca-addons/account-financial-reporting
fi

echo -e "${YELLOW}📦 Cloning OCA account-financial-tools (19.0)...${NC}"
if [ -d "oca-addons/account-financial-tools" ]; then
    echo "  Already exists, pulling latest..."
    cd oca-addons/account-financial-tools && git pull origin 19.0 && cd ../..
else
    git clone --depth 1 --branch 19.0 https://github.com/OCA/account-financial-tools.git oca-addons/account-financial-tools
fi

# Create .env from template if not exists
if [ ! -f ".env" ]; then
    echo -e "${YELLOW}📄 Creating .env from template...${NC}"
    cp .env.example .env
    echo "  ⚠️  Remember to update passwords in .env!"
fi

echo ""
echo -e "${GREEN}✅ Setup complete!${NC}"
echo ""
echo "Next steps:"
echo "  1. Review and update .env with your preferred passwords"
echo "  2. Review config/odoo.conf (update admin_passwd)"
echo "  3. Start the containers:"
echo "     docker compose up -d"
echo "  4. Open http://localhost:8069 in your browser"
echo "  5. Create a database and install your modules"
echo ""
echo "For production deployment:"
echo "  docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d"
