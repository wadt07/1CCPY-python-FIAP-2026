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
