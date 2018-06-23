from dbHelper import dbHelper

a = dbHelper('grad.icmc.usp.br', 15215, 'orcl', 'G9763193', '9763193')

# a.insert('BEBIDAS_DRINK', ['DRINK', 'BEBIDA', 'VOLUME', 'QUANTIDADE'], ['Jack n Coke', 'Coca-Cola', 2000, 1])
# a.delete('BEBIDAS_DRINK', ['DRINK', 'BEBIDA'], ['Jack n Coke', 'Coca-Cola'])
a.update('BEBIDAS_DRINK', ['DRINK', 'BEBIDA'], ['Jack n Coke', 'Coca-Cola'], ['DRINK', 'VOLUME', 'BEBIDA'], ['Caipirinha', 1000, 'Rum'])
