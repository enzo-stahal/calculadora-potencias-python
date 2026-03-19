# Potência Útil (mecânica) ------> PU ----> em Watts
PU = int(input("Insira o valor da potência em Watts: "))
# Rendimento (de 0 a 1)
n = float(input("Insira o valor do rendimento (de 0 a 1): "))
# Fator de potência (FP) (de 0 a 1) ------> FP (cosPhi)
FP = float(input("Insira o fator de potência (de 0 a 1): "))

# Potência Ativa (P)
P = PU / n
# Potência Aparente (S)
S = P / FP
# Potência Reativa(Q)
# Eponenciação ---> **
# Raiz quadrada ----> ** 0.5
Q = (S**2 - P**2)**0.5

print(f"A potência ativa será de {int(P)} W")
print(f"A potência aparente será de {int(S)} VA")
print(f"A potência reativa será de {int(Q)} VAr")
