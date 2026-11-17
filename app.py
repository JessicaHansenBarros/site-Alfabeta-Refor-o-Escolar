import os
from flask import Flask, jsonify, redirect, render_template, request, send_from_directory, session, url_for
from sqlalchemy.exc import IntegrityError

from db.banco_alunos import limpar_alunos_do_professor, listar_alunos_do_professor, salvar_aluno
from db.banco_professores import buscar_professor_login, salvar_professor
from db.conexao import criar_tabelas

app = Flask(__name__, template_folder="html")
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "alfabeta-chave-desenvolvimento")

TABELA_VALORES = {
    "Fundamental Coletivo": 9.92,
    "Fundamental Individual": 16.54,
    "Médio Coletivo": 16.54,
    "Médio Individual": 19.85,
    "Fim de Semana": 37.50,
}
VALOR_PASSE_DIA = 11.0


@app.route("/css/<path:filename>")
def servir_css(filename):
    return send_from_directory("css", filename)


@app.route("/assets/<path:filename>")
def servir_assets(filename):
    return send_from_directory("assets", filename)


@app.get("/")
def index():
    return render_template("login.html")


@app.post("/registrar")
def registrar():
    dados = request.get_json(silent=True) or request.form
    nome = dados.get("nome", "").strip()
    email = dados.get("email", "").strip()
    login = dados.get("login", "").strip()
    senha = dados.get("senha", "").strip()

    if not all([nome, email, login, senha]):
        return jsonify({"erro": "Preencha nome, email, login e senha."}), 400

    try:
        professor = salvar_professor(nome, email, login, senha)
        return jsonify({"mensagem": "Conta criada com sucesso!", "id": professor.id}), 201
    except IntegrityError:
        return jsonify({"erro": "Já existe um professor cadastrado com este email ou login."}), 409


@app.post("/login")
def login():
    dados = request.get_json(silent=True) or request.form
    login_digitado = dados.get("login", "").strip()
    senha_digitada = dados.get("senha", "").strip()

    professor = buscar_professor_login(login_digitado, senha_digitada)
    if not professor:
        return jsonify({"erro": "Login ou senha incorretos."}), 401

    session["professor_id"] = professor.id
    session["professor_nome"] = professor.nome
    return jsonify({"mensagem": f"Bem-vindo(a), {professor.nome}!", "professor_id": professor.id})


@app.get("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))


@app.get("/alunos")
def listar_alunos():
    professor_id = session.get("professor_id")
    if not professor_id:
        return jsonify({"erro": "Faça login primeiro."}), 401

    alunos = listar_alunos_do_professor(professor_id)
    total_aulas = sum(a.valor for a in alunos)
    dias_trabalhados = len({a.data_aula for a in alunos})
    total_passe = dias_trabalhados * VALOR_PASSE_DIA

    return jsonify({
        "professor": session.get("professor_nome"),
        "aulas": [
            {
                "id": a.id,
                "nome": a.nome,
                "data_aula": a.data_aula,
                "tipo_de_aula": a.tipo_de_aula,
                "valor": a.valor,
            }
            for a in alunos
        ],
        "resumo_salario": {
            "total_aulas": round(total_aulas, 2),
            "dias_trabalhados": dias_trabalhados,
            "vale_transporte": round(total_passe, 2),
            "total_com_passe": round(total_aulas + total_passe, 2),
        },
    })


@app.post("/alunos")
def adicionar_aula():
    professor_id = session.get("professor_id")
    if not professor_id:
        return jsonify({"erro": "Faça login primeiro."}), 401

    dados = request.get_json(silent=True) or request.form
    nome = dados.get("nome", "").strip()
    data_aula = dados.get("data_aula", "").strip()
    tipo_de_aula = dados.get("tipo_de_aula", "").strip()

    if tipo_de_aula not in TABELA_VALORES:
        return jsonify({"erro": "Tipo de aula inválido."}), 400
    if not nome or not data_aula:
        return jsonify({"erro": "Informe o nome do aluno e a data da aula."}), 400

    valor = TABELA_VALORES[tipo_de_aula]
    aluno = salvar_aluno(nome, data_aula, tipo_de_aula, valor, professor_id)
    return jsonify({"mensagem": "Aula registrada com sucesso!", "id": aluno.id}), 201


@app.post("/alunos/limpar")
def limpar_aulas():
    professor_id = session.get("professor_id")
    if not professor_id:
        return jsonify({"erro": "Faça login primeiro."}), 401

    limpar_alunos_do_professor(professor_id)
    return jsonify({"mensagem": "Histórico de aulas limpo com sucesso!"})


if __name__ == "__main__":
    criar_tabelas()
    app.run(host="0.0.0.0", debug=True, port=5000)
