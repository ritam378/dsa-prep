#!/bin/bash

# Coverage Check Script
# Runs tests and checks if coverage meets minimum threshold

set -e

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

COVERAGE_THRESHOLD=80

echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}Coverage Analysis${NC}"
echo -e "${GREEN}========================================${NC}\n"

# Check if pytest-cov is installed
if ! python -c "import pytest_cov" &> /dev/null; then
    echo -e "${RED}Error: pytest-cov is not installed${NC}"
    echo "Please install it with: pip install pytest-cov"
    exit 1
fi

echo -e "${YELLOW}Running tests with coverage analysis...${NC}\n"

# Run tests with coverage
pytest tests/ \
    --cov=src/dsa \
    --cov-report=html \
    --cov-report=term-missing \
    --cov-report=json \
    --cov-fail-under=$COVERAGE_THRESHOLD

if [ $? -eq 0 ]; then
    echo -e "\n${GREEN}✓ Coverage meets minimum threshold of ${COVERAGE_THRESHOLD}%${NC}"
    echo -e "${GREEN}✓ HTML report: htmlcov/index.html${NC}"
else
    echo -e "\n${RED}✗ Coverage is below minimum threshold of ${COVERAGE_THRESHOLD}%${NC}"
    echo -e "${YELLOW}Please add more tests to improve coverage${NC}"
    exit 1
fi

# Extract coverage percentage from JSON report
if [ -f "coverage.json" ]; then
    COVERAGE=$(python -c "import json; print(json.load(open('coverage.json'))['totals']['percent_covered'])")
    echo -e "${GREEN}Current coverage: ${COVERAGE}%${NC}"
fi

echo -e "\n${GREEN}========================================${NC}"
echo -e "${GREEN}Coverage check completed!${NC}"
echo -e "${GREEN}========================================${NC}"
