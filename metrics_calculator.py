

# Matriz de confusão arbitrária
VP = 70  # Verdadeiros Positivos
VN = 100 # Verdadeiros Negativos
FP = 5   # Falsos Positivos
FN = 10  # Falsos Negativos

# Cálculo das métricas
acuracia = (VP + VN) / (VP + VN + FP + FN)
sensibilidade = VP / (VP + FN)
especificidade = VN / (VN + FP)
precisao = VP / (VP + FP)
f_score = 2 * (precisao * sensibilidade) / (precisao + sensibilidade)

# Impressão dos resultados
print("Métricas de Avaliação:")
print(f"Acurácia: {acuracia:.3f}")
print(f"Sensibilidade (Recall): {sensibilidade:.3f}")
print(f"Especificidade: {especificidade:.3f}")
print(f"Precisão: {precisao:.3f}")
print(f"F-Score: {f_score:.3f}")
