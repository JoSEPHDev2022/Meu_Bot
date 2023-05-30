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

    # MENU PROJETOS: Métodos de apresentação e tratativa   
    def _display_projects_menu(self):
        self._display_header('PROJETOS')
        print('1 - Projetos em Destaque')
        print('2 - Porfólio Completo')
        print('3 - Voltar ao Menu Principal')
        print('4 - Sair')

    def _handle_projects_menu_selection(self):
        while True:
            selection = input('Escolha uma área para saber mais: ')
            if selection == constants.PROJECTS_HIGHLIGHTS:
                ... # Resposta pendente
                break
            if selection == constants.PROJECTS_PORTFOLIO:
                ... # Resposta pendente
                break
            if selection == constants.PROJECTS_RETURN_MAIN_MENU:
                self._current_menu = 'main_menu'
                break
            elif selection == constants.PROJECTS_EXIT:
                self._current_menu = 'exit'
                break
            else:
                print(constants.INVALID_ENTRY_MESSAGE)

    # MENU HABILIDADES: Métodos de apresentação e tratativa   
    def _display_skills_menu(self):
        self._display_header("HABILIDADES TECH E SOFT")
        print("1 - Tech")
        print("2 - Soft")
        print("3 - Voltar ao menu principal")
        print("4 - Sair")

    def _handle_skills_menu_selection(self):
        while True:
            selection = input('Escolha uma área para saber mais: ')
            if selection == constants.SKILLS_TECH:
                ... # Resposta pendente
                break
            if selection == constants.SKILLS_SOFT:
                ... # Resposta pendente
                break
            if selection == constants.SKILLS_RETURN_MAIN_MENU:
                self._current_menu = 'main_menu'
                break
            elif selection == constants.SKILLS_EXIT:
                self._current_menu = 'exit'
                break
            else:
                print(constants.INVALID_ENTRY_MESSAGE)

    # MENU CONTATOS: Métodos de apresentação e tratativa   
    def _display_contacts_menu(self):
        self._display_header("CONTATOS")
        print("1 - LinkedIn")
        print("2 - E-mail")
        print("3 - Voltar ao menu principal")
        print("4 - Sair")

    def _handle_contacts_menu_selection(self):
        while True:
            selection = input('Escolha uma área para saber mais: ')
            if selection == constants.CONT_LINKEDIN:
                ... # Resposta pendente
                break
            if selection == constants.CONT_EMAIL:
                ... # Resposta pendente
                break
            if selection == constants.CONT_RETURN_MAIN_MENU:
                self._current_menu = 'main_menu'
                break
            elif selection == constants.CONT_EXIT:
                self._current_menu = 'exit'
                break
            else:
                print(constants.INVALID_ENTRY_MESSAGE)

# Classe Inicializadora do Bot. Essa classe herda os atributos da classe Menu.
class Initializer(Menu):
    # Construtor que liga as duas classes e seus atributos:
    def __init__(self):
        super().__init__()

    # Método inicializador do programa:
    def run(self):
        self._get_user_name()
        self._greet_user()

        while self._current_menu != 'exit':
            # Inicializar Menu Principal:
            if self._current_menu == "main_menu":
                self._display_main_menu()
                self._handle_main_menu_selection()
            # Inicializar Menu Sobre Mim:
            elif self._current_menu == "about_me_menu":
                self._display_about_me_menu()
                self._handle_about_me_menu_selection()
            # Inicializar Sub-Menu Profissional:
            elif self._current_menu == "professional_menu":
                self._display_professional_menu()
                self._handle_professional_menu_selection()
            # Inicializar Sub-Menu Pessoal:
            elif self._current_menu == "personal_menu":
                self._display_personal_menu()
                self._handle_personal_menu_selection()
            # Inicializar Menu Projetos:
            elif self._current_menu == "projects_menu":
                self._display_projects_menu()
                self._handle_projects_menu_selection()
            # Inicializar Menu Habilidades:
            elif self._current_menu == "skills_menu":
                self._display_skills_menu()
                self._handle_skills_menu_selection()
            # Inicializar Menu Contatos:
            elif self._current_menu == "contacts_menu":
                self._display_contacts_menu()
                self._handle_contacts_menu_selection()
                