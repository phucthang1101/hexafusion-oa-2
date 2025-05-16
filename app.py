from flask import Flask, render_template, request, redirect, url_for
from utils.ai import summarize_input
from utils.db import insert_log, get_latest_logs
from dotenv import load_dotenv
import os
from utils.slack import send_slack_message

load_dotenv()
app = Flask(__name__)

@app.route("/", methods=["GET"])
def form():
    return render_template("form.html")

@app.route("/submit", methods=["POST"])
def submit():
    input_text = request.form.get("input") or request.json.get("input")
    if not input_text:
        return {"error": "Missing input"}, 400

    summary = summarize_input(input_text)
    insert_log(input_text, summary)

    # 🚀 Send Slack notification
    slack_message = f"📝 New AI Summary:\n{summary}"
    send_slack_message(slack_message)

    return redirect(url_for('dashboard'))

@app.route("/dashboard")
def dashboard():
    logs = get_latest_logs(10)
    return render_template("dashboard.html", logs=logs)

if __name__ == "__main__":
    app.run(debug=True)
