import os
import sys

# Garante caminhos absolutos corretos usando a raiz do projeto
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, 'app', 'static')

if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from bottle import Bottle, request, run, static_file

from app.controllers.application import Application


app = Bottle()
ctl = Application()


# -----------------------------------------------------------------------------
# Rotas:

@app.route('/static/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root=STATIC_DIR)


@app.route('/helper')
def helper(info=None):
    return ctl.render('helper')


# -----------------------------------------------------------------------------
# Suas rotas aqui:

@app.route('/cadastro', method=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.forms.getunicode('nome')
        email = request.forms.getunicode('email')
        login = request.forms.getunicode('login')
        senha = request.forms.getunicode('senha')
        return ctl.registrar_professor(nome, email, login, senha)
    return ctl.cadastro()


@app.route('/')
@app.route('/portal')
def portal():
    aba = request.query.getunicode('aba', 'adicionar')
    indice = request.query.getunicode('indice')
    return ctl.portal(aba=aba, indice_selecionado=indice)


@app.route('/portal', method='POST')
def portal_login():
    login = request.forms.getunicode('login') or request.forms.getunicode('usuario')
    senha = request.forms.getunicode('senha')
    return ctl.autenticar(login, senha)


@app.route('/portal/adicionar', method='POST')
def portal_adicionar():
    nome_aluno = request.forms.getunicode('nome_aluno')
    opcao_tipo = request.forms.getunicode('opcao_tipo')
    data_aula = request.forms.getunicode('data_aula')
    return ctl.adicionar_aluno(nome_aluno, opcao_tipo, data_aula)


@app.route('/portal/salario', method=['GET', 'POST'])
def portal_salario():
    if request.method == 'POST':
        tem_vt = request.forms.getunicode('tem_vt')
        return ctl.calcular_salario(tem_vt)
    return ctl.portal(aba='salario')


@app.route('/portal/alterar', method=['GET', 'POST'])
def portal_alterar():
    if request.method == 'POST':
        indice = request.forms.getunicode('indice')
        novo_nome = request.forms.getunicode('novo_nome')
        nova_data = request.forms.getunicode('nova_data')
        nova_opcao = request.forms.getunicode('nova_opcao')
        return ctl.alterar_aluno(indice, novo_nome, nova_data, nova_opcao)
    indice = request.query.getunicode('indice')
    return ctl.portal(aba='alterar', indice_selecionado=indice)


@app.route('/portal/excluir', method=['GET', 'POST'])
def portal_excluir():
    if request.method == 'POST':
        indice = request.forms.getunicode('indice')
        aba_retorno = request.forms.getunicode('aba_retorno') or 'excluir'
        return ctl.remover_aluno(indice, aba_retorno=aba_retorno)
    return ctl.portal(aba='excluir')


@app.route('/portal/perfil')
def portal_perfil():
    return ctl.portal(aba='perfil')


@app.route('/portal/perfil/atualizar', method='POST')
def portal_perfil_atualizar():
    nome = request.forms.getunicode('nome')
    email = request.forms.getunicode('email')
    login = request.forms.getunicode('login')
    nova_senha = request.forms.getunicode('nova_senha')
    return ctl.atualizar_professor(nome, email, login, nova_senha)


@app.route('/portal/perfil/excluir', method='POST')
def portal_perfil_excluir():
    return ctl.excluir_professor()


@app.route('/portal/fim-do-mes', method='POST')
def portal_fim_do_mes():
    return ctl.finalizar_mes()


@app.route('/sair')
def sair():
    return ctl.sair()


# -----------------------------------------------------------------------------

if __name__ == '__main__':
    run(app, host='0.0.0.0', port=8080, debug=True, reloader=True)
