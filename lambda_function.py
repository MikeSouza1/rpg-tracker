import json


def lambda_handler(event, context):
    """
    Função principal que a AWS Lambda executará automaticamente na nuvem.
    O parâmetro 'event' traz os dados enviados pelo cliente na requisição.
    """
    try:
        # Usa-se valores padrão como parâmetros caso nenhum seja enviado.
        # Converter para float devido ao JSON
        attack = float(event.get("attack", 0))
        crit_rate = float(event.get("crit_rate", 0))
        crit_dmg = float(event.get("crit_dmg", 0))
        bonus = float(event.get("bonus", 0.0))

        # validação de dados & segurança
        if attack <= 0:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Validação: O Ataque Base deve ser maior do que 0."})
            }

        if crit_rate < 0 or crit_rate > 100:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Validação: A Taxa Crítica deve estar entre 0 e 100."})
            }

        if crit_dmg < 0:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Validação: O Dano Crítico não pode ser negativo."})
            }

        # Aplicando fórmula de dano
        crit_multiplier = 1.0 + (crit_rate / 100.0) * (crit_dmg / 100.)
        expected_dmg = (attack * crit_multiplier) * (1.0 + bonus)

        # estrutura padrão de retorno APIs REST no AWS Lambda
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "message": "Cálculo processado com sucesso!",
                "status_input": {
                    "attack": attack,
                    "crit_ratio": f"{crit_rate}% / {crit_dmg}%",
                    "bonus": f"{bonus * 100}%"
                },
                "expected_average_damage": round(expected_dmg, 2)
            })
        }
    except ValueError:
        # Se enviadas letras ao invés de números
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Formato inválido: Todos os atributos devem ser numéricos."})
        }
    except Exception as e:
        # Falha interna da nuvem
        return {
            "statusCode": 500,
            "body": json.dumps({"error": f"Erro interno no servidor da nuvem: {str(e)}"})
        }


# =====================================================================
# BLOCO DE SIMULAÇÃO LOCAL (Para testar no VSCode antes de subir para a AWS)
# =====================================================================
if __name__ == "__main__":
    false_event = {
        "attack": 1200.0,
        "crit_rate": 60.0,
        "crit_damage": 150.0,
        "bonus": 0.15
    }

    print("--- SIMULANDO EXECUÇÃO LAMBDA LOCALMENTE ---")
    resposta = lambda_handler(false_event, context=None)

    print(f"Status Code: {resposta['statusCode']}")
    print("Corpo da Resposta (JSON):")
    print(json.dumps(json.loads(
        resposta['body']), indent=2, ensure_ascii=False))
