# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

import struct

import graph_tool

"""Parser for graph file format from ARG Databse

This module contains tools for parsing the graph specification files from
the ARG Database:

https://mivia.unisa.it/datasets/graph-database/arg-database/
"""


def parse_unlabeled_graphdb_from_file(path, directed=True):
    """Parse a graph specification file and return a retworkx graph object

    :param str path: A path to the graph specification file to parse
    :param bool directed: Whether the returned graph is directed or not
        if set to True a PyDAG function is returned (with cycle_check set to
        False so it's a PyDiGraph) to maximize compatibility with functions
        that predate the PyDiGraph class

    :returns: A retworkx PyGraph or PyDAG object representing the input gr
        file
    """
    graph = graph_tool.Graph(directed=directed)
    with open(path, "rb") as graph_file:
        data = graph_file.read(2)
        num_nodes = struct.unpack("<H", data)[0]
        graph.add_vertex(num_nodes)
        for i in range(num_nodes):
            raw_edge_count = graph_file.read(2)
            edge_count = struct.unpack_from("<H", raw_edge_count)[0]
            for j in range(edge_count):
                edge_target = struct.unpack_from("<H", graph_file.read(2))[0]
                graph.add_edge(i, edge_target)
    return graph
