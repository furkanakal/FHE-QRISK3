from concrete import fhe

def scale_param(value, param_type):
    """
    Scale the input value to a 16-bit integer based on the parameter type.
    
    :param value: The input value to scale
    :param param_type: String indicating the type of parameter ('age', 'bmi', or 'sbp')
    :return: Scaled 16-bit integer value
    """
    if param_type == 'age':
        # Assume age range: 0-100 years
        return int((value * 65535) // 100)
    elif param_type == 'bmi':
        # Assume BMI range: 10-50 kg/m^2
        return int(((value - 10) * 65535) // (50 - 10))
    elif param_type == 'sbp':
        # Assume SBP range: 80-200 mmHg
        return int(((value - 80) * 65535) // (200 - 80))
    else:
        raise ValueError(f"Unknown parameter type: {param_type}")

def qrisk3_simplified_male(age, bmi, sbp):
    # All inputs, intermediate calculations, and outputs are strictly 16-bit integers
    risk = 0
    SMOKE_IMPACT = int(0.55241588192645552 * 65535)
    age_factor = age >> 2
    risk = (risk + age_factor) & 0xFFFF
    bmi_factor = bmi >> 3
    risk = (risk + bmi_factor) & 0xFFFF
    sbp_factor = sbp >> 3
    risk = (risk + sbp_factor) & 0xFFFF
    smoke_factor = SMOKE_IMPACT >> 3
    risk = (risk + smoke_factor) & 0xFFFF
    return risk

def qrisk3_simplified_female(age, bmi, sbp):
    # All inputs, intermediate calculations, and outputs are strictly 16-bit integers
    risk = 0
    SMOKE_IMPACT = int(0.56200858012438537 * 65535)  # Female-specific smoking impact
    age_factor = age >> 2
    risk = (risk + age_factor) & 0xFFFF
    bmi_factor = bmi >> 3
    risk = (risk + bmi_factor) & 0xFFFF
    sbp_factor = sbp >> 3
    risk = (risk + sbp_factor) & 0xFFFF
    smoke_factor = SMOKE_IMPACT >> 3
    risk = (risk + smoke_factor) & 0xFFFF
    return risk

compiler_male = fhe.Compiler(
    qrisk3_simplified_male,
    {
        "age": "encrypted",
        "bmi": "encrypted",
        "sbp": "encrypted",
    }
)

compiler_female = fhe.Compiler(
    qrisk3_simplified_female,
    {
        "age": "encrypted",
        "bmi": "encrypted",
        "sbp": "encrypted",
    }
)

# Input set (all values pre-scaled to 16-bit range)
input_set = [
    (scale_param(33, 'age'), scale_param(25, 'bmi'), scale_param(120, 'sbp')),
    (scale_param(66, 'age'), scale_param(35, 'bmi'), scale_param(160, 'sbp')),
    (scale_param(99, 'age'), scale_param(20, 'bmi'), scale_param(140, 'sbp')),
]

print("Compilation for male...")
circuit_male = compiler_male.compile(input_set)

print("Compilation for female...")
circuit_female = compiler_female.compile(input_set)

print("Key generation for male...")
circuit_male.keygen()

print("Key generation for female...")
circuit_female.keygen()

print("Homomorphic evaluation...")
# Example evaluation: mid-range values for both male and female
age, bmi, sbp = scale_param(24, 'age'), scale_param(25, 'bmi'), scale_param(110, 'sbp')

# Male calculation
encrypted_age_male, encrypted_bmi_male, encrypted_sbp_male = circuit_male.encrypt(age, bmi, sbp)
encrypted_score_male = circuit_male.run(encrypted_age_male, encrypted_bmi_male, encrypted_sbp_male)
score_male = circuit_male.decrypt(encrypted_score_male)
print(f"Risk score for male: {score_male / 65535:.6f}")

# Female calculation
encrypted_age_female, encrypted_bmi_female, encrypted_sbp_female = circuit_female.encrypt(age, bmi, sbp)
encrypted_score_female = circuit_female.run(encrypted_age_female, encrypted_bmi_female, encrypted_sbp_female)
score_female = circuit_female.decrypt(encrypted_score_female)
print(f"Risk score for female: {score_female / 65535:.6f}")