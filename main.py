import glob
import shutil
import os

from dotenv import load_dotenv
# listar a pasta que vou observar
load_dotenv()

MIDIA_FOLDER = os.getenv("MIDIA_FOLDER")
AUDIO_FOLDER = os.getenv("AUDIO_FOLDER")
IMAGE_FOLDER = os.getenv("IMAGE_FOLDER")
PDFS_FOLDER = os.getenv("PDFS_FOLDER")
VIDEOS_FOLDER = os.getenv("VIDEOS_FOLDER")


def mover_arquivos():
    # mover para as pastas equivalentes ao tipo de arquivo

    for arquivo in os.listdir(MIDIA_FOLDER):
        if arquivo.endswith(".png"):
            caminho_origem = os.path.join(MIDIA_FOLDER, arquivo)
            caminho_destino = os.path.join(IMAGE_FOLDER, arquivo)
            shutil.move(caminho_origem, caminho_destino)
        # elif arquivo.endswith(".png"):
        #     shutil.move(arquivo, IMAGE_FOLDER)
        # elif arquivo.endswith(".mp4"):
        #     shutil.move(arquivo, VIDEOS_FOLDER)
        else:
            print(f"Arquivo não classificado: {arquivo}")

if __name__ == "__main__":
    mover_arquivos()
