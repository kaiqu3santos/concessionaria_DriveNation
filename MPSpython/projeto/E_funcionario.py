import json

class funcionario:

    def __init__(self, nome, dataNasc, cpf, gmail, senha, salario) -> None:
        self.nome = nome
        self.dataNasc = dataNasc
        self.gmail = gmail
        self.senha = senha
        self.salario = salario
        self.cpf = cpf

#        with open ('_funcionarios.json', 'w') as file:
#                    dictionary = {}

        self.serializeFunctionary()

    def serializeFunctionary(self):
                
                data = {}
                with open('_funcionarios.json', 'r') as outfile:
                    try:
                            data = json.load(outfile)
                    except:
                            raise ("ERRO")
                    
                    dictionary = {"nome": self.nome, "dataNasc":self.dataNasc,"cpf":self.cpf, "gmail":self.gmail, "senha":self.senha, "salario": self.salario}
                    data[self.cpf] = dictionary

                    with open('_funcionarios.json', 'w') as outfile:
                            json.dump(data, outfile, indent=4)



#f1 = funcionario('luiz', '01/01/2001', 123434234, 'guga@gmail.com', '093294203', '2123190')
#f2 = funcionario('guga', '01/01/2001', 123434234, 'guga@sadsa.com', '093294203', '2123190')
#f3 = funcionario('kaka', '01/01/4322001', 12343434234, 'gdfguga@sadsa.com', '09gdf3294203', '2123gdf190')