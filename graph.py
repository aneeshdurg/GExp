from dataclasses import dataclass
from typing import Dict, Generic, Iterable, List, Protocol, Set, TypeVar

import networkx as nx  # type: ignore[import]


class GenericNode(Protocol):
    @property
    def id(self) -> int:
        ...


class GenericEdge(Protocol):
    @property
    def id(self) -> int:
        ...

    @property
    def src(self) -> GenericNode:
        ...

    @property
    def dst(self) -> GenericNode:
        ...


N = TypeVar("N", bound=GenericNode)
E = TypeVar("E", bound=GenericEdge)


class GenericGraph(Generic[N, E]):
    nodes: Dict[int, N]
    edges: Dict[int, E]
    graph: nx.MultiDiGraph
    undir_graph_view: nx.MultiGraph

    def __init__(self, nodes: Iterable[N], edges: Iterable[E]):
        self.graph = nx.MultiDiGraph()

        # TODO(aneesh) why is the following line required?!
        self.nodes = {}

        for node in nodes:
            self.graph.add_node(node.id)
            self.nodes[node.id] = node

        for edge in edges:
            self.graph.add_edge(edge.src.id, edge.dst.id, key=edge.id)
            self.edges[edge.id] = edge

        self.undir_graph_view = nx.MultiGraph(self.graph)

    def get_out_edges(self, n: N) -> nx.classes.reportviews.OutMultiEdgeDataView:
        return self.graph.out_edges(n.id, keys=True)

    def out_degree(self, n: N) -> int:
        degree: int = self.graph.out_degree(n.id)
        return degree

    def get_in_edges(self, n: N) -> nx.classes.reportviews.InMultiEdgeDataView:
        return self.graph.in_edges(n.id, keys=True)

    def in_degree(self, n: N) -> int:
        degree: int = self.graph.in_degree(n.id)
        return degree

    def count_connected_comopnents(self) -> int:
        nccs: int = nx.number_connected_components(self.undir_graph_view)
        return nccs

    def get_connected_comopnents(self) -> List[Set[N]]:
        ccs = list(nx.connected_components(self.undir_graph_view))

        def ids_to_nodes(ids: Set[int]) -> Set[N]:
            return {self.nodes[i] for i in ids}

        return [ids_to_nodes(ids) for ids in ccs]


@dataclass
class Node:
    id: int
    name: str


@dataclass
class Edge:
    id: int
    src: Node
    dst: Node
    # TODO undirected/var length edges


InputGraph = GenericGraph[Node, Edge]


@dataclass
class PatternNode:
    id: int
    name: str
    is_subgraph: bool


@dataclass
class PatternEdge:
    id: int
    src: PatternNode
    dst: PatternNode


PatternGraph = GenericGraph[PatternNode, PatternEdge]
