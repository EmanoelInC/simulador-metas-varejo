import os
import pandas as pd

def gerar_excel_demonstracao_varejo():
    """
    Gera automaticamente o arquivo Excel de simulação com dados mascarados
    caso ele não exista localmente, garantindo reprodutibilidade e conformidade (Compliance).
    """
    nome_arquivo = "Simulador Metas MAIO 26.xlsx"
    
    if os.path.exists(nome_arquivo):
        return
        
    print(f" -> Criando arquivo Excel de demonstração com dados mascarados: {nome_arquivo}")
    
    # Aba 1: Simulador (Estrutura de metas baseada no histórico)
    df_simulador = pd.DataFrame({
        'Indicador': ['Venda Anterior (Média 3 m)', '%Meta', '$Meta'],
        'Rosário': [300600.68, 0.07, 321642.73],
        'Macaense': [150200.50, 0.05, 157710.53],
        'Marques': [180400.20, 0.06, 191224.21]
    })
    
    # Aba 2: Resultado LOJA (Margens e CMV do negócio)
    df_resultado = pd.DataFrame({
        'Métrica': ['CMV', 'LUCRO BRUTO', 'EXCEDENTE FATURAMENTO'],
        'Rosário': [0.652, 0.348, -10526.74],
        'Macaense': [0.640, 0.360, 4200.10],
        'Marques': [0.655, 0.345, -1200.50]
    })
    
    # Aba 3: Racional Rateio Meta Vendedor (Divisão de cota por equipe)
    df_rateio = pd.DataFrame({
        'Vendedor': ['Vendedor 1', 'Vendedor 2', 'Vendedor 3', 'Vendedor 4', 'Vendedor 5'],
        'Percentual_Cota': [0.20, 0.20, 0.20, 0.20, 0.20],
        'Meta_Individual_Rosario': [64328.55, 64328.55, 64328.55, 64328.55, 64328.55]
    })
    
    with pd.ExcelWriter(nome_arquivo, engine='openpyxl') as writer:
        df_simulador.to_excel(writer, sheet_name='Simulador', index=False)
        df_resultado.to_excel(writer, sheet_name='Resultado LOJA', index=False)
        df_rateio.to_excel(writer, sheet_name='Racional Rateio Meta Vendedor', index=False)

def processar_simulador_metas(caminho_arquivo):
    print("=== Iniciando Processamento do Simulador de Metas ===")
    
    # Garante a existência do arquivo físico .xlsx corporativo mascarado
    gerar_excel_demonstracao_varejo()
    
    # Etapa de Engenharia de Dados: Leitura analítica do Excel gerado
    print(f" -> Lendo arquivo físico: {caminho_arquivo}")
    df_sim = pd.read_excel(caminho_arquivo, sheet_name='Simulador')
    df_res = pd.read_excel(caminho_arquivo, sheet_name='Resultado LOJA')
    
    print("\n -> Consolidação da aba 'Simulador':")
    print(df_sim.to_string(index=False))
    
    print("\n -> Consolidação da aba 'Resultado LOJA':")
    print(df_res.to_string(index=False))
    
    # Exporta uma tabela tratada final para o pipeline comercial
    df_sim.to_csv('meta_comercial_tratada.csv', index=False)
    print("\n=== Pipeline concluído! Arquivo 'meta_comercial_tratada.csv' gerado. ===")

if __name__ == "__main__":
    processar_simulador_metas("Simulador Metas MAIO 26.xlsx")
