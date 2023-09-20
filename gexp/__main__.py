from .gexp import GExpMatch

assert GExpMatch("(a)", "()")
assert not GExpMatch("(a), (b)", "()")
assert not GExpMatch("(a)-->(b)", "()")
assert GExpMatch("(G)", "()")
assert GExpMatch("(G), (G_1)", "(), ()")
assert not GExpMatch("(G), (G_1)", "(), ()-->()")
