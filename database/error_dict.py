
errors = {'PK_ENDERECO' : 'ID conflitante',
	'UQ_ENDERECO' : 'Endereço já cadastrado',
	'CK_ENDERECO_CEP' : 'CEP inválido. Deve ser no formato XXXXX-XXX',
	
	'PK_DADOS_BANCARIOS' : 'ID conflitante',
	'UQ_DADOS_BANCARIOS' : 'Dados bancários já cadastrados',
	'CK_TIPO_CONTA' : 'Tipo da conta deve ser CC ou CP',
	
	'PK_FORNECEDOR' : 'CNPJ já cadastrado',
	'FK_FORNECEDOR' : 'Dados bancários não encontrados',
	'CK_FORNECEDOR_CNPJ' : 'CNPJ inválido. Deve ser no formato XX.XXX.XXX/XXXX-XX',
	'CK_FORNECEDOR_TELEFONE' : 'Telefone inválido. Deve ser no formato (XX)XXXX-XXXX',
	
	'PK_FUNCIONARIO' : 'CPF de funcionário já cadastrado'
	'CK_FUNCIONARIO_CPF' : 'CPF inválido. Deve ser no formato XXX.XXX.XXX-XX',
	'CK_FUNCIONARIO_CARGO' : 'Cargo deve ser GARCOM, GERENTE, BARTENDER ou OPERADOR',
	'CK_FUNCIONARIO_TEL_MOVEL' : 'Telefone móvel inválido. Deve ser no formato (XX)9XXXX-XXXX',
	'CK_FUNCIONARIO_TEL_FIXO' : 'Telefone fixo inválido. Deve ser no formato (XX)XXXX-XXXX',

	'PK_CLIENTE' : 'CPF de cliente já cadastrado',
	'FK1_CLIENTE' : 'Dados bancários não encontrados',
	'FK2_CLIENTE' : 'Endereço não encontrado',
	'CK_CLIENTE_CPF' : 'CPF inválido. Deve ser no formato XXX.XXX.XXX-XX',
	'CK_CLIENTE_TEL_FIXO' : 'Telefone fixo inválido. Deve ser no formato (XX)XXXX-XXXX',
	'CK_CLIENTE_TEL_MOVEL' : 'Telefone móvel inválido. Deve ser no formato (XX)9XXXX-XXXX',
	
	'PK_CASA_FESTA' : 'Casa de festa com esse nome já cadastrada',
	'FK_CASA_FESTA' : 'Endereço não encontrado',
	
	'PK_FESTA' : 'Festa já cadastrada',
	'FK1_FESTA' : 'Cliente não encontrado',
	'FK2_FESTA' : 'Casa de Festa não encontrada',
	'FK3_FESTA' : 'Gerente não encontrado',
	'CK_FESTA_TIPO' : 'Tipo deve ser A ou C',
	
	'PK_ANIVERSARIO' : 'Festa de aniversário já cadastrada',
	'FK_ANIVERSARIO' : 'Festa não encontrada',
	'CK_FAIXA_ETARIA' : 'Faixa etária deve ser 0-3, 4-7, 8-13 ou 14+',
	
	'PK_BARRACA_RASPADINHA' : 'Barraca de Raspadinha já cadastrada',
	'UQ_BARRACA_RASPADINHA' : 'Barraca de Raspadinha já cadastrada',
	'FK1_BARRACA_RASPADINHA' : 'Festa não encontrada',
	'FK2_BARRACA_RASPADINHA' : 'Operador não encontrado',
	
	'PK_GARCOM_FESTA' : 'Garçom já adicionado a festa',
	'FK1_GARCOM_FESTA' : 'Festa não encontrada',
	'FK2_GARCOM_FESTA' : 'Garçom não encontrado',
	
	'PK_BEBIDA' : 'Bebida já existe',
	'CK_BEBIDA' : 'Bebida bandeja deve ser S ou N',
	
	'PK_BEBIDA_BANDEJA_FESTA' : 'Bebida já adicionada a festa',
	'FK1_BEBIDA_BANDEJA_FESTA' : 'Festa não encontrada',
	'FK2_BEBIDA_BANDEJA_FESTA' : 'Bebida não encontrada',
}
