from typing import Dict, List, Iterable, Set
import itertools

from .graph import getPatternGraph

from spycy import spycy
import networkx as nx

def isIsomorphic(graph: spycy.NetworkXGraph, subgraph_a: Set[int],
                 subgraph_b: Set[int]) -> bool:
    return False


def match(pattern: spycy.NetworkXGraph, graph: spycy.NetworkXGraph) -> bool:
    res = False

    def get_connected_components(graph: nx.MultiDiGraph) -> List[Set[int]]:
        return [cc for cc in nx.weakly_connected_components(graph)]

    pattern_ccs = get_connected_components(pattern._graph)
    input_ccs = get_connected_components(graph._graph)
    if len(pattern_ccs) != len(input_ccs):
        return res

    pattern_ids = list(pattern.nodes.keys())
    if len(pattern.edges) == 0:
        permutations = itertools.permutations(input_ccs)
        for perm in permutations:
            bound_graphs: Dict[str, Set[int]] = {}
            matched = True
            for id_, subgraph in zip(pattern_ids, perm):
                name = pattern.nodes[id_]['name']
                canonical_name = name.split('_')[0]
                if canonical_name not in bound_graphs:
                    bound_graphs[canonical_name] = subgraph
                else:
                    if not isIsomorphic(graph, subgraph,
                                        bound_graphs[canonical_name]):
                        matched = False
                        break
            if matched:
                return True
        return False

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
