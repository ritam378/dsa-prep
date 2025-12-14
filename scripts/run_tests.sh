#!/bin/bash

# Run Tests Script
# This script runs the test suite with various options

set -e  # Exit on error

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}DSA Interview Prep - Test Runner${NC}"
echo -e "${GREEN}========================================${NC}\n"

# Check if pytest is installed
if ! command -v pytest &> /dev/null; then
    echo -e "${RED}Error: pytest is not installed${NC}"
    echo "Please install it with: pip install -r requirements.txt"
    exit 1
fi

# Default: run all tests
if [ $# -eq 0 ]; then
    echo -e "${YELLOW}Running all tests...${NC}\n"
    pytest tests/ -v
else
    case "$1" in
        --coverage)
            echo -e "${YELLOW}Running tests with coverage report...${NC}\n"
            pytest tests/ --cov=src/dsa --cov-report=html --cov-report=term-missing -v
            echo -e "\n${GREEN}Coverage report generated in htmlcov/index.html${NC}"
            ;;
        --fast)
            echo -e "${YELLOW}Running tests without verbose output...${NC}\n"
            pytest tests/
            ;;
        --pattern)
            if [ -z "$2" ]; then
                echo -e "${RED}Error: Please specify pattern name${NC}"
                echo "Usage: ./run_tests.sh --pattern two_pointer"
                exit 1
            fi
            echo -e "${YELLOW}Running tests for pattern: $2${NC}\n"
            pytest tests/test_core_patterns/test_$2.py -v 2>/dev/null || \
            pytest tests/test_advanced_patterns/test_$2.py -v 2>/dev/null || \
            pytest tests/test_specialized_patterns/test_$2.py -v 2>/dev/null || \
            echo -e "${RED}No tests found for pattern: $2${NC}"
            ;;
        --data-structures)
            echo -e "${YELLOW}Running data structure tests...${NC}\n"
            pytest tests/test_data_structures/ -v
            ;;
        --core)
            echo -e "${YELLOW}Running core pattern tests...${NC}\n"
            pytest tests/test_core_patterns/ -v
            ;;
        --advanced)
            echo -e "${YELLOW}Running advanced pattern tests...${NC}\n"
            pytest tests/test_advanced_patterns/ -v
            ;;
        --help)
            echo "Usage: ./run_tests.sh [OPTION]"
            echo ""
            echo "Options:"
            echo "  (no args)           Run all tests with verbose output"
            echo "  --coverage          Run tests with coverage report"
            echo "  --fast              Run tests without verbose output"
            echo "  --pattern NAME      Run tests for specific pattern"
            echo "  --data-structures   Run data structure tests only"
            echo "  --core              Run core pattern tests only"
            echo "  --advanced          Run advanced pattern tests only"
            echo "  --help              Show this help message"
            ;;
        *)
            echo -e "${RED}Unknown option: $1${NC}"
            echo "Use --help to see available options"
            exit 1
            ;;
    esac
fi

echo -e "\n${GREEN}========================================${NC}"
echo -e "${GREEN}Tests completed!${NC}"
echo -e "${GREEN}========================================${NC}"
