from modules.functions import functions

class requests:

    def finish_search():
        try:
            print("\nConsulta finalizada!!!")

        except Exception as e:
            print(str(e))

    
    def registration_50():
        try:
            lista_vendas50 = functions.generator()
            print("\nCADASTRO DAS ÚLTIMAS 50 VENDAS")
            for i in lista_vendas50:
                query = "INSERT INTO vendas (idproduto, idvendedor, valorTotal, comissao) VALUES {} ;".format(i)
                functions.do_it(query)
            querytab = "SELECT * FROM vendas"
            resultvendas = functions.search_it(querytab)
            print(resultvendas)

        except Exception as e:
            print(str(e))

    def total_sales():
        try:
            query = "SELECT sum(valorTotal) FROM vendas; "
            totalVendas = functions.search_it(query)
    
            print(f"\nTotal de vendas é: US$ {totalVendas[0][0]}\n")
        except Exception as e:
            print(str(e))

    def employee_biggest_sales():
        try:
            query = "SELECT v.nome_vendedor, x.valorTotal FROM vendedor v, vendas x WHERE v.idvendedor = x.idvendedor AND x.idvendedor = (SELECT idvendedor FROM vendas WHERE valorTotal = (SELECT max(valorTotal) FROM vendas))ORDER BY x.valorTotal DESC;"
            vendedorMax = functions.search_it(query)
            print(f"\nO funcionário com a venda de maior valor é {vendedorMax[0][0]} e o valor é US$ {vendedorMax[0][1]}.\n")
        except Exception as e:
            print(str(e))

    def sellers_sales_amount():
        try:
            query = "SELECT v.nome_vendedor, count(x.idvenda) FROM vendedor v, vendas x WHERE v.idvendedor = x.idvendedor GROUP BY v.nome_vendedor ORDER BY count(x.idvenda) DESC;"
            vendedorQuant = functions.search_it(query)
            melhores_vendedores = []
            vendas_feitas = []
            for i in range(len(vendedorQuant)):
                vendas_feitas.append(vendedorQuant[i][1])
            for venda in vendas_feitas:
                if venda == max(vendas_feitas):
                    indice = vendas_feitas.index(venda)
                    melhores_vendedores.append(vendedorQuant[indice])
                    vendedorQuant.remove(vendedorQuant[indice])

            print("\nOs funcionários com maior quantidade de vendas foram:\n")
            for best in melhores_vendedores:
                print (f"O funcionário(a) {best[0]} e fez {best[1]} vendas.\n")

        except Exception as e:
            print(str(e))

    def most_used_suppliers():
        try:
            query = "SELECT f.nome_fornecedor, count(f.idfornecedor) FROM fornecedores f WHERE f.idfornecedor IN (SELECT idfornecedor from produto where idproduto IN (SELECT idproduto from vendas)) GROUP BY f.nome_fornecedor ORDER BY  count(f.idfornecedor) DESC;"
            fornecedorQuant = functions.search_it(query)
            melhores_fornecedores=[]
            quantidade = []
            for i in range(len(fornecedorQuant)):
                quantidade.append(fornecedorQuant[i][1])
            for quant in quantidade:
                if quant == max(quantidade):
                    indice = quantidade.index(quant)
                    melhores_fornecedores.append(fornecedorQuant[indice])
                    fornecedorQuant.remove(fornecedorQuant[indice])

            print("\nOs fornecedores mais usados foram:\n")
            for bestfornecedor in melhores_fornecedores:
                print(f"O fornecedor {bestfornecedor[0]} foi utilizado {bestfornecedor[1]}.\n")
        except Exception as e:
            print(str(e))
    
    def sellers_commission():

        try:
            query = "SELECT v.nome_vendedor, sum(x.comissao) FROM vendedor v, vendas x WHERE v.idvendedor = x.idvendedor group by v.nome_vendedor ORDER BY sum(x.comissao);"
            comissao = functions.search_it(query)

            for onecomissao in comissao:
                print(f"\nO funcionário {onecomissao[0]} recebeu US$ {onecomissao[1]} de comissão.")

        except Exception as e:
            print(str(e))

    
