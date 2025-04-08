# CPM IF Tools

The tools described here aid in CPM IF-based analysis, evaluation, validation,
and general use. This directory provides an overview and description of tools
and scripts for downloading and using them.

## Tools

### [CPM IF Tools](https://github.com/Serenitix/cpm_if_tools)

Tool suite for representing, analyzing, translating, and evaluating various
elements of the CPM IF and its use. Support and maintenance provided by
Serenitix.

## How to Build the Tool Manually

1. Clone the repository:

```
git clone https://github.com/Serenitix/cpm_if_tools.git
cd cpm_if_tools
```

2. Build the tool using Cargo:

```
cargo build --release
```

3. Run the tool:

```
./target/release/cpm_if_tool --help
```

4. Optionally, run tests to validate functionality:

```
cargo test
```