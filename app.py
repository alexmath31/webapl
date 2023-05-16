from flask import Flask, url_for, render_template, request, flash, redirect

app = Flask(__name__)
app.config["SECRET_KEY"] = "asd"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/greet/<name>")
def greet(name):
    return render_template("greed.html", name=name)


@app.route("/multiply/<int:first_arg>/<int:second_arg>")
def multiply(first_arg: int, second_arg: int):
    return f"Hello, {first_arg * second_arg}"


items_storage = []


@app.route("/items", methods={"GET", "POST"})
def items_endpoint():
    flash ("Database unavailable. Try again later")
    if request.method == "POST":
        item = request.form.get("item")
        items_storage.append(item)
    return redirect(url_for("index"))

    return render_template("items.html", items=items_storage)


with app.test_request_context():
    print(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
