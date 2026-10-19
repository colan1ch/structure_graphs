[![DOI](https://zenodo.org/badge/1425449948.svg)](https://doi.org/10.5281/zenodo.23480412)

# Structure Graphs of Associative Rings — Computational Verification

Computational support for the paper

> **On the Connectivity Components of Structure Graphs of Associative Rings**
>
> Andrey M. Chernev, Nikolay A. Chernev

The repository contains the scripts that verify every computational claim of the paper and the resulting data files (CSV).

## Requirements

- Python ≥ 3.10
- [`igraph`](https://python.igraph.org/) ≥ 0.11

## Claims verified

Correspondence between scripts and statements claimed in the article see in table below.

| # | Claim | Prev. published | Script | Result |
|---|-------|-------------------|--------|--------|
| 1 | `Z_2`, `Z_3`, `Z_7` have = `n` conn.comp. | Lipkovski (2012) | `verify-small-rings` | `results/small_rings.csv` |
| 2 | `GF(4)` has = 4 conn.comp. | Ang (2013) | `verify-gf4` | `results/gf4.csv` |
| 3 | `Z_p` with `p = 7 + 12k`, `18<p < 2078`, has `> n` conn.comp. | for p<200 Lipkovski (2015) | `verify-primes-7-12k` | `results/primes_7_12k.csv` |
| 4 | `GF(9)` and `GF(49)` have `> n` conn.comp. | — | `verify-gf9-gf49` | `results/gf9_gf49.csv` |
| 5 | `GF(2^m)`, `2<m<8`, has `> n` components | — | `verify-gf2m` | `results/gf2m.csv` |
| 6 | `GF(2^11)`, `m <= 13`, `m != 2`, has `> n` components | — | `verify-gf2-11` | `results/gf2-11.csv` |
| 7 | `GF(2^13)`, `m <= 13`, `m != 2`, has `> n` components | — | `verify-gf2-13` | `results/gf2-13.csv` |

Claims 1, 2 and (part. 3)  are included for completeness and independence of exposition: they re-derive previously known cases from scratch, without relying on the published constructions.
Claims 3 (for p>200) – 7 are the new computational cases of the paper.

## Citing and data availability

If you use these scripts, please cite the paper. The archival version of this
repository is available at Zenodo:

> Chernev A.M., Chernev N.A. *Computational verification for "On the Connectivity
> Components of Structure Graphs of Associative Rings"*. Zenodo.
>
> DOI: 10.5281/zenodo.XXXXXXX

The DOI refers to a frozen snapshot; the GitHub repository may contain
additional development commits.

---

## License

MIT. See `LICENSE`.
