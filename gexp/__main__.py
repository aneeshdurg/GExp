from .gexp import GExpMatch

# TODO setup real tests
import os
if len(os.environ.get("GEXP_TEST", "")):
    assert GExpMatch("(a)", "()")
    assert not GExpMatch("(a), (b)", "()")
    assert not GExpMatch("(a)-->(b)", "()")
    assert GExpMatch("(G)", "()")
    assert GExpMatch("(G), (G_1)", "(), ()")
    assert not GExpMatch("(G), (G_1)", "(), ()-->()")
    assert GExpMatch("(A)-->(B)", "()-->()")
    assert not GExpMatch("(A)-->(A_1)", "()-->()-->()")
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
