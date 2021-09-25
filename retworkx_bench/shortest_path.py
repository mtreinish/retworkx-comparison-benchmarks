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

import retworkx

import gr_parser

# 126GB
MEM_SIZE = 1.26 * 10 ** 11


def main():
    path = sys.argv[1]
    graph = gr_parser.parse_gr_from_file(path)
    end_node = len(graph) - 1
    print("staring single source")
    single_source_shortest_path = []
    for _ in range(5):
        start = time.time()
        retworkx.digraph_dijkstra_shortest_path_lengths(
            graph, 0, goal=end_node, edge_cost_fn=float
        )
        stop = time.time()
        single_source_shortest_path.append(stop - start)
    all_pairs = []
    if len(graph) < 100000:
        print("all pairs")
        for i in range(5):
            start = time.time()
            retworkx.digraph_all_pairs_dijkstra_shortest_paths(graph, float)
            stop = time.time()
            all_pairs.append(stop - start)
    distance_matrix = []
    if float(len(graph)) ** 2 * 64 < MEM_SIZE:
        print("running_distance_matrix")
        for i in range(5):
            start = time.time()
            retworkx.digraph_distance_matrix(graph)
            stop = time.time()
            distance_matrix.append(stop - start)
    filename = ".".join(path.split("/")[-1].split(".")[0:2])
    with open(f"retworkx_{filename}.csv", "w") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Single Source"] + single_source_shortest_path)
        if all_pairs:
            csv_writer.writerow(["All Pairs Shortest Path Length"] + all_pairs)
        if distance_matrix:
            csv_writer.writerow(["Distance Matrix"] + distance_matrix)


if __name__ == "__main__":
    main()
