# CPM-Interchange-Format
This repo contains the latest Interchange Format (IF) document created by Draper Laboratory and the University of Pennsylvania for DARPA's Compartmentalization and Privilege Management (CPM) program. In addition to the PDF specification, it also contains some example files and scripts for getting started parsing and using the format.

Please send feedback or questions to Nick Roessler (nroessler@draper.com) and Andre Dehon (andre@acm.org).

## Script setup
The Python scripts included here use the `pyyaml` package. Install with `pip3 install pyyaml`.

## Contents

### `interchange_format.pdf`

This PDF contains the interchange file format specification, definitions, motivating examples, and extensions. Start here.

The current version is 1.3. 

Changes introduced in 1.3 include:
1. A new object ID syntax (Section 5.2)
2. A new informal grammar (Section 7)
3. Changes to syntax for none/all representations (Section 7.1)
4. A subsetting specification (Section 8)

### `example_traces`

This folder contains two example traces. Traces are instances of the IF format with the runtime count extension (number of privilege uses) added.

`password_example_trace.yaml` is the password example from the IF pdf document. It has some synthetic counts added to it.

`linux_example_trace.yaml` is a trace that was produced by aggregating 10 runs of BusyBox running `bzip2` for about 250M instructions each. It has a valid YAML structure but many limitations as it was collected by an early-stage tracing infrastructure. Notably, (1) the object and subject identifier strings do not adhere fully to the format, (2) it contains call data but no return data, and (3) not all code and objects that were present in the running system are included in the trace. This trace should be considered an example and not an accurate reflection of Linux behavior.

### `examples`

This folder contains some example IF yamls for encoding compartmentalizations.

`password_example.yaml` is a manually crated compartmentalization created for the `password_example_trace.yaml` trace. It places the three functions related to password checking together in compartment, and the `main` function in another.

`linux_2.yaml` is a compartmentalization produced from automatic clustering tools on the `linux_example_trace.yaml` data. It is run with a maximum number of functions per compartment of 2.

`linux_4.yaml` is a compartmentalization produced from automatic clustering tools on the `linux_example_trace.yaml` data. It is run with a maximum number of functions per compartment of 4.

### `read_format.py`
This simple Python script parses an IF file and prints it out. It illustrates using `pyyaml` and traversing the IF structure.

Usage: `python3 read_format.py <input-yaml>`

### `write_format.py`
This simple Python script creates an IF data structure and then writes it out as yaml. You can redirect to a file to capture as a file.

Usage: `python3 write_format.py`
