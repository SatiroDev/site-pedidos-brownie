from flask import Flask

from routes import brownies, admin

from flask import Flask, render_template, request, redirect, url_for, flash




app = Flask(__name__)
app.secret_key = '101010'

app.register_blueprint(brownies.brownies_bp)
app.register_blueprint(admin.admin_bp)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    brownies.criar_tabela_brownie()
    app.run(debug=True)