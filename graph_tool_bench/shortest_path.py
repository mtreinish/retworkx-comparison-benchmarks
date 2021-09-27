# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

import csv
import sys
import time

import graph_tool
import graph_tool.topology

import gr_parser

# 126GB
MEM_SIZE = 1.26 * 10 ** 11


def main():
    path = sys.argv[1]
    creation = []
    for _ in range(5):
        start = time.time()
        graph = gr_parser.parse_gr_from_file(path)
        stop = time.time()
        creation.append(stop - start)
    print(graph.edge_properties)
    edge_weights = graph.edge_properties["weights"]
    end_node = graph.num_vertices() - 1
    print("staring single source")
    single_source_shortest_path = []
    for _ in range(5):
        start = time.time()
        graph_tool.topology.shortest_distance(
            graph, source=0, target=end_node, weights=edge_weights
        )
        stop = time.time()
        single_source_shortest_path.append(stop - start)
    all_pairs = []
    if graph.num_vertices() < 100000:
        print("all pairs")
        for i in range(5):
            start = time.time()
            graph_tool.topology.shortest_distance(graph, weights=edge_weights)
            stop = time.time()
            all_pairs.append(stop - start)
    filename = ".".join(path.split("/")[-1].split(".")[0:2])
    with open(f"graph-tool_{filename}.csv", "w") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Creation"] + creation)
        csv_writer.writerow(["Single Source"] + single_source_shortest_path)
        if all_pairs:
            csv_writer.writerow(["All Pairs Shortest Path Length"] + all_pairs)


if __name__ == "__main__":
    main()
