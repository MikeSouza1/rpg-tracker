# ⚔️ RPG Theorycrafting & Character Tracker

Um sistema completo de gerenciamento e simulação matemática de personagens de RPG. Este projeto atua como um motor de *theorycrafting* simples, permitindo cadastrar unidades, calcular rotações de dano médio esperado, avaliar multiplicadores críticos e medir a eficácia de escudos com base em atributos estruturados.

## O Objetivo do Projeto
Demonstrar a aplicação de boas práticas de Engenharia de Software na modelagem de sistemas, utilizando:
- **Programação Orientada a Objetos (OOP):** Uso de herança e polimorfismo para separar lógicas de personagens Atacantes (`DPS`) e Suportes (`Support`).
- **Segurança e Validação:** Tratamento de erros rigoroso para impedir a inserção de status matematicamente impossíveis (ex: HP negativo ou Taxa Crítica acima de 100%).
- **Integração Serverless:** Preparação de funções de cálculo para execução em nuvem via AWS Lambda.
- **Garantia de Qualidade:** Cobertura de testes unitários para validar a precisão das fórmulas de dano e resiliência do sistema.

## Tecnologias Utilizadas
- **Python 3:** Lógica de negócio, cálculos matemáticos e Orientação a Objetos.
- **SQLite3:** Banco de dados relacional embutido para persistência do inventário de personagens.
- **AWS Lambda:** Handler estruturado para processamento de requisições JSON na nuvem.
- **Pytest:** Framework de testes automatizados para validação de regras de negócio.

## Arquitetura e Funcionalidades

- **CRUD de Entidades:** Criação, leitura, atualização e exclusão de personagens no banco de dados SQLite, com proteção contra *SQL Injection* via parametrização de queries (`?`).
- **Motor de Simulação de Combate:**
  - O cálculo de `Expected Average Damage` cruza Ataque Base, Taxa Crítica e Dano Crítico.
  - A classe `DPSCharacter` estende a fórmula base adicionando multiplicadores de Bônus Elemental.
  - A classe `SupportCharacter` converte percentuais de HP Máximo em integridade de escudos/cura.
- **API Serverless:** O arquivo handler recebe cargas JSON com status brutos e devolve respostas padronizadas HTTP 200 com os multiplicadores processados.
- **Testes Unitários:** O arquivo de testes simula instâncias de classes e valida se o retorno matemático das fórmulas bate exatamente com o dano e escudo esperados, garantindo confiabilidade nas simulações.

## Como reproduzir este projeto localmente

1. Clone este repositório em sua máquina.
2. Instale a biblioteca de testes (caso queira rodá-los): `pip install pytest`
3. Para iniciar o banco de dados e gerenciar os personagens, execute: `python main.py`
4. Para gerar relatórios de simulação de combate (Dano e Escudo), execute: `python simulate.py`
5. Para rodar a suíte de validação e garantir a integridade matemática das fórmulas, execute: `pytest test_models.py`
