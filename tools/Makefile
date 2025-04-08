# Default target: Show available commands
.PHONY: help
help:
	@echo "Available commands:"
	@echo "  make setup-all       - Set up all tools"
	@echo "  make setup-cpm_if    - Set up the CPM IF tools"

# Rule to set up all tools
.PHONY: setup-all
setup-all: setup-cpm_if
	@echo "All tools have been set up."

# Rule to set up the CPM IF tool
.PHONY: setup-cpm_if
setup-cpm_if:
	@echo "Setting up CPM IF tools..."
	@if [ ! -d "cpm_if_tools" ]; then \
		git clone https://github.com/Serenitix/cpm_if_tools.git; \
	fi
	cd cpm_if_tools && cargo build --release && cargo test
	@echo "CPM IF tool has been set up."