"""
    Check if structure graph of Z_p,
    p is 2 or 3 or 7
    has =p connected components  
"""
import igraph as ig
import csv

OUTPUT_FILE = "results\small-rings.csv"

def is_prime(n: int) -> bool:
    # Check if n is prime
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    if n % 3 == 0:
        return n == 3

    d = 5
    while d * d <= n:
        if n % d == 0 or n % (d + 2) == 0:
            return False
        d += 6
    return True

def build_graph(p):
    """Build structure graph for Z_p x Z_p: (a,b) -> (a+b, a*b) mod p."""
    vertices = [(a, b) for a in range(p) for b in range(p)]
    n = len(vertices)
    index_of = {pair: i for i, pair in enumerate(vertices)}

    g = ig.Graph(directed=True, n=n)
    g.vs["name"] = [f"({a},{b})" for a, b in vertices]
    g.vs["pair"] = vertices

    edges = []
    for i, (a, b) in enumerate(vertices):
        next_a = (a + b) % p
        next_b = (a * b) % p
        j = index_of[(next_a, next_b)]
        edges.append((i, j))
    g.add_edges(edges)
    return g

def main(p):
    # Counting connected components
    g = build_graph(p)
    components = g.connected_components(mode="weak")
    return len(components)

# Creating list of orders
primes = [2, 3, 7]

print(f'verify-small-rings, method = structure graph, output={OUTPUT_FILE}')
collect = [['ring', 'order', 'conn.comp.', 'expected', 'res']]
for p in primes:
    ring = 'Z_' + str(p)
    order = p
    conn_comp = main(p)
    # Assume conn.comp. = order
    expected ='='+ str(p)
    res = 'OK' if conn_comp==p else 'Wrong'   
    
    print(f'{ring}, order {p}, {conn_comp} conn.components, {res}')
    collect.append([ring, order, conn_comp, expected, res])

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerows(collect)
    
    