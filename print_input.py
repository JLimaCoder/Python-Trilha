nome = input("Informe o seu nome: ")
idade = input("Informe a sua idade: ")

print(nome, idade)
print(nome, idade, end="...\n")
print(nome, int(idade), end="...\n")
print(nome, int(idade), sep="#")
