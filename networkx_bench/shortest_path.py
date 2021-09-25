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

import networkx

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
        networkx.dijkstra_path_length(graph, 0, end_node)
        stop = time.time()
        single_source_shortest_path.append(stop - start)
    all_pairs = []
    if len(graph) < 100000:
        print("all pairs")
        for i in range(5):
            start = time.time()
            dict(networkx.all_pairs_dijkstra_path_length(graph))
            stop = time.time()
            all_pairs.append(stop - start)
    filename = ".".join(path.split("/")[-1].split(".")[0:2])
    with open(f"networkx_{filename}.csv", "w") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Single Source"] + single_source_shortest_path)
        if all_pairs:
            csv_writer.writerow(["All Pairs Shortest Path Length"] + all_pairs)


if __name__ == "__main__":
    main()
