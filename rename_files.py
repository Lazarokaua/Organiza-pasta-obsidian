import os
from dotenv import load_dotenv


load_dotenv()

MIDIA_FOLDER = os.getenv("MIDIA_FOLDER")

def renomear_arquivos(arquivos, materia):
    count = 1
    for arquivo in os.listdir(arquivos):
        caminho_origem = os.path.join(arquivos, arquivo)

        if os.path.isdir(caminho_origem):
            print(f"{arquivo} Pasta encontrda, ignorando...")
            continue

        materia_name = f"{materia}_unidade_{count}.pdf"
        caminho_destino = os.path.join(arquivos, materia_name)
        os.rename(caminho_origem, caminho_destino)
        print(arquivo)
        count += 1


if __name__ == "__main__":
    # renomear_arquivos(MIDIA_FOLDER, "ESG")
    # renomear_arquivos(MIDIA_FOLDER, "IA")
    # renomear_arquivos(MIDIA_FOLDER, "Metodos_ageis")
    # renomear_arquivos(MIDIA_FOLDER, "Negócios_inovadores")
    renomear_arquivos(MIDIA_FOLDER, "mobile")

    ## criar uma forma mais didatica e usual para essa função;
