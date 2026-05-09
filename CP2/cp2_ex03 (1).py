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
