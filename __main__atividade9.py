
from modules.requests import requests

if __name__ == "__main__":

    try:

        while True:
            print ("O que você deseja fazer?:\n")
            x = input("[1] - Cadastrar as últimas 50 vendas\n""[2] - Total de vendas\n""[3] - Funcionário com a venda de maior valor e o valor:\n"
            "[4] - Funcionário com maior quantidade de vendas e quantidade:\n""[5] - Fornecedor mais utilizado:\n""[6] - Total de comissão devido para cada funcionário (8'%'de comissão):\n"
            "[0] - Encerrar pesquisa\n""INFORME: ")

            if x == "0":# Finaliza o funcionamento do programa.
                requests.finish_search()
                break

            elif x == "1":# Realiza os 50 cadastros dentro da tabela vendas e retorna quais foram essas 50 inserções.
                requests.registration_50()


            elif x == "2":# Retorna a soma do valores de todas as vendas registradas.
                requests.total_sales()
           

            elif x == "3":# Retorna o funcionário que realizou a venda de maior valor e o valor dessa mesma venda.
                requests.employee_biggest_sales()


            elif x == "4":# Retorna 1 ou mais funcionários que realizaram a maior quantidade de vendas e mostra essa quantidade.
                requests.sellers_sales_amount()


            elif x == "5":# Retorna 1 ou mais fornecedores que foram mais utilizados e quantas vezes foram utilizados.
                requests.most_used_suppliers()


            elif x == "6":# Retorna o valor da comissão para cada vendedor.
                requests.sellers_commission()


            else:# Caso o usuário não insira um valor correspondente do MENU, irá ser mostrado uma mensagem de erro 
                # solicitando um novo valor para a busca.
                print("\nERRO: Digite um dos valores presentes no MENU!\n")

    except Exception as e:
        print(str(e))

