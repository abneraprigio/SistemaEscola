import logging  # é uma biblioteca que registra mensagens de erro durante a executação
import os       # Permite interagir com o SO
import mysql.connector
from mysql.connector.errors import Error, IntegrityError
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

def conectar_mysql():
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "127.0.0.1"),
        user=os.getenv("MYSQL_USER", "root"),
        password=os.getenv("MYSQL_PASSWORD", "senai105"),
        database=os.getenv("MYSQL_DATABASE", "escola_informatica_aula_dml")
    )
    
def inteiro_positivo(valor):
    """Devolve True para um numero inteiro positivo digitado no formulario"""
    return valor.isascii() and valor.isdigit() and int(valor) > 0

@app.get("/")
def inicio():
    return render_template("index.html")


@app.route("/alunos/cadastrar", methods=["GET", "POST"])
def cadastrar_aluno():
    # 2. GET apresenta a tela; POST recebe os campos e executa INSERT.
    if request.method == "GET":
        return render_template("cadastro.html", dados={})

    # ENTRADA: cada chave corresponde ao atributo name de um input HTML.
    dados = {
        "nome": request.form.get("nome", "").strip(),
        "email": request.form.get("email", "").strip(),
        "telefone": request.form.get("telefone", "").strip(),
    }
    if not dados["nome"] or not dados["email"]:
        return render_template("cadastro.html", dados=dados,
                               erro="Nome e e-mail são obrigatórios."), 400
    if (len(dados["nome"]) > 100 or len(dados["email"]) > 120
            or len(dados["telefone"]) > 20):
        return render_template("cadastro.html", dados=dados,
                               erro="Um dos campos excede o tamanho permitido."), 400

    












    



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    app.run(host="127.0.0.1", port=5000, debug=True)