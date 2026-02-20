from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample Interview Questions (You can later replace with AI model)
questions = [
    "Tell me about yourself.",
    "What are your strengths and weaknesses?",
    "Explain OOPS concepts in Python.",
    "What is Machine Learning?",
    "Difference between List and Tuple in Python?"
]

# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# Get Question API
@app.route("/get_question", methods=["GET"])
def get_question():
    import random
    question = random.choice(questions)
    return jsonify({"question": question})


# Submit Answer API
@app.route("/submit_answer", methods=["POST"])
def submit_answer():
    data = request.json
    answer = data.get("answer")

    # Simple evaluation logic (you can replace with AI later)
    if len(answer) > 20:
        feedback = "Good detailed answer!"
    else:
        feedback = "Try to explain more in detail."

    return jsonify({"feedback": feedback})


# IMPORTANT: Main Thread Safe Run
if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)