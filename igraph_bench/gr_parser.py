# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

import gzip

import igraph
import networkx

"""Parser for graph specification files from the 9th DIMACS challenge

This module contains tools for parsing the graph specification files from
the 9th DIMACS challenge which are documented here:

http://users.diag.uniroma1.it/challenge9/format.shtml
"""


def parse_gr_from_file(path, directed=True):
    """Parse a graph specification file and return a retworkx graph object

    :param str path: A path to the graph specification file to parse
    :param bool directed: Whether the returned graph is directed or not
        if set to True a DiGraph is returned

    :returns: A retworkx Graph or DiGraph object representing the input gr
        file
    """
    if not directed:
        return_graph = networkx.Graph()
    else:
        return_graph = networkx.DiGraph()

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
                return_graph.add_nodes_from(range(num_nodes))
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
                return_graph.add_edge(u, v, weight=weight)
            else:
                raise Exception(
                    "Invalid gr file line: '%s' doesn't start with a valid " "token"
                )
    return igraph.Graph.from_networkx(return_graph)
