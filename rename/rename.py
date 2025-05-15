import os


def renomear_arquivos(pasta):
    arquivos_png = sorted([f for f in os.listdir(pasta) if f.lower().endswith(".png")])
    for indice, nome_antigo in enumerate(arquivos_png):
        nome_novo = f"arquivo_{indice + 1:02d}.jpg"
        caminho_antigo = os.path.join(pasta, nome_antigo)
        caminho_novo = os.path.join(pasta, nome_novo)
        os.rename(caminho_antigo, caminho_novo)
    print(f"Arquivos na pasta '{pasta}' renomeados com sucesso!")


if __name__ == "__main__":
    pasta_imagens = "."  # Use "." para a pasta atual, ou coloque o caminho completo da sua pasta aqui
    renomear_arquivos(pasta_imagens)
