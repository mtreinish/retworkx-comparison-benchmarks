#!/usr/bin/env python3

from collections import defaultdict
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
    width = 0.195
    if HAS_SNS:
        sns.set_theme()
    fig, ax = plt.subplots(figsize=(12.8, 4.8))
    retworkx_rects = ax.bar(x - 3 * width / 2, retworkx_times, width, label="retworkx")
    networkx_rects = ax.bar(x - width / 2, networkx_times, width, label="NetworkX")
    igraph_rects = ax.bar(x + width / 2, igraph_times, width, label="igraph")
    graph_tools_rects = ax.bar(
        x + 3 * width / 2, graph_tools_times, width, label="graph-tool"
    )

    ax.set_ylabel("Runtime (sec.)")
    ax.set_title("Time to create a weighted directed graph", fontweight="bold")
    ax.set_xlabel("Data File")
    ax.set_xticks(x)
    ax.set_xticklabels(single_source_shortest_files)
    ax.legend(loc="upper left", bbox_to_anchor=(1.01,1))

    ax.bar_label(retworkx_rects, padding=3)
    ax.bar_label(networkx_rects, padding=3)
    ax.bar_label(igraph_rects, padding=3)
    ax.bar_label(graph_tools_rects, padding=3)
    ax.set_ylim(top=np.amax(graph_tools_times)*1.15)
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
    fig, ax = plt.subplots(figsize=(7, 4.8))
    retworkx_rects = ax.bar(x - 3 * width / 2, retworkx_times, width, label="retworkx")
    networkx_rects = ax.bar(x - width / 2, networkx_times, width, label="NetworkX")
    igraph_rects = ax.bar(x + width / 2, igraph_times, width, label="igraph")
    graph_tools_rects = ax.bar(
        x + 3 * width / 2, graph_tools_times, width, label="graph-tool"
    )

    ax.set_ylabel("Runtime (sec.)")
    ax.set_title("Single Source Shortest path between 2 nodes", fontweight="bold")
    ax.set_xlabel("Data File")
    ax.set_xticks(x)
    ax.set_xticklabels(single_source_shortest_files)
    ax.set_xlim(right=np.amax(x)*1.45)
    ax.set_ylim(top=np.amax(networkx_times)*1.15)
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
    ax.set_title("Single Source Shortest path between 2 nodes", fontweight="bold")
    ax.set_xlabel("Data File")
    ax.set_xticks(x)
    ax.set_xticklabels(single_source_shortest_files)
    ax.legend(loc="upper left")

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
    fig, ax = plt.subplots(figsize=(7, 4.8))
    retworkx_rects = ax.bar(x - 3 * width / 2, retworkx_times, width, label="retworkx")
    networkx_rects = ax.bar(x - width / 2, networkx_times, width, label="NetworkX")
    igraph_rects = ax.bar(x + width / 2, igraph_times, width, label="igraph")
    graph_tools_rects = ax.bar(
        x + 3 * width / 2, graph_tools_times, width, label="graph-tool"
    )

    ax.set_ylabel("Runtime (sec.)")
    ax.set_title("All Pairs Shortest Path Length", fontweight="bold")
    ax.set_xlabel("Data File")
    ax.set_xticks(x)
    ax.set_xticklabels(all_pair_files)
    ax.set_ylim(top=np.amax(networkx_times)*1.15)
    ax.legend()

    ax.bar_label(retworkx_rects, padding=3)
    ax.bar_label(networkx_rects, padding=3)
    ax.bar_label(igraph_rects, padding=3)
    ax.bar_label(graph_tools_rects, padding=3)
    fig.tight_layout()
    fig.savefig("all_pairs.png")

    if HAS_TIKZ:
        tikzplotlib.save("all_pairs.tex")


def isomorphism_graph():
    retworkx_times = defaultdict(float)
    networkx_times = defaultdict(float)
    igraph_times = defaultdict(float)
    graph_tool_times = defaultdict(float)
    retworkx_file = "retworkx_subgraph_iso.csv"
    with open(retworkx_file) as csvfile:
        data_reader = csv.reader(csvfile)
        for row in data_reader:
            if row[0] == "Graph":
                continue
            file_prefix = row[0].split(".")[0]
            retworkx_times[file_prefix] += float(row[1])
    networkx_file = "networkx_subgraph_iso.csv"
    with open(networkx_file) as csvfile:
        data_reader = csv.reader(csvfile)
        for row in data_reader:
            if row[0] == "Graph":
                continue
            file_prefix = row[0].split(".")[0]
            networkx_times[file_prefix] += float(row[1])
    igraph_file = "igraph_subgraph_iso.csv"
    with open(igraph_file) as csvfile:
        data_reader = csv.reader(csvfile)
        for row in data_reader:
            if row[0] == "Graph":
                continue
            file_prefix = row[0].split(".")[0]
            igraph_times[file_prefix] += float(row[1])
    graph_tools_file = "graph_tool_subgraph_iso.csv"
    with open(graph_tools_file) as csvfile:
        data_reader = csv.reader(csvfile)
        for row in data_reader:
            if row[0] == "Graph":
                continue
            file_prefix = row[0].split(".")[0]
            graph_tool_times[file_prefix] += float(row[1])
    if HAS_SNS:
        sns.set_theme()
        sns.set_context("notebook", font_scale=2, rc={"lines.linewidth": 2.5})
    fig = plt.figure(figsize=(29, 22), constrained_layout=True)
    subfigs = fig.subplots(nrows=3, ncols=3)
    for i, percent in enumerate(["si6", "si4", "si2"]):
        subfig = subfigs[i]
        # subfig.suptitle(f"Subgraph is {percent[-1]}0% of graph size", fontsize=21, fontweight="bold")
        # ax = subfig.subplots(nrows=1, ncols=3)
        ax = subfigs
        for j, valence in enumerate(["b03", "b06", "b09"]):
            indices = []
            retworkx_data = []
            networkx_data = []
            igraph_data = []
            graph_tool_data = []
            for graph, point in sorted(
                retworkx_times.items(), key=lambda x: int(x[0].split("_")[-1][1:])
            ):
                if graph.startswith("%s_%s_" % (percent, valence)):
                    indices.append(int(graph.split("_")[-1][1:]))
                    retworkx_data.append(point)
                    networkx_data.append(networkx_times[graph])
                    igraph_data.append(igraph_times[graph])
                    graph_tool_data.append(graph_tool_times[graph])

            x = np.arange(len(indices))
            ax[i, j].plot(retworkx_data, label="retworkx")
            ax[i, j].plot(networkx_data, label="NetworkX")
            ax[i, j].plot(igraph_data, label="igraph")
            ax[i, j].plot(graph_tool_data, label="graph-tool")
            ax[i, j].set_ylabel("Sum of Runtime (sec.)")
            ax[i, j].set_title(
                f"Bounded-valance graph with valence = {valence[-1]} \n and subgraph size of {percent[-1]}0%", 
                fontweight="bold", 
                fontsize=25
            )
            ax[i, j].set_xlabel("Number of graph nodes")
            ax[i, j].set_xticks(x)
            ax[i, j].set_xticklabels(indices)
            ax[i, j].legend()
            ax[i, j].set_yscale("log")

    fig.savefig("subgraph_isomorphism.png", dpi=200)

    if HAS_TIKZ:
        pass
        # tikzplotlib.save("subgraph_isomorphism.tex")


def main():
    isomorphism_graph()
    creation_time_graph()
    single_source_graph()
    single_source_graph_NY()
    all_pair_graph()


if __name__ == "__main__":
    main()
