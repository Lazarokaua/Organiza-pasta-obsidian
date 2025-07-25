import glob
import shutil
import os

from rename_files import renomear_arquivos
from dotenv import load_dotenv
# listar a pasta que vou observar
load_dotenv()

MIDIA_FOLDER = os.getenv("MIDIA_FOLDER")
AUDIO_FOLDER = os.getenv("AUDIO_FOLDER")
IMAGE_FOLDER = os.getenv("IMAGE_FOLDER")
PDFS_FOLDER = os.getenv("PDFS_FOLDER")
VIDEOS_FOLDER = os.getenv("VIDEOS_FOLDER")


if __name__ == "__main__":
    # mover para as pastas equivalentes ao tipo de arquivo

    # tuples
    tuple_pastas = (AUDIO_FOLDER, IMAGE_FOLDER, PDFS_FOLDER, VIDEOS_FOLDER)
    tuple_audios = (".m4a", ".flac", ".mp3", ".wav", ".wma")
    tuple_images = (".jpeg", ".jpg", ".png", ".gif", ".tiff")
    tuple_videos = (".mp4", ".mov", ".avi", ".mkv", ".flv")
    tuple_pdfs = (".pdf",)

    for arquivo in os.listdir(MIDIA_FOLDER):
        caminho_origem = os.path.join(MIDIA_FOLDER, arquivo)

        # Primeiro, verifica se é um diretório para ignorá-lo
        if os.path.isdir(caminho_origem):
            print(f"Ignorando pasta: {arquivo}")
            continue

        if arquivo.endswith(tuple_images):
            caminho_destino = os.path.join(IMAGE_FOLDER, arquivo)
            shutil.move(caminho_origem, caminho_destino)
        elif arquivo.endswith(tuple_pdfs):
            caminho_destino = os.path.join(PDFS_FOLDER, arquivo)
            shutil.move(caminho_origem, caminho_destino)
        elif arquivo.endswith(tuple_videos):
            caminho_destino = os.path.join(VIDEOS_FOLDER, arquivo)
            shutil.move(caminho_origem, caminho_destino)
        elif arquivo.endswith(tuple_audios):
            caminho_destino = os.path.join(AUDIO_FOLDER, arquivo)
            shutil.move(caminho_origem, caminho_destino)
        else:
            print(f"Arquivo não classificado: {arquivo}")

