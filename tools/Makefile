// SPDX-License-Identifier: MIT
//
// MIT License
//
// © 2025 Nathan Dautenhahn & Serenitix LLC
//
// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included in
// all copies or substantial portions of the Software.

# Default target: Show available commands
.PHONY: help
help:
	@echo "Available commands:"
	@echo "  make [setup|clean|test|run]-all        - Set up all tools"
	@echo "  make [setup|clean|test|run]-cpm_if     - Set up, clean, test, run the CPM IF tool"

# Rule to set up all tools
.PHONY: setup-all
setup-all: setup-cpm_if
	@echo "All tools have been set up."

# Rule to set up the CPM IF tool
.PHONY: setup-cpm_if
setup-cpm_if:
	@echo "Setting up CPM IF tool..."
	@if [ ! -d "cpm_if_tools" ]; then \
		git clone https://github.com/Serenitix/cpm_if_tools.git; \
	fi
	cd cpm_if_tools && cargo build --release && cargo test
	@echo "CPM IF tool has been set up."

# Rule to clean the CPM IF tool
.PHONY: clean-cpm_if
clean-cpm_if:
	@echo "Cleaning CPM IF tool..."
	@if [ -d "cpm_if_tools" ]; then \
		cd cpm_if_tools && cargo clean; \
	fi
	@echo "CPM IF tool has been cleaned."

# Rule to test the CPM IF tool
.PHONY: test-cpm_if
test-cpm_if:
	@echo "Running tests for CPM IF tool..."
	@if [ -d "cpm_if_tools" ]; then \
		cd cpm_if_tools && cargo test; \
	else \
		echo "CPM IF tool is not set up. Run 'make setup-cpm_if' first."; \
	fi

# Rule to run the CPM IF tool
.PHONY: run-cpm_if
run-cpm_if:
	@echo "Running CPM IF tool TBD, please see tool README..."