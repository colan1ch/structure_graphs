"""
    Check if graph of mapping g: x -> (x - x^2) on Z_p,
    p is prime number of from 7+12k
    has >1 connected components  
"""
import igraph as ig
import csv

OUTPUT_FILE = "results\primes-7-12k.csv"

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

def build_graph(p: int) -> ig.Graph:
    """
    Build graph of mapping g: x -> (x - x^2)
    on Z_p:
    """
    g = ig.Graph(directed=True)
    g.add_vertices(p)
    for a in range(p):
        b = (a - a * a) % p
        g.add_edge(a, b)
    return g

def main(p):
    # Counting connected components
    g = build_graph(p)
    components = g.connected_components(mode="weak")
    return len(components)

# Creating list of primes form 7+12k
primes = []
k = 1  # Start from p=19
while len(primes) < 100:
    p = 7 + 12 * k
    if is_prime(p):
        primes.append(p)
    k += 1

print(f'verify-primes-7-12k, method = graph of mapping, output={OUTPUT_FILE}')
collect = [['ring', 'order', 'conn.comp.', 'expected', 'res']]
for p in primes:
    ring = 'Z_' + str(p)
    order = p
    conn_comp = main(p)
    # Assume more than 1 conn.comp.
    expected ='>1'
    res = 'OK' if conn_comp>1 else 'Wrong'
        
    print(f'{ring}, order {p}, {conn_comp} conn.components, {res}')
    collect.append([ring, order, conn_comp, expected, res])

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerows(collect)
    
    