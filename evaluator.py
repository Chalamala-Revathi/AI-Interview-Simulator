def evaluate_with_logic(question, answer):

    score = 0
    feedback = []

    # 1. Length check
    if len(answer.split()) > 20:
        score += 3
        feedback.append("Good detailed answer.")
    else:
        feedback.append("Answer is too short. Try to explain more.")

    # 2. Keyword matching (basic logic)
    keywords = question.lower().split()

    match_count = 0
    for word in keywords:
        if word in answer.lower():
            match_count += 1

    if match_count > 3:
        score += 4
        feedback.append("Answer is relevant to the question.")
    else:
        feedback.append("Answer is not fully relevant.")

    # 3. Basic grammar check (simple rule)
    if answer[0].isupper() and answer.endswith("."):
        score += 3
        feedback.append("Sentence structure looks good.")
    else:
        feedback.append("Improve sentence structure (start with capital, end with period).")

    return {
        "score": score,
        "feedback": " ".join(feedback)
    }