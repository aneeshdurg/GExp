from .gexp import GExpMatch

# TODO setup real tests
import os
if len(os.environ.get("GEXP_TEST", "")):
    # Test basic pattern matching (no isomorphisms)
    assert GExpMatch("(a)", "()")
    assert not GExpMatch("(a), (b)", "()")
    assert not GExpMatch("(a)-->(b)", "()")

    # Test that a subgraph of a single node is isomorphic to any single node
    # subgraph
    assert GExpMatch("(G)", "()")
    assert GExpMatch("(G), (G_1)", "(), ()")

    # Test that a subgraph of a single node is not isomorphic to a graph with an
    # edge
    assert not GExpMatch("(G), (G_1)", "(), ()-->()")

    # Test that isomorphic subgraphs can be matched as connected
    assert GExpMatch("(A)-->(B)", "()-->()")
    # Test that no isomorphism can be solved for A
    assert not GExpMatch("(A)-->(A_1)", "()-->()-->()")

    # Test more complex isomorphic subgraphs
    # A should be isomorphic to ()-->()-->() in the following two tests
    assert GExpMatch("(A)-->(A_1)", "(a)-->(b)-->(c), (d)-->(e)-->(f), (a)-->(e)")
    assert GExpMatch(
        "(A)-->(A_1)-->(A_2)",
        """
            (a)-->(b)-->(c),
            (d)-->(e)-->(f),
            (g)-->(h)-->(i),
            (a)-->(e)-->(i)
        """
    )

import sys
pattern = sys.argv[1]
input_ = sys.argv[2]
assert GExpMatch(pattern, input_)
