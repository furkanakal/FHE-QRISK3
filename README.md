# QRISK3 Cardiovascular Risk Algorithm

## Introduction

QRISK3 is a predictive algorithm designed to estimate an individual's 10-year risk of developing cardiovascular disease (CVD). The algorithm takes into account a wide range of factors, including age, body mass index (BMI), systolic blood pressure (SBP), cholesterol ratio, smoking status, socioeconomic deprivation, and numerous medical conditions. The result is a risk score, expressed as a percentage, indicating the likelihood of CVD occurrence within 10 years.

## Mathematical Framework

The QRISK3 risk score is calculated using the following formula:

```math
\text{Risk Score} = 100 \times \left( 1 - \text{Survivor}^{\exp(a)} \right)
```

Where:
- **Survivor** is a pre-calculated survival probability for a given gender and population group.
  - For females: `Survivor = 0.988876402378082`
  - For males: `Survivor = 0.977268040180206`
  
- **\( a \)** is the **linear predictor**, which is a sum of various risk factor contributions (continuous, binary, and interaction terms).

### Linear Predictor Formula

The linear predictor \( a \) is computed as:

```math
a = \sum_{\text{continuous}} \left( \text{Risk Factor Value} \times \text{Coefficient} \right)
    + \sum_{\text{binary}} \left( \text{Risk Factor} \times \text{Coefficient} \right)
    + \sum_{\text{interaction}} \left( \text{Risk Factor Interaction Terms} \times \text{Coefficient} \right)
```

---

## Continuous Risk Factors

QRISK3 uses **fractional polynomial transformations** and **centering** for continuous variables to better fit non-linear relationships between risk factors and cardiovascular disease. The following continuous variables are included:

### Age Transformations

For **age**, two transformations are applied:

```math
\text{age}_1 = \left( \frac{\text{age}}{10} \right)^{-2}
\quad \text{and} \quad
\text{age}_2 = \frac{\text{age}}{10}
```

These are then centered around population means:
- For **females**:
  - \( \text{age}_1 = \text{age}_1 - 0.053274843841791 \)
  - \( \text{age}_2 = \text{age}_2 - 4.332503318786621 \)
- For **males**:
  - \( \text{age}_1 = \text{age}_1 - 0.234766781330109 \)
  - \( \text{age}_2 = \text{age}_2 - 77.284080505371094 \)

### Body Mass Index (BMI) Transformations

For **BMI**, the following transformations are applied:

```math
\text{bmi}_1 = \left( \frac{\text{bmi}}{10} \right)^{-2}
\quad \text{and} \quad
\text{bmi}_2 = \frac{\log(\text{bmi}/10)}{\left( \frac{\text{bmi}}{10} \right)^2}
```

These are centered as follows:
- For both **females** and **males**:
  - \( \text{bmi}_1 = \text{bmi}_1 - 0.154946178197861 \)
  - \( \text{bmi}_2 = \text{bmi}_2 - 0.144462317228317 \)

### Other Continuous Variables

- **Cholesterol Ratio (Rati)**:
  - Centered values:
    - Females: \( \text{rati} = \text{rati} - 3.47632646560669 \)
    - Males: \( \text{rati} = \text{rati} - 4.300998687744141 \)
    
- **Systolic Blood Pressure (SBP)**:
  - Centered values:
    - Females: \( \text{sbp} = \text{sbp} - 123.13001251220703 \)
    - Males: \( \text{sbp} = \text{sbp} - 128.57157897949219 \)
    
- **Standard Deviation of SBP (SBPS5)**:
  - Centered values:
    - Females: \( \text{sbps5} = \text{sbps5} - 9.002537727355957 \)
    - Males: \( \text{sbps5} = \text{sbps5} - 8.756621360778809 \)
    
- **Townsend Deprivation Index (Town)**:
  - Centered values:
    - Females: \( \text{town} = \text{town} - 0.392308831214905 \)
    - Males: \( \text{town} = \text{town} - 0.52630490064621 \)

---

## Binary Risk Factors

Binary risk factors are either **1** (if the condition or factor is present) or **0** (if absent). These include:

- **Atrial Fibrillation (b_AF)**
- **Use of Atypical Antipsychotics (b_atypicalantipsy)**
- **Use of Corticosteroids (b_corticosteroids)**
- **Migraine (b_migraine)**
- **Rheumatoid Arthritis (b_ra)**
- **Chronic Kidney Disease (b_renal)**
- **Severe Mental Illness (b_semi)**
- **Systemic Lupus Erythematosus (b_sle)**
- **Treated Hypertension (b_treatedhyp)**
- **Type 1 Diabetes (b_type1)**
- **Type 2 Diabetes (b_type2)**
- **Erectile Dysfunction (b_impotence2)** (males only)
- **Family History of Cardiovascular Disease (fh_cvd)**

---

## Interaction Terms

QRISK3 includes interaction terms to capture the relationships between multiple risk factors. Some notable interaction terms are:

- **Age and Smoking**:
  \[
  \text{age}_1 \times (\text{smoke\_cat} = 1) \times C_{\text{smoke1}} + \ldots + \text{age}_1 \times (\text{smoke\_cat} = 4) \times C_{\text{smoke4}}
  \]

- **Age and Health Conditions**:
  \[
  \text{age}_1 \times b\_AF \times C_{\text{AF}} + \text{age}_1 \times b\_corticosteroids \times C_{\text{corticosteroids}} + \ldots
  \]

- **Age and BMI**:
  \[
  \text{age}_1 \times \text{bmi}_1 \times C_{\text{age-bmi1}} + \text{age}_1 \times \text{bmi}_2 \times C_{\text{age-bmi2}}
  \]

---

## Full Risk Score Formula

### Step 1: Compute Linear Predictor \( a \)

```math
a = \text{age}_1 \times C_{\text{age}_1} + \text{age}_2 \times C_{\text{age}_2} + \text{bmi}_1 \times C_{\text{bmi}_1} + \text{bmi}_2 \times C_{\text{bmi}_2} + \text{rati} \times C_{\text{rati}} + \text{sbp} \times C_{\text{sbp}} + \text{sbps5} \times C_{\text{sbps5}} + \text{town} \times C_{\text{town}} 
+ \sum_{\text{binary conditions}} \left( \text{Condition} \times C_{\text{Condition}} \right)
+ \sum_{\text{interaction terms}} \left( \text{Interaction Term} \times C_{\text{Interaction Term}} \right)
```

### Step 2: Calculate Risk Score

```math
\text{Risk Score} = 100 \times \left( 1 - \text{Survivor}^{\exp(a)} \right)
```

Where the **Survivor** values are:
- Females: \( \text{Survivor} = 0.988876402378082 \)
- Males: \( \text{Survivor} = 0.977268040180206 \)

---

## Conclusion

The QRISK3 algorithm provides a reliable method for estimating an individual's 10-year risk of developing cardiovascular disease. By combining continuous and binary variables with interaction terms, QRISK3 offers a sophisticated model for evaluating risk in diverse populations. 

It is widely used in clinical settings to guide preventive measures and interventions for high-risk individuals.
