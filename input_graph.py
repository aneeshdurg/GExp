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


class Graph:
    nodes: List[Node]
    # incident out edges
    out_edges: Dict[Node, List[Edge]]
    in_edges: Dict[Node, List[Edge]]

    def __init__(self, nodes, edges):
        for edge in edges:
            if edge.src not in self.out_edges:
                self.out_edges[edge.src] = []
            self.out_edges[edge.src].append(edge)

            if edge.dst not in self.in_edges:
                self.in_edges[edge.dst] = []
            self.in_edges[edge.dst].append(edge)

    def get_out_edges(self, n: Node) -> List[Node]:
        return self.out_edges.get(n, [])

    def out_degree(self, n: Node) -> int:
        return len(self.out_edges.get(n, []))

    def get_in_edges(self, n: Node) -> List[Node]:
        return self.in_edges.get(n, [])

    def in_degree(self, n: Node) -> int:
        return len(self.in_edges.get(n, []))

    def get_connected_comopnent(self, root: Node) -> Set[Node]:
        component = set()
        # Just a basic dfs
        queue = [root]
        while len(stack):
            node = stack.pop()
            component.add(node)
            for edge in self.get_out_edges(node):
                if edge.dst not in component:
                    queue.append(edge.dst)

            for edge in self.get_in_edges(node):
                if edge.src not in component:
                    queue.append(edge.src)

