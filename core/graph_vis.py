import os
import networkx as nx
from core.extractor import PyAstExtractor
import networkx.algorithms.centrality as nxac
import matplotlib.pyplot as plt
from core.helpers import node_name


class ImportsGraph:
    def __init__(self):
        self.graph = nx.DiGraph()

    def _add_module(self, path):
        module = PyAstExtractor(path)
        self.graph.add_node(module.name)

        for imported_module in module.get_imports():
            if imported_module:
                self.graph.add_edge(module.name, node_name(imported_module)[0])

    def calculate_centrality_measures(self):
        degree_centrality = nxac.degree_centrality(self.graph)
        closeness_centrality = nxac.closeness_centrality(self.graph)
        betweenness_centrality = nxac.betweenness_centrality(self.graph)

        return {
            "degree_centrality": degree_centrality,
            "closeness_centrality": closeness_centrality,
            "betweenness_centrality": betweenness_centrality,
        }

    def draw_with_centrality(self):
        centrality_measures = self.calculate_centrality_measures()
        degree_centrality = centrality_measures["degree_centrality"]

        node_sizes = [degree_centrality[node] * 4000 for node in self.graph.nodes]

        plt.figure(figsize=(6, 6))
        pos = nx.spring_layout(self.graph)
        nx.draw(
            self.graph,
            pos,
            node_size=node_sizes,
            node_color="lightblue",
            with_labels=True,
            edge_color="gray",
        )
        plt.savefig("graph.png")


class SingleFileImportGraph(ImportsGraph):
    def __init__(self, file_path):
        super().__init__()
        if file_path.endswith(".py"):
            self._add_module(file_path)


def generate_centrality_graph(path: str | os.PathLike) -> None:
    single_file_graph = SingleFileImportGraph(path)
    single_file_graph.draw_with_centrality()
