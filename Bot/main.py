from bot_class import Initializer

def main():
    """
    Função principal do programa.

    Cria uma instância do inicializador do bot e executa o bot.

    """
    bot = Initializer()
    bot.run()

# Executa a função main apenas se o arquivo for executado diretamente,
# não se for importado como um módulo.
if __name__ == '__main__':
    main()
