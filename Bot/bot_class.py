'''
Classes: 
- Cada menu (e todas as suas sub-opções) terão classes específicas.
- Uma classe central que será herdada para os menus será criada para coletar
informações importantes
- Uma classe final Inicializadora que herdará os menus para iniciar o bot
'''
import datetime
import os
import platform
import constants
import requests
from time import sleep

# Classe Coletora de informações:
class GeneralMethods:
    """
    Classe que contém métodos gerais utilizados no programa.

    Atributos:
    ----------
    - _user_name (str): O nome do usuário.
    ---
    - _current_menu (str): O menu atual do programa.
    ---
    - _current_hour (int): A hora atual do sistema.
    ---
    - _current_time (str): O horário atual no formato HH:MM.
    ---
    - _current_date (str): A data atual no formato DD/MM/AAAA.

    Métodos:
    ---------
    - __init__: Inicializa os atributos da classe.
    ---
    - _clear_screen: Método personalizado para limpar o terminal com base no sistema operacional.
    ---
    - _display_header: Exibe um cabeçalho personalizado na tela.
        - Args: header_text (str): O texto do cabeçalho.
        ---
    - _get_user_name: Solicita e armazena o nome do usuário.
    ---
    - _greet_user: Exibe uma saudação ao usuário com base na hora atual.
    ---
    - _display_login_information: Exibe as informações de login do usuário na tela.
    """
    # Construtor:
    def __init__(self):
        self._user_name = ''
        self._current_menu = 'main_menu'
        self._current_hour = datetime.datetime.now().hour
        self._current_time = datetime.datetime.now().strftime('%H:%M')
        self._current_date = datetime.datetime.now().strftime('%d/%m/%Y')

    # Limpar a tela baseado no OS:
    def _clear_screen(self):
        user_system = platform.system()
        if user_system == 'Windows':
            os.system('cls')
        else:
            os.system('clear')

    # Exibir cabeçalho personalizado:
    def _display_header(self, header_text):
        self._clear_screen()
        print(f' {constants.GREEN}{constants.BOLD}{header_text}{constants.RESET} '.center(75,'-'))

    # Coletar nome do usuário:
    def _get_user_name(self):
        self._user_name = input(f'{constants.GREEN}{constants.BOLD}Por favor, insira seu nome:{constants.RESET} ').title()

    # Exibir saudações baseado em hora do dia:
    def _greet_user(self):
        if self._current_hour < 12:
            print(f'Bom Dia, {constants.BOLD}{self._user_name}{constants.RESET}!')
        elif self._current_hour < 18:
            print(f'Boa Tarde, {constants.BOLD}{self._user_name}{constants.RESET}!')
        else:
            print(f'Boa Noite, {constants.BOLD}{self._user_name}{constants.RESET}!')

    # Exibir informações de login do usuário:
    def _display_login_information(self):
        print(f'\nData do Acesso: {constants.BOLD}{self._current_date}{constants.RESET}')
        print(f'Hora do Acesso: {constants.BOLD}{self._current_time}{constants.RESET}\n')

#===================================================================================================#
# Classe Menu Principal:
class MainMenu(GeneralMethods):
    """
    Classe que representa o menu principal do programa. Fornece métodos para exibir o Menu Principal e
    lidar com a seleção do usuário.

    Atributos:
    ---------
        Nenhum atributo adicional além dos herdados da classe GeneralMethods.

    Métodos:
    ---------
    - _display_main_menu(): Apresenta o menu principal na tela.
    ---
    - _handle_main_menu_selection(): Lida com a entrada do usuário no menu principal.
    """

    # Construtor
    def __init__(self):
        super().__init__()

    # Exibe o menu principal:
    def _display_main_menu(self):
        self._display_header('MENU PRINCIPAL')
        self._greet_user()
        self._display_login_information()
        print('[1] - Sobre Mim')
        print('[2] - Meus Projetos')
        print('[3] - Habilidades Tech e Soft')
        print('[4] - Contatos')
        print('[5] - Sair')

    # Lidar com a entrada do usuário:
    def _handle_main_menu_selection(self):
        while True:
            user_choice = input(f'\n{constants.BOLD}Escolha uma área para saber mais:{constants.RESET} ')
            if user_choice == constants.MENU_ABOUT_ME:
                self._current_menu = 'about_me_menu'
                break
            elif user_choice == constants.MENU_PROJECTS:
                self._current_menu = 'projects_menu'
                break
            elif user_choice == constants.MENU_SKILLS:
                self._current_menu = 'skills_menu'
                break
            elif user_choice == constants.MENU_CONTACTS:
                self._current_menu = 'contacts_menu'
                break
            elif user_choice == constants.MENU_EXIT:
                self._current_menu = 'exit'
                break
            else:
                print(constants.INVALID_ENTRY_MESSAGE)

