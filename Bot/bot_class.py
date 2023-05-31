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

# Classe Coletora de informações:
class GeneralMethods:
    def __init__(self):
        self._user_name = ''
        self._current_menu = 'main_menu'
        self._current_hour = datetime.datetime.now().hour
        self._current_time = datetime.datetime.now().strftime('%H:%M')
        self._current_date = datetime.datetime.now().strftime('%d/%m/%Y')

    # Método personalizado para limpar terminal baseado em OS:
    def _clear_screen(self):
        user_system = platform.system()
        if user_system == 'Windows':
            os.system('cls')
        else:
            os.system('clear')

    # Método para apresentação de um header personalizado:
    def _display_header(self, header_text):
        self._clear_screen()
        print(f' {header_text} '.center(75,'-'))

    # Método para exibir Saudação baseado na hora do dia:
    def _greet_user(self):
        if self._current_hour < 12:
            print(f'Bom Dia, {self._user_name}!')
        elif self._current_hour < 18:
            print(f'Boa Tarde, {self._user_name}!')
        else:
            print(f'Boa Noite, {self._user_name}!')
    
    # Método para coletar user_name:
    def _get_user_name(self):
        self._user_name = input('Por favor, insira seu nome: ').title()

    # Método para mostrar informações de entrada do usuário:
    def _display_login_information(self):
        print(f'Data do Acesso: {self._current_date}')
        print(f'Hora do Acesso: {self._current_time}')
        print(f'Usuário Logado: {self._user_name}\n')

