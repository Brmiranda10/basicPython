import os

# Define o caminho para a pasta
pasta = "C:\\Users\\miran\\OneDrive\\Python\\rename\\imagens_teste"

try:
    # Lista todos os arquivos na pasta
    arquivos = sorted([f for f in os.listdir(pasta) if f.lower().endswith(".jpg")])

    # Renomeia os arquivos
    for i, nome_antigo in enumerate(arquivos):
        nome_novo = f"arquivo_{i+1:02d}.jpg"
        caminho_antigo = os.path.join(pasta, nome_antigo)
        caminho_novo = os.path.join(pasta, nome_novo)
        os.rename(caminho_antigo, caminho_novo)
        print(f'Arquivo "{nome_antigo}" renomeado para "{nome_novo}"')

    print("Arquivos renomeados com sucesso!")

except FileNotFoundError:
    print(f'Erro: A pasta "{pasta}" não foi encontrada.')
except Exception as e:
    print(f"Ocorreu um erro: {e}")
