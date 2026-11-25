# Cyclomatic complexity of the flow graph in Exp 8
# Given: E = 17 edges, N = 13 nodes, 5 predicate nodes
edges = [(1,2),(2,3),(2,4),(3,5),(4,5),(4,6),(5,7),(6,7),(6,8),
         (7,9),(8,9),(8,10),(9,11),(10,11),(10,12),(11,13),(12,13)]
nodes = sorted({n for e in edges for n in e})
E, N, P = len(edges), len(nodes), 1          # P = connected components
out_deg = {n: sum(1 for a, _ in edges if a == n) for n in nodes}
predicates = [n for n, k in out_deg.items() if k >= 2]
print(f"Nodes (N)            = {N}")
print(f"Edges (E)            = {E}")
print(f"Predicate nodes      = {len(predicates)}  {predicates}")
print(f"V(G) = E - N + 2P    = {E} - {N} + 2 = {E - N + 2 * P}")
print(f"V(G) = predicates + 1 = {len(predicates)} + 1 = {len(predicates) + 1}")
v = E - N + 2 * P
risk = "Low" if v <= 10 else "Moderate" if v <= 20 else "High" if v <= 50 else "Very high"
print(f"Independent paths    = {v}  (min. test cases for basis path testing)")
