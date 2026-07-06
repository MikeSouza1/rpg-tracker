# Arquivo onde fica a criação da database dos personagens, bem como seu CRUD

import sqlite3
from models import Character

def configure_database():
    # Abre a conexão com o banco de dados e o cria se não existir.
    connection = sqlite3.connect("banco_rpg.db")

    # Cria um cursor para executar comandos SQL.
    cursor = connection.cursor()

    # Instrução SQL baseada no mapa feito
    
    sql_command_create_table = """
    CREATE TABLE IF NOT EXISTS Personagem (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL CHECK(length(nome) > 0),
        nível  INTEGER NOT NULL CHECK(nível >= 1),
        hp_base REAL CHECK(hp_base > 0),
        atk_base REAL CHECK(atk_base > 0),
        crit_rate REAL CHECK(crit_rate >= 0 AND crit_rate <= 100),
        crit_damage REAL CHECK(crit_damage >= 0)
    )
    """

    # Cursor executa o comando
    cursor.execute(sql_command_create_table)

    # Salva a operação no banco de dados
    connection.commit()
    connection.close()

    print("Banco de dados pronto e tabela 'Personagem' garantida!")

def create_character(name, level, hp, atk, crit_rate, crit_damage):
    # Valida-se os dados antes de mais nada, invocando erro caso algum ocorra
    try:
        Character(0, name, level, hp, atk, crit_rate, crit_damage)
    except ValueError as validation_error:
        print(f"\n[BLOQUEADO PELA APLICAÇÃO] Não foi possivel salvar no Banco: {validation_error}")
        return
    
    # Salva no banco de dados caso tenha passado da validação
    try:
        connection = sqlite3.connect("banco_rpg.db")
        cursor = connection.cursor()

        # Comando para inserir os dados. "?" são espaços reservados para evitar SQL Injection, garantindo que o que o usuário inserir seja tratado como texto apenas.
        sql_command_insert = """
        INSERT INTO Personagem (nome, nível, hp_base, atk_base, crit_rate, crit_damage)
        VALUES (?, ?, ?, ?, ?, ?)
        """

        # Cria-se uma tupla com os valores adquiridos na função e então executa o comando na mesma ordem
        values = (name, level, hp, atk, crit_rate, crit_damage)
        cursor.execute(sql_command_insert, values)

        connection.commit()
        connection.close()

        print(f"Personagem {name} cadastrado com sucesso!")
    except sqlite3.IntegrityError as db_error:
        # Se por algum motivo passar do primeiro try, há uma segunda checagem direto na DB.
        print(f"\n[BLOQUEADO PELO BANCO DE DADOS] Violou restrição de integridade: {db_error}")

def list_character():
    connection = sqlite3.connect("banco_rpg.db")
    cursor = connection.cursor()

    # Comando para ler todas as colunas da tabela
    sql_command_select = "SELECT * FROM Personagem"
    cursor.execute(sql_command_select)

    # pega as linhas lidas e guarda numa variável
    characters = cursor.fetchall()
    connection.close()

    # formatando a saida no terminal para ficar legível
    print("\n--- Lista de Personagens Cadastrados ---")
    if not characters:
        print("Nenhum personagem cadastrado ainda.")
    else:
        for c in characters:
            # a DB devolve os dados em uma tupla, na mesma ordem que a tabela foi criada
            print(f"ID: {c[0]}  |  Nome: {c[1]} (Nv. {c[2]})")
            print(f"       |  HP: {c[3]}  |  Atk: {c[4]}  | CR: {c[5]}  | CD: {c[6]}%\n")


def update_character(id_character, new_level, new_hp, new_atk):
    connection = sqlite3.connect("banco_rpg.db")
    cursor = connection.cursor()

    # Comando SQL: UPDATE na tabela, SET (defina) os novos valores, WHERE (onde) o id for igual ao que foi passado.
    sql_command_update = """
    UPDATE Personagem
    SET nível = ?, hp_base = ?, atk_base = ?
    WHERE id = ?    
    """

    # Tupla na mesma ordem dos ?
    values = (new_level, new_hp, new_atk, id_character)
    cursor.execute(sql_command_update, values)

    # Catch no nome do personagem para printar no final
    sql_command_select = "SELECT nome FROM Personagem WHERE id = ?"
    values_name = (id_character,)
    cursor.execute(sql_command_select, values_name)
    name_character = cursor.fetchone()[0]

    connection.commit()
    connection.close()

    print(f"\nAtributos do personagem {name_character} atualizados com sucesso!")

def delete_character(id_character):
    connection = sqlite3.connect("banco_rpg.db")
    cursor = connection.cursor()

    # Comando para deletar um personagem, atento ao Where
    cursor.execute("DELETE FROM Personagem WHERE id = ?", (id_character,))
    connection.commit()
    connection.close()

    print(f"\nPersonagem de ID {id_character} foi deletado do sistema.")

def search_character_by_id(id_character):
    # Usado para procurar um personagem em específico (ou nenhum se não tiver)
    connection = sqlite3.connect("banco_rpg.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Personagem WHERE id = ?", (id_character,))
    character = cursor.fetchone()

    connection.close()
    return character # retorna a tupla com os dados do personagem


# Verifica se esse arquivo está sendo rodado diretamente e chama a função
if __name__ == "__main__":
    configure_database()

    # adicionar primeiro personagem de teste
    # create_character("Kenneth", 99, 20000.0, 2300.0, 90.0, 250.0)
    # create_character("Lisanne", 76, 23000.0, 1600.0, 50.0, 130.0)
    # create_character("Seraph", 100, 25000.0, 2500.0, 105.0, 300.0)
    # update_character(1, 94, 20000.0, 2300.0)

    # função de listar
    list_character()

    # função de deletar 
    # delete_character(3)