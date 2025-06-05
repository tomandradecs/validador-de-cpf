# Este projeto focara na criacao de uma funcao que valida um numero de cpf (apenas os 11 digitos numericos) de acordo com as regras estabelecidas pela Receita Federal Brasileira.
# Voce nao vai precisar interagir com o usuario neste momento, apenas criar a funcao de validacao que retorna True ou False.
# Oque voce vai aprender:
# Manipulacao de strings e listas, lacos de repeticao, calculos e logica matematica, funcoes, tratamento de excecoes.
# Entendendo a validacao do CPF:
# Considere os primeiros 9 digitos do cpf.
# Multiplique o primeiro digito por 10, o segundo por 9, o terceiro por 8, e assim por diante, ate o nono digito por 2.
# Some todos esses resultados.
# Calcule o resto da divisao dessa soma por 11.
# Se o resto for 0 ou 1, o primeiro digito verificador é 0.
# Caso contrario, o primeiro digito verificador é 11 - resto.


def validar_cpf(cpf):
    """
    Valida um número de CPF (apenas 11 dígitos numéricos) de acordo com o algoritmo.
    Retorna True se o CPF for válido, False caso contrário.
    """
    # 1. Verifica se o CPF tem 11 dígitos e é composto apenas por números
    if len(cpf) != 11 or not cpf.isdigit():
        return False

    # 2. Verifica se todos os dígitos são iguais (ex: "11111111111").
    # CPFs com dígitos repetidos são inválidos por regra, mesmo que passem nos cálculos.
    if cpf == cpf[0] * 11:
        return False

    # 3. Calcula o primeiro dígito verificador
    # Multiplicadores de 10 a 2 para os primeiros 9 dígitos
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = soma % 11
    primeiro_digito_calculado = 0 if resto < 2 else 11 - resto

    # 4. Verifica se o primeiro dígito verificador calculado corresponde ao 10º dígito do CPF
    if int(cpf[9]) != primeiro_digito_calculado:
        return False

    # 5. Calcula o segundo dígito verificador
    # Multiplicadores de 11 a 2 para os primeiros 10 dígitos (incluindo o primeiro verificador)
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = soma % 11
    segundo_digito_calculado = 0 if resto < 2 else 11 - resto

    # 6. Verifica se o segundo dígito verificador calculado corresponde ao 11º dígito do CPF
    return int(cpf[10]) == segundo_digito_calculado


# --- Exemplos de uso para testar a função ---
if __name__ == "__main__":
    print("--- Testes de Validação de CPF ---")

    # CPF Válido (exemplo real, mas para fins didáticos)
    cpf_valido_exemplo = "12345678909"
    print(
        f"CPF {cpf_valido_exemplo}: {'Válido' if validar_cpf(cpf_valido_exemplo) else 'Inválido'}"
    )  # Deve ser Válido

    # CPF Inválido (dígitos verificadores incorretos)
    cpf_invalido_dv = "12345678900"
    print(
        f"CPF {cpf_invalido_dv}: {'Válido' if validar_cpf(cpf_invalido_dv) else 'Inválido'}"
    )  # Deve ser Inválido

    # CPFs com todos os dígitos iguais (Inválidos por regra)
    cpf_todos_zeros = "00000000000"
    print(
        f"CPF {cpf_todos_zeros}: {'Válido' if validar_cpf(cpf_todos_zeros) else 'Inválido'}"
    )  # Deve ser Inválido
    cpf_todos_uns = "11111111111"
    print(
        f"CPF {cpf_todos_uns}: {'Válido' if validar_cpf(cpf_todos_uns) else 'Inválido'}"
    )  # Deve ser Inválido
    cpf_todos_noves = "99999999999"
    print(
        f"CPF {cpf_todos_noves}: {'Válido' if validar_cpf(cpf_todos_noves) else 'Inválido'}"
    )  # Deve ser Inválido

    # CPF com caracteres não numéricos
    cpf_com_letras = "1234567890a"
    print(
        f"CPF {cpf_com_letras}: {'Válido' if validar_cpf(cpf_com_letras) else 'Inválido'}"
    )  # Deve ser Inválido

    # CPF com menos de 11 dígitos
    cpf_curto = "123456789"
    print(
        f"CPF {cpf_curto}: {'Válido' if validar_cpf(cpf_curto) else 'Inválido'}"
    )  # Deve ser Inválido

    # CPF com mais de 11 dígitos
    cpf_longo = "123456789012"
    print(
        f"CPF {cpf_longo}: {'Válido' if validar_cpf(cpf_longo) else 'Inválido'}"
    )  # Deve ser Inválido

    # CPF com dígitos em sequência (geralmente inválido, mas o algoritmo pode passar alguns)
    # Importante: CPFs em sequência como "01234567890" podem ser válidos matematicamente, mas não são CPFs reais.
    # O foco aqui é o algoritmo e a regra dos dígitos repetidos.
    cpf_sequencia = "12345678901"  # Exemplo que passaria pelo algoritmo
    print(
        f"CPF {cpf_sequencia}: {'Válido' if validar_cpf(cpf_sequencia) else 'Inválido'}"
    )  # Depende do algoritmo (se correto, deve ser inválido)

    # CPF aleatório (geralmente inválido)
    cpf_aleatorio = "98765432100"
    print(
        f"CPF {cpf_aleatorio}: {'Válido' if validar_cpf(cpf_aleatorio) else 'Inválido'}"
    )  # Deve ser Inválido
