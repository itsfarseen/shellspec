SHELLSPEC = ../shellspec.py --verbose

SPECS = basic_spec.txt file_spec.txt interactive_spec.txt env_spec.txt snippet_spec.txt

.PHONY: all test-basic test-file test-interactive test-env test-snippet list

all: test-basic test-file test-interactive test-env test-snippet

test-basic:
	$(SHELLSPEC) basic_spec.txt

test-file:
	$(SHELLSPEC) file_spec.txt

test-interactive:
	$(SHELLSPEC) interactive_spec.txt

test-env:
	$(SHELLSPEC) env_spec.txt

test-snippet:
	$(SHELLSPEC) snippet_spec.txt

list:
	@echo "Available tests:"
	@echo "  make all"
	@echo "  make test-basic"
	@echo "  make test-file"
	@echo "  make test-interactive"
	@echo "  make test-env"
	@echo "  make test-snippet"