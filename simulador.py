import pandas as pd
import os

def gerar_excel_demonstracao_varejo():
    nome_arquivo = "Simulador Metas MAIO 26.xlsx"
    
    # Se o arquivo já existir, não faz nada
    if os.path.exists(nome_arquivo):
        return
        
    print(f" -> Criando arquivo de demonstração: {nome_arquivo}")
    
    # Criando dados fictícios para a aba Simulador
    df_simulador = pd.DataFrame({
        'Indicador': ['Venda Anterior (Média 3 m)', '%Meta', '$Meta'],
        'Rosário': [300600.68, 0.07, 321642.73],
        'Macaense': [150200.50, 0.05, 157710.53],
        'Marques': [180400.20, 0.06, 191224.21]
    })
    
    # Criando dados fictícios para a aba Resultado LOJA
    df_resultado = pd.DataFrame({
        'Métrica': ['CMV', 'LUCRO BRUTO', 'EXCEDENTE FATURAMENTO'],
        'Rosário': [0.652, 0.348, -10526.74],
        'Macaense': [0.640, 0.360, 4200.10],
        'Marques': [0.655, 0.345, -1200.50]
    })
    
    # Criando dados fictícios para a aba Racional Rateio
    df_rateio = pd.DataFrame({
        'Vendedor': ['Vendedor 1', 'Vendedor 2', 'Vendedor 3', 'Vendedor 4', 'Vendedor 5'],
        'Percentual_Cota': [0.20, 0.20, 0.20, 0.20, 0.20],
        'Meta_Individual_Rosario': [64328.55, 64328.55, 64328.55, 64328.55, 64328.55]
    })
    
    # Salvando tudo em um único arquivo Excel com múltiplas abas
    with pd.ExcelWriter(nome_arquivo, engine='openpyxl') as writer:
        df_simulador.to_excel(writer, sheet_name='Simulador', index=False)
        df_resultado.to_excel(writer, sheet_name='Resultado LOJA', index=False)
        df_rateio.to_excel(writer, sheet_name='Racional Rateio Meta Vendedor', index=False)

def processar_simulador_metas(caminho_arquivo):
    print("=== Iniciando Processamento do Simulador de Metas ===")
    
    # Garante que o arquivo Excel existe
    gerar_excel_demonstracao_varejo()
    
    # Lendo a aba real do Excel gerado
    df_simulador = pd.read_excel(caminho_arquivo, sheet_name='Simulador')
    print("\n -> Dados lidos da aba 'Simulador':")
    print(df_simulador)
    
    # Executa os cálculos matemáticos do pipeline
    # ... (restante do seu código de processamento)
    print("\n=== Processamento concluído com sucesso! ===")

if __name__ == "__main__":
    processar_simulador_metas("Simulador Metas MAIO 26.xlsx")
