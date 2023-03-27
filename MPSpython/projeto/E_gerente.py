import json

class gerente:

        def __init__(self, nome, dataNasc, cpf, gmail, senha, salario) -> None:
                self.nome = nome
                self.dataNasc = dataNasc
                self.gmail = gmail
                self.senha = senha
                self.salario = salario
                self.cpf = cpf

        #        with open ('_gerentes.json', 'w') as file:
        #                    dictionary = {}

                self.serializeGerente()

        def serializeGerente(self):
                        
                        data = {}
                        with open('_gerentes.json', 'r') as outfile:
                                try:
                                        data = json.load(outfile)
                                except:
                                        raise ("ERRO")
                        
                        dictionary = {"nome": self.nome, "dataNasc":self.dataNasc,"cpf":self.cpf, "gmail":self.gmail, "senha":self.senha, "salario": self.salario}
                        data[self.gmail] = dictionary

                        with open('_gerentes.json', 'w') as outfile:
                                json.dump(data, outfile, indent=4)
                                

#g1 = gerente('Paulo', '01/01/2001', 123434234, 'guga@gmail.com', '093294203', '2123190')
#g2 = gerente('Felipe', '01/01/2001', 123434234, 'guga@gmail.com', '093294203', '2123190')
g3 = gerente('admin', '01/01/2001', "1234", 'admin', '1234', '2123190')