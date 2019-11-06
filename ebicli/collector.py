import requests
import sys


def request(cnpj):
    endpoint = "https://www.receitaws.com.br/v1/cnpj/"
    url = endpoint + cnpj
    try:
        request = requests.get(url).json()
        return request
    except requests.exceptions.RequestException as e:
        print(e)
        sys.exit(1)


def imprimir_dados(dados):
    if "message" not in dados:
        print("Nome: ", dados["nome"])
        print("UF: ", dados["uf"])
        print("Telefone: ", dados["telefone"])
        print("Email: ", dados["email"])
        print("Data de abetura: ", dados["abertura"])
        print("\n\n")
        print(
            "Atividade principal:\n", dados["atividade_principal"][0]["text"]
        )
        print(15 * "-")
        print("\n\n")
        print("Atividades secundarias:")
        for item in dados["atividades_secundarias"]:
            print(item["text"])
            print(15 * "-", "\n")
    else:
        print(dados["message"])


def main():
    cnpj = input("Insira um CNPJ:")
    dados = request(cnpj)
    imprimir_dados(dados)


if __name__ == "__main__":
    main()
