# retworkx comparison benchmarks

This repository contains the benchmarks for the benchmarks section of the
the retworkx paper in JOSS

## Running benchmarks

A bash script entry point `run_benchmarks.sh` is included to download all the
data and run the benchmarks for all the compared graph frameworks. However,
to run the graph-tool benchmarks you will need to install graph-tool manually.
Locally I did this from source for the results in `results/` but they also
provide a docker image and anaconda's conda-forge repository includes a package
(I didn't use these since everything else was run with system python in isolated
venvs).

TODO

- Add benchmarks for additional algorithms (probably using different data sets)

## Hosted csv results

The `results/` directory contains the preliminary data from running on some
of the graphs. These were all run on the same environment with an i7-6900k with
128GB of DDR4 3200MHz RAM running Python 3.9.7 from the Arch Linux package
repository with Linux kernel 5.11.14-arch1-1.

The following versions of the graph libraries being benchmarked were used:

- retworkx 0.10.2
- python-igraph 0.9.6
- networkx 2.6.3
- graph-tool 2.43 (with boost 1.76)

These were all installed from the packages available on PyPI using pip, with
the exception of graph-tool which is not packaged on PyPI and that was compiled
from the source tarball using the default options (using ./configure && make).
