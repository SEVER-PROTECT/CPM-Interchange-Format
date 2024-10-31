# CPM-Interchange-Format
This repo contains the latest Interchange Format (IF) document created by Draper Laboratory and the University of Pennsylvania for DARPA's Compartmentalization and Privilege Management (CPM) program. In addition to the PDF specification, it also contains some example files and scripts for getting started parsing and using the format.

Please send feedback or questions to Nick Roessler (nroessler@draper.com) and Andre Dehon (andre@acm.org).

## Script setup
The Python scripts included here use the `pyyaml` package. Install with `pip3 install pyyaml`.

## Contents

### `interchange_format.pdf`

This PDF contains the interchange file format specification, definitions, motivating examples, and extensions. Start here.

The current version is 1.1.

### `example_traces`

This folder contains two example traces. Traces are instances of the IF format with the runtime count extension (number of privilege uses) added.

`example_trace_1.yaml` is a small, hand-crafted example privilege trace for a fictional system.

`example_trace_2.yaml` is a trace captured from the Linux kernel from a duration of 20M instructions under the workload of running `bzip2`. It has a valid YAML structure but many limitations as it was collected by an early-stage tracing infrastructure. Notably, (1) the object and subject identifier strings do not adhere fully to the format, (2) it contains call data but no return data, and (3) not all code and objects that were present in the running system are included in the trace. This trace should be considered an example and not an accurate reflection of Linux behavior.

### `examples`

This folder contains two examples of the base IF format encoding compartmentalizations. These compartmentalization schemes are generated from automatic clustering tools running on the  `example_trace_2.yaml` input trace. The `cluster_2.yaml` compartmentalization has a maximum of 2 functions per cluster, and the `cluster_4.yaml` compartmentalization has a maximum of 4 functions per cluster.

### `read_format.py`
This simple Python script parses an IF file and prints it out. It illustrates using `pyyaml` and traversing the IF structure.

Usage: `python3 read_format.py <input-yaml>`

### `write_format.py`
This simple Python script creates an IF data structure and then writes it out as yaml. You can redirect to a file to capture as a file.

Usage: `python3 write_format.py`