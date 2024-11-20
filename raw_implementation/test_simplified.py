import numpy as np
import matplotlib.pyplot as plt
from main import qrisk3_male
from simplified import qrisk3_simplified_male
import os

# Create the directory if it doesn't exist
os.makedirs('raw_implementation/test_results', exist_ok=True)

def compare_qrisk3_scores(param_name, param_range, fixed_params):
    main_scores = []
    simplified_scores = []
    
    for value in param_range:
        params = fixed_params.copy()
        params[param_name] = value
        
        main_score = qrisk3_male(**params)
        simplified_score = qrisk3_simplified_male(
            params['age'], params['bmi'], params['sbp'], params['smoke_cat']
        )
        
        main_scores.append(main_score)
        simplified_scores.append(simplified_score)
    
    plt.figure(figsize=(10, 6))
    plt.plot(param_range, main_scores, label='Main QRISK3')
    plt.plot(param_range, simplified_scores, label='Simplified QRISK3')
    plt.xlabel(param_name)
    plt.ylabel('Risk Score (%)')
    plt.title(f'QRISK3 Comparison: {param_name}')
    plt.legend()
    plt.grid(True)
    plt.savefig(f'raw_implementation/test_results/qrisk3_comparison_{param_name}.png')
    plt.close()

# Define fixed parameters
fixed_params = {
    'age': 45, 'b_AF': 0, 'b_atypicalantipsy': 0, 'b_corticosteroids': 0,
    'b_impotence2': 0, 'b_migraine': 0, 'b_ra': 0, 'b_renal': 0, 'b_semi': 0,
    'b_sle': 0, 'b_treatedhyp': 0, 'b_type1': 0, 'b_type2': 0, 'bmi': 25,
    'ethrisk': 0, 'fh_cvd': 0, 'rati': 4.3, 'sbp': 120, 'sbps5': 0,
    'smoke_cat': 0, 'surv': 10, 'town': 0
}

# Compare age
age_range = range(30, 85, 5)
compare_qrisk3_scores('age', age_range, fixed_params)

# Compare smoking category
smoke_cat_range = range(5)
compare_qrisk3_scores('smoke_cat', smoke_cat_range, fixed_params)

# Compare BMI
bmi_range = np.arange(18.5, 40.1, 1.5)
compare_qrisk3_scores('bmi', bmi_range, fixed_params)

# Compare SBP
sbp_range = range(90, 201, 10)
compare_qrisk3_scores('sbp', sbp_range, fixed_params)

print("Comparison graphs have been generated and saved in the 'raw_implementation/test_results' directory.")