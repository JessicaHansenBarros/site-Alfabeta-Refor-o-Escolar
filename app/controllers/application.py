import sys
import os
from bottle import template, redirect, TEMPLATE_PATH

# Calcula o diretório base do projeto (bmvc_start_from_this)
CONTROLLER_DIR = os.path.dirname(os.path.abspath(__file__))
APP_DIR = os.path.dirname(CONTROLLER_DIR)
BASE_DIR = os.path.dirname(APP_DIR)
VIEWS_DIR = os.path.join(APP_DIR, 'views', 'html')

# Adiciona apenas a raiz do projeto ao sys.path para importações canônicas `app.*`
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

# Adiciona ao TEMPLATE_PATH do Bottle de forma absoluta
if VIEWS_DIR not in TEMPLATE_PATH:
    TEMPLATE_PATH.insert(0, VIEWS_DIR)

from app.models.classes.portal import PortalAlfabeta


def formatar_data(data_str: str) -> str:
    """Converte datas HTML (AAAA-MM-DD) para o formato do banco (DD/MM/AA)."""
    if not data_str:
        return ""
    limpa = data_str.strip()
    if "-" in limpa:
        partes = limpa.split("-")
        if len(partes) == 3:
            ano = partes[0][-2:]
            return f"{partes[2]}/{partes[1]}/{ano}"
    return limpa


