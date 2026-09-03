from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    """Homepage: the original apology page."""
    return render_template("home.html")

@app.route("/next")
def next_page():
    """Second page shown after clicking 'It's Okay'."""
    return render_template("next.html")

@app.route("/last")
def last_page():
    """Final page shown after sealing the promise."""
    return render_template("last.html")

# Optional aliases, so these pages are also easy to open directly.
@app.route("/home")
def home_alias():
    return redirect(url_for("home"))

@app.route("/final")
def final_alias():
    return redirect(url_for("last_page"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
