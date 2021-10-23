# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

from collections import defaultdict
import csv
import os
import statistics
import sys
import time

import igraph

import graphsdb_parser

# 126GB
MEM_SIZE = 1.26 * 10 ** 11

group_types = {
    "bvg": ["b03", "b06", "b09"],
}


def main():
    path = sys.argv[1]
    subgraph_prefix = ["si6", "si4", "si2"]
    subgraph_iso_times = defaultdict(list)
    with open(f"igraph_subgraph_iso.csv", "w") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Graph", "avg_time"])
        for prefix in subgraph_prefix:
            for group, g_types in group_types.items():
                for g_type in g_types:
                    graph_dir_path = os.path.join(path, prefix, group, g_type)
                    if not os.path.isdir(graph_dir_path):
                        continue
                    for filename in os.listdir(graph_dir_path):
                        if "B" in filename:
                            continue
                        graph_files = [filename.replace("A", "B"), filename]
                        graph_name = filename
                        graphs = []
                        for graph_file in graph_files:
                            graph_file_path = os.path.join(graph_dir_path, graph_file)
                            graphs.append(
                                graphsdb_parser.parse_unlabeled_graphdb_from_file(
                                    graph_file_path, directed=False
                                )
                            )
                        for i in range(5):
                            start = time.time()
                            res = graphs[0].subisomorphic_vf2(graphs[1])
                            stop = time.time()
                            if not res:
                                error_str = " ".join(graph_files)
                                raise Exception("%s should be isomorphic" % error_str)
                            subgraph_iso_times[graph_name].append(stop - start)
                        csv_writer.writerow(
                            [
                                graph_name,
                                statistics.mean(subgraph_iso_times[graph_name]),
                            ]
                        )


if __name__ == "__main__":
    main()
