from E_cliente import *
from E_estoque import *
from E_funcionario import *
from E_gerente import *
from E_pagamento import *
from E_veiculo import *
from E_venda import *
import json
import F_tela_gerente
import F_veiculos
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
    def __init__(self, placa, marca, modelo, cor, combustivel, valor, especificacoes):
        
        new = True

        with open("_veiculos.json", encoding='utf-8') as carros:
            dados = json.load(carros)

        for i in dados:
            carro = (i['placa'])
            if placa == carro:
                new = False

        if new:
            new_veiculo = veiculo(placa, marca, modelo, cor, combustivel, especificacoes, valor)

#----------------------------------------------------------------------------------------------------------

class C_registrarVenda:
    def __init__  (self, veiculo, funcionario, cliente, valor, formaDePagamento, valorEntrada, tempoParcela):
        valorParcela = (float(valor) - float(valorEntrada))/float(tempoParcela)
        new_venda = venda(veiculo, funcionario, cliente, valor, formaDePagamento, valorEntrada, tempoParcela, valorParcela)
        C_DescadastrarVeículo(veiculo)

#----------------------------------------------------------------------------------------------------------

class C_DescadastrarVeículo:
    
    def __init__(self, placa):
        self.placa = placa

        with open("_veiculos.json", encoding='utf-8') as carros:
            dados = json.load(carros)

        index = ''

        for i in dados:
            if i['placa'] == self.placa:
                index = dados.index(i)
        
        if index != '':
            with open("_veiculos.json", "r") as file:
                data = json.load(file)
                data.pop(index)

            with open('_veiculos.json', 'w') as file:
                json.dump(data, file)

#c1 = C_DescadastrarVeículo('placa')

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
        self.tela.tela_gerente(self.gmail)

    def tela_funcionario(self):
        self.tela.tela_funcionario(self.gmail)

#C_EfetuarLogon('admin', '1234')
#----------------------------------------------------------------------------------------------------------

class C_ExcluirFuncionario:
    
    def __init__(self, cpf):
        self.cpf = cpf

        with open("_funcionarios.json", encoding='utf-8') as carros:
            dados = json.load(carros)

        index = ''

        for i in dados:
            if i['cpf'] == self.cpf:
                index = dados.index(i)
        
        if index != '':
            with open("_funcionarios.json", "r") as file:
                data = json.load(file)
                data.pop(index)

            with open('_funcionarios.json', 'w') as file:
                json.dump(data, file)

#c = C_ExcluirFuncionario("12343433234")

#----------------------------------------------------------------------------------------------------------

class C_GerenciarFaturamento:
    pass

#----------------------------------------------------------------------------------------------------------

class C_VisualizarFuncionarios:
    
    def __init__(self):
        self.lista_funcionarios = []
        with open("_funcionarios.json", encoding='utf-8') as funcionarios:
            dados = json.load(funcionarios)

        for i in dados:
            funcionario = 'NOME: '+i['nome']+', GMAIL: '+i['gmail']+ ', SALARIO: '+ i['salario']
            self.lista_funcionarios.append(funcionario)
#----------------------------------------------------------------------------------------------------------

class C_VisualizarVendas:
    
    def __init__(self):
        self.lista_vendas = []
        with open("_vendas.json", encoding='utf-8') as vendas:
            dados = json.load(vendas)

        for i in dados:
            venda = 'VEICULO: '+i['veiculo']+', VALOR: '+i['valor']+ ', FUNCIONARIO: '+ i['funcionario'] +', CLIENTE: '+i['cliente']
            self.lista_vendas.append(venda)

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

#----------------------------------------------------------------------------------------------------------

class C_VisualizarVeiculos:
    
    def __init__(self):
        self.veiculos = []

        with open("_veiculos.json", encoding='utf-8') as carros:
            dados = json.load(carros)

        for i in dados:
            carro = i['marca']+', '+ i['modelo'] +', '+i['placa']
            self.veiculos.append(carro)