-- Inserir Cidades
INSERT INTO usuarios_cidade (nome, estado, pais) VALUES
('São Paulo', 'São Paulo', 'Brasil'),
('Rio de Janeiro', 'Rio de Janeiro', 'Brasil'),
('Belo Horizonte', 'Minas Gerais', 'Brasil'),
('Curitiba', 'Paraná', 'Brasil'),
('Porto Alegre', 'Rio Grande do Sul', 'Brasil'),
('Salvador', 'Bahia', 'Brasil'),
('Fortaleza', 'Ceará', 'Brasil'),
('Recife', 'Pernambuco', 'Brasil'),
('Brasília', 'Distrito Federal', 'Brasil'),
('Manaus', 'Amazonas', 'Brasil'),
('Natal', 'Rio Grande do Norte', 'Brasil'),
('Vitória', 'Espírito Santo', 'Brasil'),
('Goiânia', 'Goiás', 'Brasil'),
('São Luís', 'Maranhão', 'Brasil'),
('Maceió', 'Alagoas', 'Brasil');

-- Inserir Especialidades
INSERT INTO medicos_especialidade (nome) VALUES
('Cardiologia'),
('Dermatologia'),
('Pediatria'),
('Neurologia'),
('Ortopedia'),
('Oftalmologia'),
('Ginecologia'),
('Endocrinologia'),
('Psiquiatria'),
('Urologia'),
('Reumatologia'),
('Pneumologia'),
('Otorrinolaringologia'),
('Radiologia'),
('Cirurgia Geral');

-- Inserir Usuários (Pacientes e Médicos)
-- Pacientes
INSERT INTO usuarios_usuario (username, email, password, tipo_usuario, cidade_id) VALUES
('joao_paciente', 'joao@example.com', 'hashed_password', 'paciente', 1),
('maria_paciente', 'maria@example.com', 'hashed_password', 'paciente', 2),
('ana_paciente', 'ana@example.com', 'hashed_password', 'paciente', 3),
('luan_paciente', 'luan@example.com', 'hashed_password', 'paciente', 4),
('paula_paciente', 'paula@example.com', 'hashed_password', 'paciente', 5),
('ricardo_paciente', 'ricardo@example.com', 'hashed_password', 'paciente', 6),
('juliana_paciente', 'juliana@example.com', 'hashed_password', 'paciente', 7),
('felipe_paciente', 'felipe@example.com', 'hashed_password', 'paciente', 8),
('gabriela_paciente', 'gabriela@example.com', 'hashed_password', 'paciente', 9),
('roberto_paciente', 'roberto@example.com', 'hashed_password', 'paciente', 10),
('beatriz_paciente', 'beatriz@example.com', 'hashed_password', 'paciente', 11),
('lucas_paciente', 'lucas@example.com', 'hashed_password', 'paciente', 12),
('carla_paciente', 'carla@example.com', 'hashed_password', 'paciente', 13),
('renata_paciente', 'renata@example.com', 'hashed_password', 'paciente', 14),
('gustavo_paciente', 'gustavo@example.com', 'hashed_password', 'paciente', 15);

-- Médicos
INSERT INTO usuarios_usuario (username, email, password, tipo_usuario, cidade_id) VALUES
('dr_carlos', 'carlos@example.com', 'hashed_password', 'medico', 1),
('dr_ana', 'ana@example.com', 'hashed_password', 'medico', 2),
('dr_jose', 'jose@example.com', 'hashed_password', 'medico', 3),
('dr_lucas', 'lucas@example.com', 'hashed_password', 'medico', 4),
('dr_paulo', 'paulo@example.com', 'hashed_password', 'medico', 5),
('dr_renata', 'renata@example.com', 'hashed_password', 'medico', 6),
('dr_felipe', 'felipe@example.com', 'hashed_password', 'medico', 7),
('dr_ana_clara', 'anaclara@example.com', 'hashed_password', 'medico', 8),
('dr_roberto', 'roberto@example.com', 'hashed_password', 'medico', 9),
('dr_pedro', 'pedro@example.com', 'hashed_password', 'medico', 10),
('dr_maria', 'maria@example.com', 'hashed_password', 'medico', 11),
('dr_juliana', 'juliana@example.com', 'hashed_password', 'medico', 12),
('dr_gustavo', 'gustavo@example.com', 'hashed_password', 'medico', 13),
('dr_carla', 'carla@example.com', 'hashed_password', 'medico', 14),
('dr_ricardo', 'ricardo@example.com', 'hashed_password', 'medico', 15);

-- Inserir Pacientes
INSERT INTO usuarios_paciente (usuario_id, data_nascimento, telefone) VALUES
(1, '1985-03-25', '11987654321'),
(2, '1992-07-14', '21987654321'),
(3, '1980-02-10', '31987654321'),
(4, '1995-05-18', '41987654321'),
(5, '1987-11-12', '51987654321'),
(6, '1990-06-22', '61987654321'),
(7, '1988-09-05', '71987654321'),
(8, '1991-03-28', '81987654321'),
(9, '1983-10-15', '91987654321'),
(10, '1994-01-09', '02987654321'),
(11, '1982-08-20', '12987654321'),
(12, '1989-04-13', '22987654321'),
(13, '1993-12-01', '32987654321'),
(14, '1986-07-07', '42987654321'),
(15, '1992-11-28', '52987654321');

-- Inserir Médicos
INSERT INTO usuarios_medico (usuario_id, crm, clinica) VALUES
(16, '123456-SP', 'Clínica da Saúde'),
(17, '654321-RJ', 'Clínica Ana'),
(18, '234567-MG', 'Clínica Belo Horizonte'),
(19, '345678-PR', 'Clínica Curitiba'),
(20, '456789-RS', 'Clínica Porto Alegre'),
(21, '567890-BA', 'Clínica Salvador'),
(22, '678901-CE', 'Clínica Fortaleza'),
(23, '789012-PE', 'Clínica Recife'),
(24, '890123-DF', 'Clínica Brasília'),
(25, '901234-AM', 'Clínica Manaus'),
(26, '012345-RN', 'Clínica Natal'),
(27, '123457-ES', 'Clínica Vitória'),
(28, '234567-GO', 'Clínica Goiânia'),
(29, '345678-MA', 'Clínica São Luís'),
(30, '456789-AL', 'Clínica Maceió');

-- Associar Médicos com Especialidades
INSERT INTO usuarios_medico_especialidades (medico_id, especialidade_id) VALUES
(16, 1), (16, 2), (16, 3), -- Dr. Carlos
(17, 1), (17, 4), (17, 5), -- Dr. Ana
(18, 2), (18, 6), (18, 3), -- Dr. José
(19, 7), (19, 8), (19, 9), -- Dr. Lucas
(20, 10), (20, 11), (20, 12), -- Dr. Paulo
(21, 13), (21, 14), (21, 15), -- Dr. Renata
(22, 1), (22, 9), (22, 5), -- Dr. Felipe
(23, 2), (23, 3), (23, 12), -- Dr. Ana Clara
(24, 1), (24, 6), (24, 4), -- Dr. Roberto
(25, 10), (25, 11), (25, 13), -- Dr. Pedro
(26, 14), (26, 15), (26, 8), -- Dr. Maria
(27, 7), (27, 9), (27, 5), -- Dr. Juliana
(28, 2), (28, 4), (28, 3), -- Dr. Gustavo
(29, 12), (29, 11), (29, 10), -- Dr. Carla
(30, 6), (30, 13), (30, 8); -- Dr. Ricardo