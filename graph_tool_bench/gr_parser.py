# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

import gzip

import graph_tool

"""Parser for graph specification files from the 9th DIMACS challenge

This module contains tools for parsing the graph specification files from
the 9th DIMACS challenge which are documented here:

http://users.diag.uniroma1.it/challenge9/format.shtml
"""


def parse_gr_from_file(path, directed=True):
    """Parse a graph specification file and return a retworkx graph object

    :param str path: A path to the graph specification file to parse
    :param bool directed: Whether the returned graph is directed or not
        if set to True a PyDAG function is returned (with cycle_check set to
        False so it's a PyDiGraph) to maximize compatibility with functions
        that predate the PyDiGraph class

    :returns: A retworkx PyGraph or PyDAG object representing the input gr
        file
    """
    return_graph = graph_tool.Graph(directed=directed)
    edge_weight = return_graph.new_edge_property("double")
    return_graph.edge_properties["weights"] = edge_weight
    nodes_added = False
    if path.endswith("gz"):
        open_call = gzip.open
    else:
        open_call = open
    with open_call(path, "rt") as fd:
        for line in fd:
            if line.startswith("c"):
                continue
            if line.startswith("p"):
                num_nodes = int(line.split(" ")[2])
                return_graph.add_vertex(num_nodes)
                nodes_added = True
            elif line.startswith("a"):
                if not nodes_added:
                    raise Exception(
                        "Invalid gr file, program line not first non-comment " "line."
                    )
                components = line.split(" ")
                u = int(components[1]) - 1
                v = int(components[2]) - 1
                weight = float(components[3])
                edge_index = return_graph.add_edge(u, v)
                edge_weight[edge_index] = weight
            else:
                raise Exception(
                    "Invalid gr file line: '%s' doesn't start with a valid " "token"
                )

    return return_graph
