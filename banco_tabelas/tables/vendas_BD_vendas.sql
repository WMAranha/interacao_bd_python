-- Vendas (idvenda, idproduto, idvendedor, valorTotal, comissão) --

use vendas;
#drop tables vendas;
#truncate table vendas;

create table vendas (
idvenda integer auto_increment,
idproduto integer not null,
idvendedor integer not null,
valorTotal numeric (10,2),
comissao numeric (10,2),
constraint pk_idvenda primary key (idvenda),
constraint fk_produto_vendas foreign key (idproduto) references produto (idproduto),
constraint fk_vendedor_vendas foreign key (idvendedor) references vendedor (idvendedor)
);

select * from vendas;

# Realiza os 50 cadastros dentro da tabela vendas e retorna quais foram essas 50 inserções.
INSERT INTO vendas (idproduto, idvendedor, valorTotal, comissao) VALUES {};

# Retorna a soma do valores de todas as vendas registradas.
SELECT sum(valorTotal) FROM vendas;

# Retorna o funcionário que realizou a venda de maior valor e o valor dessa mesma venda.
SELECT v.nome_vendedor, x.valorTotal FROM vendedor v, vendas x WHERE v.idvendedor = x.idvendedor 
AND x.idvendedor = (SELECT idvendedor FROM vendas WHERE valorTotal = (SELECT max(valorTotal) FROM vendas))ORDER BY x.valorTotal DESC;

# Retorna 1 ou mais funcionários que realizaram a maior quantidade de vendas e mostra essa quantidade.
SELECT v.nome_vendedor, count(x.idvenda) FROM vendedor v, vendas x WHERE v.idvendedor = x.idvendedor 
GROUP BY v.nome_vendedor ORDER BY count(x.idvenda) DESC;

# Retorna 1 ou mais fornecedores que foram mais utilizados e quantas vezes foram utilizados.
SELECT f.nome_fornecedor, count(f.idfornecedor) FROM fornecedores f WHERE f.idfornecedor IN (SELECT idfornecedor from produto where idproduto 
IN (SELECT idproduto from vendas)) GROUP BY f.nome_fornecedor ORDER BY  count(f.idfornecedor) DESC;

# Retorna o valor da comissão para cada vendedor.
SELECT v.nome_vendedor, sum(x.comissao) FROM vendedor v, vendas x WHERE v.idvendedor = x.idvendedor group by v.nome_vendedor ORDER BY sum(x.comissao);












