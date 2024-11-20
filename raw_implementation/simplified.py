import numpy as np

def qrisk3_simplified_male(age, bmi, sbp, smoke_cat):
    # Survivor function for males (10-year risk)
    survivor_male = 0.977268040180206

    # Smoking categories coefficients
    Ismoke_male = [0, 0.19128222863388983, 0.55241588192645552, 0.63835053027506072, 0.78983819881858019]

    # Polynomial transformations
    dage = age / 10
    age_1 = dage ** -1  # Fractional polynomial for age
    age_2 = dage ** 3  # Fractional polynomial for age
    
    dbmi = bmi / 10
    bmi_1 = dbmi ** -2  # Fractional polynomial for BMI
    bmi_2 = dbmi ** -2 * np.log(dbmi)  # Second fractional polynomial for BMI

    # Centering continuous variables (subtracting population means)
    age_1 -= 0.234766781330109  # Age centering
    age_2 -= 77.284080505371094  # Age centering
    bmi_1 -= 0.149176135659218  # BMI centering
    bmi_2 -= 0.141913309693336  # BMI centering
    sbp -= 128.57157897949219  # SBP centering

    # Start of sum for linear predictor 'a'
    a = 0

    # Add continuous variable contributions
    a += age_1 * -17.839781666005575  # Coefficient for age_1
    a += age_2 * 0.0022964880605765492  # Coefficient for age_2
    a += bmi_1 * 2.4562776660536358  # Coefficient for bmi_1
    a += bmi_2 * -8.3011122314711354  # Coefficient for bmi_2
    a += sbp * 0.012910126542553305  # Coefficient for SBP

    # Add smoking category contribution
    a += Ismoke_male[smoke_cat]  # Coefficient for smoking category

    # Calculate the risk score
    score = 100.0 * (1 - pow(survivor_male, np.exp(a)))
    
    return score

# Example usage:
age = 24
bmi = 25
sbp = 110  # Systolic blood pressure
smoke_cat = 2  # Smoking category (e.g., 1 for light smoker)

# Calculate simplified male QRISK3 score
male_score = qrisk3_simplified_male(age, bmi, sbp, smoke_cat)
print(f"Simplified Male QRISK3 score: {male_score:.2f}%")
