def calculate_ats_score(skills):

    score = 40

    score += len(skills) * 6

    if len(skills) >= 8:
        score += 10

    if score > 100:
        score = 100

    return score