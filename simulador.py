import pandas as pd
import numpy as np

def processar_simulador_metas(caminho_arquivo):
    print("=== Iniciando Processamento do Simulador de Metas ===")
    
    # 1. Simulação de leitura das abas do arquivo real mascarado
    # Em produção, apontaria para 'Simulador Metas MAIO 26.xlsx'
    # Criando dados fictícios estruturados para demonstração do portfólio
    dados_simulados = {
        'Filial': ['Rosário', 'Macaense', 'Marques', 'Centro', 'Copacabana'],
        'Venda_Anterior_Media_3M': [300600.68, 150200.50, 180400.20, 450000.00, 290000.00],
        'Percentual_Meta': [0.07, 0.05, 0.06, 0.08, 0.07]
    }
    
    df = pd.DataFrame(dados_simulados)
    
    # 2. Engenharia de Recursos / Racional de Metas
    df['Valor_Meta_Projetada'] = df['Venda_Anterior_Media_3M'] * (1 + df['Percentual_Meta'])
    df['CMV_Estimado'] = df['Valor_Meta_Projetada'] * 0.652  # Baseado no racional real de 65.2%
    df['Lucro_Bruto_Projetado'] = df['Valor_Meta_Projetada'] * 0.348  # Margem de 34.8%
    
    # 3. Racional de Rateio por Vendedor (Exemplo com 5 vendedores por loja)
    df['Meta_Por_Vendedor_Medio'] = df['Valor_Meta_Projetada'] / 5
    
    print("\n -> Cenário Comercial Projetado:")
    print(df.round(2).to_string(index=False))
    
    # Salvando o resultado processado
    df.to_csv('meta_processada_maio26.csv', index=False)
    print("\n=== Arquivo 'meta_processada_maio26.csv' gerado com sucesso! ===")

if __name__ == "__main__":
    processar_simulador_metas("Simulador Metas MAIO 26.xlsx")