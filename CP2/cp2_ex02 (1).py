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
