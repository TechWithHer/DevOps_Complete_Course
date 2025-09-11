from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>My MVP Web App</h1>
    <a href='/run/test1'>Run Test 1</a><br>
    <a href='/run/test2'>Run Test 2</a><br>
    <a href='/run/test3'>Run Test 3</a><br>
    """

@app.route("/run/<testname>")
def run_test(testname):
    result = subprocess.getoutput(f"python3 tests/{testname}.py")
    return f"<pre>{result}</pre>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

