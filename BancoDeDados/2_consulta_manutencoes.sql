-- CONSULTA PARA LISTAR MANUTENCOES
SELECT 
    v.modelo,
    v.marca,
    m.descricao,
    m.dataManutencao,
    m.custo
FROM 
    Manutencao m
JOIN 
    Veiculo v ON m.idVeiculo = v.idVeiculo
ORDER BY 
    m.dataManutencao DESC;