import datetime
import os
import platform

class Menu:
    # Definindo constantes de menus para facilitar manutenção:
    OPTION_ABOUT_ME = '1'
    OPTION_PROJECTS = '2'
    OPTION_SKILLS = '3'
    OPTION_CONTACTS = '4'
    OPTION_EXIT = '5'

    # Método construtor:
    def __init__(self):
        self._user_name = ''
        self._current_menu = 'main_menu'

    # Método personalizado de limpar terminal baseado em OS:
    def _clear_screen(self):
        user_system = platform.system()
        if user_system == 'Windows':
            os.system('cls')
        else:
            os.system('clear')

    # Método para apresentação de um Header personalizado:
    def _display_header(self, text):
        self._clear_screen()
        print(f' {text} '.center(75, '-'))

    # Método para exibir Saudação baseado na hora do dia:
    def _greet_user(self):
        current_hour = datetime.datetime.now().hour
        if current_hour < 12:
            print(f'Bom dia, {self._user_name.capitalize()}!')
        elif current_hour < 18:
            print(f'Boa tarde, {self._user_name.capitalize()}!')
        else:
            print(f'Boa noite, {self._user_name.capitalize()}!')

    # Método para coleta de user name:
    def _get_user_name(self):
        self._user_name = input('Por favor, insira seu nome: ')

        
    
