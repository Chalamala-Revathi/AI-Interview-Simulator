def generate_feedback(score):
    if score >= 8:
        return "Excellent answer. Very strong understanding."
    elif score >= 5:
        return "Good answer. Try to add more technical depth."
    else:
        return "Answer needs improvement. Revise the concept clearly."