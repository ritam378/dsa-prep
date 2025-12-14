#!/bin/bash

# Setup Script
# Sets up the development environment for DSA interview prep

set -e

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}DSA Interview Prep - Setup${NC}"
echo -e "${BLUE}========================================${NC}\n"

# Check Python version
echo -e "${YELLOW}Checking Python version...${NC}"
PYTHON_VERSION=$(python --version 2>&1 | awk '{print $2}')
echo -e "Python version: ${GREEN}$PYTHON_VERSION${NC}\n"

# Check if we're in the project root
if [ ! -f "pyproject.toml" ]; then
    echo -e "${RED}Error: Please run this script from the project root directory${NC}"
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo -e "${YELLOW}Creating virtual environment...${NC}"
    python -m venv venv
    echo -e "${GREEN}✓ Virtual environment created${NC}\n"
else
    echo -e "${GREEN}✓ Virtual environment already exists${NC}\n"
fi

# Activate virtual environment
echo -e "${YELLOW}Activating virtual environment...${NC}"
source venv/bin/activate
echo -e "${GREEN}✓ Virtual environment activated${NC}\n"

# Upgrade pip
echo -e "${YELLOW}Upgrading pip...${NC}"
pip install --upgrade pip > /dev/null
echo -e "${GREEN}✓ pip upgraded${NC}\n"

# Install dependencies
echo -e "${YELLOW}Installing dependencies...${NC}"
pip install -r requirements.txt
echo -e "${GREEN}✓ Dependencies installed${NC}\n"

# Make scripts executable
echo -e "${YELLOW}Making scripts executable...${NC}"
chmod +x scripts/*.sh
echo -e "${GREEN}✓ Scripts are now executable${NC}\n"

# Run a quick test
echo -e "${YELLOW}Running a quick test to verify setup...${NC}"
if python -c "import pytest; import sys; sys.path.insert(0, 'src'); from dsa.core_patterns import two_pointer" 2>/dev/null; then
    echo -e "${GREEN}✓ Import test passed${NC}\n"
else
    echo -e "${RED}✗ Import test failed${NC}"
    echo -e "${YELLOW}Please check your Python path and dependencies${NC}\n"
fi

echo -e "${BLUE}========================================${NC}"
echo -e "${GREEN}Setup completed successfully!${NC}"
echo -e "${BLUE}========================================${NC}\n"

echo -e "${YELLOW}Next steps:${NC}"
echo -e "1. Activate virtual environment: ${GREEN}source venv/bin/activate${NC}"
echo -e "2. Run tests: ${GREEN}./scripts/run_tests.sh${NC}"
echo -e "3. Check coverage: ${GREEN}./scripts/check_coverage.sh${NC}"
echo -e "4. Start solving problems: ${GREEN}Check problems/ directory${NC}"
echo -e "5. Read the docs: ${GREEN}docs/LEARNING_GUIDE.md${NC}\n"

echo -e "${GREEN}Happy coding!${NC}"