#===================================================================================================#           
# Classe Menu Sobre Mim:
class AboutMeMenu(GeneralMethods):
    """
    Classe que representa o menu "Sobre Mim" do programa. Fornece métodos para exibir o menu "Sobre Mim",
    lidar com a seleção do usuário e exibir submenus relacionados.

    Atributos:
    ---------
        Nenhum atributo adicional além dos herdados da classe GeneralMethods.

    Métodos:
    ---------
    - _display_about_me_menu(): Apresenta o menu "Sobre Mim" na tela.
    ---
    - _handle_about_me_menu_selection(): Lida com a entrada do usuário no menu "Sobre Mim".
    ---
    - _display_professional_menu(): Apresenta o submenu "Sobre Mim: Profissional" na tela.
    ---
    - _handle_professional_menu_selection(): Lida com a entrada do usuário no submenu "Sobre Mim: Profissional".
    ---
    - _display_professional_resume_menu(): Apresenta o subsubmenu "Profissional: Resumo Profissional" na tela.
    ---
    - _display_professional_objective_menu(): Apresenta o subsubmenu "Profissional: Objetivo Profissional" na tela.
    ---
    - _handle_professional_final_menus(): Lida com a entrada do usuário nos menus finais do submenu "Sobre Mim: Profissional".
    ---
    - _display_personal_menu(): Apresenta o submenu "Sobre Mim: Pessoal" na tela.
    ---
    - _handle_personal_menu_selection(): Lida com a entrada do usuário no submenu "Sobre Mim: Pessoal".
    ---
    - _display_personal_me_menu(): Apresenta o subsubmenu "Sobre Mim: Quem Sou Eu" na tela.
    ---
    - _display_personal_hobbys_menu(): Apresenta o subsubmenu "Sobre Mim: Hobbys" na tela.
    ---
    - _handle_personal_final_menus(): Lida com a entrada do usuário nos menus finais do submenu "Sobre Mim: Pessoal".
    """

    # Construtor:
    def __init__(self):
        super().__init__()

    # Exbir Menu Sobre Mim:
    def _display_about_me_menu(self):
        self._display_header('SOBRE MIM')
        self._greet_user()
        self._display_login_information()
        print('[1] - Profissional')
        print('[2] - Pessoal')
        print('[3] - Voltar ao Menu Principal')
        print('[4] - Sair')

    # Lidar com entrada do usuário:
    def _handle_about_me_menu_selection(self):
        while True:
            user_choice = input(f'\n{constants.BOLD}Escolha uma área para saber mais:{constants.RESET} ')
            if user_choice == constants.ABOUT_PROFESSIONAL:
                self._current_menu = 'professional_menu'
                break
            elif user_choice == constants.ABOUT_PERSONAL:
                self._current_menu = 'personal_menu'
                break
            elif user_choice == constants.GENERAL_RETURN:
                self._current_menu = 'main_menu'
                break
            elif user_choice == constants.GENERAL_EXIT:
                self._current_menu = 'exit'
                break
            else:
                print(constants.INVALID_ENTRY_MESSAGE)

    # Exibir Sub-Menu Profissional:
    def _display_professional_menu(self):
        self._display_header('SOBRE MIM: PROFISSIONAL')
        self._greet_user()
        self._display_login_information()
        print('[1] - Resumo Profissional')
        print('[2] - Objetivo')
        print('[3] - Voltar ao Menu Anterior')
        print('[4] - Sair')

    # Lidar com entrada do usuário:
    def _handle_professional_menu_selection(self):
        while True:
            user_choice = input(f'\n{constants.BOLD}Escolha uma área para saber mais:{constants.RESET} ')
            if user_choice == constants.PROF_RESUME:
                self._current_menu = 'prof_resume_menu'
                break
            elif user_choice == constants.PROF_OBJECTIVE:
                self._current_menu = 'prof_objective_menu'
                break
            elif user_choice == constants.GENERAL_RETURN:
                self._current_menu = 'about_me_menu'
                break
            elif user_choice == constants.GENERAL_EXIT:
                self._current_menu = 'exit'
                break
            else:
                print(constants.INVALID_ENTRY_MESSAGE)  

    # Exibir Sub-Menu Final Resumo Profissional:
    def _display_professional_resume_menu(self):
        self._display_header('PROFISSIONAL: RESUMO PROFISSIONAL')
        self._greet_user()
        self._display_login_information()
        print('TEMP TEMP TEMP')
        print('[1] - Voltar ao Menu Anterior')
        print('[2] - Sair')

    # Exibir Sub-Menu Final Objetivo Profissional:
    def _display_professional_objective_menu(self):
        self._display_header('PROFISSIONAL: RESUMO PROFISSIONAL')
        self._greet_user()
        self._display_login_information()
        print('TEMP TEMP TEMP')
        print('[1] - Voltar ao Menu Anterior')
        print('[2] - Sair')

    # Lidar com entrada do usuário nos menus finais:
    def _handle_professional_final_menus(self):
        while True:
            user_choice = input(f'\n{constants.BOLD}Escolha para voltar ou sair:{constants.RESET} ')
            if user_choice == constants.FINAL_RETURN:
                self._current_menu = 'professional_menu'
                break
            elif user_choice == constants.FINAL_EXIT:
                self._current_menu = 'exit'
                break
            else:
                print(constants.INVALID_ENTRY_MESSAGE)

    # Exibir Sub-Menu Pessoal:
    def _display_personal_menu(self):
        self._display_header('SOBRE MIM: PESSOAL')
        self._greet_user()
        self._display_login_information()
        print('[1] - Quem sou Eu')
        print('[2] - Meus Hobbys')
        print('[3] - Voltar ao Menu Anterior')
        print('[4] - Sair')

    # Lidar com entrada do usuário:
    def _handle_personal_menu_selection(self):
        while True:
            user_choice = input(f'\n{constants.BOLD}Escolha uma área para saber mais:{constants.RESET} ')
            if user_choice == constants.PERSONAL_ME:
                self._current_menu = 'personal_me_menu'
                break
            elif user_choice == constants.PERSONAL_HOBBYS:
                self._current_menu = 'personal_hobbys_menu'
                break
            elif user_choice == constants.GENERAL_RETURN:
                self._current_menu = 'about_me_menu'
                break
            elif user_choice == constants.GENERAL_EXIT:
                self._current_menu = 'exit'
                break
            else:
                print(constants.INVALID_ENTRY_MESSAGE)

    # Exibir Sub-Menu Final Quem Sou Eu:
    def _display_personal_me_menu(self):
        self._display_header('SOBRE MIM: QUEM SOU EU')
        self._greet_user()
        self._display_login_information()
        print('TEMP TEMP TEMP')
        print('[1] - Voltar ao Menu Anterior')
        print('[2] - Sair')

    # Exibir Sub-Menu-Final Hobbys:
    def _display_personal_hobbys_menu(self):
        self._display_header('SOBRE MIM: HOBBYS')
        self._greet_user()
        self._display_login_information()
        print('TEMP TEMP TEMP')
        print('[1] - Voltar ao Menu Anterior')
        print('[2] - Sair')

    # Lidar com entrada do usuário nos menus finais:
    def _handle_personal_final_menus(self):
        while True:
            user_choice = input(f'\n{constants.BOLD}Escolha para voltar ou sair:{constants.RESET} ')
            if user_choice == constants.FINAL_RETURN:
                self._current_menu = 'personal_menu'
                break
            elif user_choice == constants.FINAL_EXIT:
                self._current_menu = 'exit'
                break
            else:
                print(constants.INVALID_ENTRY_MESSAGE)

