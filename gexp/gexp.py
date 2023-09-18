from typing import Dict, Optional

from .graph import getPatternGraph

import networkx as nx

class GExpResult:
    nodes: Dict[int, int]
    edges: Dict[int, int]
    pass


def GExpMatch(pattern: str, inp: str) -> Optional[GExpResult]:
    # cypher = spycy.CypherExecutor()

    pattern_graph = getPatternGraph(pattern)
    input_graph = getPatternGraph(inp)

    pattern_ccs = nx.weakly_connected_components(pattern_graph._graph)
    input_ccs = nx.weakly_connected_components(input_graph._graph)
    def count_ccs(ccs):
        return sum(1 for _ in ccs)
    if count_ccs(pattern_ccs) != count_ccs(input_ccs):
        return None
    return GExpResult()
