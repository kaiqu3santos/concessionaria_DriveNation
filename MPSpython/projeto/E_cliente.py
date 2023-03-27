import json

class cliente:

    def __init__(self, nome, gmail, cpf, rg, telefone) -> None:
        self.gmail = gmail
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.telefone =  telefone

#        with open ('_clientes.json', 'w') as file:
#                   dictionary = {}

        self.serializeCliente()

    def serializeCliente(self):
                
                data = {}
                with open('_clientes.json', 'r') as outfile:
                    try:
                            data = json.load(outfile)
                    except:
                            raise ("ERRO")
                    
                    dictionary = {"nome": self.nome, "rg":self.rg,"cpf":self.cpf, "gmail":self.gmail, "telefone":self.telefone}
                    data[self.cpf] = dictionary

                    with open('_clientes.json', 'w') as outfile:
                            json.dump(data, outfile, indent=4)

#c1 = cliente('danilo', 'danilo@gmail.com', '4326234643', '7812643', '82174')