from flask import Flask, render_template, request 

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def pagina_principal():
    resultado = None 

    if request.method == "POST":

        peso = float(request.form.get("peso"))
        altura = float(request.form.get("altura"))
        resultado = round(peso/(altura ** 2), 2)
        
    historico =["Item A", "Item B", "Item C"]

    return render_template(
        "index.html",
        valor_calculado=resultado,
        lista_itens=historico
    )

if __name__ == "__main__":
    app.run(debug=True)
