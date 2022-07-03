"""
CP004TIN2 Metodos Numericos
29-05-2022 Método dos Trapézios
RA 210395 - Gabriel Coelho Crispi
RA 210491 - João Victor Athayde Grilo
RA 210200 - Luan Bruno Domingues de Oliveira
RA 210331 - Pedro Henrique Lisboa
"""



# *** IMPORTA BIBLIOTECAS ***
import numpy as np
import os
import sympy as sym



# *** DEFININDO FUNÇÕES ***
# Para não ter que sempre repetir durante a main()
def titulo():
    os.system('cls')
    print('***** MÉTODO DOS TRAPÉZIOS *****')
    print('   para polinomios de 5° grau   \n')

# Printa o polinômio
def print_poli(pesos):
    poli_print = ''
    for expoente, peso in enumerate(pesos):
        poli_print += f'+ {peso}*x^{expoente} '
    return poli_print

# Calcula o Polinômio
def f(pesos, x):
    resultado = 0
    for expoente, peso in enumerate(pesos):
        resultado += peso * x ** expoente
    return resultado

# Calcula quantidade de trapézios de acordo com a variável "n"
def base_trapezios(a, b, n):
    return (b-a)/n 

# Aplicação do método dos trapézios
def met_trapezios(a, b, n, funcao, pesos):
    x = np.linspace(a, b, n+1, dtype=float)         # cria uma lista de números em sequencia de "a" até "b" com "n+1" valores
    y = funcao(pesos, x)                            # cria f(x)
    h = base_trapezios(a=a, b=b, n=n)               # calcula tamanho da base do trapézio
    resultado = (h/2) * (y[0] + (2*(np.sum(y[1:-1]))) + y[-1]) # aplica a fórmula nos valores
    return resultado

# Calcula o erro do resultado
def erro(a, b, n, pesos):
    h = base_trapezios(a=a, b=b, n=n)               # calcula tamanho da base do trapézio
    x_var = sym.Symbol('x')
    x = list(np.linspace(a, b, (int(b)*2)+1))            # cria uma lista de números em sequencia de "a" até "b" com "n+1" valores

    # utilização da biblioteca sympy para derivar a função
    func = pesos[0] + pesos[1]*x_var**1 + pesos[2]*x_var**2 + pesos[3]*x_var**3 + pesos[4]*x_var**4 + pesos[5]*x_var**5
    dx1 = sym.diff(func)
    dx2 = sym.diff(dx1)

    # calcula os valores de f(x) e acha o maior
    y = []
    for num in x:
        y.append(dx2.subs(x_var, num))
    max_intervalo_dx2 = max(y)

    erro_n = n * ((h**3)/12) * max_intervalo_dx2
    return erro_n
    
# Recebe "n"
def recebe_n():
    n_bool = False
    while(n_bool == False):    # apenas continua quando "n" for inteiro e positivo, até 9
        titulo()
        n = input('Insira com quantas divisões deseja calcular: ')

        if str.isdigit(n) == True and int(n) <= 18446744073709551616 and int(n) > 0:
            n = int(n)
            n_bool = True
        else:
            print('Você precisa digitar um número INTEIRO e POSITIVO, entre 1 e 9!!!')
            os.system('pause')
            n_bool = False
        return n

# Recebe limites de integração
def recebe_limites_inte():
    limites_integracao = []
    for i in range(2):
        lim = input(f'Insira o {i+1}° limite da integral: ')
        limites_integracao.append(float(lim))
    return limites_integracao

# Recebe o polinômio
def recebe_poli(grau_poli=5):
    pesos = []
    for i in range(grau_poli+1):
        if i == 0:   # primeiro elemento da lista é a constante do polinômio
            peso = float(input(f'Insira a constante de soma do polinômio: '))
            pesos.append(peso)
        else:
            peso = float(input(f'Insira o peso do termo que multiplica x^{i}: '))
            pesos.append(peso)
    return pesos



# *** MAIN ***
def main():
    titulo()
    
    # declaração do limite de grau do polinômio
    grau_poli = 5  # descrito no PDF para aplicação do Método dos Trapézios em polinõmios de grau 5
    
    # recebe variavel n
    n = recebe_n()

    # recebe os limites de integração (a, b)
    limites_integracao = recebe_limites_inte()

    # recebe o polinomio
    titulo()
    pesos = recebe_poli(grau_poli)
    
    # mostra polinomio e resultados
    titulo()
    print(f'Segue polinônio montado: {print_poli(pesos)}')
    print(f'Resultado Integral Simples: {met_trapezios(limites_integracao[0], limites_integracao[1], 1, f, pesos)}, Erro de: {erro(min(limites_integracao), max(limites_integracao), 1, pesos)}')
    print(f'Resultado Integral Composta: {met_trapezios(limites_integracao[0], limites_integracao[1], n, f, pesos)}, Erro de: {erro(min(limites_integracao), max(limites_integracao), n, pesos)}')

# chama função main
if __name__ == "__main__":
    main()