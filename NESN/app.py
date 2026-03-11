from flask import Flask, render_template, request, redirect

app = Flask(__name__, template_folder="templates", static_folder="static")

users = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form.get("email", "")
        password = request.form.get("password", "")
        users.append({"email": email, "password": password})
        return redirect("/dashboard")
    return render_template("signup.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/admin")
def admin():
    return render_template("admin.html")

@app.route("/healthz")
def healthz():
    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
