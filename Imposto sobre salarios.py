# NESSE PROGRAMA VAMOS TER UMA CALCULADORA DE SALARIOS
salario_bruto = float(input("Escreva seu salario bruto: "))
salario_liquido = 0

FAIXA_INSS1 = 7.5/100
FAIXA_INSS2 = 9.0/100
FAIXA_INSS3 = 12.0/100
FAIXA_INSS4 = 14.0/100
FAIXA_IRRF1 = 7.0/100
FAIXA_IRRF2 = 15/100
FAIXA_IRRF3 = 22.5/100
FAIXA_IRRF4 = 27.5/100

if salario_bruto<1302:
    desconto_INSS = salario_bruto*FAIXA_INSS1
    salario_base_calculo = salario_bruto - desconto_INSS

if salario_bruto>1303 and salario_bruto<2571:
    desconto_INSS = salario_bruto*FAIXA_INSS2
    salario_base_calculo = salario_bruto - desconto_INSS + 19.53       

if salario_bruto>2571 and salario_bruto<3856:
    desconto_INSS = salario_bruto*FAIXA_INSS3
    salario_base_calculo = salario_bruto - desconto_INSS + 96.67

if salario_bruto>3856 and salario_bruto<7507:
    desconto_INSS = salario_bruto*FAIXA_INSS4
    salario_base_calculo = salario_bruto - desconto_INSS + 173,80


if salario_base_calculo>1903.0:
    if salario_base_calculo>1903 and salario_base_calculo<2826:
        desconto_IRRF = salario_base_calculo*FAIXA_IRRF1
        salario_liquido = salario_base_calculo - desconto_IRRF

    if salario_base_calculo>2827 and salario_base_calculo< 3751:
        desconto_IRRF = salario_base_calculo*FAIXA_IRRF2
        salario_liquido = salario_base_calculo - desconto_IRRF

    if salario_base_calculo>37512 and salario_base_calculo<4664:
        desconto_IRRF = salario_base_calculo*FAIXA_IRRF3
        salario_liquido = salario_base_calculo - desconto_IRRF

    if salario_base_calculo>4665:
        desconto_IRRF = salario_base_calculo*FAIXA_IRRF4
        salario_liquido = salario_base_calculo - desconto_IRRF

else:
    salario_liquido = salario_base_calculo


print(f"Seu salario liquido e {salario_liquido}")


