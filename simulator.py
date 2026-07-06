# Arquivo com a função de simular o dano do personagem (ou seu escudo gerado) baseado em uma fórmula simples

from main import search_character_by_id
from models import DPSCharacter, SupportCharacter

def simulate_performance(id_character, role_type="DPS"):
    data = search_character_by_id(id_character)

    if data is None:
        print("Personagem não encontrado no banco de dados.")
    
    id_char, name, level, hp, atk, crit_rate, crit_damage = data

    # Instanciando o objeto com base na escolha da função.
    if role_type.upper() == "DPS":
        # cria-se um DPS com 15% de dano elemental passivo
        character_obj = DPSCharacter(id_char, name, level, hp, atk, crit_rate, crit_damage, elemental_bonus=0.15)
    else:
        # cria-se um suporte com 20% de heal bonus
        character_obj = SupportCharacter(id_char, name, level, hp, atk, crit_rate, crit_damage, heal_bonus=0.2)
    
    # Imprime o relatorio encapsulado dentro do próprio objeto
    print(character_obj.get_performance_report())

    # Se for suporte, é exibido também o escudo dele
    if isinstance(character_obj, SupportCharacter):
        shield = character_obj.calculate_shield_strenght()
        print(f"-> Bônus de Suporte | Força do Escudo Gerado: {shield: .2f}\n")
    

def calc_average_damage(id_character):
    character_data = search_character_by_id(id_character)

    if character_data is None:
        print(f"Erro: Personagem não foi encontrado.")
        return
    
    # Desestruturando a Tupla na ordem da DB
    id_char, nome, nivel, hp, ataque, taxa_crit, dano_crit = character_data

    # convertendo taxas de % para decimal
    taxa_crit_decimal = taxa_crit / 100
    dano_crit_decimal = dano_crit / 100

    # Fórmula de dano critico médio do jogo 
    expected_damage = ataque * (1 + (taxa_crit_decimal * dano_crit_decimal))

    report = f"""
    =====================================
    ANÁLISE DE PERFORMANCE: {nome}  
    =====================================
    Nível: {nivel}
    Ataque Base: {ataque}
    Taxa Crítica: {taxa_crit}% / {dano_crit}%
    Dano Médio Esperado: {expected_damage:.2f}
    =====================================
    """

    print(report)

# teste
if __name__ == "__main__":
    print("--- TESTE 1: Simulação como Atacante (DPS) ---")
    simulate_performance(id_character=1, role_type="DPS")
    print("\n")
    print("--- TESTE 2: Simulação como Suporte (Support) ---")
    simulate_performance(id_character=2, role_type="SUPPORT")