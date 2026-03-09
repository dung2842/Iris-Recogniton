def decision(score, threshold=0.8):

    if score >= threshold:
        return "Authenticated"
    else:
        return "Rejected"