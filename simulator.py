from main import search_character_by_id

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
    calc_average_damage(1)
    calc_average_damage(2)