import requests

class Collector:
    URL = "https://www.receitaws.com.br/v1/cnpj/"
    def __init__(self, cnpj):
        self.cnpj = cnpj
        self.request = requests.get(self.URL + self.cnpj).json()

    def get_atividade_principal(self):
        return self.request["atividade_principal"][0]['text']

    def get_atividades_secundarias(self):
        for item in self.request["atividades_secundarias"]:
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

if __name__ == '__main__':
    cnpj = input('informe um cnpj:')
    c = Collector(cnpj)
    print("Nome: ", c.get_nome())
    print("\nUF: ", c.get_uf())
    print("\nTelefone: ", c.get_telefone())
    print("\nEmail: ", c.get_email())
    print("\nData de abertura: ", c.get_data_de_abertura())
    print("\nAtividade principal: ", c.get_atividade_principal())
    #print("\nAtividades Secundarias: ", c.get_atividades_secundarias())

