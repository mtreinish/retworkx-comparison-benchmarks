# retworkx comparison benchmarks

This repository contains the benchmarks for the benchmarks section of the
the retworkx paper in JOSS

## Running benchmarks

A bash script entry point `run_benchmarks.sh` is included to download all the
data and run the benchmarks for all the compared graph frameworks.

TODO

- add variant for other graph libraries
- graphing results
- Add benchmarks for additional algorithms (probably using different data sets)

## Hosted csv results

The `results/` directory contains the preliminary data from running on some
of the graphs. These were all run on the same environment with an i7-6900k with
128GB of DDR4 3200MHz RAM running Python 3.9.3 from the Arch Linux package
repository with Linux kernel 5.11.14-arch1-1.
