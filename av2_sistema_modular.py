# AV2 - 3º BIMESTRE
# Arquivo: av2_sistema_modular.py

dados_brutos = [
    "  carlos eduardo silva;desenvolvedor;11988887777  ",
    "  ana paula mendes;analista de rh;21977776666  ",
    "  roberto carlos oliveira;gerente de projetos;31966665555  "
]


# 1. Funcao
def limpar_e_formatar_texto(texto):
    return texto.strip().upper()


# 2. Funcao
def extrair_codigo_ou_ddd(dado):
    return dado.strip()[0:2]


# 3. Funcao
def processar_e_exibir_cadastros(lista_dados):
    total = 0

    for item in lista_dados:
        nome, cargo, telefone = item.split(";")

        nome = limpar_e_formatar_texto(nome)
        cargo = limpar_e_formatar_texto(cargo)
        ddd = extrair_codigo_ou_ddd(telefone)

        print(f"Nome: {nome}")
        print(f"Cargo: {cargo}")
        print(f"DDD: {ddd}")
        print("--------------------")

        total += 1

    return total


# Programa principal
def main():
    print("================================")
    print(" SISTEMA DE GESTAO - AV2")
    print("================================")

    total_processado = processar_e_exibir_cadastros(dados_brutos)

    print(f"Total de registros: {total_processado}")
    print("PROCESSAMENTO CONCLUIDO")


if __name__ == "__main__":
    main()
