from E_cliente import *
from E_estoque import *
from E_funcionario import *
from E_gerente import *
from E_pagamento import *
from E_veiculo import *
from E_venda import *
import json
import F_tela_gerente
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class C_AlterarDadosDoFuncionario():
    pass

#----------------------------------------------------------------------------------------------------------
 
class C_AlterarDadosDoVeiculo():
    pass

#----------------------------------------------------------------------------------------------------------

class C_cadastrarCliente:

    def __init__(self, nome, cpf, rg, tel, gmail) -> None:
       new_cliente = cliente(nome, cpf, rg, tel, gmail)

#----------------------------------------------------------------------------------------------------------

class C_cadastrarFuncionario:

    def __init__ (self, gmail, senha, nome, cpf, dataNasc, salario):
        new_funcionario = funcionario(nome, dataNasc, cpf, gmail, senha, salario)

#----------------------------------------------------------------------------------------------------------

class C_CadastrarGerente:
    def __init__(self, gmail, senha, nome, cpf, dataNasc, salario):
        new_gerente = gerente(nome, dataNasc, cpf, gmail, senha, salario)

#----------------------------------------------------------------------------------------------------------

class C_CadastrarVeiculo:
    def __init__(placa, marca, modelo, cor, combustivel, valor, especificacoes):
        new_veiculo = veiculo(marca, modelo, cor, combustivel, especificacoes, valor, placa)

#----------------------------------------------------------------------------------------------------------

class C_registrarVenda:
    def __init__  (self, veiculo, funcionario, cliente, valor, formaDePagamento, valorEntrada, tempoParcela):
        valorParcela = (float(valor) - float(valorEntrada))/float(tempoParcela)
        new_venda = venda(veiculo, funcionario, cliente, valor, formaDePagamento, valorEntrada, tempoParcela, valorParcela)

#----------------------------------------------------------------------------------------------------------

class C_DescadastrarVeículo:
    pass

#----------------------------------------------------------------------------------------------------------

class C_EfetuarLogoff:
    pass

#----------------------------------------------------------------------------------------------------------

class C_EfetuarLogon:

    def __init__(self, tela, gmail, senha) -> None:
        self.tela = tela
        self.gmail = gmail
        self.senha = senha
        self.login()

    def login(self):
            with open('_gerentes.json') as f:
                    data = json.load(f)

            if (self.gmail in data):
                gerente = data[self.gmail]
                if (gerente["senha"] == (self.senha)):
                    self.tela_gerente()

            with open('_funcionarios.json') as f:
                    data = json.load(f)

            if (self.gmail in data):
                gerente = data[self.gmail]
                if (gerente["senha"] == (self.senha)):
                    self.tela_funcionario()       

    def tela_gerente(self):
        self.tela.tela_gerente()

    def tela_funcionario(self):
        self.tela.tela_funcionario()

#C_EfetuarLogon('admin', '1234')
#----------------------------------------------------------------------------------------------------------

class C_ExcluirFuncionario:
    pass

#----------------------------------------------------------------------------------------------------------

class C_GerenciarFaturamento:
    pass

#----------------------------------------------------------------------------------------------------------

class C_PagarFuncionário:
    pass

#----------------------------------------------------------------------------------------------------------

class C_RegistrarVenda:
    pass

#----------------------------------------------------------------------------------------------------------

class C_VisualizarFaturamentoFuncionario:
    pass

#----------------------------------------------------------------------------------------------------------

class C_VisualizarFaturamentoTotal:
    pass

#----------------------------------------------------------------------------------------------------------

class C_VisualizarFuncionario:
    pass

#----------------------------------------------------------------------------------------------------------

class C_VisualizarVeiculo:
    pass