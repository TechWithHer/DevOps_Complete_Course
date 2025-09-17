from flask import Flask, render_template, request
import logging
import os
import json

# ===== Logging Setup (same as main.py) =====
LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "nettoolbox.log")
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ===== Import NetToolbox test modules =====
try:
    from nettoolbox import dns_test, http_test, ping_test
except ImportError as e:
    raise ImportError(f"❌ Could not import NetToolbox modules: {e}")

# ===== Flask App =====
app = Flask(__name__)

# Available tests (same as CLI menu)
TESTS = {
    "ping": ("Ping Test", ping_test.run),
    "dns": ("DNS Test", dns_test.run),
    "http": ("HTTP Test", http_test.run),
}

@app.route("/")
def home():
    """Home page with test list and input form."""
    return render_template("index.html", tests=TESTS)

@app.route("/run/<testname>", methods=["GET"])
def run_test(testname):
    """Run selected test on a user-provided target."""
    target = request.args.get("target", "").strip()
    if not target:
        return f"<h2>❌ No target provided</h2><a href='/'>⬅ Back</a>"

    if testname not in TESTS:
        return f"<h2>❌ Invalid test '{testname}'</h2><a href='/'>⬅ Back</a>"

    test_label, test_func = TESTS[testname]
    try:
        result = test_func(target)
        logging.info(result)
        return f"""
        <h2>Result of {test_label} on {target}</h2>
        <pre>{json.dumps(result, indent=4)}</pre>
        <br><a href='/'>⬅ Back</a>
        """
    except Exception as e:
        return f"<h2>❌ Error running {test_label}</h2><pre>{str(e)}</pre><br><a href='/'>⬅ Back</a>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
