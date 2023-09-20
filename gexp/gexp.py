from typing import Dict, Optional

from .graph import getPatternGraph

from spycy import spycy
import networkx as nx


def match(pattern: spycy.NetworkXGraph, graph: spycy.NetworkXGraph) -> bool:
    res = False

    def get_connected_components(graph: nx.MultiDiGraph):
        return [cc for cc in nx.weakly_connected_components(graph)]

    pattern_ccs = get_connected_components(pattern._graph)
    input_ccs = get_connected_components(graph._graph)
    if len(pattern_ccs) != len(input_ccs):
        return res

    if len(pattern.edges) == 0:
        return True
        # permutations = itertools.permutations(input_ccs)
        # for perm in permutations:
        #     result = MatchResult()
        #     for idx, (nodeid, node) in enumerate(pgraph.nodes.items()):
        #         print("!!!", perm[idx], node.name)
        #         result.node_ids_to_props[nodeid] = 0

    # Copy the graph and check that it succeeded
    original_graph = graph._graph.copy()
    assert isinstance(original_graph, nx.MultiDiGraph)
    try:
        # TODO bind edges and call match recursively
        return res
    finally:
        graph._graph = original_graph


def GExpMatch(pattern: str, inp: str) -> bool:
    pattern_graph = getPatternGraph(pattern)
    input_graph = getPatternGraph(inp)
    return match(pattern_graph, input_graph)
