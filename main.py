from classes.professor import Professor
from metodos.registrar_professor import registrar_professor
from metodos.menu_inicial import menu_inicial
from metodos.menu_principal import menu_principal
from db.conexao import criar_tabelas

if __name__ == "__main__":
    criar_tabelas()
    menu_inicial()






