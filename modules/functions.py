
import mysql.connector
import random # Importa o Modulo Random para gerar números Pseudo-aleatórios


class functions:

    def do_it(query):#INSERT. UPDATE. DELETE
        try:
            con = mysql.connector.connect(user='root', password='gw64709499', host='127.0.0.1', database='vendas')
            cursor = con.cursor()
            cursor.execute(query)
            cursor.close()
            con.commit()
            con.close()
        except Exception as e:
            print(e)

    def search_it(query):#SELECT
        try:
            con = mysql.connector.connect(user='root', password='gw64709499', host='127.0.0.1', database='vendas')
            cursor = con.cursor()
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            con.close()

    def generator():

        # (idvenda, idproduto, idvendedor, valorTotal, comissão)

        vendas =[] # Criando a lista vazia, ela vai receber todas as entradas geradas
        for i in range(50): # Laço que vai repetir 50 vezes automaticamente para gerar as 50 vendas. (essa quantidade pode ser alterada se você precisar)
            venda = [] #Lista que vai receber individualmente cada entrada a ser salva em vendas. (essa entrada será apagada a cada repetição)
            idproduto = random.randrange(1,2001) # Vai escolher um produto aleatório entres os 2000 cadastrados
            idvendedor = random.randrange(1, 1001) # Vai escolher um vendedor aleatorio entre os 1000 cadastrados
            valorTotal = float(random.randrange(100, 30001)/100) # Vai gerar um valor de venda entre R$1,00 e R$300,00
            comissao = round(valorTotal * 0.08, 2) # Calcula a comissão baseado no valor de venda, OBS: A função Round é para arrendondar para 2 casas decimais.
            
            venda.append(idproduto) # o comando venda.append() vai salvar dentro da lista venda as informações dentro do parenteses.
            venda.append(idvendedor)
            venda.append(valorTotal)
            venda.append(comissao)

            vendas.append(venda) # Salvando as informações da lista venda, em vendas.

        venda_insert = [] # Lista final que vai receber todas os dados das vendas prontos para o insert.

        for venda in vendas: # O laço vai percorrer cada venda da lista transformando ela em uma TUPLA, para ficar no formato correto do insert
            venda_pronta = tuple(venda) # convertendo cada venda de vendas em uma tupla
            venda_insert.append(venda_pronta) #Salvando tudo em ordem na lista vendas_insert

        return venda_insert # Vai retornar no terminal a lista de vendas pronta para ser levada pro código da query de insert.