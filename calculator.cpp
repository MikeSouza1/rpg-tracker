#include <iostream>
#include <iomanip> // Biblioteca para formatar casas decimais na saida

using namespace std;

// Função recebe doubles e retorna obrigatoriamente doubles
double calculateExpectedDamage(double attack, double critRate, double critDMG, double bonus = 0.0) {
    // Convertendo as porcentagens em decimais
    double critMultiplier = 1.0 + (critRate / 100.0) * (critDMG / 100.0);
    double baseDamage = attack * critMultiplier;

    // Aplicando o bônus elemental (ex: 0.15 para 15%)
    return baseDamage * (1.0 + bonus);
}

int main () {
    // declarando variáveis e seus tipos
    double attack, critRate, critDMG, bonus;

    cout << "=========================================\n";
    cout << "   C++ DAMAGE ENGINE   \n";
    cout << "=========================================\n";

    // Recebendo inputs do terminal
    cout << "Insira o Ataque Base: ";
    cin >> attack;

    cout << "Insira a Taxa Crítica: ";
    cin >> critRate;

    cout << "Insira o Dano Crítico: ";
    cin >> critDMG;

    cout << "Insira o Dano Bônus Elemental (ex: 15%): ";
    cin >> bonus;

    // executando o calculo
    double expectedDmg = calculateExpectedDamage(attack, critRate, critDMG, bonus);

    // formatando a saida
    cout << fixed << setprecision(2);
    cout << "\n-----------------------------------------\n";
    cout << "Expected Average Damage: " << expectedDmg << "\n";
    cout << "-----------------------------------------\n";

    return 0; 
}