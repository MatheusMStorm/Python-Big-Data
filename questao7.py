sequencia_fim = int(input('Até qual termo você quer imprimir a sequência de Fibonacci? \n'))
seq_fibonacci = [1,1]

i = 2
while i < sequencia_fim:
    seq_fibonacci.append(seq_fibonacci[i-1] + seq_fibonacci[i-2])
    i += 1

print(seq_fibonacci)