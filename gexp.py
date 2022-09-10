from dataclasses import dataclass
from typing import Dict, List, Union

from input_graph import Graph

@dataclass
class PatternEdge:
    id: int
    src: PatternNode
    dst: PatternNode


@dataclass
class PatternNode:
    id: int
    name: str
    is_subgraph: bool


@dataclass
class PatternGraph:
    nodes: List[PatternNode]
    # incident out edges
    edges: Dict[str, List[PatternEdge]]

    def get(id: int) -> Node:
        pass

    def no_subgraph_nodes(self) -> bool:
        for n in self.nodes:
            if n.is_subgraph:
                return False
        return True

    def degree(self, n: PatternNode) -> int:
        return len(self.edges.get(n, []))


class GExpResult:
    nodes: Dict[int, int]
    edges: Dict[int, int]
    pass


def GExpMatch(pattern: PatternEdge, inp: Graph, mapping: GExpResult) -> GExpResult:
    if len(mapping.nodes) == len(pattern.nodes):
        return mapping

    for n in pattern.nodes:
        if n.id not in mapping.nodes:
            continue
        actual_node = inp.get(mapping[n.id])
        for e in pattern.edges.get(n.name, []):
            if e.dst.id in mapping.nodes:
                continue
            target_node = e.dst
            target_degree = pattern.degree(e.dst)
            for potential_target in inp.edges.get(actual_node):
                if inp.degree(potential_target) != attern.degre



def GExpMatch(pattern: PatternEdge, inp: Graph) -> GExpResult:
    assert pattern.no_subgraph_nodes(), "Unsupported pattern"

    pass

if __name__ == "__main__":
    a = Node('a')
    test_graph = Graph([a], [])

    pa = PatternNode('pattern_a', False)
    pattern_graph_1 = PatternGraph([pa], {})
    assert GExpMatch(pattern_graph_1, test_graph)

    pb = PatternNode('pattern_b', False)
    pattern_graph_2 = PatternGraph([pa, pb], {})
    assert not GExpMatch(pattern_graph_2, test_graph)

    pattern_graph_3 = PatternGraph([pa, pb], {pa.name, PatternEdge(pa, pb)})
    assert not GExpMatch(pattern_graph_3, test_graph)

    pG = PatternNode('G', True)
    pattern_graph_4 = PatternGraph([pG], {})
    assert GExpMatch(pattern_graph_4, test_graph)