#===================================================================================================# 
# Classe Menu Projetos:
class ProjectsMenu(GeneralMethods):
    """
    Classe que representa o menu de projetos.

    Esta classe herda da classe GeneralMethods e fornece métodos para exibir o menu de projetos,
    lidar com a seleção do usuário e exibir submenus relacionados aos projetos.

    Atributos:
    --------
        Nenhum atributo adicional além dos herdados da classe GeneralMethods.

    Métodos:
    ------
    - _display_projects_menu(): Apresenta o menu de projetos na tela, mostrando as opções disponíveis.
    ---
    - _handle_projects_menu_selection():Lida com a entrada do usuário no menu de projetos, processando a escolha feita 
    e atualizando o menu atual ou saindo do programa.
    ---
    - _display_project_highlights_menu(): Apresenta o submenu de "Projetos em Destaque" na tela.
    ---
    - _display_project_description(): Coleta via API do GitHub das descrições e nomes dos projetos em destaque.
        - Args: project_name (str): Nome do Projeto.
    ---
    - _display_project_porfolio_menu(): Apresenta o submenu de "Portfólio Completo" na tela.
    ---
    - _handle_projects_final_menus(): Lida com os menus finais relacionados aos projetos, permitindo que o usuário retorne 
    ao menu de projetos ou saia do programa.
    """

    # Construtor:
    def __init__(self):
        super().__init__()

    # Método de apresentação do menu:
    def _display_projects_menu(self):
        self._display_header('PROJETOS')
        self._greet_user()
        self._display_login_information()
        print('[1] - Projetos em Destaque')
        print('[2] - Porfólio Completo')
        print('[3] - Voltar ao Menu Principal')
        print('[4] - Sair')

    # Método para lidar com entrada do usuário:
    def _handle_projects_menu_selection(self):
        while True:
            user_choice = input(f'\n{constants.BOLD}Escolha uma área para saber mais:{constants.RESET} ')
            if user_choice == constants.PROJECTS_HIGHLIGHTS:
                self._current_menu = 'projects_highlights_menu'
                break
            if user_choice == constants.PROJECTS_PORTFOLIO:
                self._current_menu = 'projects_portfolio_menu'
                break
            if user_choice == constants.GENERAL_RETURN:
                self._current_menu = 'main_menu'
                break
            elif user_choice == constants.GENERAL_EXIT:
                self._current_menu = 'exit'
                break
            else:
                print(constants.INVALID_ENTRY_MESSAGE)

    # SubSub-Menu Projetos em Destaque:
    def _display_project_highlights_menu(self):
        self._display_header('PROJETOS: PROJETOS EM DESTAQUE')
        self._greet_user()
        self._display_login_information()

        projects = ['Dash_Financeiro_Power_BI', 'EDA_Pirated_Movies', 'Meu_Bot']

        for project_name in projects:
            self._display_project_description(project_name)

        print('[1] - Voltar ao Menu Anterior')
        print('[2] - Sair') 

    # Coleta de informações dos projetos via API:
    def _display_project_description(self, project_name):
        # Constrói a URL do projeto no GitHub
        project_url = f"https://api.github.com/repos/JoSEPHDev2022/{project_name}"

        # Realiza a requisição para obter as informações do projeto
        try:
            response = requests.get(project_url)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            # Exibe uma mensagem de erro se a requisição falhar
            print(f"Erro ao obter informações do projeto {project_name}: {e}")
            return

        # Extrai os dados do projeto da resposta da requisição
        project_data = response.json()
        description = project_data.get("description")
        repository_url = project_data.get("html_url")

        # Imprime o nome do projeto em negrito
        print(f'---{constants.BOLD}{project_name}{constants.RESET}---')

        # Imprime a descrição do projeto, se estiver disponível
        if description:
            print(f"{description}\n")
        else:
            print("Descrição não disponível\n")

        # Imprime o link do repositório do projeto, se estiver disponível
        if repository_url:
            print(f"Link do repositório: {repository_url}\n")
        else:
            print("Link do repositório não disponível\n")

    # SubSub-Menu Portfólio Completo:
    def _display_project_porfolio_menu(self):
        self._display_header('PROJETOS: PORTFÓLIO COMPLETO')
        self._greet_user()
        self._display_login_information()
        print('TEMP TEMP TEMP')
        print('[1] - Voltar ao Menu Anterior')
        print('[2] - Sair')    

    # Método único para lidar com menus finais dos projetos:
    def _handle_projects_final_menus(self):
        while True:
            user_choice = input(f'\n{constants.BOLD}Escolha para voltar ou sair:{constants.RESET} ')
            if user_choice == constants.FINAL_RETURN:
                self._current_menu = 'projects_menu'
                break
            elif user_choice == constants.FINAL_EXIT:
                self._current_menu = 'exit'
                break
            else:
                print(constants.INVALID_ENTRY_MESSAGE)
