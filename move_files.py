import shutil
import os
import time
import fitz
from google import genai

from rename_files import renomear_arquivos
from dotenv import load_dotenv
# listar a pasta que vou observar
load_dotenv()
client = genai.Client()

MIDIA_FOLDER = os.getenv("MIDIA_FOLDER")
AUDIO_FOLDER = os.getenv("AUDIO_FOLDER")
IMAGE_FOLDER = os.getenv("IMAGE_FOLDER")
PDFS_FOLDER = os.getenv("PDFS_FOLDER")
VIDEOS_FOLDER = os.getenv("VIDEOS_FOLDER")


def extrair_nome_com_gemini(texto_pdf):
    prompt = (
        "Você é um organizador de arquivos PDF. Seu trabalho é gerar um nome de arquivo curto, direto e padronizado, "
        "com base no conteúdo textual das 3 primeiras páginas do PDF fornecido.\n\n"
        "Se o conteúdo for um material acadêmico da faculdade, como apostilas, provas ou slides, utilize o formato:\n"
        "materia_unidade_x.pdf (tudo em minúsculo, sem espaços, com underline).\n"
        "Exemplo: filosofia_unidade_2.pdf\n\n"
        "Se o conteúdo não for acadêmico (como e-books, artigos, recibos, relatórios, etc), use um nome descritivo curto "
        "baseado no tema principal. Exemplo: resumo_inteligencia_artificial.pdf\n\n"
        "Nunca inclua aspas, crases ou pontuação especial. Apenas o nome final do arquivo.\n\n"
        "Conteúdo:\n"
        f"{texto_pdf}"
    )
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[
                {"role": "user", "parts": [{"text": prompt}]}
            ]
        )
        return response.candidates[0].content.parts[0].text.strip().splitlines()[0].replace("`", "").replace('"', "").replace("'", "")
    except Exception as e:
        print(f"[ERRO] Falha na chamada da IA: {e}")
        return None




if __name__ == "__main__":
    # timestamp com o tempo inicial
    start_time = time.time()


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
            try:
                with fitz.open(caminho_origem) as doc:
                    texto = ""
                    for i in range(min(3, len(doc))):
                        texto += doc[i].get_text() + "\n"

                novo_nome = extrair_nome_com_gemini(texto)
                print(f"[DEBUG] Nome sugerido pela IA: {novo_nome}")
                if novo_nome:
                    if not novo_nome.endswith(".pdf"):
                        novo_nome += ".pdf"
                    caminho_destino = os.path.join(PDFS_FOLDER, novo_nome)
                    os.rename(caminho_origem, caminho_destino)
                    print(f"Renomeado pela IA: {arquivo} → {novo_nome}")
                else:
                    caminho_destino = os.path.join(PDFS_FOLDER, arquivo)
                    shutil.move(caminho_origem, caminho_destino)
            except Exception as e:
                print(f"Erro ao processar PDF com IA: {arquivo}: {e}")
                caminho_destino = os.path.join(PDFS_FOLDER, arquivo)
                shutil.move(caminho_origem, caminho_destino)
            continue
        elif arquivo.endswith(tuple_videos):
            caminho_destino = os.path.join(VIDEOS_FOLDER, arquivo)
            shutil.move(caminho_origem, caminho_destino)
        elif arquivo.endswith(tuple_audios):
            caminho_destino = os.path.join(AUDIO_FOLDER, arquivo)
            shutil.move(caminho_origem, caminho_destino)
        else:
            print(f"Arquivo não classificado: {arquivo}")

    end_time = time.time()
    tempo_total = end_time - start_time
    print(f"Tempo total de execução: {tempo_total:.2f} segundos")




# Bloco de resumo ao final do script
print("\nResumo da organização:")
print(f"Total de PDFs: {len([f for f in os.listdir(PDFS_FOLDER) if f.endswith(tuple_pdfs)])}")
print(f"Total de imagens: {len([f for f in os.listdir(IMAGE_FOLDER) if f.endswith(tuple_images)])}")
print(f"Total de vídeos: {len([f for f in os.listdir(VIDEOS_FOLDER) if f.endswith(tuple_videos)])}")
print(f"Total de áudios: {len([f for f in os.listdir(AUDIO_FOLDER) if f.endswith(tuple_audios)])}")
print("✅ Organização e renomeação concluídas!")
