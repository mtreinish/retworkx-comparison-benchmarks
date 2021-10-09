#!/usr/bin/env python3

import csv
import statistics

import matplotlib.pyplot as plt

try:
    import seaborn as sns
    HAS_SNS = True
except ImportError:
    HAS_SNS = False
    print("Skipping seaborn import (graphs will have different theme)")

try:
    import tikzplotlib
    HAS_TIKZ = True
except:
    HAS_TIKZ = False
    print("Skipping seaborn import (no TikZ output will be generated)")

import numpy as np



def creation_time_graph():
    # Only use slower larger datasets, the following is the full list:
    # single_source_shortest_files = [
    #     'USA-road-1.USA', 'USA-road-d.NY', 'USA-road-d.USA', 'USA-road-t.NY',
    #     'USA-road-t.USA', 'rome99.gr'
    # ]
    single_source_shortest_files = [
        "USA-road-1.USA",
        "USA-road-d.USA",
        "USA-road-t.USA",
    ]
    retworkx_times = []
    networkx_times = []
    igraph_times = []
    graph_tools_times = []
    for file in single_source_shortest_files:
        retworkx_file = "retworkx_" + file + ".csv"
        with open(retworkx_file) as csvfile:
            data_reader = csv.reader(csvfile)
            for row in data_reader:
                if row[0] == "Creation":
                    retworkx_times.append(statistics.mean([float(x) for x in row[1:]]))
        networkx_file = "networkx_" + file + ".csv"
        with open(networkx_file) as csvfile:
            data_reader = csv.reader(csvfile)
            for row in data_reader:
                if row[0] == "Creation":
                    networkx_times.append(statistics.mean([float(x) for x in row[1:]]))
        igraph_file = "igraph_" + file + ".csv"
        with open(igraph_file) as csvfile:
            data_reader = csv.reader(csvfile)
            for row in data_reader:
                if row[0] == "Creation":
                    igraph_times.append(statistics.mean([float(x) for x in row[1:]]))
        graph_tools_file = "graph-tool_" + file + ".csv"
        with open(graph_tools_file) as csvfile:
            data_reader = csv.reader(csvfile)
            for row in data_reader:
                if row[0] == "Creation":
                    graph_tools_times.append(
                        statistics.mean([float(x) for x in row[1:]])
                    )
    x = np.arange(len(single_source_shortest_files))
    width = 0.175
    if HAS_SNS:
        sns.set_theme()
    fig, ax = plt.subplots()
    retworkx_rects = ax.bar(x - 3 * width / 2, retworkx_times, width, label="retworkx")
    networkx_rects = ax.bar(x - width / 2, networkx_times, width, label="NetworkX")
    igraph_rects = ax.bar(x + width / 2, igraph_times, width, label="igraph")
    graph_tools_rects = ax.bar(
        x + 3 * width / 2, graph_tools_times, width, label="graph-tool"
    )

    ax.set_ylabel("Runtime (sec.)")
    ax.set_title("Time to create a weighted directed graph")
    ax.set_xlabel("Data File")
    ax.set_xticks(x)
    ax.set_xticklabels(single_source_shortest_files)
    ax.legend()

    ax.bar_label(retworkx_rects, padding=3)
    ax.bar_label(networkx_rects, padding=3)
    ax.bar_label(igraph_rects, padding=3)
    ax.bar_label(graph_tools_rects, padding=3)
    fig.tight_layout()
    fig.savefig("creation.png")

    if HAS_TIKZ:
        tikzplotlib.save("creation.tex")