class Application:
    """
    Controlador principal do BMVC (padrão hgmachine/bmvc_start_from_this).
    Gerencia a navegação entre páginas e a integração com o Model PortalAlfabeta.
    """

    def __init__(self, portal_model: PortalAlfabeta | None = None):
        # Instancia o Model de domínio (PortalAlfabeta), permitindo injeção nos testes
        self.portal_model = portal_model if portal_model is not None else PortalAlfabeta()
        self.current_user = None

        # Dicionário de páginas gerenciadas pelo Controller (padrão BMVC)
        self.pages = {
            'portal': self.portal,
            'cadastro': self.cadastro,
            'helper': self.helper,
        }

    def render(self, page, parameter=None, **kwargs):
        """Método de despacho padrão do BMVC."""
        content = self.pages.get(page, self.helper)
        if kwargs:
            return content(**kwargs)
        return content(parameter)

    def helper(self, info=None):
        """Página helper padrão do template BMVC."""
        return template('helper.tpl')

    def cadastro(self, erro=None, mensagem=None):
        """Renderiza a página de cadastro de professor."""
        return template('cadastro.html', erro=erro, mensagem=mensagem)

    def registrar_professor(self, nome, email, login, senha):
        """Registra um novo professor no banco JSON e redireciona para o login."""
        try:
            self.portal_model.registrar_professor(
                nome=nome or "",
                email=email or "",
                login=login or "",
                senha=senha or "",
            )
            return template(
                'login.html',
                mensagem="Conta criada com sucesso! Faça login para continuar.",
            )
        except ValueError as e:
            return template('cadastro.html', erro=str(e))

    def portal(
        self,
        aba='adicionar',
        mensagem=None,
        erro=None,
        tem_vt=None,
        resumo=None,
        indice_selecionado=None
    ):
        """
        Página principal:
        - Se logado, exibe o painel do Portal com a aba selecionada.
        - Se deslogado, renderiza a tela de login.
        """
        if not self.current_user:
            return template('login.html', erro=erro, mensagem=mensagem)

        # Se acessou a aba de salário e ainda não calculou, calcula automaticamente
        if aba == 'salario' and resumo is None:
            tem_vt = 'sim' if tem_vt is None else tem_vt
            valor_diario = 11.0 if tem_vt == 'sim' else None
            try:
                resumo = self.portal_model.calcular_salario(self.current_user, valor_diario)
            except Exception as e:
                print(f"[Erro] Falha ao calcular salário: {e}")

        indice_int = None
        if indice_selecionado is not None and str(indice_selecionado).strip() != "":
            try:
                indice_int = int(indice_selecionado)
            except (TypeError, ValueError):
                indice_int = None

        aulas = self.portal_model.listar_aulas(self.current_user)
        return template(
            'portal.html',
            professor=self.current_user,
            aulas=aulas,
            aba=aba,
            mensagem=mensagem,
            erro=erro,
            tem_vt=tem_vt,
            resumo=resumo,
            indice_selecionado=indice_int,
            enumerate=enumerate
        )

    def autenticar(self, login, senha):
        """Autentica o professor contra o banco JSON."""
        login_limpo = (login or "").strip()
        senha_limpa = (senha or "").strip()

        if not login_limpo or not senha_limpa:
            return template('login.html', erro="Por favor, preencha o login e a senha.")

        professor = self.portal_model.autenticar(login_limpo, senha_limpa)
        if professor:
            self.current_user = professor
            return self.portal(aba='adicionar')

        return template('login.html', erro="Login ou senha incorretos! Verifique e tente novamente.")

    def adicionar_aluno(self, nome_aluno, opcao_tipo, data_aula):
        """Cadastra nova aula para o professor logado."""
        if not self.current_user:
            return redirect('/portal')

        nome_limpo = (nome_aluno or "").strip()
        data_formatada = formatar_data(data_aula)

        if not nome_limpo or not opcao_tipo or not data_formatada:
            return self.portal(aba='adicionar', erro="Todos os campos são obrigatórios!")

        try:
            nova_aula = self.portal_model.adicionar_aula(
                professor=self.current_user,
                nome_aluno=nome_limpo,
                data_aula=data_formatada,
                opcao_tipo=opcao_tipo
            )
            return self.portal(
                aba='adicionar',
                mensagem=f"Aula para o aluno '{nova_aula.aluno.nome}' adicionada com sucesso!"
            )
        except Exception as e:
            return self.portal(aba='adicionar', erro=f"Erro ao adicionar aula: {e}")

    def calcular_salario(self, tem_vt_str):
        """Calcula o salário do professor com opção de vale-transporte (R$ 11,00/dia)."""
        if not self.current_user:
            return redirect('/portal')

        # Se escolheu 'sim', o valor fixo é R$ 11,00 por dia de aula
        optou_vt = str(tem_vt_str).strip().lower() in ['sim', '1', 'true']
        valor_diario = 11.0 if optou_vt else None

        try:
            resumo = self.portal_model.calcular_salario(self.current_user, valor_diario)
            return self.portal(
                aba='salario',
                tem_vt='sim' if optou_vt else 'nao',
                resumo=resumo
            )
        except Exception as e:
            return self.portal(aba='salario', erro=f"Erro ao calcular salário: {e}")

    def alterar_aluno(self, indice_str, novo_nome, nova_data, nova_opcao):
        """Modifica dados de uma aula existente."""
        if not self.current_user:
            return redirect('/portal')

        try:
            indice = int(indice_str)
            data_formatada = formatar_data(nova_data) if nova_data else None
            opcao = nova_opcao.strip() if nova_opcao and nova_opcao.strip() else None

            self.portal_model.alterar_aula(
                professor=self.current_user,
                indice=indice,
                novo_nome_aluno=novo_nome,
                nova_data_aula=data_formatada,
                nova_opcao_tipo=opcao
            )
            return self.portal(aba='alterar', mensagem="Aula atualizada com sucesso!")
        except Exception as e:
            return self.portal(aba='alterar', erro=f"Erro ao alterar aula: {e}")

    def remover_aluno(self, indice_str, aba_retorno='excluir'):
        """Remove uma aula específica da agenda do professor logado."""
        if not self.current_user:
            return redirect('/portal')

        abas_validas = {
            'adicionar', 'salario', 'alterar', 'excluir',
            'historico', 'fim_do_mes', 'perfil'
        }
        aba_destino = aba_retorno if aba_retorno in abas_validas else 'excluir'

        try:
            indice = int(indice_str)
            aula_removida = self.portal_model.remover_aula(self.current_user, indice)
            return self.portal(
                aba=aba_destino,
                mensagem=(
                    f"Aula do aluno '{aula_removida.aluno.nome}' "
                    f"({aula_removida.data_aula}) excluída com sucesso!"
                )
            )
        except Exception as e:
            return self.portal(aba=aba_destino, erro=f"Erro ao excluir aula: {e}")

    def atualizar_professor(self, nome, email, login, nova_senha):
        """Atualiza os dados cadastrais do professor logado."""
        if not self.current_user:
            return redirect('/portal')

        try:
            self.portal_model.atualizar_professor(
                professor=self.current_user,
                novo_nome=nome,
                novo_email=email,
                novo_login=login,
                nova_senha=nova_senha
            )
            return self.portal(
                aba='perfil',
                mensagem="Dados da conta atualizados com sucesso!"
            )
        except Exception as e:
            return self.portal(aba='perfil', erro=f"Erro ao atualizar conta: {e}")

    def excluir_professor(self):
        """Exclui a conta do professor logado e suas aulas associadas."""
        if not self.current_user:
            return redirect('/portal')

        try:
            self.portal_model.remover_professor(self.current_user)
            self.current_user = None
            return template(
                'login.html',
                mensagem="Sua conta foi excluída com sucesso."
            )
        except Exception as e:
            return self.portal(aba='perfil', erro=f"Erro ao excluir conta: {e}")

    def finalizar_mes(self):
        """Encerra e limpa a agenda do professor para o próximo mês."""
        if not self.current_user:
            return redirect('/portal')

        try:
            removidas = self.portal_model.finalizar_mes(self.current_user)
            return self.portal(
                aba='fim_do_mes',
                mensagem=f"Mês finalizado com sucesso! {removidas} aulas foram arquivadas."
            )
        except Exception as e:
            return self.portal(aba='fim_do_mes', erro=f"Erro ao finalizar mês: {e}")

    def sair(self):
        """Efetua logout do professor."""
        self.current_user = None
        return redirect('/portal')
