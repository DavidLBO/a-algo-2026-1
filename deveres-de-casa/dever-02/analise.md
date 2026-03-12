## Análise de Desempenho do Algoritmo Fatorial Recursivo

Resultados obtidos do tempo de execução:

n = 10 -> 0.00000191 seconds
n = 100 -> 0.00001693 seconds
n = 500 -> 0.00013757 seconds
n = 1000 -> recursion limit reached

## Análise da Complexidade

O algoritmo de fatorial recursivo apresentado opera em O(n). Cada chamada realiza apenas uma operação de forma constante, a multiplicação, e após isso a chamada da função.

Isso resulta em um crescimento linear no tempo de execução, conforme o valor de n aumentar.

Obs: Dentro do python há um limite na profundidade de recursão, o tratamento do erro RecursionError está presente no código para lidar adequadamente com esta situação.