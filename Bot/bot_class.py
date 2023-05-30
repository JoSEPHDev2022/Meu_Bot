import datetime
import os
import platform
import constants

class Menu:
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

    # MENU PRINCIPAL: Métodos de apresentação e tratativa
    def _display_main_menu(self):
        self._display_header('MENU PRINCIPAL')
        print('1 - Sobre Mim')
        print('2 - Meus Projetos')
        print('3 - Habilidades Tech e Soft')
        print('4 - Contatos')
        print('5 - Sair')

    def _handle_main_menu_selection(self):
        while True:
            selection = input('Escolha uma área para saber mais: ')
            if selection == constants.MENU_ABOUT_ME:
                self._current_menu = 'about_me_menu'
                break
            elif selection == constants.MENU_PROJECTS:
                self._current_menu = 'projects_menu'
                break
            elif selection == constants.MENU_SKILLS:
                self._current_menu = 'skills_menu'
                break
            elif selection == constants.MENU_CONTACTS:
                self._current_menu = 'contacts_menu'
                break
            elif selection == constants.MENU_EXIT:
                self._current_menu = 'exit'
                break
            else:
                print(constants.INVALID_ENTRY_MESSAGE)

    # MENU SOBRE MIM: Métodos de apresentação e tratativa
    def _display_about_me_menu(self):
        self._display_header('SOBRE MIM')
        print('1 - Profissional')
        print('2 - Pessoal')
        print('3 - Voltar ao Menu Principal')
        print('4 - Sair')

    def _handle_about_me_menu_selection(self):
        while True:
            selection = input('Escolha uma área para saber mais: ')
            if selection == constants.ABOUT_PROFESSIONAL:
                self._current_menu = 'professional_menu'
                break
            elif selection == constants.ABOUT_PERSONAL:
                self._current_menu = 'personal_menu'
                break
            elif selection == constants.ABOUT_RETURN_MAIN_MENU:
                self._current_menu = 'main_menu'
                break
            elif selection == constants.ABOUT_EXIT:
                self._current_menu = 'exit'
                break
            else:
                print(constants.INVALID_ENTRY_MESSAGE)

    # SUB-MENUS SOBRE MIM:
    # PROFISSIONAL:
    def _display_professional_menu(self):
        self._display_header('PROFISSIONAL')
        print('1 - Resumo Profissional')
        print('2 - Objetivo')
        print('3 - Voltar ao Menu Anterior')
        print('4 - Sair')

    def _handle_professional_menu_selection(self):
        while True:
            selection = input('Escolha uma área para saber mais: ')
            if selection == constants.PROF_RESUME:
                ... # Resposta pendente
                break
            elif selection == constants.PROF_OBJECTIVE:
                ... # Resposta pendente
                break
            elif selection == constants.PROF_RETURN_ABOUT_MENU:
                self._current_menu = 'about_me_menu'
                break
            elif selection == constants.PROF_EXIT:
                self._current_menu = 'exit'
                break
            else:
                print(constants.INVALID_ENTRY_MESSAGE) 

    # PESSOAL:
    def _display_personal_menu(self):
        self._display_header('PESSOAL')
        print('1 - Quem sou Eu')
        print('2 - Meus Hobbys')
        print('3 - Voltar ao Menu Anterior')
        print('4 - Sair')

    def _handle_personal_menu_selection(self):
        while True:
            selection = input('Escolha uma área para saber mais: ')
            if selection == constants.PERSONAL_ME:
                ... # Resposta pendente
                break
            elif selection == constants.PERSONAL_HOBBYS:
                ... # Resposta pendente
                break
            elif selection == constants.PERSONAL_RETURN_ABOUT_MENU:
                self._current_menu = 'about_me_menu'
                break
            elif selection == constants.PERSONAL_EXIT:
                self._current_menu = 'exit'
                break
            else:
                print(constants.INVALID_ENTRY_MESSAGE)

            
