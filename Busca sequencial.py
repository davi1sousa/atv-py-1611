#realiza uma busca sequencial dos numeros inteiros
def busca_sequencial(lista, alvo): #alvo é o numero a ser buscado na lista
    for i, num in enumerate (lista):
        if num == alvo :
            return i
    return -1 #retorna -1 caso nao exista valor na lista

#realiza uma busca binaria dos numeros inteiros
def busca_binaria(lista, alvo): #alvo é o numero a ser buscado na lista
    inicio, fim =0, len(lista) -1
    while inicio <= fim:
        meio = (inicio + fim)// 2
        meio_valor=lista[meio]

        if meio_valor == alvo:
            return meio
        elif meio_valor < alvo:
            inicio = meio +1
        else:
            fim = meio -1

    return -1 #retorna -1 caso nao exista valor na lista

#declara a lista ordenada
lista_ordenada= [1 ,2, 3, 4, 5, 6, 7, 8, 9, 10]

#variavel para definir as buscas dos numeros
num_alvo_seq= 3 
num_alvo_bin=1

#busca o numero alvo na lista ordenada
resultado_sequencial= busca_sequencial (lista_ordenada, num_alvo_seq)
result_binario= busca_binaria (lista_ordenada, num_alvo_bin)

#imprime o numero alvo buscado
print(f"Busca Sequencial - Número Alvo: {num_alvo_seq}, Posição: {resultado_sequencial}")
print(f"Busca Binária - Número Alvo: {num_alvo_bin}, Posição: {result_binario}")
