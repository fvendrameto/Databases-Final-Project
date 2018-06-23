# -*- coding: utf-8 -*-

import cx_Oracle
import datetime

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
				values[i] = "'" + value + "'"
			elif isinstance(value, int):
				values[i] = str(value)
			elif isinstance(value, datetime.datetime):
				values[i] = "%2d/%02d/%4d" % (value.day, value.month, value.year)
		return values

	def _run_command(self, cmd):
		cursor = self.connection.cursor()
		cursor.execute(cmd)
		self.connection.commit()
		cursor.close()

	def insert(self, table, fields, values):
		values = self._preprocess_values(values)				
		cmd = 'INSERT INTO ' + table + ' (' + ', '.join(fields) + ') VALUES ( ' + ', '.join(values) + ') '

		self._run_command(cmd)

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


	