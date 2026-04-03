# Análise de Complexidade — Cálculos Detalhados

---

## Merge Sort

A recorrência é `T(n) = 2T(n/2) + cn`. Expandindo nível a nível:

```
Nível 0:  T(n)     = 2T(n/2)   + cn        custo = cn
Nível 1:  T(n)     = 4T(n/4)   + 2cn       custo = cn
Nível 2:  T(n)     = 8T(n/8)   + 3cn       custo = cn
Nível k:  T(n)     = 2^k T(n/2^k) + k·cn
```

A condição de parada é `T(1) = c`, ou seja, `n/2^k = 1`, logo `k = log₂n`.

Substituindo:

```
T(n) = 2^(log₂n) · T(1) + (log₂n) · cn
     = n·c + cn·log₂n
     = Θ(n log n)
```

Resultado: `T(n) = Θ(n log n)` — vale para melhor, médio e pior caso. Espaço auxiliar: `O(n)`.

---

## Multiplicação de Matrizes

Cada entrada `C[i][j] = Σ A[i][k] · B[k][j]` exige `n` multiplicações e `n−1` adições. Como há `n²` entradas na matriz resultado:

```
multiplicações: n² × n     = n³
adições:        n² × (n−1) = n³ − n²

total = n³ + n³ − n² = 2n³ − n² = Θ(n³)
```

Resultado: `T(n) = Θ(n³)`.

---

## Recorrências

Para todas as recorrências abaixo é usado o Teorema Mestre: dado `T(n) = aT(n/b) + f(n)`, calcula-se `c* = log_b(a)` e compara-se `f(n)` com `n^c*`.

---

### 2T(n/4) + √n

a = 2, b = 4, f(n) = n^(1/2).

```
c* = log₄2 = log₂2 / log₂4 = 1/2

n^c* = n^(1/2)

f(n) = n^(1/2) = Θ(n^(1/2) · log⁰n)  →  Caso 2, k = 0

T(n) = Θ(n^(1/2) · log^(0+1) n) = Θ(√n · log n)
```

---

### 2T(n/4) + n

a = 2, b = 4, f(n) = n.

```
c* = log₄2 = 1/2  (mesmo cálculo acima)

n^c* = n^(1/2)

f(n) = n = Ω(n^(1/2 + ε))  para ε = 1/2,  pois n^(1/2 + 1/2) = n  ✓  →  Caso 3

Condição de regularidade:
  a · f(n/b) = 2 · (n/4) = n/2 ≤ (1/2) · n = c · f(n),  com c = 1/2 < 1  ✓

T(n) = Θ(f(n)) = Θ(n)
```

---

### 16T(n/4) + n²

a = 16, b = 4, f(n) = n².

```
c* = log₄16 = log₄(4²) = 2

n^c* = n²

f(n) = n² = Θ(n² · log⁰n)  →  Caso 2, k = 0

T(n) = Θ(n² · log^(0+1) n) = Θ(n² log n)
```

---

## Resumo

| Problema        | Recorrência       | c*  | f(n)    | Caso | Resultado   |
|-----------------|-------------------|-----|---------|------|-------------|
| Merge Sort      | 2T(n/2) + cn      | 1   | n       | 2    | Θ(n log n)  |
| Matriz ingênua  | —                 | —   | —       | —    | Θ(n³)       |
| 2T(n/4) + √n    | 2T(n/4) + n^(1/2) | 1/2 | n^(1/2) | 2    | Θ(√n log n) |
| 2T(n/4) + n     | 2T(n/4) + n       | 1/2 | n       | 3    | Θ(n)        |
| 16T(n/4) + n²   | 16T(n/4) + n²     | 2   | n²      | 2    | Θ(n² log n) |
