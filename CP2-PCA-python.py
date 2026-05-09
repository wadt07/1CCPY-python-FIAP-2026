# ========== EXERCÍCIO 01 ==========
# - o código do estado de procedência da carga transportada, sendo um inteiro entre 1 e 5
# - a quantidade de carga em toneladas
# - o código identificador da mercadoria, um inteiro entre 10 e 40
#
# O programa deve calcular:
# - a conversão do peso da carga para quilogramas
# - o valor monetário da mercadoria
# - o imposto incidente com base no estado de procedência e no valor da carga
# - o montante final a ser pago (carga + imposto)

cod_estado = int(input("Informe o código do estado de procedência (1 a 5): "))
peso_ton = float(input("Informe a quantidade de carga em toneladas: "))
cod_mercadoria = int(input("Informe o código da mercadoria (10 a 40): "))

peso_kg = peso_ton * 1000

if 10 <= cod_mercadoria <= 20:
    valor_por_kg = 100.0
elif 21 <= cod_mercadoria <= 30:
    valor_por_kg = 250.0
elif 31 <= cod_mercadoria <= 40:
    valor_por_kg = 340.0

valor_mercadoria = valor_por_kg * peso_kg

match cod_estado:
    case 1:
        taxa_imposto = 0.35
    case 2:
        taxa_imposto = 0.25
    case 3:
        taxa_imposto = 0.15
    case 4:
        taxa_imposto = 0.05
    case 5:
        taxa_imposto = 0.0

valor_imposto = valor_mercadoria * taxa_imposto
montante_final = valor_mercadoria + valor_imposto

print(f"Peso convertido (kg): {peso_kg}")
print(f"Valor da mercadoria: R${valor_mercadoria:.2f}")
print(f"Imposto aplicado: R${valor_imposto:.2f}")
print(f"Montante total: R${montante_final:.2f}")

# ========== EXERCÍCIO 02 ==========
# organize-os em ordem decrescente de modo que A seja o maior lado.
# Em seguida, classifique o triângulo conforme as regras abaixo:
#
# - Se A >= B+C → exiba: NAO FORMA TRIANGULO
# - Se A² = B² + C² → exiba: TRIANGULO RETANGULO
# - Se A² > B² + C² → exiba: TRIANGULO OBTUSANGULO
# - Se A² < B² + C² → exiba: TRIANGULO ACUTANGULO
# - Caso os três lados sejam idênticos → exiba: TRIANGULO EQUILATERO
# - Caso apenas dois lados sejam iguais → exiba: TRIANGULO ISOSCELES

s1 = float(input("Informe o primeiro lado: "))
s2 = float(input("Informe o segundo lado: "))
s3 = float(input("Informe o terceiro lado: "))

# Ordenação decrescente: A é o maior, C o menor
if s1 >= s2 and s1 >= s3:
    A = s1
    if s2 >= s3:
        B = s2
        C = s3
    else:
        B = s3
        C = s2
elif s2 >= s1 and s2 >= s3:
    A = s2
    if s1 >= s3:
        B = s1
        C = s3
    else:
        B = s3
        C = s1
else:
    A = s3
    if s1 >= s2:
        B = s1
        C = s2
    else:
        B = s2
        C = s1

if A >= B + C:
    print("NAO FORMA TRIANGULO")
else:
    # Classificação pelo ângulo
    if (A ** 2) == (B ** 2) + (C ** 2):
        classe_angulo = "TRIANGULO RETANGULO"
    elif (A ** 2) > (B ** 2) + (C ** 2):
        classe_angulo = "TRIANGULO OBTUSANGULO"
    else:
        classe_angulo = "TRIANGULO ACUTANGULO"

    # Classificação pelos lados
    if A == B == C:
        classe_lado = "TRIANGULO EQUILATERO"
    elif A == B or B == C or A == C:
        classe_lado = "TRIANGULO ISOSCELES"
    else:
        classe_lado = "TRIANGULO ESCALENO"

    print(classe_angulo)
    print(classe_lado)

# ========== EXERCÍCIO 03 ==========
nota_cp2 = float(input("Nota CP2: "))
nota_cp3 = float(input("Nota CP3: "))
nota_sp1 = float(input("Nota Sprint 1: "))
nota_sp2 = float(input("Nota Sprint 2: "))
nota_gs  = float(input("Nota Global Solution: "))

