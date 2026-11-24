<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Portal do Educador - Alfabeta</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..900;1,400..900&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Inder&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/static/css/portal.css">
</head>
<body>

    <header>
        <div class="logo">
            <img src="/static/assets/imagens/logo alfabeta.png" alt="logo alfabeta">
        </div>
        <div class="user-nav">
            <div class="user-badge">
                <div class="avatar">👨‍🏫</div>
                <span>Olá, <b>{{ professor.nome }}</b></span>
            </div>
            <a href="/sair" class="btn-sair">
                <span>🚪 Sair</span>
            </a>
        </div>
    </header>

    <div class="banner-portal">
        <img src="/static/assets/imagens/Gemini_Generated_Image_n6afk8n6afk8n6af 1.png" alt="banner">
        <div class="banner-text">
            <h1>Portal do Educador - Estimar Salário</h1>
        </div>
    </div>

    <div class="dashboard-container">
        
        <!-- Menu Lateral -->
        <aside class="sidebar">
            <a href="/portal?aba=adicionar" class="sidebar-btn {{ 'active' if aba == 'adicionar' else '' }}">
                <span>👤+</span>
                <span>Adicionar aluno</span>
            </a>
            <a href="/portal?aba=salario" class="sidebar-btn {{ 'active' if aba == 'salario' else '' }}">
                <span>💳</span>
                <span>Salário desse mês</span>
            </a>
            <a href="/portal?aba=alterar" class="sidebar-btn {{ 'active' if aba == 'alterar' else '' }}">
                <span>✏️</span>
                <span>Alterar aluno</span>
            </a>
            <a href="/portal?aba=excluir" class="sidebar-btn {{ 'active' if aba == 'excluir' else '' }}">
                <span>🗑️</span>
                <span>Excluir aluno</span>
            </a>
            <a href="/portal?aba=historico" class="sidebar-btn {{ 'active' if aba == 'historico' else '' }}">
                <span>🕒</span>
                <span>Histórico de aulas</span>
            </a>
            <a href="/portal?aba=fim_do_mes" class="sidebar-btn {{ 'active' if aba == 'fim_do_mes' else '' }}">
                <span>⏱️</span>
                <span>Fim do mês</span>
            </a>
            <a href="/portal?aba=perfil" class="sidebar-btn {{ 'active' if aba == 'perfil' else '' }}">
                <span>👨‍🏫</span>
                <span>Minha conta</span>
            </a>
        </aside>

        <!-- Conteúdo Principal -->
        <main class="main-content">

            % if defined('mensagem') and mensagem:
                <div class="alert-success">{{ mensagem }}</div>
            % end

            % if defined('erro') and erro:
                <div class="alert-error">{{ erro }}</div>
            % end

            <!-- 1. ABA ADICIONAR ALUNO (CONFORME SUA IMAGEM) -->
            % if aba == 'adicionar':
                <h2 class="content-title">Adicionar Novo Aluno</h2>
                <div class="form-card">
                    <form action="/portal/adicionar" method="POST">
                        <div class="form-group">
                            <label for="nome_aluno">Nome do Aluno:</label>
                            <input type="text" id="nome_aluno" name="nome_aluno" required placeholder="Digite o nome completo do aluno">
                        </div>

                        <div class="form-group">
                            <label for="opcao_tipo">Tipo de Aluno:</label>
                            <select id="opcao_tipo" name="opcao_tipo" required>
                                <option value="" disabled selected>Selecione o tipo de aluno</option>
                                <option value="1">1) Aluno de ensino fundamental coletivo (R$ 9,92)</option>
                                <option value="2">2) Aluno de fundamental individual (R$ 16,54)</option>
                                <option value="3">3) Aluno de ensino médio coletivo (R$ 16,54)</option>
                                <option value="4">4) Aluno de ensino médio individual (R$ 19,85)</option>
                                <option value="5">5) aula no fim de semana (R$ 37,50)</option>
                            </select>
                        </div>

                        <div class="form-group">
                            <label for="data_aula">Data da aula dada:</label>
                            <input type="date" id="data_aula" name="data_aula" required>
                        </div>

                        <button type="submit" class="btn-salvar">Salvar</button>
                    </form>
                </div>

            <!-- 2. ABA SALÁRIO DESSE MÊS -->
            % elif aba == 'salario':
                <h2 class="content-title">Salário desse mês</h2>
                <div class="form-card">
                    <form action="/portal/salario" method="POST">
                        <div class="form-group">
                            <label style="font-weight: 600; margin-bottom: 8px;">O usuário tem vale-transporte (R$ 11,00 por dia de aula)?</label>
                            <div style="display: flex; gap: 30px; margin-top: 10px; font-size: 1.05rem;">
                                <label style="display: flex; align-items: center; gap: 8px; cursor: pointer;">
                                    <input type="radio" name="tem_vt" value="sim" onchange="this.form.submit()" {{ 'checked' if (not defined('tem_vt') or tem_vt == 'sim') else '' }} style="width: 20px; height: 20px; accent-color: #00B359;">
                                    <span><b>Sim</b> (R$ 11,00 / dia trabalhado)</span>
                                </label>
                                <label style="display: flex; align-items: center; gap: 8px; cursor: pointer;">
                                    <input type="radio" name="tem_vt" value="nao" onchange="this.form.submit()" {{ 'checked' if (defined('tem_vt') and tem_vt == 'nao') else '' }} style="width: 20px; height: 20px; accent-color: #00B359;">
                                    <span><b>Não</b> (Sem vale-transporte)</span>
                                </label>
                            </div>
                        </div>
                        <button type="submit" class="btn-salvar">Recalcular Salário</button>
                    </form>

                    % if defined('resumo') and resumo:
                        % optou_sim = (defined('tem_vt') and tem_vt == 'sim') or (not defined('tem_vt'))
                        <div class="salario-grid">
                            <div class="salario-card">
                                <div>Total das Aulas</div>
                                <div class="valor">R$ {{ f"{resumo.total_aulas:.2f}".replace('.', ',') }}</div>
                            </div>
                            <div class="salario-card">
                                <div>Dias Trabalhados</div>
                                <div class="valor">{{ resumo.dias_trabalhados }} dia(s)</div>
                            </div>
                            % if optou_sim:
                                <div class="salario-card" style="border-color: #38A169;">
                                    <div>Vale-Transporte (R$ 11/dia)</div>
                                    <div class="valor" style="color: #2F6F4E;">+ R$ {{ f"{resumo.total_vale_transporte:.2f}".replace('.', ',') }}</div>
                                    <small style="color: #4A5568; display: block; margin-top: 4px;">
                                        ({{ resumo.dias_trabalhados }} dia(s) × R$ 11,00)
                                    </small>
                                </div>
                                <div class="salario-card destaque">
                                    <div>Salário Total (Aulas + VT)</div>
                                    <div class="valor">R$ {{ f"{resumo.total_geral:.2f}".replace('.', ',') }}</div>
                                    <small style="color: #2F6F4E; font-size: 0.85rem; display: block; margin-top: 4px;">
                                        (R$ {{ f"{resumo.total_aulas:.2f}".replace('.', ',') }} + R$ {{ f"{resumo.total_vale_transporte:.2f}".replace('.', ',') }})
                                    </small>
                                </div>
                            % else:
                                <div class="salario-card">
                                    <div>Vale-Transporte</div>
                                    <div class="valor" style="color: #718096; font-size: 1.1rem; margin-top: 12px;">Não optante (R$ 0,00)</div>
                                </div>
                                <div class="salario-card destaque">
                                    <div>Salário Total</div>
                                    <div class="valor">R$ {{ f"{resumo.total_geral:.2f}".replace('.', ',') }}</div>
                                </div>
                            % end
                        </div>

                        % if resumo.dias_trabalhados == 0 and optou_sim:
                            <p style="color: #718096; text-align: center; margin-top: 15px; font-size: 0.95rem;">
                                💡 <i>Aviso: Este professor ainda não possui aulas cadastradas. Como o vale é calculado por dia de aula trabalhado (0 dias × R$ 11,00 = R$ 0,00), adicione um aluno na aba <b>Adicionar aluno</b> para registrar dias de aula!</i>
                            </p>
                        % end
                    % end
                </div>

            <!-- 3. ABA ALTERAR ALUNO -->
            % elif aba == 'alterar':
                <h2 class="content-title">Alterar Aula de Aluno</h2>
                <div class="form-card">
                    % if aulas:
                        <form action="/portal/alterar" method="POST">
                            <div class="form-group">
                                <label for="indice">Selecione a aula para alterar:</label>
                                <select id="indice" name="indice" required>
                                    % for idx, aula in enumerate(aulas):
                                        <option value="{{ idx }}" {{ 'selected' if (defined('indice_selecionado') and indice_selecionado == idx) else '' }}>{{ idx + 1 }} - {{ aula.aluno.nome }} ({{ aula.data_aula }} - {{ aula.tipo_aula }})</option>
                                    % end
                                </select>
                            </div>

                            <div class="form-group">
                                <label for="novo_nome">Novo Nome do Aluno (opcional):</label>
                                <input type="text" id="novo_nome" name="novo_nome" placeholder="Deixe em branco para manter o mesmo">
                            </div>

                            <div class="form-group">
                                <label for="nova_data">Nova Data da Aula (opcional):</label>
                                <input type="date" id="nova_data" name="nova_data">
                            </div>

                            <div class="form-group">
                                <label for="nova_opcao">Novo Tipo de Aluno (opcional):</label>
                                <select id="nova_opcao" name="nova_opcao">
                                    <option value="">Manter tipo atual</option>
                                    <option value="1">1) Aluno de ensino fundamental coletivo (R$ 9,92)</option>
                                    <option value="2">2) Aluno de fundamental individual (R$ 16,54)</option>
                                    <option value="3">3) Aluno de ensino médio coletivo (R$ 16,54)</option>
                                    <option value="4">4) Aluno de ensino médio individual (R$ 19,85)</option>
                                    <option value="5">5) aula no fim de semana (R$ 37,50)</option>
                                </select>
                            </div>

                            <button type="submit" class="btn-salvar">Atualizar Aula</button>
                        </form>
                    % else:
                        <p style="color: #718096; text-align: center;">Nenhuma aula registrada para alterar.</p>
                    % end
                </div>

            <!-- 4. ABA EXCLUIR ALUNO -->
            % elif aba == 'excluir':
                <h2 class="content-title">Excluir Aula de Aluno</h2>
                <div class="form-card">
                    % if aulas:
                        <form action="/portal/excluir" method="POST" onsubmit="return confirm('Tem certeza que deseja excluir esta aula?');">
                            <input type="hidden" name="aba_retorno" value="excluir">
                            <div class="form-group">
                                <label for="indice_excluir">Selecione a aula para excluir:</label>
                                <select id="indice_excluir" name="indice" required>
                                    % for idx, aula in enumerate(aulas):
                                        <option value="{{ idx }}">{{ idx + 1 }} - {{ aula.aluno.nome }} ({{ aula.data_aula }} - {{ aula.tipo_aula }} - R$ {{ f"{aula.calcular_valor():.2f}".replace('.', ',') }})</option>
                                    % end
                                </select>
                            </div>

                            <button type="submit" class="btn-perigo">Excluir Aula Selecionada</button>
                        </form>
                    % else:
                        <p style="color: #718096; text-align: center;">Nenhuma aula registrada para excluir.</p>
                    % end
                </div>

            <!-- 5. ABA HISTÓRICO DE AULAS -->
            % elif aba == 'historico':
                <h2 class="content-title">Histórico de Aulas</h2>
                <div class="form-card">
                    <p style="color: #4A5568; margin-bottom: 15px;">Abaixo estão todas as aulas registradas no seu histórico cronológico.</p>
                </div>

            <!-- 6. ABA FIM DO MÊS -->
            % elif aba == 'fim_do_mes':
                <h2 class="content-title">Fim do Mês</h2>
                <div class="form-card" style="text-align: center;">
                    <p style="font-size: 1.1rem; color: #4A5568; margin-bottom: 20px;">
                        Ao finalizar o mês, todas as aulas registradas serão computadas e arquivadas, liberando a sua agenda para o próximo mês.
                    </p>
                    <form action="/portal/fim-do-mes" method="POST" onsubmit="return confirm('Tem certeza que deseja finalizar o mês atual?');">
                        <button type="submit" class="btn-salvar" style="background-color: #C53030; max-width: 300px; margin: 0 auto;">
                            Confirmar e Fechar Mês
                        </button>
                    </form>
                </div>

            <!-- 7. ABA MINHA CONTA (READ / UPDATE / DELETE PROFESSOR) -->
            % elif aba == 'perfil':
                <h2 class="content-title">Minha Conta</h2>

                <div class="form-card">
                    <h3 style="margin-bottom: 16px; color: #1A202C;">Dados Cadastrais</h3>
                    <div class="perfil-resumo">
                        <div class="perfil-item">
                            <span>ID do Professor</span>
                            <strong>#{{ professor.id }}</strong>
                        </div>
                        <div class="perfil-item">
                            <span>Nome Completo</span>
                            <strong>{{ professor.nome }}</strong>
                        </div>
                        <div class="perfil-item">
                            <span>E-mail</span>
                            <strong>{{ professor.email }}</strong>
                        </div>
                        <div class="perfil-item">
                            <span>Login</span>
                            <strong>{{ professor.login }}</strong>
                        </div>
                        <div class="perfil-item">
                            <span>Aulas na Agenda</span>
                            <strong>{{ len(aulas) }} aula(s)</strong>
                        </div>
                    </div>
                </div>

                <div class="form-card">
                    <h3 style="margin-bottom: 16px; color: #1A202C;">Atualizar Dados da Conta</h3>
                    <form action="/portal/perfil/atualizar" method="POST">
                        <div class="form-group">
                            <label for="perfil_nome">Nome completo:</label>
                            <input type="text" id="perfil_nome" name="nome" required value="{{ professor.nome }}">
                        </div>

                        <div class="form-group">
                            <label for="perfil_email">E-mail:</label>
                            <input type="email" id="perfil_email" name="email" required value="{{ professor.email }}">
                        </div>

                        <div class="form-group">
                            <label for="perfil_login">Login:</label>
                            <input type="text" id="perfil_login" name="login" required value="{{ professor.login }}">
                        </div>

                        <div class="form-group">
                            <label for="perfil_nova_senha">Nova senha (opcional):</label>
                            <input type="password" id="perfil_nova_senha" name="nova_senha" placeholder="Deixe em branco para manter a senha atual" autocomplete="new-password">
                        </div>

                        <button type="submit" class="btn-salvar">Salvar Alterações</button>
                    </form>
                </div>

                <div class="form-card" style="border-color: #FEB2B2;">
                    <h3 style="margin-bottom: 10px; color: #9B2C2C;">Excluir Conta</h3>
                    <p style="color: #4A5568; margin-bottom: 16px;">
                        Esta ação remove permanentemente sua conta de professor e todas as aulas vinculadas à sua agenda.
                    </p>
                    <form action="/portal/perfil/excluir" method="POST" onsubmit="return confirm('Tem certeza que deseja excluir permanentemente sua conta e todas as suas aulas?');">
                        <button type="submit" class="btn-perigo">Excluir Minha Conta</button>
                    </form>
                </div>
            % end

            <!-- TABELA: ALUNOS ADICIONADOS RECENTEMENTE -->
            <div class="table-card">
                <h3>Alunos Adicionados Recentemente</h3>
                % if aulas:
                    <table>
                        <thead>
                            <tr>
                                <th>Nome</th>
                                <th>Tipo de Aluno</th>
                                <th>Data</th>
                                <th>Ações</th>
                            </tr>
                        </thead>
                        <tbody>
                            % for idx, aula in enumerate(aulas):
                                <tr>
                                    <td>
                                        <div class="aluno-cell">
                                            <div class="aluno-avatar">👤</div>
                                            <span>{{ aula.aluno.nome }}</span>
                                        </div>
                                    </td>
                                    <td>
                                        <span class="tipo-badge">Aluno de {{ aula.tipo_aula.lower() }} (R$ {{ f"{aula.calcular_valor():.2f}".replace('.', ',') }})</span>
                                    </td>
                                    <td>{{ aula.data_aula }}</td>
                                    <td>
                                        <div class="acoes-cell">
                                            <a href="/portal?aba=alterar&indice={{ idx }}" class="btn-acao btn-acao-editar">✏️ Editar</a>
                                            <form action="/portal/excluir" method="POST" style="margin: 0; display: inline;" onsubmit="return confirm('Tem certeza que deseja excluir esta aula?');">
                                                <input type="hidden" name="indice" value="{{ idx }}">
                                                <input type="hidden" name="aba_retorno" value="{{ aba }}">
                                                <button type="submit" class="btn-acao btn-acao-excluir">🗑️ Excluir</button>
                                            </form>
                                        </div>
                                    </td>
                                </tr>
                            % end
                        </tbody>
                    </table>
                % else:
                    <p style="color: #718096; text-align: center; padding: 20px;">Nenhuma aula adicionada recentemente.</p>
                % end
            </div>

        </main>
    </div>

</body>
</html>
