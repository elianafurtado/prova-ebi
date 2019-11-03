import requests


class Collector:
    URL = "https://www.receitaws.com.br/v1/cnpj/"
    def __init__(self, cnpj):
        self.cnpj = cnpj
        self.request = requests.get(self.URL + self.cnpj).json()

    def get_atividade_principal(self):
        return self.request["atividade_principal"][0]['text']

    def get_atividades_secundarias(self):
        for item in self.requ   est["atividades_secundarias"]:
            print(item['text'])
    def get_nome(self):
        return self.request["nome"]

    def get_uf(self):
        return self.request["uf"]

    def get_telefone(self):
        return self.request["telefone"]

    def get_email(self):
        return self.request["email"]

    def get_data_de_abertura(self):
        return self.request["abertura"]


c = Collector("17895646000187")
print(c.get_nome())
print(c.get_uf())
print(c.get_telefone())
print(c.get_email())
print(c.get_data_de_abertura())
print(c.get_atividade_principal())
print(c.get_atividades_secundarias())
