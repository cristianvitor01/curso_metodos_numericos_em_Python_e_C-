# -*- coding: utf-8 -*-

'''
**************************************************************************************
* Name: Método da Bisseção em python                                                 *
* Copyright: Computação Cientifica                                                   *
* Author: Luciano Mendes                                                             *
* Date: 25/07/20 hora: 05:18pm                                                       *
* Description: Programa encontra soluções para equações usando o método da Bisseção  *
**************************************************************************************
'''

import pandas as pd
import math

def f(x):
    return (0.25 * x ** 4 + 2.1 * x ** 3 - 7.3 * x ** 2 + 3.04)

l = 1e-5
e = 1e-5
Ni = 10000

a = float(input("Entre com o valor de 'a' do intervalo [a,b]: "))
b = float(input("Entre com o valor de 'b' do intervalo [a,b]: "))

cont = 0

c = b - a
x = (a + b)/2.0

# Criar listas para armazenar os resultados em cada iteração
iteracao = []
a_vals = []
b_vals = []
c_vals = []
f_a_vals = []
f_b_vals = []
f_c_vals = []

while(c > l):
    if(f(a)*f(x) < 0.0):
        b = x
    if(f(a)*f(x)> 0.0):
        a = x
    c = b - a
    x = (a + b)/2.0
    cont = cont + 1
    if(cont >= Ni or math.fabs(f(x)) < e):
        break
    
    # Adicionar os valores atuais à lista de resultados
    iteracao.append(cont)
    a_vals.append(a)
    b_vals.append(b)
    c_vals.append(c)
    f_a_vals.append(f(a))
    f_b_vals.append(f(b))
    f_c_vals.append(f(x))

# Criar um dicionário com as listas de resultados
resultados = {'Iteração': iteracao, 'a': a_vals, 'b': b_vals, 'c': c_vals, 'f(a)': f_a_vals, 'f(b)': f_b_vals, 'f(c)': f_c_vals}

# Converter o dicionário em um DataFrame do Pandas
df = pd.DataFrame(resultados)

# Exibir o DataFrame como uma tabela
print(df)

print()
print("\n\nRaíz: %f\nIterações: %d\nf(%f) = %f \n\n" %(x,cont,x,f(x)))



