#===================================================================================================# 
# Classe Menu Habilidades:
class SkillsMenu(GeneralMethods):
    """
    Classe que representa o menu de habilidades.

    Esta classe herda da classe GeneralMethods e fornece métodos para exibir o menu de habilidades,
    lidar com a seleção do usuário e exibir submenus relacionados às habilidades.

    Atributos:
    ----------
        Nenhum atributo adicional além dos herdados da classe GeneralMethods.

    Métodos:
    ---------
    - _display_skills_menu(): Apresenta o menu de habilidades na tela, mostrando as opções disponíveis.
    ---
    - _handle_skills_menu_selection(): Lida com a entrada do usuário no menu de habilidades, processando a escolha feita 
    e atualizando o menu atual ou saindo do programa.
    ---
    - _display_tech_skills_menu(): Apresenta o submenu de "Tech Skills" na tela.
    ---
    - _display_soft_skills_menu(): Apresenta o submenu de "Soft Skills" na tela.
    ---
    - _handle_skills_final_menus(): Lida com os menus finais relacionados às habilidades, permitindo que o usuário retorne 
    ao menu de habilidades ou saia do programa.
    """
    
    # Construtor:
    def __init__(self):
        super().__init__()

    # Método de apresentação do menu:
    def _display_skills_menu(self):
        self._display_header("HABILIDADES TECH E SOFT")
        self._greet_user()
        self._display_login_information()
        print("[1] - Tech")
        print("[2] - Soft")
        print("[3] - Voltar ao menu principal")
        print("[4] - Sair")

    # Método para lidar com entrada do usuário:
    def _handle_skills_menu_selection(self):
        while True:
            user_choice = input(f'\n{constants.BOLD}Escolha uma área para saber mais:{constants.RESET} ')
            if user_choice == constants.SKILLS_TECH:
                self._current_menu = 'tech_skills_menu'
                break
            if user_choice == constants.SKILLS_SOFT:
                self._current_menu = 'soft_skills_menu'
                break
            if user_choice == constants.GENERAL_RETURN:
                self._current_menu = 'main_menu'
                break
            elif user_choice == constants.GENERAL_EXIT:
                self._current_menu = 'exit'
                break
            else:
                print(constants.INVALID_ENTRY_MESSAGE)

    # SubSub-Menu Tech Skills:
    def _display_tech_skills_menu(self):
        self._display_header('HABILIDADES: TECH')
        self._greet_user()
        self._display_login_information()
        print('TEMP TEMP TEMP')
        print('[1] - Voltar ao Menu Anterior')
        print('[2] - Sair') 

    # SubSub-Menu Soft Skills:
    def _display_soft_skills_menu(self):
        self._display_header('HABILIDADES: SOFT')
        self._greet_user()
        self._display_login_information()
        print('TEMP TEMP TEMP')
        print('[1] - Voltar ao Menu Anterior')
        print('[2] - Sair') 
        
    # Método único para lidar com menus finais das habilidades:
    def _handle_skills_final_menus(self):
        while True:
            user_choice = input(f'\n{constants.BOLD}Escolha para voltar ou sair:{constants.RESET} ')
            if user_choice == constants.FINAL_RETURN:
                self._current_menu = 'skills_menu'
                break
            elif user_choice == constants.FINAL_EXIT:
                self._current_menu = 'exit'
                break
            else:
                print(constants.INVALID_ENTRY_MESSAGE)

