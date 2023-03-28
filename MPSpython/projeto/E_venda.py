import json
from E_pagamento import pagamento

class venda:

    def __init__(self, veiculo, funcionario, cliente, valor, formaDePagamento, valorEntrada, tempoParcela, valorParcela) -> None:
        self.veiculo = veiculo
        self.funcionario = funcionario
        self.cliente = cliente
        new_pagamento = pagamento(valor, formaDePagamento, valorEntrada, tempoParcela, valorParcela)

        self.serializeVenda(valor, formaDePagamento, valorEntrada, tempoParcela, valorParcela) 
        
    def serializeVenda(self, valor, formaDePagamento, valorEntrada, tempoParcela, valorParcela):
                
                data = {}
                with open('_vendas.json', 'r') as outfile:
                    try:
                            data = json.load(outfile)
                    except:
                            raise ("ERRO")
                    
                    dictionary = {'veiculo':self.veiculo, 'funcionario':self.funcionario, 
                                  'cliente':self.cliente, 'valor':valor, 
                                  'formaDePagamento':formaDePagamento, 'valorEntrada':valorEntrada, 
                                  'tempoParcela':tempoParcela, 'valorParcela':valorParcela}
                    data.append(dictionary)

                    with open('_vendas.json', 'w') as outfile:
                            json.dump(data, outfile, indent=4)

#v1 = venda('veiculo', 'funcionario', 'cliente', 'valor', 'formaDePagamento', 'valorEntrada', 'tempoParcela', 'valorParcela')