def single_source_graph():
    # Only use slower larger datasets, the following is the full list:
    # single_source_shortest_files = [
    #     'USA-road-1.USA', 'USA-road-d.NY', 'USA-road-d.USA', 'USA-road-t.NY',
    #     'USA-road-t.USA', 'rome99.gr'
    # ]
    single_source_shortest_files = [
        "USA-road-1.USA",
        "USA-road-d.USA",
        "USA-road-t.USA",
    ]
    retworkx_times = []
    networkx_times = []
    igraph_times = []
    graph_tools_times = []
    for file in single_source_shortest_files:
        retworkx_file = "retworkx_" + file + ".csv"
        with open(retworkx_file) as csvfile:
            data_reader = csv.reader(csvfile)
            for row in data_reader:
                if row[0] == "Single Source":
                    retworkx_times.append(statistics.mean([float(x) for x in row[1:]]))
        networkx_file = "networkx_" + file + ".csv"
        with open(networkx_file) as csvfile:
            data_reader = csv.reader(csvfile)
            for row in data_reader:
                if row[0] == "Single Source":
                    networkx_times.append(statistics.mean([float(x) for x in row[1:]]))
        igraph_file = "igraph_" + file + ".csv"
        with open(igraph_file) as csvfile:
            data_reader = csv.reader(csvfile)
            for row in data_reader:
                if row[0] == "Single Source":
                    igraph_times.append(statistics.mean([float(x) for x in row[1:]]))
        graph_tools_file = "graph-tool_" + file + ".csv"
        with open(graph_tools_file) as csvfile:
            data_reader = csv.reader(csvfile)
            for row in data_reader:
                if row[0] == "Single Source":
                    graph_tools_times.append(
                        statistics.mean([float(x) for x in row[1:]])
                    )
    x = np.arange(len(single_source_shortest_files))
    width = 0.175
    if HAS_SNS:
        sns.set_theme()
    fig, ax = plt.subplots()
    retworkx_rects = ax.bar(x - 3 * width / 2, retworkx_times, width, label="retworkx")
    networkx_rects = ax.bar(x - width / 2, networkx_times, width, label="NetworkX")
    igraph_rects = ax.bar(x + width / 2, igraph_times, width, label="igraph")
    graph_tools_rects = ax.bar(
        x + 3 * width / 2, graph_tools_times, width, label="graph-tool"
    )

    ax.set_ylabel("Runtime (sec.)")
    ax.set_title("Single Source Shortest path between 2 nodes")
    ax.set_xlabel("Data File")
    ax.set_xticks(x)
    ax.set_xticklabels(single_source_shortest_files)
    ax.legend()

    ax.bar_label(retworkx_rects, padding=3)
    ax.bar_label(networkx_rects, padding=3)
    ax.bar_label(igraph_rects, padding=3)
    ax.bar_label(graph_tools_rects, padding=3)
    fig.tight_layout()
    fig.savefig("single_source_shortest_path.png")

    if HAS_TIKZ:
        tikzplotlib.save("single_source_shortest_path.tex")


def single_source_graph_NY():
    single_source_shortest_files = [
        "USA-road-d.NY",
        "USA-road-t.NY",
    ]
    retworkx_times = []
    networkx_times = []
    igraph_times = []
    graph_tools_times = []
    for file in single_source_shortest_files:
        retworkx_file = "retworkx_" + file + ".csv"
        with open(retworkx_file) as csvfile:
            data_reader = csv.reader(csvfile)
            for row in data_reader:
                if row[0] == "Single Source":
                    retworkx_times.append(statistics.mean([float(x) for x in row[1:]]))
        networkx_file = "networkx_" + file + ".csv"
        with open(networkx_file) as csvfile:
            data_reader = csv.reader(csvfile)
            for row in data_reader:
                if row[0] == "Single Source":
                    networkx_times.append(statistics.mean([float(x) for x in row[1:]]))
        igraph_file = "igraph_" + file + ".csv"
        with open(igraph_file) as csvfile:
            data_reader = csv.reader(csvfile)
            for row in data_reader:
                if row[0] == "Single Source":
                    igraph_times.append(statistics.mean([float(x) for x in row[1:]]))
        graph_tools_file = "graph-tool_" + file + ".csv"
        with open(graph_tools_file) as csvfile:
            data_reader = csv.reader(csvfile)
            for row in data_reader:
                if row[0] == "Single Source":
                    graph_tools_times.append(
                        statistics.mean([float(x) for x in row[1:]])
                    )
    x = np.arange(len(single_source_shortest_files))
    width = 0.2333
    if HAS_SNS:
        sns.set_theme()
    fig, ax = plt.subplots()
    retworkx_rects = ax.bar(x - 3 * width / 2, retworkx_times, width, label="retworkx")
    networkx_rects = ax.bar(x - width / 2, networkx_times, width, label="NetworkX")
    igraph_rects = ax.bar(x + width / 2, igraph_times, width, label="igraph")
    graph_tools_rects = ax.bar(
        x + 3 * width / 2, graph_tools_times, width, label="graph-tool"
    )

    ax.set_ylabel("Runtime (sec.)")
    ax.set_title("Single Source Shortest path between 2 nodes")
    ax.set_xlabel("Data File")
    ax.set_xticks(x)
    ax.set_xticklabels(single_source_shortest_files)
    ax.legend()

    ax.bar_label(retworkx_rects, padding=3)
    ax.bar_label(networkx_rects, padding=3)
    ax.bar_label(igraph_rects, padding=3)
    ax.bar_label(graph_tools_rects, padding=3)
    fig.tight_layout()
    fig.savefig("single_source_shortest_path_2.png")

    if HAS_TIKZ:
        tikzplotlib.save("single_source_shortest_path_2.tex")


