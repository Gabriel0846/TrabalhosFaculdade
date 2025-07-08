-- CRIAÇÃO DO BANCO DE DADOS
CREATE DATABASE LocadoraVeiculos;
USE LocadoraVeiculos;

-- TABELA CLIENTE
CREATE TABLE Cliente (
    idCliente INT NOT NULL AUTO_INCREMENT,
    CPF VARCHAR(20) NOT NULL,
    nome VARCHAR(50) NOT NULL,
    telefone VARCHAR(20) NOT NULL,
    email VARCHAR(50) NOT NULL,
    endereco VARCHAR(100) NOT NULL,
    PRIMARY KEY (idCliente),
    UNIQUE (CPF)
);

-- TABELA VEICULO
CREATE TABLE Veiculo (
    idVeiculo INT NOT NULL AUTO_INCREMENT,
    modelo VARCHAR(50) NOT NULL,
    marca VARCHAR(50) NOT NULL,
    ano INT NOT NULL,
    placa VARCHAR(10) NOT NULL,
    valorDiaria DECIMAL(7,2) NOT NULL,
    estado ENUM('DISPONIVEL', 'ALUGADO', 'MANUTENCAO') NOT NULL,
    PRIMARY KEY (idVeiculo),
    UNIQUE (placa)
);

-- TABELA PAGAMENTO
CREATE TABLE Pagamento (
    idPagamento INT NOT NULL AUTO_INCREMENT,
    forma ENUM('CARTAO', 'PIX', 'DINHEIRO') NOT NULL,
    dataPagamento DATE NOT NULL,
    valorTotal DECIMAL(7,2) NOT NULL,
    estado ENUM('PAGO', 'PENDENTE') NOT NULL,
    PRIMARY KEY (idPagamento)
);

-- TABELA LOCACAO
CREATE TABLE Locacao (
    idLocacao INT NOT NULL AUTO_INCREMENT,
    idCliente INT NOT NULL,
    idPagamento INT NOT NULL,
    dataInicio DATE NOT NULL,
    dataFim DATE NOT NULL,
    PRIMARY KEY (idLocacao),
    FOREIGN KEY (idCliente) REFERENCES Cliente(idCliente),
    FOREIGN KEY (idPagamento) REFERENCES Pagamento(idPagamento)
);

-- TABELA LOCACAOVEICULO
CREATE TABLE LocacaoVeiculo (
    idLocacao INT NOT NULL,
    idVeiculo INT NOT NULL,
    PRIMARY KEY (idLocacao, idVeiculo),
    FOREIGN KEY (idLocacao) REFERENCES Locacao(idLocacao),
    FOREIGN KEY (idVeiculo) REFERENCES Veiculo(idVeiculo)
);

-- TABELA MANUTENCAO
CREATE TABLE Manutencao (
    idManutencao INT NOT NULL AUTO_INCREMENT,
    idVeiculo INT NOT NULL,
    descricao VARCHAR(100) NOT NULL,
    dataManutencao DATE NOT NULL,
    custo DECIMAL(7,2) NOT NULL,
    PRIMARY KEY (idManutencao),
    FOREIGN KEY (idVeiculo) REFERENCES Veiculo(idVeiculo)
);