#===================================================================================================# 
# Classe Menu Contatos:
class ContactsMenu(GeneralMethods):
    """
    Classe que representa o menu de contatos.

    Esta classe herda da classe GeneralMethods e fornece métodos para exibir o menu de contatos,
    lidar com a seleção do usuário e exibir submenus relacionados aos contatos.

    Atributos:
    ----------
        Nenhum atributo adicional além dos herdados da classe GeneralMethods.

    Métodos:
    ----------
    - _display_contacts_menu(): Apresenta o menu de contatos na tela, mostrando as opções disponíveis.
    ---
    - _handle_contacts_menu_selection(): Lida com a entrada do usuário no menu de contatos, processando a escolha feita 
    e atualizando o menu atual ou saindo do programa.
    ---
    - _display_linkedin_menu(): Apresenta o submenu do LinkedIn na tela.
    ---
    - _display_email_menu(): Apresenta o submenu de e-mail na tela.
    ---
    - _handle_contacts_final_menus(): Lida com os menus finais relacionados aos contatos, permitindo que o usuário retorne 
    ao menu de contatos ou saia do programa.
    """

    # Construtor:
    def __init__(self):
        super().__init__()

    # Método de apresentação do menu:
    def _display_contacts_menu(self):
        self._display_header("CONTATOS")
        self._greet_user()
        self._display_login_information()
        print("[1] - LinkedIn")
        print("[2] - E-mail")
        print("[3] - Voltar ao menu principal")
        print("[4] - Sair") 

    # Método para lidar com entrada do usuário:
    def _handle_contacts_menu_selection(self):
        while True:
            user_choice = input(f'\n{constants.BOLD}Escolha uma área para saber mais:{constants.RESET} ')
            if user_choice == constants.CONT_LINKEDIN:
                self._current_menu = 'linkedin_menu'
                break
            if user_choice == constants.CONT_EMAIL:
                self._current_menu = 'email_menu'
                break
            if user_choice == constants.GENERAL_RETURN:
                self._current_menu = 'main_menu'
                break
            elif user_choice == constants.GENERAL_EXIT:
                self._current_menu = 'exit'
                break
            else:
                print(constants.INVALID_ENTRY_MESSAGE)

    # SubSub-Menu LinkedIn:
    def _display_linkedin_menu(self):
        self._display_header('CONTATOS: LINKEDIN')
        self._greet_user()
        self._display_login_information()
        print('TEMP TEMP TEMP')
        print('[1] - Voltar ao Menu Anterior')
        print('[2] - Sair') 

    # SubSub-Menu Email:
    def _display_email_menu(self):
        self._display_header('CONTATOS: E-MAIL')
        self._greet_user()
        self._display_login_information()
        print('TEMP TEMP TEMP')
        print('[1] - Voltar ao Menu Anterior')
        print('[2] - Sair')

    # Método único para lidar com menus finais dos Contatos:
    def _handle_contacts_final_menus(self):
        while True:
            user_choice = input(f'\n{constants.BOLD}Escolha para voltar ou sair:{constants.RESET} ')
            if user_choice == constants.FINAL_RETURN:
                self._current_menu = 'contacts_menu'
                break
            elif user_choice == constants.FINAL_EXIT:
                self._current_menu = 'exit'
                break
            else:
                print(constants.INVALID_ENTRY_MESSAGE)

