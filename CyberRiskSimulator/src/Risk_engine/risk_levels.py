def get_risk_level(score):


    if score >= 80:

        return "Critical"


    elif score >= 60:

        return "High"


    elif score >= 40:

        return "Medium"


    else:

        return "Low"