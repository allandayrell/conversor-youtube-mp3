import sys

def exibir_ajuda():
    """Exibe as instruções de uso do script."""
    print("Uso: python main.py <URL_DO_YOUTUBE> \"<CAMINHO_DA_PASTA>\"")
    print("Exemplo: python main.py \"https://youtu.be/some_video\" \"Minhas Musicas/Rock\"")

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
    
    print(f"URL recebida: {url_do_video}")
    print(f"Pasta de destino: {caminho_da_pasta}")



if __name__ == "__main__":
    main()