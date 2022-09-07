# GExp - regex for graphs

GExp aims to provide a way to decompose graphs into subgraphs by specifying a
pattern and the solving for an homomorphism between the pattern and the input
graph.

## Motivation

The motivating use case is graph pattern mining engines. Suppose you're building
a pattern matching engine, and you'd like to decompose patterns into more
efficient intermediate patterns. For example, take the following cypher pattern:

```
MATCH
  (a)--(b)--(c)--(a),
  (d)--(e)--(f)--(d),
  (a)--(d)
RETURN count(*)
```

This is two triangles connected by an edge:

```
   (a)--------(d) 
  /   \      /   \
(b)---(c)  (e)---(f)
```

However, if you enumerate all matches for the first triangle, you have a super
set of all possible matches for the second triangle, which could be the basis
for potentially faster execution plans.

With `GExp` this pattern could be extracted as:

```
G1-e-G2
```

Where `G` represents some subgraph, and `G<n>` represents a subgraph ismorphic
to `G`. If `GExp` matches `G1-e-G2` against the cypher query above, it could
resolve the expression as:

```
G1 = a, b, c
G2 = d, e, f
e = a-->d
```

Another possible usecase could be to implement a kind of `grep` for graph query
files allowing one to search a set of queries for specific subgraphs to explore
how relevant matching a certain kind of graph is across a set of queries.

## Planned features

node/edge capturing
Subgraph capturing
optional edges/subgraphs

