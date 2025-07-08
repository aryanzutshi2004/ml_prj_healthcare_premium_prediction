def calculate_risk(disease):
    risk_score = {
        "diabetes": 6,
        "high blood pressure": 6,
        "heart disease": 8,
        "thyroid": 5,
        "no disease": 0,
        None: 0
    }

    disease.lower().split(" & ")
    total_risk = 0
    for d in disease.lower().split(" & "):
        total_risk = total_risk + risk_score.get(d)
    return total_risk