def all_pair_graph():
    all_pair_files = ["rome99.gr"]
    all_pair_libs = ["retworkx", "networkx", "igraph"]
    retworkx_times = []
    networkx_times = []
    igraph_times = []
    graph_tools_times = []
    for file in all_pair_files:
        retworkx_file = "retworkx_" + file + ".csv"
        with open(retworkx_file) as csvfile:
            data_reader = csv.reader(csvfile)
            for row in data_reader:
                if row[0] == "All Pairs Shortest Path Length":
                    retworkx_times.append(statistics.mean([float(x) for x in row[1:]]))
        networkx_file = "networkx_" + file + ".csv"
        with open(networkx_file) as csvfile:
            data_reader = csv.reader(csvfile)
            for row in data_reader:
                if row[0] == "All Pairs Shortest Path Length":
                    networkx_times.append(statistics.mean([float(x) for x in row[1:]]))
        igraph_file = "igraph_" + file + ".csv"
        with open(igraph_file) as csvfile:
            data_reader = csv.reader(csvfile)
            for row in data_reader:
                if row[0] == "All Pairs Shortest Path Length":
                    igraph_times.append(statistics.mean([float(x) for x in row[1:]]))
        graph_tools_file = "graph-tool_" + file + ".csv"
        with open(graph_tools_file) as csvfile:
            data_reader = csv.reader(csvfile)
            for row in data_reader:
                if row[0] == "All Pairs Shortest Path Length":
                    graph_tools_times.append(
                        statistics.mean([float(x) for x in row[1:]])
                    )
    x = np.arange(len(all_pair_files))
    width = 0.2333
    if HAS_SNS:
        sns.set_theme()
    fig, ax = plt.subplots()
    retworkx_rects = ax.bar(x - 3 * width / 2, retworkx_times, width, label="retworkx")
    networkx_rects = ax.bar(x - width / 2, networkx_times, width, label="NetworkX")
    igraph_rects = ax.bar(x + width / 2, igraph_times, width, label="igraph")
    graph_tools_rects = ax.bar(
        x + 3 * width / 2, graph_tools_times, width, label="graph-tool"
    )

    ax.set_ylabel("Runtime (sec.)")
    ax.set_title("All Pairs Shortest Path Length")
    ax.set_xlabel("Data File")
    ax.set_xticks(x)
    ax.set_xticklabels(all_pair_files)
    ax.legend()

    ax.bar_label(retworkx_rects, padding=3)
    ax.bar_label(networkx_rects, padding=3)
    ax.bar_label(igraph_rects, padding=3)
    ax.bar_label(graph_tools_rects, padding=3)
    fig.tight_layout()
    fig.savefig("all_pairs.png")

    if HAS_TIKZ:
        tikzplotlib.save("all_pairs.tex")


def main():
    creation_time_graph()
    single_source_graph()
    single_source_graph_NY()
    all_pair_graph()


if __name__ == "__main__":
    main()
