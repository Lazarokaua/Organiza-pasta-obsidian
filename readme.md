# Organiza Pasta Midias


## Referências
[Awari]('https://awari.com.br/python-movendo-arquivos-com-facilidade/')

## Objetivo
Este projeto tem como objetivo principal automatizar a organização de arquivos de mídia em uma pasta específica, movendo-os para subpastas categorizadas por tipo (imagens, vídeos, documentos, etc.).

## Como Usar
1.  **Clone o Repositório:**
    ```bash
    git clone <link-do-seu-repositorio>
    ```
2.  **Instale as Dependências:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Configure a Pasta de Origem:**
    Abra o arquivo `main.py` e altere a variável `PASTA_ORIGEM` para o caminho da pasta que você deseja organizar.
    ```python
    PASTA_ORIGEM = "C:/Users/SeuUsuario/SuaPastaDeMidias" # Altere este caminho
    ```
4.  **Execute o Script:**
    ```bash
    python main.py
    ```

## Estrutura de Pastas Criadas
O script criará as seguintes subpastas dentro da `PASTA_ORIGEM` (se ainda não existirem):
- `Imagens`
- `Videos`
- `Documentos`
- `Outros`

## Tecnologias Utilizadas
- Python

## Contribuição
Sinta-se à vontade para contribuir com melhorias ou novas funcionalidades. Basta fazer um fork do projeto, criar uma nova branch e enviar um pull request.

## Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