#===================================================================================================#
# Classe Menu Principal:
class MainMenu(GeneralMethods):
    def __init__(self):
        super().__init__()

    # Método de apresentação do menu:
    def _display_main_menu(self):
        self._display_header('MENU PRINCIPAL')
        self._display_login_information()
        print('1 - Sobre Mim')
        print('2 - Meus Projetos')
        print('3 - Habilidades Tech e Soft')
        print('4 - Contatos')
        print('5 - Sair')

    # Método para lidar com entrada do usuário:
    def _handle_main_menu_selection(self):
        while True:
            user_choice = input('\nEscolha uma área para saber mais: ')
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
    def __init__(self):
        super().__init__()

    # Método de apresentação do menu:
    def _display_about_me_menu(self):
        self._display_header('SOBRE MIM')
        self._display_login_information()
        print('1 - Profissional')
        print('2 - Pessoal')
        print('3 - Voltar ao Menu Principal')
        print('4 - Sair')

    # Método para lidar com entrada do usuário:
    def _handle_about_me_menu_selection(self):
        while True:
            user_choice = input('\nEscolha uma área para saber mais: ')
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

    # Sub-menu Profissional:
    def _display_professional_menu(self):
        self._display_header('SOBRE MIM: PROFISSIONAL')
        self._display_login_information()
        print('1 - Resumo Profissional')
        print('2 - Objetivo')
        print('3 - Voltar ao Menu Anterior')
        print('4 - Sair')

    def _handle_professional_menu_selection(self):
        while True:
            user_choice = input('\nEscolha uma área para saber mais: ')
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

    # SubSub-Menu Resumo Profissional:
    def _display_professional_resume_menu(self):
        self._display_header('PROFISSIONAL: RESUMO PROFISSIONAL')
        self._display_login_information()
        print('TEMP TEMP TEMP')
        print('1 - Voltar ao Menu Anterior')
        print('2 - Sair')

    # SubSub-Menu Objetivo Profissional:
    def _display_professional_objective_menu(self):
        self._display_header('PROFISSIONAL: RESUMO PROFISSIONAL')
        self._display_login_information()
        print('TEMP TEMP TEMP')
        print('1 - Voltar ao Menu Anterior')
        print('2 - Sair')

    # Método único para lidar com menus finais profissionais:
    def _handle_professional_final_menus(self):
        while True:
            user_choice = input('\nEscolha para voltar ou sair: ')
            if user_choice == constants.FINAL_RETURN:
                self._current_menu = 'professional_menu'
                break
            elif user_choice == constants.FINAL_EXIT:
                self._current_menu = 'exit'
                break
            else:
                print(constants.INVALID_ENTRY_MESSAGE)

    # Sub-menu Pessoal:
    def _display_personal_menu(self):
        self._display_header('SOBRE MIM: PESSOAL')
        self._display_login_information()
        print('1 - Quem sou Eu')
        print('2 - Meus Hobbys')
        print('3 - Voltar ao Menu Anterior')
        print('4 - Sair')

    def _handle_personal_menu_selection(self):
        while True:
            user_choice = input('\nEscolha uma área para saber mais: ')
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

    # SubSub-Menu Quem Sou Eu:
    def _display_personal_me_menu(self):
        self._display_header('SOBRE MIM: QUEM SOU EU')
        self._display_login_information()
        print('TEMP TEMP TEMP')
        print('1 - Voltar ao Menu Anterior')
        print('2 - Sair')

    # SubSub-Menu Hobbys:
    def _display_personal_hobbys_menu(self):
        self._display_header('SOBRE MIM: HOBBYS')
        self._display_login_information()
        print('TEMP TEMP TEMP')
        print('1 - Voltar ao Menu Anterior')
        print('2 - Sair')

    # Método único para tratativas dos menus finais de resposta:
    def _handle_personal_final_menus(self):
        while True:
            user_choice = input('\nEscolha para voltar ou sair: ')
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
    def __init__(self):
        super().__init__()

    # Método de apresentação do menu:
    def _display_projects_menu(self):
        self._display_header('PROJETOS')
        self._display_login_information()
        print('1 - Projetos em Destaque')
        print('2 - Porfólio Completo')
        print('3 - Voltar ao Menu Principal')
        print('4 - Sair')

    # Método para lidar com entrada do usuário:
    def _handle_projects_menu_selection(self):
        while True:
            user_choice = input('\nEscolha uma área para saber mais: ')
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
        self._display_login_information()
        print('TEMP TEMP TEMP')
        print('1 - Voltar ao Menu Anterior')
        print('2 - Sair')

    # SubSub-Menu Portfólio Completo:
    def _display_project_porfolio_menu(self):
        self._display_header('PROJETOS: PORTFÓLIO COMPLETO')
        self._display_login_information()
        print('TEMP TEMP TEMP')
        print('1 - Voltar ao Menu Anterior')
        print('2 - Sair')    

    # Método único para lidar com menus finais dos projetos:
    def _handle_projects_final_menus(self):
        while True:
            user_choice = input('\nEscolha para voltar ou sair: ')
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
    def __init__(self):
        super().__init__()

    # Método de apresentação do menu:
    def _display_skills_menu(self):
        self._display_header("HABILIDADES TECH E SOFT")
        self._display_login_information()
        print("1 - Tech")
        print("2 - Soft")
        print("3 - Voltar ao menu principal")
        print("4 - Sair")

    # Método para lidar com entrada do usuário:
    def _handle_skills_menu_selection(self):
        while True:
            user_choice = input('\nEscolha uma área para saber mais: ')
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
        self._display_login_information()
        print('TEMP TEMP TEMP')
        print('1 - Voltar ao Menu Anterior')
        print('2 - Sair') 

    # SubSub-Menu Soft Skills:
    def _display_soft_skills_menu(self):
        self._display_header('HABILIDADES: SOFT')
        self._display_login_information()
        print('TEMP TEMP TEMP')
        print('1 - Voltar ao Menu Anterior')
        print('2 - Sair') 
        
    # Método único para lidar com menus finais das habilidades:
    def _handle_skills_final_menus(self):
        while True:
            user_choice = input('\nEscolha para voltar ou sair: ')
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
    def __init__(self):
        super().__init__()

    # Método de apresentação do menu:
    def _display_contacts_menu(self):
        self._display_header("CONTATOS")
        self._display_login_information()
        print("1 - LinkedIn")
        print("2 - E-mail")
        print("3 - Voltar ao menu principal")
        print("4 - Sair") 

    # Método para lidar com entrada do usuário:
    def _handle_contacts_menu_selection(self):
        while True:
            user_choice = input('\nEscolha uma área para saber mais: ')
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
        self._display_login_information()
        print('TEMP TEMP TEMP')
        print('1 - Voltar ao Menu Anterior')
        print('2 - Sair') 

    # SubSub-Menu Email:
    def _display_email_menu(self):
        self._display_header('CONTATOS: E-MAIL')
        self._display_login_information()
        print('TEMP TEMP TEMP')
        print('1 - Voltar ao Menu Anterior')
        print('2 - Sair')

    # Método único para lidar com menus finais dos Contatos:
    def _handle_contacts_final_menus(self):
        while True:
            user_choice = input('\nEscolha para voltar ou sair: ')
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
    def __init__(self):
        super().__init__()

    def run(self):
        self._get_user_name()
        self._greet_user()

        while self._current_menu != 'exit':
            # Inicializar Menu Principal:
            if self._current_menu == 'main_menu':
                self._display_main_menu()
                self._handle_main_menu_selection()
            # Inicializar Menu Sobre Mim:
            elif self._current_menu == 'about_me_menu':
                self._display_about_me_menu()
                self._handle_about_me_menu_selection()
            # Inicializar sub-menu Profissional:
            elif self._current_menu == 'professional_menu':
                self._display_professional_menu()
                self._handle_professional_menu_selection()
            # Inicializar subsub-menu Resumo Profissional:
            elif self._current_menu == 'prof_resume_menu':
                self._display_professional_resume_menu()
                self._handle_professional_final_menus()
            # Inicializar subsub-menu Objetivo Profissional:
            elif self._current_menu == 'prof_objective_menu':
                self._display_professional_objective_menu()
                self._handle_professional_final_menus()
            # Inicializar sub-menu Pessoal:
            elif self._current_menu == 'personal_menu':
                self._display_personal_menu()
                self._handle_personal_menu_selection()
            # Inicializar subsub-menu Quem Sou Eu:
            elif self._current_menu == 'personal_me_menu':
                self._display_personal_me_menu()
                self._handle_personal_final_menus()
            # Inicializar subsub-menu Hobbys:
            elif self._current_menu == 'personal_hobbys_menu':
                self._display_personal_hobbys_menu()
                self._handle_personal_final_menus()
            # Inicializar Menu Projetos:
            elif self._current_menu == 'projects_menu':
                self._display_projects_menu()
                self._handle_projects_menu_selection()
            # Inicializar sub-menu Projetos em Destaque:
            elif self._current_menu == 'projects_highlights_menu':
                self._display_project_highlights_menu()
                self._handle_projects_final_menus()
            # Inicializar sub-menu Porfólio Completo:
            elif self._current_menu == 'projects_portfolio_menu':
                self._display_project_porfolio_menu()
                self._handle_projects_final_menus()
            # Inicializar Menu Habilidades:
            elif self._current_menu == 'skills_menu':
                self._display_skills_menu()
                self._handle_skills_menu_selection()
            # Inicializar sub-menu Tech:
            elif self._current_menu == 'tech_skills_menu':
                self._display_tech_skills_menu()
                self._handle_skills_final_menus()
            # Inicializar sub-menu Soft:
            elif self._current_menu == 'soft_skills_menu':
                self._display_soft_skills_menu()
                self._handle_skills_final_menus()
            # Inicializar Menu Contatos:
            elif self._current_menu == 'contacts_menu':
                self._display_contacts_menu()
                self._handle_contacts_menu_selection()
            # Inicializar sub-menu LinkedIn:
            elif self._current_menu == 'linkedin_menu':
                self._display_linkedin_menu()
                self._handle_contacts_final_menus()
            # Inicializar sub-menu e-mail:
            elif self._current_menu == 'email_menu':
                self._display_email_menu()
                self._handle_contacts_final_menus()