# Identificar a menor nota entre os checkpoints
pior_cp = nota_cp1
if nota_cp2 < pior_cp:
    pior_cp = nota_cp2
if nota_cp3 < pior_cp:
    pior_cp = nota_cp3

# Descarta a menor e soma os dois melhores checkpoints
soma_dois_melhores = nota_cp1 + nota_cp2 + nota_cp3 - pior_cp

media_parcial = ((soma_dois_melhores + nota_sp1 + nota_sp2) / 4) * 0.4 + (nota_gs * 0.6)
media_com_peso = media_parcial * 0.4

print(f"\nMédia calculada: {media_parcial:.1f}")
print(f"Média ponderada: {media_com_peso:.1f}")

# ========== EXERCÍCIO 04 ==========
    return salario * 0.015 * horas

def calc_desconto_faltas(salario, faltas):
    return salario * 0.02 * faltas

def calc_bonus(cargo, tem_bonus):
    if tem_bonus == "n":
        return 0
    if cargo == 1:
        return 1000
    elif cargo == 2:
        return 500
    elif cargo == 3:
        return 300
    else:
        return 100


# Entrada de dados
funcionario = input("Nome do colaborador: ")
print("Cargos disponíveis: 1-Gerente  2-Analista  3-Assistente  4-Estagiário")
cargo = int(input("Selecione o cargo: "))
salario = float(input("Salário base (R$): "))
horas_extras = int(input("Quantidade de horas extras: "))
faltas = int(input("Número de faltas no período: "))
tem_bonus = input("Colaborador recebe bônus? (s/n): ").lower()

# Cálculos
extras = calc_horas_extras(salario, horas_extras)
bonus = calc_bonus(cargo, tem_bonus)
desconto = calc_desconto_faltas(salario, faltas)

acrescimos = extras + bonus
salario_bruto = salario + acrescimos
salario_liquido = salario_bruto - desconto

# Exibição do resultado
print("\n===== FOLHA DE PAGAMENTO =====")
print(f"Colaborador:        {funcionario}")
print(f"Salário base:       R$ {salario:.2f}")
print(f"Total de acréscimos: R$ {acrescimos:.2f}")
print(f"Total de descontos:  R$ {desconto:.2f}")
print(f"Salário bruto:      R$ {salario_bruto:.2f}")
print(f"Salário líquido:    R$ {salario_liquido:.2f}")

# ========== EXERCÍCIO 05 ==========

def aprovacao_credito(idade, renda, valor):
    if idade > 18 and valor <= 20 * renda:
        return True
    return False

def obter_taxa_juros(num_parcelas):
    if num_parcelas <= 6:
        return 0.05
    elif num_parcelas <= 12:
        return 0.08
    else:
        return 0.10

def calcular_prestacao(valor, taxa, num_parcelas):
    fator = (1 + taxa) ** num_parcelas
    prestacao = valor * (taxa * fator) / (fator - 1)
    return prestacao

def calcular_total_pago(prestacao, num_parcelas):
    return prestacao * num_parcelas

def calcular_encargos(total_pago, valor_original):
    return total_pago - valor_original


# ──────────── Programa Principal ────────────

cliente = input("Nome do cliente: ")
idade   = int(input("Idade do cliente: "))
renda   = float(input("Renda mensal bruta (R$): "))
valor   = float(input("Valor solicitado para empréstimo (R$): "))
parcelas = int(input("Prazo de pagamento em parcelas (3 a 24): "))

if aprovacao_credito(idade, renda, valor):
    taxa      = obter_taxa_juros(parcelas)
    prestacao = calcular_prestacao(valor, taxa, parcelas)
    total     = calcular_total_pago(prestacao, parcelas)
    encargos  = calcular_encargos(total, valor)

    print("\n=== CRÉDITO APROVADO ===")
    print(f"Cliente................: {cliente}")
    print(f"Valor financiado.......: R$ {valor:.2f}")
    print(f"Taxa mensal de juros...: {taxa * 100:.1f}%")
    print(f"Valor da prestação.....: R$ {prestacao:.2f}")
    print(f"Total a ser pago.......: R$ {total:.2f}")
    print(f"Total em encargos......: R$ {encargos:.2f}")
else:
    print("\n=== CRÉDITO NEGADO ===")
    print(f"Cliente: {cliente}")
    print("Justificativa: menor de idade ou valor solicitado ultrapassa 20x a renda mensal")

