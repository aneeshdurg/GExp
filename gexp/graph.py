from dataclasses import dataclass


from spycy import spycy
from spycy.gen.CypherLexer import CypherLexer
from spycy.gen.CypherParser import CypherParser
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener as ErrorListener_

@dataclass
class PanicErrorListener(ErrorListener_):
    errors_caught: int = 0

    def syntaxError(self, recognizer, offendingSymbol, line, col, msg, e):
        raise Exception(
            "Syntax error at line {} col {}: {}".format(line, col, msg)
        )

def patternGraphToNetworkXGraph(pgraph: spycy.pattern_graph.Graph) -> spycy.NetworkXGraph:
    graph = spycy.NetworkXGraph()

    assert len(pgraph.paths) == 0
    node_to_networkx_node = {}
    for node, data in pgraph.nodes.items():
        node_to_networkx_node[node] = graph.add_node(data.__dict__)

    for edge in pgraph.edges.values():
        graph.add_edge(node_to_networkx_node[edge.start],
                       node_to_networkx_node[edge.end], edge.__dict__)
    return graph


def getPatternGraph(pattern) -> spycy.NetworkXGraph:
    # Setup the cypher parser
    error_listener = PanicErrorListener()
    input_stream = InputStream(pattern)
    lexer = CypherLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(error_listener)
    stream = CommonTokenStream(lexer)
    parser = CypherParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)

    # Parse a pattern graph
    root = parser.oC_Pattern()

    # Use spycy to convert it into a python object
    pgraph = spycy.ConcreteExpressionEvaluator.interpret_pattern(root)
    return patternGraphToNetworkXGraph(pgraph)
