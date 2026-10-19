"""
    Check if structure graph of GF(2^k)
    has >2^k connected components  
"""
import igraph as ig
import csv


OUTPUT_FILE = "results\gf2-11.csv"

# --------------------------- Class of field GF(2^n) ---------------------------
class GF2n:
    """Galois field char 2."""
    def __init__(self, n, irreducible_poly):
        self.n = n
        self.size = 1 << n
        self.irr = irreducible_poly
        self.mod_mask = (1 << n) - 1

    def add(self, a, b):
        return a ^ b

    def mul(self, a, b):
        result = 0
        while b:
            if b & 1:
                result ^= a
            a <<= 1
            if a & (1 << self.n):
                a ^= self.irr
            b >>= 1
        return result

    def element_str(self, x):
        if x == 0:
            return "0"
        if x == 1:
            return "1"
        terms = []
        for i in range(self.n):
            if (x >> i) & 1:
                if i == 0:
                    terms.append("1")
                elif i == 1:
                    terms.append("x")
                else:
                    terms.append(f"x^{i}")
        return " + ".join(terms)

# Standart irreducible polynoms
IRREDUCIBLE_POLYS = {
    1: 0b11,          # x+1
    2: 0b111,         # x^2+x+1
    3: 0b1011,        # x^3+x+1
    4: 0b10011,       # x^4+x+1
    5: 0b100101,      # x^5+x^2+1
    6: 0b1000011,     # x^6+x+1
    7: 0b10000011,    # x^7+x+1
    8: 0b100011011,   # x^8+x^4+x^3+x+1
    9: 0b1000010001,  # x^9+x^4+1
    10: 0b10000001001, # x^10+x^3+1
    11: 0b100000000101,      # x^11 + x^2 + 1
    12: 0b1000000001001,     # x^12 + x^3 + 1
    13: 0b10000000011011,    # x^13 + x^4 + x^3 + x + 1
}

def build_graph(gf):
    """Build structural graph (a,b)->(a+b, a*b)
    for GF(4).
    """
    size = gf.size
    total_v = size * size
    edges = []

    for a in range(size):
        for b in range(size):
            src = a * size + b
            s = gf.add(a, b)
            p = gf.mul(a, b)
            dst = s * size + p
            edges.append((src, dst))

    g = ig.Graph(n=total_v, edges=edges, directed=True)

    return g

def main(p, verbose=True, plot=True):
    gf = GF2n(p, IRREDUCIBLE_POLYS[p])
    g = build_graph(gf)
    components = g.connected_components(mode="weak")
    return len(components)
    

# Creating list of extension degrees
primes = [11]

print(f'verify-gf2-11, method = structure graph, output = {OUTPUT_FILE}')
collect = [['ring', 'order', 'conn.comp.', 'expected', 'res']]
for p in primes:
    order = 2**p
    ring = 'GF(' + str(order) + ')'
    conn_comp = main(p)
    # Assume conn.comp. > order
    expected ='>'+ str(order)
    res = 'OK' if conn_comp>order else 'Wrong'   
    
    print(f'{ring}, order {order}, {conn_comp} conn.components, {res}')
    collect.append([ring, order, conn_comp, expected, res])

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerows(collect)
   
