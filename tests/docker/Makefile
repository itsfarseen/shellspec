# Docker CI tests for different operating systems

REPO_ROOT := $(shell git rev-parse --show-toplevel)

.PHONY: ubuntu ubuntu-22 arch alpine all

ubuntu:
	@echo "=== Building Ubuntu CI Docker image ==="
	docker build -f Dockerfile.ci -t shellspec-ci-ubuntu .
	@echo "=== Running tests in Ubuntu Docker ==="
	docker run --rm \
		-v "$(REPO_ROOT):/workspace:ro" \
		shellspec-ci-ubuntu

ubuntu-22:
	@echo "=== Building Ubuntu 22.04 CI Docker image ==="
	docker build -f Dockerfile.ci-ubuntu-22 -t shellspec-ci-ubuntu-22 .
	@echo "=== Running tests in Ubuntu 22.04 Docker ==="
	docker run --rm \
		-v "$(REPO_ROOT):/workspace:ro" \
		shellspec-ci-ubuntu-22

arch:
	@echo "=== Building Arch Linux CI Docker image ==="
	docker build -f Dockerfile.ci-arch -t shellspec-ci-arch .
	@echo "=== Running tests in Arch Linux Docker ==="
	docker run --rm \
		-v "$(REPO_ROOT):/workspace:ro" \
		shellspec-ci-arch

alpine:
	@echo "=== Building Alpine Linux CI Docker image ==="
	docker build -f Dockerfile.ci-alpine -t shellspec-ci-alpine .
	@echo "=== Running tests in Alpine Linux Docker ==="
	docker run --rm \
		-v "$(REPO_ROOT):/workspace:ro" \
		shellspec-ci-alpine

all: ubuntu ubuntu-22 arch alpine