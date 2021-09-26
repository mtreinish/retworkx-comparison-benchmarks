#!/bin/bash

# Download shortest path data sets from 9th dimacs challenge
mkdir -p dimacs_9/distance dimacs_9/time
pushd dimacs_9
 Challenge benchmark
wget http://www.dis.uniroma1.it/%7echallenge9/temp/USA-road-1.USA.gr.gz
pushd distance
wget https://users.diag.uniroma1.it/challenge9/data/USA-road-d/USA-road-d.USA.gr.gz
wget https://users.diag.uniroma1.it/challenge9/data/USA-road-d/USA-road-d.NY.gr.gz
wget https://users.diag.uniroma1.it/challenge9/data/rome/rome99.gr
popd
pushd time
wget https://users.diag.uniroma1.it/challenge9/data/USA-road-t/USA-road-t.USA.gr.gz
wget https://users.diag.uniroma1.it/challenge9/data/USA-road-t/USA-road-t.NY.gr.gz
popd
popd
# Build venvs
virtualenv retworkx_venv
retworkx_venv/bin/pip install -U retworkx
virtualenv networkx_venv
networkx_venv/bin/pip install -U networkx
virtualenv igraph_venv
igraph_venv/bin/pip install -U python-igraph
virtualenv snap_venv
snap_venv/bin/pip install -U snap-stanford

for gr_file in dimacs_9/USA-road-1.USA.gr.gz dimacs_9/distance/USA-road-d.USA.gr.gz dimacs_9/distance/USA-road-d.NY.gr.gz dimacs_9/time/USA-road-t.USA.gr.gz dimacs_9/time/USA-road-t.NY.gr.gz ; do
    retworkx_venv/bin/python retworkx_bench/shortest_path.py $gr_file
done

mkdir results
mv *csv results/