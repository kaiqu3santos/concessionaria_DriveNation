import json

class veiculo:

    def __init__(self, placa, marca, modelo, cor, combustivel, especificacoes, valor) -> None:
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.combustivel = combustivel
        self.especificacoes = especificacoes
        self.valor = valor

#        with open ('_veiculos.json', 'w') as file:
#                    dictionary = {}

        self.serializeVeiculos()

    def serializeVeiculos(self):
                
                data = {}
                with open('_veiculos.json', 'r') as outfile:
                    try:
                            data = json.load(outfile)
                    except:
                            raise ("ERRO")
                    
                    dictionary = {"placa": self.placa, "marca":self.marca,"modelo":self.modelo, 
                                  "cor":self.cor, "combustivel":self.combustivel, "valor": self.valor}
                    data.append(dictionary)

                    with open('_veiculos.json', 'w') as outfile:
                            json.dump(data, outfile, indent=4)

#v1 = veiculo('placa', 'marca', 'modelo', 'cor', 'combustivel', 'especificacoes', 'valor')
#v2 = veiculo('45terw', 'marca', 'modelo', 'cor', 'combustivel', 'especificacoes', 'valor')
#v3 = veiculo('12345', 'marca', 'modelo', 'cor', 'combustivel', 'especificacoes', 'valor')
#v4 = veiculo('4321', 'marca', 'modelo', 'cor', 'combustivel', 'especificacoes', 'valor')