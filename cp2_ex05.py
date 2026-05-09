
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
