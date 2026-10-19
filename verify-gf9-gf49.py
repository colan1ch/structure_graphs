"""
    Check if graph of mapping g: x -> (x - x^2) on GF(9) and GF(49),
    has >1 connected components  
"""
import igraph as ig
import galois
import csv

OUTPUT_FILE = "results\primes-gf9-gf49.csv"

def build_graph(p: int, n: int = 1) -> ig.Graph:
    """
    Build graph of mapping g: x -> (x - x^2)
    for field GF(p^n)
    """
    global GF

    q = p ** n
    GF = galois.GF(q)
    elements = GF.elements                # All field elements
    # 
    element_to_idx = {int(elem): i for i, elem in enumerate(elements)}

    g = ig.Graph(directed=True)
    g.add_vertices(q)

    for i, x in enumerate(elements):
        y = x - x * x 
        j = element_to_idx[int(y)]        
        g.add_edge(i, j)

    return g, elements


def main(p: int, n: int = 2):
    """
    Build graph of mapping g: x -> (x - x^2)
    for field GF(p^n)
    """
    g, elements = build_graph(p, n)
    components = g.connected_components(mode="weak")
    return len(components)


primes=[3, 7]
print(f'verify-gf9-gf49, method = graph of mapping, output={OUTPUT_FILE}')
collect = [['ring', 'order', 'conn.comp.', 'expected', 'res']]
for p in primes:
    order = p**2
    ring = 'GF(' + str(order) + ')'    
    conn_comp = main(p, 2)
    # Assume more than 1 conn.comp.
    expected ='>1'
    res = 'OK' if conn_comp>1 else 'Wrong'
        
    print(f'{ring}, order {order}, {conn_comp} conn.components, {res}')
    collect.append([ring, order, conn_comp, expected, res])

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerows(collect)
