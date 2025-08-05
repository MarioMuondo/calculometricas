# Cálculo de Métricas de Avaliação de Aprendizado

Este projeto realiza o cálculo das principais métricas para avaliação de modelos de classificação, utilizando uma matriz de confusão arbitrária.

## 🔢 Matriz de Confusão Utilizada

|                | Previsto Positivo | Previsto Negativo |
|----------------|-------------------|-------------------|
| **Real Positivo** | VP = 70           | FN = 10           |
| **Real Negativo** | FP = 5            | VN = 100          |

## 📐 Métricas Calculadas

- **Acurácia** = (VP + VN) / (VP + VN + FP + FN)
- **Sensibilidade (Recall)** = VP / (VP + FN)
- **Especificidade** = VN / (VN + FP)
- **Precisão (Precision)** = VP / (VP + FP)
- **F-Score** = 2 * (Precisão * Sensibilidade) / (Precisão + Sensibilidade)

## 🧮 Valores Calculados

- Acurácia: 0.94
- Sensibilidade (Recall): 0.875
- Especificidade: 0.952
- Precisão: 0.933
- F-Score: 0.903

## ▶️ Como Executar

```bash
python metrics_calculator.py
