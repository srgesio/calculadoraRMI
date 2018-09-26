import Pyro4
from tkinter import *

calcular = Pyro4.Proxy("PYRONAME:calculadoraTop")    # use name server object lookup uri shortcut

op = 30

while op != 0:
    
    op = input("CALCULADORA TOP \n-----------------\n\"1\" para Somar\n\"2\" para Subtrair\n\"3\" para Multiplicar\n\"4\" para Dividir\n\"0\" para Sair\n\nOperação >>")
    
    if (op.strip() == '0'):
        print('Saindo...')
        op=0
        break
    elif(op.strip()== '1'):
        entrada1 = input(">> ").strip()
        entrada2 = input(">> ").strip()
        print('\n\n\n\n{}\n\n\n\n'.format(calcular.somar(float(entrada1), float(entrada2))))
        
    elif(op.strip()== '2'):
        entrada1 = input(">> ").strip()
        entrada2 = input(">> ").strip()
        print('\n\n\n\n{}\n\n\n\n'.format(calcular.subtrair(float(entrada1), float(entrada2))))
        
    elif(op.strip()== '3'):
        entrada1 = input(">> ").strip()
        entrada2 = input(">> ").strip()
        print('\n\n\n\n{}\n\n\n\n'.format(calcular.multiplicar(float(entrada1), float(entrada2))))
        
    elif(op.strip()== '4'):
        entrada1 = input(">> ").strip()
        entrada2 = input(">> ").strip()
        print('\n\n\n\n{}\n\n\n\n'.format(calcular.dividir(float(entrada1), float(entrada2))))


        