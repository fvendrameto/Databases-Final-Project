# -*- coding: utf-8 -*-
import os
os.environ["NLS_LANG"] = '.AL32UTF8'

import cx_Oracle
from cx_Oracle import DatabaseError
import datetime
import re
from database.error_dict import errors
from unicodedata import normalize

INSERT_SUCCESS = None
UPDATE_SUCCESS = None

def getError(error_msg):
	regex = re.compile(r'[^.]*.([^\)]*)')
	msg = regex.match(error_msg)[1]

	return msg

class dbHelper():
	def __init__(self, ip, port, sid, user, password):
		'''
		Cria um novo objeto dbHelper
		Args: 
			ip: IP de acesso ao banco de dados
			port: porta de acesso ao banco de dados
			sid: SID do banco de dados
			user: Usuario do banco de dados
			password: Senha de acesso do usuario fornecido
		'''
		self.dns_tns = cx_Oracle.makedsn(ip, port, sid)
		self.connection = cx_Oracle.connect(user, password, self.dns_tns)
		

	def _preprocess_values(self, values):
		'''
		Preprocessa os valores que serao inseridos no banco.
		Args: 
			values: Os valores que devem ser processados
		Return:
			Um vetor contendo os valores já processados
		'''		
		for i, value in enumerate(values):
			if isinstance(value, str):
				values[i] = re.sub(r"'", '', value)
				values[i] = "'" + values[i] + "'"
			elif isinstance(value, int):
				values[i] = str(value)
			elif isinstance(value, float):
				values[i] = "%.2f" % (value)
			elif isinstance(value, datetime.datetime) or isinstance(value, datetime.date):
				values[i] = "TO_DATE('%02d/%02d/%4d', 'DD/MM/YYYY')" % (value.day, value.month, value.year)
			elif value is None:
				values[i] = "NULL"
		return values

	def commit(self):
		'''
		Faz o commit das alteraçoes realizadas no banco
		'''	
		self.connection.commit()

	def rollback(self):
		'''
		Descarta alteraçoes realizadas no banco desde o ultimo commit
		'''	
		self.connection.rollback()
	
	def _run_command(self, cmd):
		'''
		Executa um comando SQL no banco
		Args: 
			cmd: O comando que deve ser executado
		'''	
		cursor = self.connection.cursor()
		cursor.execute(cmd)
		cursor.close()

	def insert(self, table, fields, values):
		'''
		Insere os dados fornecidos nos campos da tabela fornecida
		Args: 
			table: A tabela que deve ser realizada a inserção
			fields: Lista de campos que devem ser realizadas as inserções
			values: Lista de valores que devem ser inseridos
		'''	
		values = self._preprocess_values(values)

		cmd = 'INSERT INTO ' + table + ' (' + ', '.join(fields) + ') VALUES ( ' + ', '.join(values) + ') '

		self._run_command(cmd)

	def insertIntoEndereco(self, values):
		'''
		Insere os dados fornecidos na tabela de enderecos
		Args: 
			values: Lista com os valores que devem ser inseridos
		Return:
			String com o a mensagem de erro ou um codigo de sucesso
		'''	
		table = 'ENDERECO'
		fields = ['ID', 'RUA', 'CIDADE', 'ESTADO', 'NUMERO', 'CEP']

		try:
			self.insert(table, fields, values)
		except DatabaseError as e:
			error = getError(str(e))
			return errors[error]
		
		return INSERT_SUCCESS

	def insertIntoDadosBancarios(self, values):
		'''
		Insere os dados fornecidos na tabela de dados bancarios
		Args: 
			values: Lista com os valores que devem ser inseridos
		Return:
			String com o a mensagem de erro ou um codigo de sucesso
		'''	
		table = 'DADOS_BANCARIOS'
		fields = ['ID', 'BANCO', 'AGENCIA', 'CONTA', 'TIPO_CONTA']

		try:
			self.insert(table, fields, values)
		except DatabaseError as e:
			error = getError(str(e))
			return errors[error]

		return INSERT_SUCCESS

	def insertIntoFornecedor(self, values):
		'''
		Insere os dados fornecidos na tabela de fornecedores
		Args: 
			values: Lista com os valores que devem ser inseridos
		Return:
			String com o a mensagem de erro ou um codigo de sucesso
		'''	
		table = 'FORNECEDOR'
		fields = ['CNPJ', 'NOME', 'TELEFONE', 'DADOS_BANCARIOS']

		try:
			self.insert(table, fields, values)
		except DatabaseError as e:
			error = getError(str(e))
			return errors[error]
		
		return INSERT_SUCCESS

	def insertIntoFuncionario(self, values):
		'''
		Insere os dados fornecidos na tabela de funcionarios
		Args: 
			values: Lista com os valores que devem ser inseridos
		Return:
			String com o a mensagem de erro ou um codigo de sucesso
		'''	
		table = 'FUNCIONARIO'
		fields = ['CPF', 'NOME', 'TEL_FIXO', 'TEL_MOVEL', 'COMISSAO', 'CARGO']

		try:
			self.insert(table, fields, values)
		except DatabaseError as e:
			error = getError(str(e))

			return errors[error]

		return INSERT_SUCCESS

	def insertIntoCliente(self, values):
		'''
		Insere os dados fornecidos na tabela de clientes
		Args: 
			values: Lista com os valores que devem ser inseridos
		Return:
			String com o a mensagem de erro ou um codigo de sucesso
		'''	
		table = 'CLIENTE'
		fields = ['CPF', 'NOME', 'DADOS_BANCARIOS', 'TEL_FIXO', 'TEL_MOVEL', 'ENDERECO']

		try:
			self.insert(table, fields, values)
		except DatabaseError as e:
			error = getError(str(e))
			return errors[error]

		return INSERT_SUCCESS

	def insertIntoCasaFesta(self, values):
		'''
		Insere os dados fornecidos na tabela de casas de festas
		Args: 
			values: Lista com os valores que devem ser inseridos
		Return:
			String com o a mensagem de erro ou um codigo de sucesso
		'''	
		table = 'CASA_FESTA'
		fields = ['NOME', 'ENDERECO']

		try:
			self.insert(table, fields, values)
		except DatabaseError as e:
			error = getError(str(e))
			return errors[error]

		return INSERT_SUCCESS

	def insertIntoFesta(self, values):
		'''
		Insere os dados fornecidos na tabela de festas
		Args: 
			values: Lista com os valores que devem ser inseridos
		Return:
			String com o a mensagem de erro ou um codigo de sucesso
		'''	
		table = 'FESTA'
		fields = ['CLIENTE', 'DATA', 'NUMERO_CONVIDADOS', 'TIPO', 'PRECO', 'CASA_FESTA', 'GERENTE']

		try:
			self.insert(table, fields, values)
		except DatabaseError as e:
			error = getError(str(e))
			return errors[error]

		return INSERT_SUCCESS

	def insertIntoAniversario(self, values):
		'''
		Insere os dados fornecidos na tabela de aniversarios
		Args: 
			values: Lista com os valores que devem ser inseridos
		Return:
			String com o a mensagem de erro ou um codigo de sucesso
		'''	
		table = 'ANIVERSARIO'
		fields = ['CLIENTE', 'DATA', 'NOME_ANIVERSARIANTE', 'TEMA', 'FAIXA_ETARIA']

		try:
			self.insert(table, fields, values)
		except DatabaseError as e:
			error = getError(str(e))
			return errors[error]

		return INSERT_SUCCESS
	
	def insertIntoBarracaRaspadinha(self, values):
		'''
		Insere os dados fornecidos na tabela de barracas de raspadinha
		Args: 
			values: Lista com os valores que devem ser inseridos
		Return:
			String com o a mensagem de erro ou um codigo de sucesso
		'''	
		table = 'BARRACA_RASPADINHA'
		fields = ['ID', 'CLIENTE', 'DATA', 'NUMERO', 'OPERADOR']

		try:
			self.insert(table, fields, values)
		except DatabaseError as e:
			error = getError(str(e))
			return errors[error]

		return INSERT_SUCCESS

	def insertIntoGarcomFesta(self, values):
		'''
		Insere os dados fornecidos na tabela que relaciona garcons e as festas em que trabalham
		Args: 
			values: Lista com os valores que devem ser inseridos
		Return:
			String com o a mensagem de erro ou um codigo de sucesso
		'''	
		table = 'GARCOM_FESTA'
		fields = ['CLIENTE', 'DATA', 'GARCOM']

		try:
			self.insert(table, fields, values)
		except DatabaseError as e:
			error = getError(str(e))
			return errors[error]

		return INSERT_SUCCESS

	def insertIntoBebida(self, values):
		'''
		Insere os dados fornecidos na tabela de bebidas
		Args: 
			values: Lista com os valores que devem ser inseridos
		Return:
			String com o a mensagem de erro ou um codigo de sucesso
		'''	
		table = 'BEBIDA'
		fields = ['NOME', 'VOLUME', 'QUANTIDADE', 'BANDEJA', 'PRECO']

		try:
			self.insert(table, fields, values)
		except DatabaseError as e:
			error = getError(str(e))
			return errors[error]

		return INSERT_SUCCESS

	def insertIntoBebidaBandejaFesta(self, values):
		'''
		Insere os dados fornecidos na tabela que relaciona festas e as bebidas alocadas as mesmas
		Args: 
			values: Lista com os valores que devem ser inseridos
		Return:
			String com o a mensagem de erro ou um codigo de sucesso
		'''	
		table = 'BEBIDA_BANDEJA_FESTA'
		fields = ['CLIENTE', 'DATA', 'BEBIDA', 'VOLUME', 'QUANTIDADE']

		try:
			self.insert(table, fields, values)
		except DatabaseError as e:
			error = getError(str(e))
			return errors[error]

		return INSERT_SUCCESS

	def delete(self, table, fields, values):
		'''
		Remove as tuplas da tabela dada que satisfazem as condições fornecidas
		Args: 
			table: A tabela que deve ser realizada a remoção
			fields: Lista de campos que devem possuir os valores de values
			values: Lista de valores para cada campo fornecido em fields
		'''	
		values = self._preprocess_values(values)				
		where_statements = []
		for i, field in enumerate(fields):
			where_statements.append('UPPER(' + field + ') = UPPER(' + values[i] + ')')

		cmd = 'DELETE FROM ' + table + ' WHERE (' + ' AND '.join(where_statements) + ')'
		self._run_command(cmd)


	def update(self, table, where_fields, where_values, update_fields, update_values):
		'''
		Atualiza as tuplas da tabela dada que satisfazem as condições fornecidas com os valores dados
		Args: 
			table: A tabela que deve ser realizada a remoção
			where_fields: Lista de campos que devem possuir os valores de where_values
			where_values: Lista de valores para cada campo fornecido em where_fields
			update_fields: Lista de campos que devem ser atualizados
			update_values: Lista de valores que devem ser atualizados
		'''
		where_statements = []
		for i, field in enumerate(where_fields):
			where_statements.append(field + ' = ' + where_values[i])

		set_statements = []
		for i, field in enumerate(update_fields):
			set_statements.append(field + ' = ' + update_values[i])

		cmd = 'UPDATE '  + table  + ' SET ' + ', '.join(set_statements) + ' WHERE (' + ' AND '.join(where_statements) + ')'
		self._run_command(cmd)

	def updateEndereco(self, where_values, values):
		'''
		Atualiza os valores da tabela de endereços com os valores dados
		Args: 
			where_values: Lista de valores usados como condição para cada campo
			values: Lista de valores para serem atualizados
		'''
		values = self._preprocess_values(values)
		where_values = self._preprocess_values(where_values)
		
		table = 'ENDERECO'
		fields = ['RUA', 'CIDADE', 'ESTADO', 'NUMERO', 'CEP']
		where_fields = ['ID']

		try:
			self.update(table, where_fields, where_values, fields, values)		
		except DatabaseError as e:
			error = getError(str(e))
			return errors[error]

		return UPDATE_SUCCESS

	def updateDadosBancarios(self, where_values, values):
		'''
		Atualiza os valores da tabela de dados bancarios com os valores dados
		Args: 
			where_values: Lista de valores usados como condição para cada campo
			values: Lista de valores para serem atualizados
		'''
		values = self._preprocess_values(values)
		where_values = self._preprocess_values(where_values)

		table = 'DADOS_BANCARIOS'
		fields = ['BANCO', 'AGENCIA', 'CONTA', 'TIPO_CONTA']
		where_fields = ['ID']

		try:
			self.update(table, where_fields, where_values, fields, values)		
		except DatabaseError as e:
			error = getError(str(e))
			return errors[error]

		return UPDATE_SUCCESS

	def updateFornecedor(self, where_values, values):
		'''
		Atualiza os valores da tabela de fornecedores com os valores dados
		Args: 
			where_values: Lista de valores usados como condição para cada campo
			values: Lista de valores para serem atualizados
		'''
		values = self._preprocess_values(values)
		where_values = self._preprocess_values(where_values)
		
		table = 'FORNECEDOR'
		fields = ['NOME', 'TELEFONE', 'DADOS_BANCARIOS']
		where_fields = ['CNPJ']

		try:
			self.update(table, where_fields, where_values, fields, values)		
		except DatabaseError as e:
			error = getError(str(e))
			return errors[error]

		return UPDATE_SUCCESS

	def updateFuncionario(self, where_values, values):
		values = self._preprocess_values(values)
		where_values = self._preprocess_values(where_values)
		
		table = 'FUNCIONARIO'
		fields = ['NOME', 'TEL_FIXO', 'TEL_MOVEL', 'COMISSAO', 'CARGO']
		where_fields = ['CPF']

		try:
			self.update(table, where_fields, where_values, fields, values)		
		except DatabaseError as e:
			error = getError(str(e))
			return errors[error]

		return UPDATE_SUCCESS

	def updateCliente(self, where_values, values):
		values = self._preprocess_values(values)
		where_values = self._preprocess_values(where_values)
		
		table = 'CLIENTE'
		fields = ['NOME', 'DADOS_BANCARIOS', 'TEL_FIXO', 'TEL_MOVEL', 'ENDERECO']
		where_fields = ['CPF']

		try:
			self.update(table, where_fields, where_values, fields, values)		
		except DatabaseError as e:
			error = getError(str(e))
			return errors[error]

		return UPDATE_SUCCESS

	def updateCasaFesta(self, where_values, values):
		values = self._preprocess_values(values)
		where_values = self._preprocess_values(where_values)
		
		table = 'CASA_FESTA'
		fields = ['ENDERECO']
		where_fields = ['NOME']

		try:
			self.update(table, where_fields, where_values, fields, values)		
		except DatabaseError as e:
			error = getError(str(e))
			return errors[error]

		return UPDATE_SUCCESS

	def updateFesta(self, where_values, values):
		values = self._preprocess_values(values)
		where_values = self._preprocess_values(where_values)
		
		table = 'FESTA'
		fields = ['NUMERO_CONVIDADOS', 'TIPO', 'PRECO', 'CASA_FESTA', 'GERENTE']
		where_fields = ['CLIENTE', 'DATA']

		try:
			self.update(table, where_fields, where_values, fields, values)		
		except DatabaseError as e:
			error = getError(str(e))
			return errors[error]

		return UPDATE_SUCCESS

	def updateAniversario(self, where_values, values):
		values = self._preprocess_values(values)
		where_values = self._preprocess_values(where_values)
		
		table = 'ANIVERSARIO'
		fields = ['NOME_ANIVERSARIANTE', 'TEMA', 'FAIXA_ETARIA']
		where_fields = ['CLIENTE', 'DATA']

		try:
			self.update(table, where_fields, where_values, fields, values)		
		except DatabaseError as e:
			error = getError(str(e))
			return errors[error]

		return UPDATE_SUCCESS

	def updateBarracaRaspadinha(self, where_values, values):
		values = self._preprocess_values(values)
		where_values = self._preprocess_values(where_values)
		
		table = 'BARRACA_RASPADINHA'
		fields = ['CLIENTE', 'DATA', 'NUMERO', 'OPERADOR']
		where_fields = ['ID']

		try:
			self.update(table, where_fields, where_values, fields, values)		
		except DatabaseError as e:
			error = getError(str(e))
			return errors[error]

		return UPDATE_SUCCESS

	def updateBebida(self, where_values, values):
		values = self._preprocess_values(values)
		where_values = self._preprocess_values(where_values)
		
		table = 'BEBIDA'
		fields = ['QUANTIDADE', 'BANDEJA', 'PRECO']
		where_fields = ['NOME', 'VOLUME']

		try:
			self.update(table, where_fields, where_values, fields, values)		
		except DatabaseError as e:
			error = getError(str(e))
			return errors[error]

		return UPDATE_SUCCESS

	def updateBebidaBandejaFesta(self, where_values, values):
		values = self._preprocess_values(values)
		where_values = self._preprocess_values(where_values)
		
		table = 'BEBIDA_BANDEJA_FESTA'
		fields = ['QUANTIDADE']
		where_fields = ['CLIENTE', 'DATA', 'BEBIDA', 'VOLUME']

		try:
			self.update(table, where_fields, where_values, fields, values)		
		except DatabaseError as e:
			error = getError(str(e))
			return errors[error]

		return UPDATE_SUCCESS

	def _run_select(self, cmd):
		cursor = self.connection.cursor()
		cursor.execute(cmd)

		result = []
		for elem in cursor:
			vals = []
			for i, value in enumerate(elem):
				if isinstance(value, datetime.datetime):
					vals.append("%02d/%02d/%4d" % (value.day, value.month, value.year))
				else:
					vals.append(str(value))
			result.append(vals)

		cursor.close()
		return result

	def getAllAniversarios(self, data_inicio, data_fim, gerente, casa_festa):
		data_inicio, data_fim, processed_gerente, processed_casa_festa = self._preprocess_values([data_inicio, data_fim, gerente, casa_festa])
		where_constraints = "(F.DATA BETWEEN " + data_inicio + " AND " + data_fim + " "

		if(casa_festa != 'Todas'):
			where_constraints += "AND F.CASA_FESTA = " + processed_casa_festa + " "
		if(gerente != "Todos"):
			where_constraints += "AND F.GERENTE = " + processed_gerente + " "
		where_constraints += ')'

		cmd = "SELECT F.CLIENTE, F.DATA, F.NUMERO_CONVIDADOS, F.PRECO, F.GERENTE, F.CASA_FESTA, A.NOME_ANIVERSARIANTE, A.TEMA, A.FAIXA_ETARIA, COUNT(GF.GARCOM)\
			FROM FESTA F JOIN ANIVERSARIO A ON A.CLIENTE = F.CLIENTE AND A.DATA = F.DATA\
			LEFT JOIN GARCOM_FESTA GF ON (GF.DATA = A.DATA AND GF.CLIENTE = A.CLIENTE)\
			WHERE " + where_constraints + "\
			GROUP BY(F.CLIENTE, F.DATA, F.NUMERO_CONVIDADOS, F.PRECO, F.GERENTE, F.CASA_FESTA, A.NOME_ANIVERSARIANTE, A.TEMA, A.FAIXA_ETARIA)"

		return self._run_select(cmd)

	def getGarconsFesta(self, cliente, data):
		cliente, data = self._preprocess_values([cliente, data])
		cmd = "SELECT FU.NOME, GF.GARCOM AS CPF, FU.COMISSAO FROM\
			FESTA F JOIN GARCOM_FESTA GF ON (F.CLIENTE = GF.CLIENTE AND F.DATA = GF.DATA)\
			AND (F.CLIENTE = " + cliente + " AND F.DATA = " + data + ")\
			JOIN FUNCIONARIO FU ON FU.CPF = GF.GARCOM"

		return self._run_select(cmd)

	def getBarracasAniversario(self, cliente, data):
		cliente, data = self._preprocess_values([cliente, data])
		cmd = "SELECT B.NUMERO, FU.NOME, B.OPERADOR AS CPF, FU.COMISSAO FROM\
			FESTA F JOIN BARRACA_RASPADINHA B ON (F.CLIENTE = B.CLIENTE AND F.DATA = B.DATA)\
			AND (F.CLIENTE = " + cliente + " AND F.DATA = " + data + ")\
			JOIN FUNCIONARIO FU ON FU.CPF = B.OPERADOR"

		return self._run_select(cmd)

	def getEnderecoFesta(self, cliente, data):
		cliente, data = self._preprocess_values([cliente, data])
		cmd = "SELECT E.RUA, E.NUMERO, E.CEP, E.CIDADE, E.ESTADO FROM\
		FESTA F JOIN CASA_FESTA CF ON (F.CASA_FESTA = CF.NOME)\
		AND (F.CLIENTE = " + cliente + " AND F.DATA = " + data + ")\
		JOIN ENDERECO E ON E.ID = CF.ENDERECO"

		return self._run_select(cmd)

	def getGarconsLivres(self, data):
		data = self._preprocess_values([data])[0]
		cmd = "SELECT F.NOME, F.CPF, F.COMISSAO FROM FUNCIONARIO F WHERE UPPER(F.CARGO) = 'GARÇOM' AND\
			F.CPF NOT IN(\
			SELECT GF.GARCOM FROM GARCOM_FESTA GF WHERE GF.DATA = " + data + ")"

		return self._run_select(cmd)

	def getOperadoresLivres(self, data):
		data = self._preprocess_values([data])[0]
		cmd = "SELECT F.NOME, F.CPF, F.COMISSAO FROM FUNCIONARIO F WHERE UPPER(F.CARGO) = 'OPERADOR' AND\
			F.CPF NOT IN(\
			SELECT BR.OPERADOR FROM BARRACA_RASPADINHA BR WHERE BR.DATA = " + data + ")"
		
		return self._run_select(cmd)

	def getGerentesLivres(self, data):
		data = self._preprocess_values([data])[0]
		cmd = "SELECT F.NOME, F.CPF, F.COMISSAO FROM FUNCIONARIO F WHERE UPPER(F.CARGO) = 'GERENTE' AND\
			F.CPF NOT IN(\
			SELECT FE.GERENTE FROM FESTA FE WHERE FE.DATA = " + data + ")"
		
		return self._run_select(cmd)

	def getNomeCasasFesta(self):
		cmd = "SELECT NOME FROM CASA_FESTA"
		return self._run_select(cmd)

	def getAllGerentes(self):
		cmd = "SELECT F.CPF, F.NOME, F.TEL_MOVEL, F.TEL_FIXO, F.COMISSAO, MIN(FE.DATA) AS DATA_PROXIMA_FESTA\
			FROM FUNCIONARIO F LEFT JOIN FESTA FE ON FE.GERENTE = F.CPF AND FE.DATA > SYSDATE AND FE.TIPO = 'A'\
			WHERE UPPER(F.CARGO) = 'GERENTE'\
			GROUP BY(F.CPF, F.NOME, F.TEL_MOVEL, F.TEL_FIXO, F.COMISSAO)"
		return self._run_select(cmd)

	def getAllOperadores(self):
		cmd = "SELECT F.CPF, F.NOME, F.TEL_MOVEL, F.TEL_FIXO, F.COMISSAO, MIN(BR.DATA) AS DATA_PROXIMA_FESTA \
				FROM FUNCIONARIO F LEFT JOIN BARRACA_RASPADINHA BR ON BR.OPERADOR = F.CPF\
				LEFT JOIN FESTA FE ON BR.CLIENTE = FE.CLIENTE AND BR.DATA = FE.DATA AND FE.DATA > SYSDATE AND FE.TIPO = 'A' \
				WHERE UPPER(F.CARGO) = 'OPERADOR'\
				GROUP BY(F.CPF, F.NOME, F.TEL_MOVEL,  F.TEL_FIXO, F.COMISSAO)"
		return self._run_select(cmd)

	def getAllGarcons(self):
		cmd = "SELECT F.CPF, F.NOME, F.TEL_MOVEL, F.TEL_FIXO, F.COMISSAO, MIN(GF.DATA) AS DATA_PROXIMA_FESTA\
			FROM FUNCIONARIO F LEFT JOIN GARCOM_FESTA GF ON GF.GARCOM = F.CPF\
			LEFT JOIN FESTA FE ON GF.CLIENTE = FE.CLIENTE AND GF.DATA = FE.DATA AND FE.DATA > SYSDATE AND FE.TIPO = 'A' \
			WHERE UPPER(F.CARGO) = 'GARÇOM'\
			GROUP BY(F.CPF, F.NOME, F.TEL_MOVEL,  F.TEL_FIXO, F.COMISSAO)"
		return self._run_select(cmd)

	def getBebidasInInterval(self, min_value=0, max_value=99999):
		cmd = "SELECT B.NOME, B.VOLUME, B.QUANTIDADE, B.PRECO FROM BEBIDA B WHERE B.QUANTIDADE BETWEEN " + str(min_value) + " AND " + str(max_value)
		return self._run_select(cmd)

	def getBebida(self, nome, volume):
		nome, volume = self._preprocess_values([nome, volume])
		cmd = """SELECT QUANTIDADE, BANDEJA, PRECO FROM BEBIDA
		WHERE NOME = """ + nome + " AND VOLUME = " + volume
		return self._run_select(cmd)

	def getGerente(self, cpf):
		cpf = self._preprocess_values([cpf])[0]
		cmd = """SELECT * FROM FUNCIONARIO
		WHERE CPF = """ + cpf + " AND CARGO = 'GERENTE'"
		return self._run_select(cmd)

	def getCliente(self, cpf):
		cpf = self._preprocess_values([cpf])[0]
		cmd = """SELECT * FROM CLIENTE
		WHERE CPF = """ + cpf
		return self._run_select(cmd)

	def getAllFornecedores(self):
		cmd = "SELECT F.CNPJ, F.NOME, F.TELEFONE, D.BANCO, D.AGENCIA, D.CONTA, D.TIPO_CONTA FROM FORNECEDOR F JOIN DADOS_BANCARIOS D ON F.DADOS_BANCARIOS = D.ID"
		return self._run_select(cmd)

	def getDadosBancariosFornecedor(self, cnpj):
		cnpj = self._preprocess_values([cnpj])[0]
		cmd = """SELECT F.DADOS_BANCARIOS, D.BANCO, D.AGENCIA, D.CONTA, D.TIPO_CONTA
			FROM FORNECEDOR F JOIN DADOS_BANCARIOS D ON F.DADOS_BANCARIOS = D.ID
			WHERE F.CNPJ = """ + cnpj
		return self._run_select(cmd)

	def getAllCasasFesta(self):
		cmd = "SELECT CF.NOME, E.RUA, E.NUMERO, E.CIDADE, E.CEP, MIN(FE.DATA) AS DATA_PROXIMA_FESTA\
			FROM CASA_FESTA CF JOIN ENDERECO E ON CF.ENDERECO = E.ID\
			LEFT JOIN FESTA FE ON FE.CASA_FESTA = CF.NOME AND FE.DATA > SYSDATE AND FE.TIPO = 'A' \
			GROUP BY(CF.NOME, E.RUA, E.NUMERO, E.CIDADE, E.CEP)\
		"
		return self._run_select(cmd)

	def getEnderecoCasaFesta(self, nome):
		nome = self._preprocess_values([nome])[0]
		cmd = """SELECT CF.ENDERECO, E.RUA, E.NUMERO, E.CIDADE, E.ESTADO, E.CEP
		FROM CASA_FESTA CF JOIN ENDERECO E ON CF.ENDERECO = E.ID
		WHERE CF.NOME = """ + nome
		
		return self._run_select(cmd)

	def getAllClientes(self):
		cmd = "SELECT C.CPF, C.NOME, C.TEL_FIXO, C.TEL_MOVEL, D.BANCO, D.AGENCIA, D.CONTA, D.TIPO_CONTA, COUNT(F.CLIENTE) AS NUMERO_FESTAS\
			FROM CLIENTE C JOIN DADOS_BANCARIOS D ON C.DADOS_BANCARIOS = D.ID\
			LEFT JOIN FESTA F ON C.CPF = F.CLIENTE\
			GROUP BY(C.CPF, C.NOME, C.TEL_FIXO, C.TEL_MOVEL, D.BANCO, D.AGENCIA, D.CONTA, D.TIPO_CONTA)"
		return self._run_select(cmd)

	def getEnderecoCliente(self, cpf):
		cpf = self._preprocess_values([cpf])[0]
		cmd = """SELECT C.ENDERECO, E.RUA, E.NUMERO, E.CIDADE, E.ESTADO, E.CEP
			FROM CLIENTE C JOIN ENDERECO E ON C.ENDERECO = E.ID
			WHERE C.CPF = """ + cpf
		return self._run_select(cmd)

	def getDadosBancariosCliente(self, cpf):
		cpf = self._preprocess_values([cpf])[0]
		cmd = """SELECT C.DADOS_BANCARIOS, D.BANCO, D.AGENCIA, D.CONTA, D.TIPO_CONTA
			FROM CLIENTE C JOIN DADOS_BANCARIOS D ON C.DADOS_BANCARIOS = D.ID
			WHERE C.CPF = """ + cpf
		return self._run_select(cmd)
