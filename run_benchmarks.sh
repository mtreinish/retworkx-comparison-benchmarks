#!/bin/bash

# Download shortest path data sets from 9th dimacs challenge
mkdir -p dimacs_9/distance dimacs_9/time
pushd dimacs_9
# Challenge benchmark
wget http://www.dis.uniroma1.it/%7echallenge9/temp/USA-road-1.USA.gr.gz
pushd distance
wget http://users.diag.uniroma1.it/challenge9/data/USA-road-d/USA-road-d.USA.gr.gz
wget http://users.diag.uniroma1.it/challenge9/data/USA-road-d/USA-road-d.NY.gr.gz
wget http://users.diag.uniroma1.it/challenge9/data/rome/rome99.gr
popd
pushd time
wget http://users.diag.uniroma1.it/challenge9/data/USA-road-t/USA-road-t.USA.gr.gz
wget http://users.diag.uniroma1.it/challenge9/data/USA-road-t/USA-road-t.NY.gr.gz
popd
popd
mkdir arg_db
pushd arg_db
wget https://mivia.unisa.it/database/graphsdb.zip
unzip graphsdb.zip
pushd graphsdb
for i in `ls *zip` ; do
    unzip $i
done
popd
popd
# Build venvs
virtualenv retworkx_venv
retworkx_venv/bin/pip install -U retworkx
virtualenv networkx_venv
networkx_venv/bin/pip install -U networkx
virtualenv igraph_venv
igraph_venv/bin/pip install -U python-igraph networkx

echo "Shortest path benchmarks"
echo "Running retworkx benchmarks"
for gr_file in dimacs_9/USA-road-1.USA.gr.gz dimacs_9/distance/USA-road-d.USA.gr.gz dimacs_9/distance/USA-road-d.NY.gr.gz dimacs_9/time/USA-road-t.USA.gr.gz dimacs_9/time/USA-road-t.NY.gr.gz dimacs_9/distance/rome99.gr; do
    retworkx_venv/bin/python retworkx_bench/shortest_path.py $gr_file
done
echo "Running NetworkX benchmarks"
for gr_file in dimacs_9/USA-road-1.USA.gr.gz dimacs_9/distance/USA-road-d.USA.gr.gz dimacs_9/distance/USA-road-d.NY.gr.gz dimacs_9/time/USA-road-t.USA.gr.gz dimacs_9/time/USA-road-t.NY.gr.gz dimacs_9/distance/rome99.gr; do
    networkx_venv/bin/python networkx_bench/shortest_path.py $gr_file
done
echo "Running igraph benchmarks"
for gr_file in dimacs_9/USA-road-1.USA.gr.gz dimacs_9/distance/USA-road-d.USA.gr.gz dimacs_9/distance/USA-road-d.NY.gr.gz dimacs_9/time/USA-road-t.USA.gr.gz dimacs_9/time/USA-road-t.NY.gr.gz dimacs_9/distance/rome99.gr; do
    igraph_venv/bin/python igraph_bench/shortest_path.py $gr_file
done
echo "Running graph-tool benchmarks"
for gr_file in dimacs_9/USA-road-1.USA.gr.gz dimacs_9/distance/USA-road-d.USA.gr.gz dimacs_9/distance/USA-road-d.NY.gr.gz dimacs_9/time/USA-road-t.USA.gr.gz dimacs_9/time/USA-road-t.NY.gr.gz dimacs_9/distance/rome99.gr; do
    python graph_tool_bench/shortest_path.py $gr_file
done
echo "Isomorphism benchmarks"
echo "Running retworkx benchmarks"
retworkx_venv/bin/python retworkx_bench/isomorphism.py arg_db/graphsdb
echo "Running NetworkX benchmarks"
networkx_venv/bin/python networkx_bench/isomorphism.py arg_db/graphsdb
echo "Running igraph benchmarks"
igraph_venv/bin/python igraph_bench/isomorphism.py arg_db/graphsdb
echo "Running graph-tool benchmarks"
python graph_tool_bench/isomorphism.py arg_db/graphsdb

# Process results
mv *csv results/
pushd results
python ../graph_results.py
