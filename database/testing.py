from dbHelper import dbHelper

a = dbHelper('grad.icmc.usp.br', 15215, 'orcl', 'G9763193', '9763193')

# print(a.insertIntoEndereco([1011, 'aaa', 'aaa', 'SP', 121, '1860-000']))
# print(a.insertIntoEndereco([101, 'Rua Marciano Magalhaes', 'Petropolis', 'RJ', 1065, '25630-021']))

# a.insert('BEBIDAS_DRINK', ['DRINK', 'BEBIDA', 'VOLUME', 'QUANTIDADE'], ['Jack n Coke', 'Coca-Cola', 2000, 1])
# a.delete('BEBIDAS_DRINK', ['DRINK', 'BEBIDA'], ['Jack n Coke', 'Coca-Cola'])
# a.update('BEBIDAS_DRINK', ['DRINK', 'BEBIDA'], ['Jack n Coke', 'Coca-Cola'], ['DRINK', 'VOLUME', 'BEBIDA'], ['Caipirinha', 1000, 'Rum'])

# a.getAllAniversarios()
# a.getGarconsFesta('165.928.307-86','23/09/2018')
# a.getBarracasAniversario('165.928.307-86','23/09/2018')
# a.getEnderecoFesta('165.928.307-86','23/09/2018')
# a.getGarconsLivres('23/09/2018')
# a.getOperadoresLivres('23/09/2018')
# a.getGerentesLivres('23/09/2018')
# a.getAllCasasFesta()
# a.getAllGerentes()
# a.getAllOperadores()
# a.getAllGarcons()
# a.getBebidasInInterval(0,1000)
# a.getAllFornecedores()
# a.getAllClientes()
