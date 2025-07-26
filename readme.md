# Organizador de Mídia com IA

## Objetivo
Este projeto automatiza a organização de arquivos de mídia (imagens, vídeos, áudios e PDFs) de uma pasta de origem para subpastas categorizadas. O grande diferencial é o uso da API do Google Gemini para analisar o conteúdo de arquivos PDF e renomeá-los de forma inteligente e padronizada.

## Funcionalidades Principais
- **Organização por Tipo**: Move arquivos de imagem, vídeo e áudio para pastas de destino específicas.
- **Renomeação Inteligente de PDFs**:
  - Extrai o texto das primeiras páginas de cada arquivo PDF.
  - Envia o texto para a API do Google Gemini.
  - Renomeia o arquivo com base no conteúdo, seguindo padrões pré-definidos (ex: `materia_unidade_x.pdf` para material de estudo ou um nome descritivo para outros documentos).
- **Configuração Flexível**: Utiliza um arquivo `.env` para gerenciar facilmente a chave da API e os caminhos das pastas.

## Como Usar

1.  **Clone o Repositório:**
    ```bash
    git clone https://github.com/Lazarokaua/Organiza-pasta-obsidian.git
    cd Organiza-pasta-obsidian
    ```

2.  **Configure o Ambiente:**
    - Crie um arquivo chamado `.env` na raiz do projeto. Você pode copiar o `.env.example` para começar:
      ```bash
      cp .env.example .env
      ```
    - Abra o arquivo `.env` e preencha as variáveis:
      - `GEMINI_API_KEY`: Sua chave de API do Google Gemini.
      - `MIDIA_FOLDER`: O caminho absoluto para a pasta que você deseja organizar.
      - `AUDIO_FOLDER`, `IMAGE_FOLDER`, `PDFS_FOLDER`, `VIDEOS_FOLDER`: Os caminhos absolutos para as pastas de destino.

3.  **Instale as Dependências:**
    É recomendado criar um ambiente virtual.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute o Script:**
    ```bash
    python move_files.py
    ```

## Estrutura de Pastas
O script moverá os arquivos da pasta definida em `MIDIA_FOLDER` para as pastas de destino configuradas no arquivo `.env`. Certifique-se de que as pastas de destino existam antes de executar o script.

```env
MIDIA_FOLDER="/caminho/absoluto/para/sua/pasta_de_midia"
AUDIO_FOLDER="/caminho/absoluto/para/sua/pasta_de_audio"
IMAGE_FOLDER="/caminho/absoluto/para/sua/pasta_de_imagens"
PDFS_FOLDER="/caminho/absoluto/para/sua/pasta_de_pdfs"
VIDEOS_FOLDER="/caminho/absoluto/para/sua/pasta_de_videos"
GEMINI_API_KEY="SUA_CHAVE_DE_API_VEM_AQUI"
```

## Tecnologias Utilizadas
- Python
- Google Gemini API
- PyMuPDF (fitz)
- python-dotenv

## Contribuição
Sinta-se à vontade para contribuir com melhorias ou novas funcionalidades. Basta fazer um fork do projeto, criar uma nova branch e enviar um pull request.

## Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---

## Referências
- Awari - Python: Movendo Arquivos com Facilidade
- Google AI for Developers
