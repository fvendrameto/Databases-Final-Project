import cx_Oracle

class dbHelper():
	def __init__(self, ip, port, sid):
		self.dns_tns = cx_Oracle(ip, port, sid)
		
