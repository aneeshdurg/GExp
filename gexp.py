from dataclasses import dataclass
from typing import Dict, List, Union, Optional

from graph import Node, Edge, InputGraph, PatternNode, PatternEdge, PatternGraph


class GExpResult:
    nodes: Dict[int, int]
    edges: Dict[int, int]
    pass


def GExpMatch(pattern: PatternGraph, inp: InputGraph) -> Optional[GExpResult]:
    # assert pattern.no_subgraph_nodes(), "Unsupported pattern"
    if pattern.count_connected_comopnents() != inp.count_connected_comopnents():
        return None
    return GExpResult()


if __name__ == "__main__":
    a = Node(0, "a")
    test_graph = InputGraph([a], [])

    pa = PatternNode(0, "pattern_a", False)
    pattern_graph_1 = PatternGraph([pa], {})
    assert GExpMatch(pattern_graph_1, test_graph)

    pb = PatternNode(0, "pattern_b", False)
    pattern_graph_2 = PatternGraph([pa, pb], {})
    assert not GExpMatch(pattern_graph_2, test_graph)

    pattern_graph_3 = PatternGraph([pa, pb], [PatternEdge(0, pa, pb)])
    assert not GExpMatch(pattern_graph_3, test_graph)

    pG = PatternNode(0, "G", True)
    pattern_graph_4 = PatternGraph([pG], {})
    assert GExpMatch(pattern_graph_4, test_graph)
