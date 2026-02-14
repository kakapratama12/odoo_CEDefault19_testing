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
mkdir -p config
mkdir -p nginx

# List of OCA repositories to clone (19.0 branch)
start_dir=$(pwd)
REPOS=(
    "https://github.com/OCA/mis-builder.git"
    "https://github.com/OCA/account-financial-reporting.git"
    "https://github.com/OCA/account-reconcile.git"
    "https://github.com/OCA/reporting-engine.git"
    "https://github.com/OCA/server-tools.git"
    "https://github.com/OCA/server-ux.git"
)

echo -e "${YELLOW}📦 Cloning OCA addons into addons/ directory...${NC}"

cd addons

for repo_url in "${REPOS[@]}"; do
    repo_name=$(basename "$repo_url" .git)
    
    if [ -d "$repo_name" ]; then
        echo "  Checking $repo_name..."
        if [ -d "$repo_name/.git" ]; then
            echo "    Git repo exists, pulling latest..."
            git -C "$repo_name" pull origin 19.0 || echo -e "${YELLOW}    ⚠️  Pull failed or branch 19.0 not found for $repo_name${NC}"
        else
            echo -e "${YELLOW}    ⚠️  Directory $repo_name exists but is not a git repo. Skipping.${NC}"
        fi
    else
        echo "  Cloning $repo_name..."
        git clone --depth 1 --branch 19.0 "$repo_url" "$repo_name"
    fi
done

cd "$start_dir"

# Create .env from template if not exists
if [ ! -f ".env" ]; then
    echo -e "${YELLOW}📄 Creating .env from template...${NC}"
    cp .env.example .env
    echo "  ⚠️  Remember to update passwords in .env!"
fi

echo ""
echo -e "${GREEN}✅ Setup complete!${NC}"
echo ""
echo "Next steps for VPS Deployment:"
echo "  1. Run this script: ./setup.sh"
echo "  2. Restart Odoo to load new addons: docker compose restart odoo"
echo "  3. Log in to Odoo as Admin"
echo "  4. Go to Apps -> Update Apps List"
echo "  5. Install 'Default Odoo 19 CE by Odi' (mis_financial_reports)"
echo ""
