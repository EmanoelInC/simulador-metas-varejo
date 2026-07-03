# Simulador Inteligente de Metas e Análise de Rentabilidade (Varejo)

Este projeto automatiza o desenvolvimento de cenários comerciais para redes de varejo, utilizando **Python** para processamento preditivo de metas e análise de margens.

## 📈 Problema de Negócio
A definição manual de metas comerciais frequentemente ignora sazonalidades locais, médias móveis de performance e o impacto direto no CMV (Custo de Mercadoria Vendida). Este projeto resolve esse gargalo automatizando o desdobramento de metas com base em dados históricos.

## 🛠️ Tecnologias Utilizadas
* **Python**: Core do processamento.
* **Pandas**: Manipulação de dados e cálculos matriciais.
* **Numpy**: Vetorização das regras de negócio comerciais.

## 📊 Estrutura do Algoritmo
1. **Leitura Estatística**: Coleta da média móvel de faturamento dos últimos 3 meses.
2. **Modelagem Financeira**: Aplicação automática do teto de Markup e trava de margem em **34.8%**.
3. **Racional de Rateio**: Divisão proporcional e meritocrática da meta para a força de vendas na ponta.