#===================================================================================================# 
# Classe Inicializadora do Bot:
class Initializer(MainMenu, AboutMeMenu, ProjectsMenu, SkillsMenu, ContactsMenu):
    """
    Classe responsável por inicializar e executar o bot do menu interativo.

    Essa classe herda as funcionalidades dos menus principais e submenus, e define um dicionário
    para mapear cada menu a uma função correspondente. Além disso, fornece métodos para executar
    cada menu individualmente e executar o bot como um todo.

    Atributos:
    ----------
        menu_functions (dict): Um dicionário que mapeia cada menu a uma função correspondente.

    Métodos:
    ---------
        run():
            Executa o bot, inicializando a interação com o usuário e navegando pelos menus.

        run_main_menu():
            Executa o menu principal.

        run_about_me_menu():
            Executa o submenu "Sobre Mim".

        run_professional_menu():
            Executa o submenu "Experiência Profissional".

        run_professional_resume_menu():
            Executa o submenu "Resumo Profissional".

        run_professional_objective_menu():
            Executa o submenu "Objetivo Profissional".

        run_personal_menu():
            Executa o submenu "Informações Pessoais".

        run_personal_me_menu():
            Executa o submenu "Sobre Mim (Pessoal)".

        run_personal_hobbys_menu():
            Executa o submenu "Hobbies".

        run_projects_menu():
            Executa o submenu "Projetos".

        run_project_highlights_menu():
            Executa o submenu "Projetos em Destaque".

        run_project_portfolio_menu():
            Executa o submenu "Portfólio Completo".

        run_skills_menu():
            Executa o submenu "Habilidades".

        run_tech_skills_menu():
            Executa o submenu "Habilidades Técnicas".

        run_soft_skills_menu():
            Executa o submenu "Habilidades Sociais".

        run_contacts_menu():
            Executa o submenu "Contatos".

        run_linkedin_menu():
            Executa o submenu "LinkedIn".

        run_email_menu():
            Executa o submenu "E-mail".

    Exemplo de uso:
        # Criando uma instância do inicializador do bot
        initializer = Initializer()

        # Executando o bot
        initializer.run()
    """

    # Construtor:
    def __init__(self):
        super().__init__()

    # Definindo dicionário para chamada de cada menu:
        self.menu_functions = {
            'main_menu': self.run_main_menu,
            'about_me_menu': self.run_about_me_menu,
            'professional_menu': self.run_professional_menu,
            'prof_resume_menu': self.run_professional_resume_menu,
            'prof_objective_menu': self.run_professional_objective_menu,
            'personal_menu': self.run_personal_menu,
            'personal_me_menu': self.run_personal_me_menu,
            'personal_hobbys_menu': self.run_personal_hobbys_menu,
            'projects_menu': self.run_projects_menu,
            'projects_highlights_menu': self.run_project_highlights_menu,
            'projects_portfolio_menu': self.run_project_portfolio_menu,
            'skills_menu': self.run_skills_menu,
            'tech_skills_menu': self.run_tech_skills_menu,
            'soft_skills_menu': self.run_soft_skills_menu,
            'contacts_menu': self.run_contacts_menu,
            'linkedin_menu': self.run_linkedin_menu,
            'email_menu': self.run_email_menu
        }

    def run(self):
        self._get_user_name()
        while self._current_menu != 'exit':
            if self._current_menu in self.menu_functions:
                menu_function = self.menu_functions[self._current_menu]
                menu_function()
        print(f'\n{constants.BOLD}Finalizando Bot...{constants.RESET}')
        sleep(1)
        print(f'{constants.BOLD}Bot Finalizado!{constants.RESET}')

    def run_main_menu(self):
        self._display_main_menu()
        self._handle_main_menu_selection()

    def run_about_me_menu(self):
        self._display_about_me_menu()
        self._handle_about_me_menu_selection()

    def run_professional_menu(self):
        self._display_professional_menu()
        self._handle_professional_menu_selection()

    def run_professional_resume_menu(self):
        self._display_professional_resume_menu()
        self._handle_professional_final_menus()

    def run_professional_objective_menu(self):
        self._display_professional_objective_menu()
        self._handle_professional_final_menus()

    def run_personal_menu(self):
        self._display_personal_menu()
        self._handle_personal_menu_selection()

    def run_personal_me_menu(self):
        self._display_personal_me_menu()
        self._handle_personal_final_menus()

    def run_personal_hobbys_menu(self):
        self._display_personal_hobbys_menu()
        self._handle_personal_final_menus()

    def run_projects_menu(self):
        self._display_projects_menu()
        self._handle_projects_menu_selection()

    def run_project_highlights_menu(self):
        self._display_project_highlights_menu()
        self._handle_projects_final_menus()

    def run_project_portfolio_menu(self):
        self._display_project_porfolio_menu()
        self._handle_projects_final_menus()

    def run_skills_menu(self):
        self._display_skills_menu()
        self._handle_skills_menu_selection()

    def run_tech_skills_menu(self):
        self._display_tech_skills_menu()
        self._handle_skills_final_menus()

    def run_soft_skills_menu(self):
        self._display_soft_skills_menu()
        self._handle_skills_final_menus()

    def run_contacts_menu(self):
        self._display_contacts_menu()
        self._handle_contacts_menu_selection()

    def run_linkedin_menu(self):
        self._display_linkedin_menu()
        self._handle_contacts_final_menus()

    def run_email_menu(self):
        self._display_email_menu()
        self._handle_contacts_final_menus()
