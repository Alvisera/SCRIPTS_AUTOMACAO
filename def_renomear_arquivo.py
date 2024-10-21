import os
impor time

def renomear_arquivo(pasta_downloads, nome_do_arquivo):

    # Define o caminho completo do novo arquivo
    novo_nome_base = os.path.join(pasta_downloads, nome_do_arquivo)
    extensao = '.zip'
    
    # Verifica se o arquivo já existe e cria um novo nome se necessário
    
    while os.path.exists(novo_nome_base + extensao):
        novo_nome_base = os.path.join(pasta_downloads, f"{nome_do_arquivo}")

    # Renomeia o arquivo após o download
    
    arquivo_baixado = os.path.join(pasta_downloads, "arquivo_completo.zip")  # Ajuste para o nome real do arquivo que você espera
    if os.path.exists(arquivo_baixado):
        os.rename(arquivo_baixado, novo_nome_base + extensao)
        print(f"Arquivo renomeado para: {novo_nome_base + extensao}")
    else:
        print("Arquivo para renomear não encontrado.")


pasta_matriz_saidas = r"robo_download_nfe\matriz\saidas" 
nome_arq = f'MATRIZ - {notas_fiscais} - {inicio}'
nome_do_arquivo = nome_arq.replace('/', '_')
print(nome_do_arquivo)

# Verifica se o arquivo foi baixado com sucesso
if os.path.exists(os.path.join(pasta_matriz_saidas, "arquivo_completo.zip")):
    renomear_arquivo(pasta_matriz_saidas, nome_do_arquivo)
    break  # Sai do loop se o download foi bem-sucedido
else:
    print("Download falhou. Tentando novamente...")
    time.sleep(2)  # Aguarda um tempo antes de tentar novamente