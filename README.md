# conversor-youtube-mp3
Ferramenta de linha de comando para baixar áudio de vídeos do YouTube como MP3 como forma de estudo.

## Funcionalidades

-   Converte qualquer URL de vídeo do YouTube para um arquivo de áudio MP3.
-   Usa o título do vídeo como o nome do arquivo MP3.
-   Cria a pasta de destino automaticamente se ela não existir.
-   Interface de linha de comando (CLI) direta e fácil de usar.

## Pré-requisitos (Configuração do Ambiente)

Antes de executar o script, certifique-se de que você tem as seguintes ferramentas instaladas no seu sistema. Estas instruções são para ambientes baseados em Debian/Ubuntu (como o WSL).

1.  **Python 3 e PIP:**
    ```bash
    sudo apt update && sudo apt install python3 python3-pip -y
    ```

2.  **FFmpeg:**
    ```bash
    sudo apt install ffmpeg -y
    ```

## Instalação (Dependências do Projeto)

Após clonar o repositório, navegue até a pasta do projeto e instale as bibliotecas Python necessárias:

```bash
pip3 install yt-dlp