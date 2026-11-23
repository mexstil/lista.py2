#Questão11.py
# 11. A Tabuada Mágica: Peça ao usuário para digitar um número inteiro.
# Use um laço for para imprimir a tabuada completa desse número (de x 1 até x 10).

numero = int(input("Digite um número inteiro: "))

for multiplicador in range(1, 11):
    resultado = numero * multiplicador
    print(f"{numero} x {multiplicador} = {resultado}")


#Questão12.py
# 12. O Cofre Persistente: Crie uma senha secreta (ex: "dragoo123").
# Use um laço while que pede a senha repetidamente. Enquanto errar,
# mostre "Senha incorreta, tente novamente!". Quando acertar,
# encerre o loop e mostre "Cofre Aberto!".

senha_secreta = "dragoo123"
senha_digitada = input("Digite a senha: ")

while senha_digitada != senha_secreta:
    print("Senha incorreta, tente novamente!")
    senha_digitada = input("Digite a senha: ")

print("Cofre Aberto! ")

#Questão13.py
# 13. Contagem Regressiva da NASA: Use o for com passo negativo
# para fazer uma contagem regressiva de 10 até 0. Quando chegar
# no 0, imprima "DECOLAR! ".

for contador in range(10, -1, -1):
    print(contador)
print("DECOLAR! ")

#Questão14.py
# 14. Somador de Moedas: Peça para o usuário digitar quantas moedas
# encontrou em 5 baús diferentes (usando um for de 5 voltas).
# A cada volta, some o valor em uma variável total_ouro e,
# no final, mostre a riqueza acumulada.

total_ouro = 0

for baud in range(5):
    moedas = int(input(f"Quantas moedas no baú {baud + 1}? "))
    total_ouro = total_ouro + moedas

print(f" Você acumulou {total_ouro} moedas de ouro!")

#Questão15.py
# 15. O Detector de Números Pares: Use um for de 1 até 20.
# Dentro do loop, use um if com o operador resto (% 2 == 0)
# para imprimir apenas os números pares.

for numero in range(1, 21):
    if numero % 2 == 0:
        print(numero)

#Questão16.py
# 16. A Barra de Stamina (Energia): O herói começa com energia = 100.
# Crie um while que rode enquanto a energia for maior que 0.
# A cada volta, pergunte se quer "correr" (-20) ou "pular" (-15).
# Quando a energia acabar, mostre "O herói desmaiou de cansaço!".

energia = 100

while energia > 0:
    print(f" Energia atual: {energia}")
    acao = input("Quer correr ou pular? ").lower()
   
    if acao == "correr":
        energia = energia - 20
    elif acao == "pular":
        energia = energia - 15
    else:
        print("Ação inválida! Escolha 'correr' ou 'pular'.")

print("O herói desmaiou de cansaço! ")

#Questão17.py
# 17. Validador de Nota Escolar: Peça uma nota de 0 a 10.
# Enquanto digitar um número inválido (menor que 0 ou maior que 10),
# o while deve repetir pedindo uma nota válida.

nota = float(input("Digite uma nota de 0 a 10: "))

while nota < 0 or nota > 10:
    print("Nota inválida! Digite um valor entre 0 e 10.")
    nota = float(input("Digite uma nota de 0 a 10: "))

print(f" Nota registrada: {nota}")

#Questão18.py
# 18. O Contador de Letras: Peça uma palavra. Use um for letra
# por letra e imprima cada letra em uma linha separada.
# No final, mostre quantas letras 'a' existem nela.

palavra = input("Digite uma palavra: ")
contagem_a = 0

for letra in palavra:
    print(letra)
    if letra.lower() == 'a':
        contagem_a = contagem_a + 1

print(f"A palavra tem {contagem_a} letra(s) 'a'!")

#Questão19.py
# 19. A Escada de Asteriscos: Peça um número N. Use um laço
# para desenhar uma escada no terminal usando o símbolo *.

n = int(input("Digite um número para o tamanho da escada: "))

for linha in range(1, n + 1):
    print("*" * linha)

#Questão20.py
# 20. O Caixa de Supermercado: Peça preços usando while.
# Some até que o usuário digite 0. Mostre o total.

total = 0
preco = float(input("Digite o preço do produto (0 para terminar): "))

while preco != 0:
    total += preco
    preco = float(input("Digite o preço do produto (0 para terminar): "))

print(f" Total da compra: R$ {total:.2f}")

#Questão21.py
# 21. Batalha de Turnos: Herói = 100 vida, Goblin = 80 vida.
# Enquanto ambos vivos, jogador escolhe: 1-Atacar (-15) ou 2-Curar (+10).
# Goblin contra-ataca (-12) sempre. Mostre o vencedor.

vida_heroi = 100
vida_goblin = 80

while vida_heroi > 0 and vida_goblin > 0:
    print(f"\n Herói: {vida_heroi} HP |  Goblin: {vida_goblin} HP")
    escolha = input("Escolha: 1 - Atacar | 2 - Curar: ")
   
    if escolha == "1":
        vida_goblin -= 15
        print(" Você ataca! Goblin perde 15 HP!")
    elif escolha == "2":
        vida_heroi += 10
        print(" Você se cura! +10 HP!")
    else:
        print(" Escolha inválida!")
        continue
   
    if vida_goblin > 0:
        vida_heroi -= 12
        print(" Goblin ataca! Você perde 12 HP!")

print("\n VOCÊ VENCEU!" if vida_heroi > 0 else "\n Você foi derrotado...")

#Questão22.py
# 22. O Limite de Tentativas: Senha com máximo de 3 tentativas.
# Bloqueia após 3 erros.

