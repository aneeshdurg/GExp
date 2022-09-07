from dataclasses import dataclass
from typing import Dict, List, Union

@dataclass
class Node:
    name: str


@dataclass
class Edge:
    src: Node
    dst: Node


@dataclass
class Graph:
    nodes: List[Node]
    # incident out edges
    edges: Dict[str, List[Edge]]


@dataclass
class Subgraph:
    name: str


@dataclass
class PatternEdge:
    src: Union[Node, Subgraph]
    dst: Union[Node, Subgraph]


@dataclass
class PatternGraph:
    nodes: List[Union[Node, Subgraph]]
    # incident out edges
    edges: Dict[str, List[PatternEdge]]


class GExpResult:
    # ??
    pass


def GExpMatch(pattern: PatternEdge, inp: Graph) -> GExpResult:
    pass

if __name__ == "__main__":
    a = Node('a')
    test_graph = Graph([a], {})

    pa = Node('pattern_a')
    pattern_graph_1 = PatternGraph([pa], {})
    assert GExpMatch(pattern_graph_1, test_graph)

    pb = Node('pattern_b')
    pattern_graph_2 = PatternGraph([pa, pb], {})
    assert not GExpMatch(pattern_graph_2, test_graph)

    pattern_graph_3 = PatternGraph([pa, pb], {pa.name, PatternEdge(pa, pb)})
    assert not GExpMatch(pattern_graph_3, test_graph)

    pG = Subgraph('G')
    pattern_graph_4 = PatternGraph([pG], {})
    assert GExpMatch(pattern_graph_4, test_graph)
