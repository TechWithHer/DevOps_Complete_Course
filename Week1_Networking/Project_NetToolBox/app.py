from flask import Flask, render_template, url_for
import subprocess

app = Flask(__name__)

@app.route("/")
def home():
    # Pass test names to the HTML page
    tests = ["Ping Test", "DNS Test", "HTTP Test"]
    return render_template("index.html", tests=tests)

@app.route("/run/<testname>")
def run_test(testname):
    try:
        result = subprocess.getoutput(f"python3 tests/{testname}.py")
        return f"<h2>Result of {testname}</h2><pre>{result}</pre><br><a href='/'>⬅ Back</a>"
    except Exception as e:
        return f"<h2>Error running {testname}</h2><pre>{str(e)}</pre><br><a href='/'>⬅ Back</a>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