SENHA_CORRETA = "42"
tentativas = 0

while tentativas < 3:
    tentativa = input("Digite a senha: ")
    if tentativa == SENHA_CORRETA:
        print(" Senha correta! Acesso liberado!")
        break
    tentativas += 1
    if tentativas < 3:
        print(f" Errada! Restam {3 - tentativas} tentativas.")
else:
    print(" Cartão Bloqueado! Chamando os guardas!")

#Questão23.py
# 23. Adivinhe o Número Secreto: Maior = "Chutou alto!", Menor = "Chutou baixo!"
# Conta quantas tentativas até acertar.

import random
secreto = random.randint(1, 100)
tentativas = 0

while True:
    chute = int(input("Adivinhe o número (1 a 100): "))
    tentativas += 1
    if chute == secreto:
        print(f" Parabéns! Acertou em {tentativas} tentativas!")
        break
    elif chute > secreto:
        print(" Chutou alto! Tente um número menor.")
    else:
        print(" Chutou baixo! Tente um número maior.")

#Questão24.py
# 24. Relógio Digital: Mostrar de 00:00 até 02:59 usando for aninhado.

for hora in range(3):
    for minuto in range(60):
        print(f"{hora:02d}:{minuto:02d}")

#Questão25.py
# 25. Verificar se um número é primo. Tem apenas 2 divisores.

numero = int(input("Digite um número inteiro positivo: "))
divisores = 0

for teste in range(1, numero + 1):
    if numero % teste == 0:
        divisores += 1

if divisores == 2:
    print(f" {numero} é um Número Primo!")
else:
    print(f" {numero} NÃO é um Número Primo!")

#Questão26.py
# 26. Sequência de Fibonacci: 0, 1, 1, 2, 3, 5, 8...
# Mostrar os N primeiros termos.

n = int(input("Quantos termos da sequência deseja ver? "))
a, b = 0, 1
contador = 0

while contador < n:
    print(a, end=" ")
    a, b = b, a + b
    contador += 1

#Questão27.py
# 27. Elevador: 10 andares. Usuário escolhe destino (-1 = sair).
# Simula subindo/descendo andar por andar.

andar_atual = 0
total_andares = 10

while True:
    print(f"\n Andar atual: {andar_atual}º")
    destino = int(input(f"Para qual andar deseja ir? (0 a {total_andares}) | -1 = Sair: "))
   
    if destino == -1:
        print(" Saindo do elevador. Até logo!")
        break
    if destino < 0 or destino > total_andares:
        print(" Andar inválido!")
        continue
   
    while andar_atual != destino:
        if destino > andar_atual:
            andar_atual += 1
            print(f" Subindo... Andar {andar_atual}")
        else:
            andar_atual -= 1
            print(f" Descendo... Andar {andar_atual}")
   
    print(f" Chegou ao {andar_atual}º andar!")

#Questão28.py
# 28. Simulador de Juros do Cofrinho: 100 moedas, rende 10% ao mês.
# Pergunte quantos meses e mostre o saldo mês a mês (juros compostos).

saldo = 100.0
meses = int(input("Por quantos meses vai deixar o dinheiro render? "))

for mes in range(1, meses + 1):
    saldo = saldo * 1.10
    print(f"Mês {mes}: {saldo:.2f} moedas")

print(f"\n Após {meses} meses, você terá {saldo:.2f} moedas!")

#Questão29.py
# 29. O Fatorial Explosivo: Calcular e mostrar o fatorial de um número positivo.

numero = int(input("Digite um número positivo: "))

while numero < 0:
    print(" Digite um número positivo!")
    numero = int(input("Digite um número positivo: "))

fatorial = 1
contador = numero

while contador > 0:
    fatorial = fatorial * contador
    contador = contador - 1

print(f"\n {numero}! = {fatorial}")

#Questão30.py
# 30. O DESAFIO DO CHEFÃO: Simulador de máquina de fliperama.
# Começa com 5 fichas. Menu: 1-Corrida(1f), 2-Luta(2f), 3-Comprar, 4-Sair.
# Bloqueia jogada sem fichas. 3 fases por jogo. Encerra em 4 ou sem fichas.

fichas = 5

while True:
    print("\n" + "=" * 35)
    print(f" Fichas disponíveis: {fichas}")
    print("=" * 35)
    print("1 - Jogar Corrida (custa 1 ficha)")
    print("2 - Jogar Luta   (custa 2 fichas)")
    print("3 - Comprar mais fichas")
    print("4 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "4":
        print(" Obrigado por jogar! Até a próxima!")
        break

    elif opcao == "1":
        if fichas < 1:
            print(" Sem fichas! Compre mais para jogar.")
            continue
        fichas -= 1
        print("\n Corrida iniciada!")
        for fase in range(1, 4):
            print(f"   Jogando... Fase {fase} de 3!")
        print("Corrida concluída! Você venceu!")

    elif opcao == "2":
        if fichas < 2:
            print(" Precisa de 2 fichas! Compre mais.")
            continue
        fichas -= 2
        print("\n  Luta iniciada!")
        for fase in range(1, 4):
            print(f"   Lutando... Fase {fase} de 3!")
        print(" Luta concluída! Você venceu!")

    elif opcao == "3":
        compra = int(input("Quantas fichas deseja comprar? "))
        if compra > 0:
            fichas += compra
            print(f" Compra realizada! Agora você tem {fichas} fichas.")
        else:
            print(" Quantidade inválida!")

    else:
        print(" Opção inválida! Escolha entre 1 e 4.")

    if fichas <= 0:
        print("\n Acabaram suas fichas! Até logo!")
        break
