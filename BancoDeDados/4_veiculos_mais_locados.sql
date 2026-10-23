-- CONSULTA PARA VEICULOS MAIS LOCADOS
SELECT 
    v.modelo,
    v.marca,
    COUNT(lv.idLocacao) AS NUMERO_LOCACOES
FROM 
    Veiculo v
LEFT JOIN 
    LocacaoVeiculo lv ON v.idVeiculo = lv.idVeiculo
GROUP BY 
    v.idVeiculo
ORDER BY 
    NUMERO_LOCACOES DESC;