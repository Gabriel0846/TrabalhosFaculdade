-- CONSULTA PARA CLIENTES COM PAGAMENTOS PENDENTES
SELECT 
    c.nome,
    p.valorTotal AS VALOR_DEVIDO
FROM 
    Cliente c
JOIN 
    Locacao l ON c.idCliente = l.idCliente
JOIN 
    Pagamento p ON l.idPagamento = p.idPagamento
WHERE 
    p.estado = 'PENDENTE'
ORDER BY 
    c.nome ASC;