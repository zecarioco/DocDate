-- Inserir cidades
INSERT INTO usuarios_cidade (nome, estado, pais) VALUES
('São Paulo', 'SP', 'Brasil'),
('Rio de Janeiro', 'RJ', 'Brasil'),
('Belo Horizonte', 'MG', 'Brasil'),
('Curitiba', 'PR', 'Brasil'),
('Porto Alegre', 'RS', 'Brasil'),
('Fortaleza', 'CE', 'Brasil'),
('Recife', 'PE', 'Brasil'),
('Salvador', 'BA', 'Brasil'),
('Brasília', 'DF', 'Brasil'),
('Manaus', 'AM', 'Brasil'),
('Belém', 'PA', 'Brasil'),
('Vitória', 'ES', 'Brasil'),
('Goiânia', 'GO', 'Brasil'),
('Florianópolis', 'SC', 'Brasil'),
('Campo Grande', 'MS', 'Brasil');

-- Inserir especialidades (evitar duplicação)
INSERT INTO medicos_especialidade (nome) 
SELECT 'Cardiologia' WHERE NOT EXISTS (SELECT 1 FROM medicos_especialidade WHERE nome = 'Cardiologia');
INSERT INTO medicos_especialidade (nome) 
SELECT 'Ortopedia' WHERE NOT EXISTS (SELECT 1 FROM medicos_especialidade WHERE nome = 'Ortopedia');
INSERT INTO medicos_especialidade (nome) 
SELECT 'Ginecologia' WHERE NOT EXISTS (SELECT 1 FROM medicos_especialidade WHERE nome = 'Ginecologia');
INSERT INTO medicos_especialidade (nome) 
SELECT 'Neurologia' WHERE NOT EXISTS (SELECT 1 FROM medicos_especialidade WHERE nome = 'Neurologia');
INSERT INTO medicos_especialidade (nome) 
SELECT 'Pediatria' WHERE NOT EXISTS (SELECT 1 FROM medicos_especialidade WHERE nome = 'Pediatria');
INSERT INTO medicos_especialidade (nome) 
SELECT 'Dermatologia' WHERE NOT EXISTS (SELECT 1 FROM medicos_especialidade WHERE nome = 'Dermatologia');
INSERT INTO medicos_especialidade (nome) 
SELECT 'Psiquiatria' WHERE NOT EXISTS (SELECT 1 FROM medicos_especialidade WHERE nome = 'Psiquiatria');
INSERT INTO medicos_especialidade (nome) 
SELECT 'Oftalmologia' WHERE NOT EXISTS (SELECT 1 FROM medicos_especialidade WHERE nome = 'Oftalmologia');
INSERT INTO medicos_especialidade (nome) 
SELECT 'Endocrinologia' WHERE NOT EXISTS (SELECT 1 FROM medicos_especialidade WHERE nome = 'Endocrinologia');
INSERT INTO medicos_especialidade (nome) 
SELECT 'Gastroenterologia' WHERE NOT EXISTS (SELECT 1 FROM medicos_especialidade WHERE nome = 'Gastroenterologia');
INSERT INTO medicos_especialidade (nome) 
SELECT 'Urologia' WHERE NOT EXISTS (SELECT 1 FROM medicos_especialidade WHERE nome = 'Urologia');
INSERT INTO medicos_especialidade (nome) 
SELECT 'Reumatologia' WHERE NOT EXISTS (SELECT 1 FROM medicos_especialidade WHERE nome = 'Reumatologia');
INSERT INTO medicos_especialidade (nome) 
SELECT 'Radiologia' WHERE NOT EXISTS (SELECT 1 FROM medicos_especialidade WHERE nome = 'Radiologia');
INSERT INTO medicos_especialidade (nome) 
SELECT 'Mastologia' WHERE NOT EXISTS (SELECT 1 FROM medicos_especialidade WHERE nome = 'Mastologia');
INSERT INTO medicos_especialidade (nome) 
SELECT 'Oncologia' WHERE NOT EXISTS (SELECT 1 FROM medicos_especialidade WHERE nome = 'Oncologia');

-- Inserir usuários com senha fictícia e outros campos preenchidos, incluindo is_active
INSERT INTO usuarios_usuario (username, first_name, last_name, email, password, tipo_usuario, cidade_id, is_superuser, is_staff, is_active) VALUES
('usuario1', 'João', 'Silva', 'joao.silva@mail.com', 'senha123', 'paciente', 1, false, false, true),
('usuario2', 'Maria', 'Oliveira', 'maria.oliveira@mail.com', 'senha123', 'paciente', 2, false, false, true),
('usuario3', 'Pedro', 'Santos', 'pedro.santos@mail.com', 'senha123', 'paciente', 3, false, false, true),
('usuario4', 'Ana', 'Costa', 'ana.costa@mail.com', 'senha123', 'paciente', 4, false, false, true),
('usuario5', 'Carlos', 'Lima', 'carlos.lima@mail.com', 'senha123', 'paciente', 5, false, false, true),
('medico1', 'Dr. André', 'Pereira', 'andre.pereira@mail.com', 'senha123', 'medico', 6, true, true, true),
('medico2', 'Dr. Fernanda', 'Alves', 'fernanda.alves@mail.com', 'senha123', 'medico', 7, true, true, true),
('medico3', 'Dr. Rodrigo', 'Silva', 'rodrigo.silva@mail.com', 'senha123', 'medico', 8, true, true, true),
('medico4', 'Dr. Camila', 'Lima', 'camila.lima@mail.com', 'senha123', 'medico', 9, true, true, true),
('medico5', 'Dr. Thiago', 'Souza', 'thiago.souza@mail.com', 'senha123', 'medico', 10, true, true, true),
('medico6', 'Dr. Lucas', 'Oliveira', 'lucas.oliveira@mail.com', 'senha123', 'medico', 11, true, true, true),
('medico7', 'Dr. Júlia', 'Rodrigues', 'julia.rodrigues@mail.com', 'senha123', 'medico', 12, true, true, true),
('medico8', 'Dr. Felipe', 'Martins', 'felipe.martins@mail.com', 'senha123', 'medico', 13, true, true, true),
('medico9', 'Dr. Rafaela', 'Silva', 'rafaela.silva@mail.com', 'senha123', 'medico', 14, true, true, true),
('medico10', 'Dr. Gustavo', 'Pereira', 'gustavo.pereira@mail.com', 'senha123', 'medico', 15, true, true, true);

-- Inserir médicos com relacionamento adequado aos usuários
-- Isso deve ser feito apenas depois que os usuários são inseridos
INSERT INTO usuarios_medico (usuario_id, crm, clinica) VALUES
(6, 'CRM123', 'Clínica ABC'),
(7, 'CRM124', 'Clínica XYZ'),
(8, 'CRM125', 'Clínica 123'),
(9, 'CRM126', 'Clínica Alpha'),
(10, 'CRM127', 'Clínica Beta');

-- Associar médicos às especialidades
INSERT INTO usuarios_medico_especialidades (medico_id, especialidade_id) VALUES
(6, 1), (6, 2), (7, 3), (7, 4), (8, 5), (8, 6), (9, 7), (9, 8), (10, 9), (10, 10);

-- Inserir pacientes com relacionamento adequado aos usuários
-- Garantir que não haja duplicação de usuario_id
INSERT INTO usuarios_paciente (usuario_id, data_nascimento, telefone) VALUES
(1, '1980-01-01', '11999999999'),
(2, '1985-02-14', '11888888888'),
(3, '1990-03-25', '11777777777'),
(4, '1995-04-30', '11666666666'),
(5, '2000-05-20', '11555555555');