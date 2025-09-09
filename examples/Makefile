.PHONY: list test-calculator test-file-processor test-interactive-calculator test-all clean help

# Default target - list all available test cases
list:
	@echo "Available test cases:"
	@echo "  calculator            - Test the calculator script functionality"
	@echo "  file-processor        - Test the file processor script functionality"
	@echo "  interactive-calculator - Test the interactive calculator with pexpect"
	@echo "  all                   - Run all test cases"
	@echo ""
	@echo "Usage:"
	@echo "  make test-calculator             # Run calculator tests"
	@echo "  make test-file-processor         # Run file processor tests"
	@echo "  make test-interactive-calculator # Run interactive calculator tests"
	@echo "  make test-all                   # Run all tests"
	@echo "  make clean                      # Clean up test artifacts"

# Test the calculator script
test-calculator:
	@echo "Running calculator tests..."
	../shellspec.py --verbose calculator_spec.txt

# Test the file processor script
test-file-processor:
	@echo "Running file processor tests..."
	../shellspec.py --verbose file_processor_spec.txt

# Test the interactive calculator script with pexpect
test-interactive-calculator:
	@echo "Running interactive calculator tests..."
	../shellspec.py --verbose interactive_calculator_spec.txt

# Run all tests
test-all: test-calculator test-file-processor test-interactive-calculator
	@echo "All tests completed!"

# Clean up test artifacts
clean:
	@echo "Cleaning up test artifacts..."
	rm -f test_sample.txt test_sample.txt.bak empty_file.txt single_word.txt
	@echo "Cleanup completed!"

# Show help
help: list