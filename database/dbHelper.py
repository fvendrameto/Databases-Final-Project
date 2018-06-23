# -*- coding: utf-8 -*-

import cx_Oracle
import datetime

from unicodedata import normalize

class dbHelper():
	def __init__(self, ip, port, sid, user, password):
		'''
		Cria um novo objeto dbHelper
		Args:
			ip: Endereço IP do 
		'''
		self.dns_tns = cx_Oracle.makedsn(ip, port, sid)
		self.connection = cx_Oracle.connect(user, password, self.dns_tns)
		

	def _preprocess_values(self, values):
		for i, value in enumerate(values):
			if isinstance(value, str):
				values[i] = normalize('NFKD', values[i]).encode('ASCII', 'ignore').decode('ASCII')
				values[i] = values[i].upper()
				values[i] = "'" + value + "'"
			elif isinstance(value, int):
				values[i] = str(value)
			elif isinstance(value, datetime.datetime):
				values[i] = "'%2d/%02d/%4d'" % (value.day, value.month, value.year)
		return values

	def commit(self):
		self.connection.commit()
	
	def _run_command(self, cmd):
		cursor = self.connection.cursor()
		cursor.execute(cmd)
		cursor.close()

	def insert(self, table, fields, values):
		values = self._preprocess_values(values)				
		cmd = 'INSERT INTO ' + table + ' (' + ', '.join(fields) + ') VALUES ( ' + ', '.join(values) + ') '

		self._run_command(cmd)

	def insertIntoEndereco(self, values):


	def delete(self, table, fields, values):
		values = self._preprocess_values(values)				
		where_statements = []
		for i, field in enumerate(fields):
			where_statements.append(field + ' = ' + values[i])
		cmd = 'DELETE FROM ' + table + ' WHERE (' + ' AND '.join(where_statements) + ')'

		self._run_command(cmd)

	def update(self, table, where_fields, where_values, update_fields, update_values):
		where_values = self._preprocess_values(where_values)
		update_values = self._preprocess_values(update_values)

		where_statements = []
		for i, field in enumerate(where_fields):
			where_statements.append(field + ' = ' + where_values[i])

		set_statements = []
		for i, field in enumerate(update_fields):
			set_statements.append(field + ' = ' + update_values[i])

		cmd = 'UPDATE '  + table  + ' SET ' + ', '.join(set_statements) + ' WHERE (' + ' AND '.join(where_statements) + ')'

		self._run_command(cmd)


	def _run_select(self, cmd):
		cursor = self.connection.cursor()
		cursor.execute(cmd)

		result = []
		for elem in cursor:
			vals = []
			for i, value in enumerate(elem):
				if isinstance(value, datetime.datetime):
					vals.append("%2d/%02d/%4d" % (value.day, value.month, value.year))
				else:
					vals.append(str(value))
			result.append(vals)

		cursor.close()
		return result

	def getAllAniversarios(self, data_inicio, data_fim, gerente, casa_festa):
		data_inicio, data_fim, gerente, casa_festa = self._preprocess_values([data_inicio, data_fim, gerente, casa_festa])
		where_constraints = []
		where_constraints.append("(F.DATA BETWEEN" + data_inicio + " AND " + data_fim + ") ")
				
		if(gerente == "Todos"):
			where_constraints.append("AND F.CASA_FESTA = " + casa_festa + " ")
		elif(casa_festa == "Todas"):
			where_constraints.append("AND F.GERENTE = " + gerente + " ")
		else:
			where_constraints.append("AND F.GERENTE = " + gerente + " ")
			where_constraints.append("AND F.CASA_FESTA = " + casa_festa + " ")
		
		cmd = "SELECT F.CLIENTE, F.DATA, F.NUMERO_CONVIDADOS, F.PRECO, F.GERENTE, F.CASA_FESTA, A.NOME_ANIVERSARIANTE, A.TEMA, A.FAIXA_ETARIA, COUNT(GF.GARCOM)\
			FROM FESTA F JOIN ANIVERSARIO A ON A.CLIENTE = F.CLIENTE AND A.DATA = F.DATA\
			WHERE " + where_constraints + "\
			LEFT JOIN GARCOM_FESTA GF ON (GF.DATA = A.DATA AND GF.CLIENTE = A.CLIENTE)\
			GROUP BY(F.CLIENTE, F.DATA, F.NUMERO_CONVIDADOS, F.PRECO, F.GERENTE, F.CASA_FESTA, A.NOME_ANIVERSARIANTE, A.TEMA, A.FAIXA_ETARIA)"

		return self._run_select(cmd)

	def getGarconsFesta(self, cliente, data):
		cliente, data = self._preprocess_values([cliente, data])
		cmd = "SELECT FU.NOME, GF.GARCOM AS CPF, FU.COMISSAO FROM\
			FESTA F JOIN GARCOM_FESTA GF ON (F.CLIENTE = GF.CLIENTE AND F.DATA = GF.DATA)\
			AND (F.CLIENTE = " + cliente + " AND F.DATA = TO_DATE(" + data + ", 'DD/MM/YYYY'))\
			JOIN FUNCIONARIO FU ON FU.CPF = GF.GARCOM"

		return self._run_select(cmd)

	def getBarracasAniversario(self, cliente, data):
		cliente, data = self._preprocess_values([cliente, data])
		cmd = "SELECT B.NUMERO, FU.NOME, B.OPERADOR AS CPF, FU.COMISSAO FROM\
			FESTA F JOIN BARRACA_RASPADINHA B ON (F.CLIENTE = B.CLIENTE AND F.DATA = B.DATA)\
			AND (F.CLIENTE = " + cliente + " AND F.DATA = TO_DATE(" + data + ", 'DD/MM/YYYY'))\
			JOIN FUNCIONARIO FU ON FU.CPF = B.OPERADOR"

		return self._run_select(cmd)

	def getEnderecoFesta(self, cliente, data):
		cliente, data = self._preprocess_values([cliente, data])
		cmd = "SELECT E.RUA, E.NUMERO, E.CEP, E.CIDADE, E.ESTADO FROM\
		FESTA F JOIN CASA_FESTA CF ON (F.CASA_FESTA = CF.NOME)\
		AND (F.CLIENTE = " + cliente + " AND F.DATA = TO_DATE(" + data + ", 'DD/MM/YYYY'))\
		JOIN ENDERECO E ON E.ID = CF.ENDERECO"

		return self._run_select(cmd)

	def getGarconsLivres(self, data):
		data = self._preprocess_values([data])[0]
		cmd = "SELECT F.NOME, F.CPF, F.COMISSAO FROM FUNCIONARIO F WHERE UPPER(F.CARGO) = 'GARCOM' AND\
			F.CPF NOT IN(\
			SELECT GF.GARCOM FROM GARCOM_FESTA GF WHERE GF.DATA = TO_DATE(" + data + ", 'DD/MM/YYYY'))"

		return self._run_select(cmd)

	def getOperadoresLivres(self, data):
		data = self._preprocess_values([data])[0]
		cmd = "SELECT F.NOME, F.CPF, F.COMISSAO FROM FUNCIONARIO F WHERE UPPER(F.CARGO) = 'OPERADOR' AND\
			F.CPF NOT IN(\
			SELECT BR.OPERADOR FROM BARRACA_RASPADINHA BR WHERE BR.DATA = TO_DATE(" + data + ", 'DD/MM/YYYY'))"
		
		return self._run_select(cmd)

	def getGerentesLivres(self, data):
		data = self._preprocess_values([data])[0]
		cmd = "SELECT F.NOME, F.CPF, F.COMISSAO FROM FUNCIONARIO F WHERE UPPER(F.CARGO) = 'GERENTE' AND\
			F.CPF NOT IN(\
			SELECT FE.GERENTE FROM FESTA FE WHERE FE.DATA = TO_DATE(" + data + ", 'DD/MM/YYYY'))"
		
		return self._run_select(cmd)

	def getNomeCasasFesta(self):
		cmd = "SELECT NOME FROM CASA_FESTA"
		return self._run_select(cmd)

	def getAllGerentes(self):
		cmd = "SELECT F.CPF, F.NOME, F.TEL_MOVEL, F.TEL_FIXO, F.COMISSAO, FE.CASA_FESTA, MIN(FE.DATA) AS DATA_PROXIMA_FESTA\
			FROM FUNCIONARIO F LEFT JOIN FESTA FE ON FE.GERENTE = F.CPF WHERE UPPER(F.CARGO) = 'GERENTE'\
			GROUP BY(F.CPF, F.NOME, F.TEL_MOVEL, F.TEL_FIXO, F.COMISSAO, FE.CASA_FESTA)"
		return self._run_select(cmd)

	def getAllOperadores(self):
		cmd = "SELECT F.CPF, F.NOME, F.TEL_MOVEL, F.TEL_FIXO, F.COMISSAO, FE.CASA_FESTA, MIN(BR.DATA) AS DATA_PROXIMA_FESTA \
				FROM FUNCIONARIO F LEFT JOIN BARRACA_RASPADINHA BR ON BR.OPERADOR = F.CPF WHERE UPPER(F.CARGO) = 'OPERADOR'\
				JOIN FESTA FE ON BR.CLIENTE = FE.CLIENTE AND BR.DATA = FE.DATA\
				GROUP BY(F.CPF, F.NOME, F.TEL_MOVEL,  F.TEL_FIXO, F.COMISSAO, FE.CASA_FESTA)"
		return self._run_select(cmd)

	def getAllGarcons(self):
		cmd = "SELECT F.CPF, F.NOME, F.TEL_MOVEL, F.TEL_FIXO, F.COMISSAO, FE.CASA_FESTA, MIN(GF.DATA) AS DATA_PROXIMA_FESTA\
			FROM FUNCIONARIO F LEFT JOIN GARCOM_FESTA GF ON GF.GARCOM = F.CPF WHERE UPPER(F.CARGO) = 'GARCOM'\
			JOIN FESTA FE ON GF.CLIENTE = FE.CLIENTE AND GF.DATA = FE.DATA\
			GROUP BY(F.CPF, F.NOME, F.TEL_MOVEL,  F.TEL_FIXO, F.COMISSAO, FE.CASA_FESTA)"
		return self._run_select(cmd)

	def getBebidasInInterval(self, min_value, max_value):
		cmd = "SELECT B.NOME, B.VOLUME, B.QUANTIDADE, B.PRECO FROM BEBIDA B WHERE B.QUANTIDADE BETWEEN " + str(min_value) + " AND " + str(max_value)
		return self._run_select(cmd)

	def getAllFornecedores(self):
		cmd = "SELECT F.CNPJ, F.NOME, F.TELEFONE, D.BANCO, D.AGENCIA, D.CONTA, D.TIPO_CONTA FROM FORNECEDOR F JOIN DADOS_BANCARIOS D ON F.DADOS_BANCARIOS = D.ID"
		return self._run_select(cmd)

	def getAllClientes(self):
		cmd = "SELECT C.CPF, C.NOME, C.TEL_FIXO, C.TEL_MOVEL, D.BANCO, D.AGENCIA, D.CONTA, D.TIPO_CONTA, COUNT(*) AS NUMERO_FESTAS\
			FROM CLIENTE C JOIN DADOS_BANCARIOS D ON C.DADOS_BANCARIOS = D.ID\
			LEFT JOIN FESTA F ON C.CPF = F.CLIENTE\
			GROUP BY(C.CPF, C.NOME, C.TEL_FIXO, C.TEL_MOVEL, D.BANCO, D.AGENCIA, D.CONTA, D.TIPO_CONTA)"
		return self._run_select(cmd)

	def getAllCasasFesta(self):
		cmd = "SELECT CF.NOME, E.RUA, E.NUMERO, E.CIDADE, E.CEP, MIN(FE.DATA) AS DATA_PROXIMA_FESTA\
			FROM CASA_FESTA CF JOIN ENDERECO E ON CF.ENDERECO = E.ID\
			LEFT JOIN FESTA FE ON FE.CASA_FESTA = CF.NOME\
			GROUP BY(CF.NOME, E.RUA, E.NUMERO, E.CIDADE, E.CEP)\
		"
		return self._run_select(cmd)
