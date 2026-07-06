# Arquivo para testar as funções de dano

from models import DPSCharacter, SupportCharacter, Character
import pytest

# 1 - Testando o calculo do dano com base na classe mãe
def test_base_character_expected_damage():
    # Cria-se um personagem base com números exatos para se ter controle
    test_character = Character(
        char_id=99,
        name='Dummy',
        level=1,
        base_hp=10000.0,
        base_atk=1000.0,
        crit_rate=50.0,
        crit_dmg=100.0
    )

    # O dano esperado, com esses atributos, deve ser exatamente 1500.0
    assert test_character.calculate_expected_dmg() == pytest.approx(1500.0)

# 2 - Testando o bônus passivo de dano da classe DPS
def test_dps_character_bonus_damage():
    test_dps_character = DPSCharacter(
        char_id=100,
        name='DPS Dummy',
        level=1,
        base_hp=10000.0,
        base_atk=1000.0,
        crit_rate=50.0,
        crit_dmg=100.0,
        elemental_bonus=0.15 # 15%
    )

    # Com o dano sendo 1500, + os 15% de dano elemental, o resultado deve ser 1725.0
    assert test_dps_character.calculate_expected_dmg() == pytest.approx(1725.0)

# 3 - Testando o escudo gerado pelo personagem suporte
def test_support_character_shield():
    test_support_character = SupportCharacter(
        char_id=101,
        name='Support Dummy',
        level=1,
        base_hp=10000.0,
        base_atk=1000.0,
        crit_rate=50.0,
        crit_dmg=100.0,
        heal_bonus=0.2
    )

    # Escudo = (10000 * 0.25) * (1 + 0.20) = 2500 * 1.2 = 3000.0
    assert test_support_character.calculate_shield_strenght() == pytest.approx(3000.0)