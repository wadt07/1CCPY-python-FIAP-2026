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
