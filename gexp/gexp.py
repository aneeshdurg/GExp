from typing import Dict, List, Iterable, Set
import itertools

from .graph import getPatternGraph

from spycy import spycy
import networkx as nx

def isIsomorphic(graph: nx.MultiDiGraph, subgraph_a: Set[int],
                 subgraph_b: Set[int]) -> bool:
    graph_a = graph.subgraph(subgraph_a)
    graph_b = graph.subgraph(subgraph_b)
    return nx.is_isomorphic(graph_a, graph_b)


def match(pattern: nx.MultiDiGraph, graph: nx.MultiDiGraph) -> bool:
    res = False

    def get_connected_components(graph: nx.MultiDiGraph) -> List[Set[int]]:
        return [cc for cc in nx.weakly_connected_components(graph)]

    pattern_ccs = get_connected_components(pattern)
    input_ccs = get_connected_components(graph)
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
    pattern_edges = [edge for edge in pattern.edges]
    for edge in pattern_edges:
        pattern.remove_edge(*edge)

    for edge_list in itertools.permutations(graph.edges, len(pattern_edges)):
        original_graph = graph.copy()
        assert isinstance(original_graph, nx.MultiDiGraph)

        for edge in edge_list:
            graph.remove_edge(*edge)
        if match(pattern, graph):
            return True

        graph = original_graph
    return False


def removeWhitespace(s: str):
    return ''.join(s.split())


def GExpMatch(pattern: str, inp: str) -> bool:
    pattern_graph = getPatternGraph(removeWhitespace(pattern))
    input_graph = getPatternGraph(removeWhitespace(inp))
    return match(pattern_graph._graph, input_graph._graph)
