import sys
from pathlib import Path
import yt_dlp

def exibir_ajuda():
    """Exibe as instruções de uso do script."""
    print("Uso: python main.py <URL_DO_YOUTUBE> \"<CAMINHO_DA_PASTA>\"")
    print("Exemplo: python main.py \"https://youtu.be/some_video\" \"Minhas Musicas/Rock\"")

def baixar_audio_como_mp3(url_video: str, pasta_destino: Path):
    """
    Baixa o áudio de uma URL do YouTube e salva como MP3 na pasta de destino.
    """
    # Configurações do yt-dlp
    # '%(title)s.%(ext)s' -> Usa o título do vídeo como nome do arquivo
    # O str() é importante para converter o objeto Path para uma string que o yt-dlp entende
    opcoes_ydl = {
        'format': 'bestaudio/best',
        'outtmpl': str(pasta_destino / '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192', 
        }],
        'quiet': True, 
    }

    print(f"Iniciando download de: {url_video}")
    
    try:
        with yt_dlp.YoutubeDL(opcoes_ydl) as ydl:
            ydl.download([url_video])
        print("✅ Download concluído com sucesso!")
        print(f"Arquivo salvo em: '{pasta_destino}'")
    except yt_dlp.utils.DownloadError as e:
        print(f"❌ Erro ao baixar: Verifique se a URL está correta e o vídeo está disponível.")
    except Exception as e:
        print(f"❌ Ocorreu um erro inesperado: {e}")


def main():
    """Função principal que orquestra o script."""
    argumentos = sys.argv
    
    # O tamanho esperado da lista de argumentos é 3:
    # [0] = nome do script, [1] = URL, [2] = Pasta
    if len(argumentos) != 3:
        exibir_ajuda()
        sys.exit(1)

    url_do_video = argumentos[1]
    caminho_da_pasta = argumentos[2]
    
    # Prepara a pasta de destino
    pasta_destino = Path(caminho_da_pasta)
    pasta_destino.mkdir(parents=True, exist_ok=True)
    
    # Executa a função principal de download
    baixar_audio_como_mp3(url_do_video, pasta_destino)


if __name__ == "__main__":
    main()