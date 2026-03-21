from getopt import long_has_args

print("ola mundo")

print(7+4)
print("7+4")
print("7"+"4") # CONCATENAÇÃO DE STRINGS

#Comentarios de 1 linha em python
...

# VARIAVEIS
nome = "guilherme" # string - texto
idade = 18 # int - numero
peso = 51.8 # float - num. decimal

print(nome, idade, peso)
print(f"oiiii, {nome}!!!")
# INPUT - SIMULÇÃO DE FORMS NO CMD
nome = input("digite seu nome: ")
idade = int(input("digite sua idade: "))
print("oiii", nome, " vc tem" , idade, "anos" )
print(f"oiii {nome}! vc tem {idade} anos")

nova_idade = idade + 1
print(nova_idade)
