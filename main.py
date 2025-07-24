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

# mover para as pastas equivalentes ao tipo de arquivo
