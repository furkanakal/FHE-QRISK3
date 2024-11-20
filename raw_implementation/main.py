import numpy as np

def qrisk3_female(age, b_AF, b_atypicalantipsy, b_corticosteroids, b_migraine, b_ra, b_renal, b_semi, b_sle, b_treatedhyp, b_type1, b_type2, bmi, ethrisk, fh_cvd, rati, sbp, sbps5, smoke_cat, surv, town):
    # Survivor function for females
    survivor_female = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.988876402378082, 0, 0, 0, 0, 0]

    # Ethnicity risk and smoking categories for females
    Iethrisk_female = [0, 0, 0.28040314332995425, 0.56298994142075398, 0.29590000851116516, 0.072785379877982545, -0.17072135508857317, -0.39371043314874971, -0.32632495283530272, -0.17127056883241784]
    Ismoke_female = [0, 0.13386833786546262, 0.56200858012438537, 0.66749593377502547, 0.84948177644830847]

    # Polynomial transformations
    dage = age / 10
    age_1 = dage ** -2
    age_2 = dage
    dbmi = bmi / 10
    bmi_1 = dbmi ** -2
    bmi_2 = dbmi ** -2 * np.log(dbmi)

    # Centering continuous variables
    age_1 -= 0.053274843841791
    age_2 -= 4.332503318786621
    bmi_1 -= 0.154946178197861
    bmi_2 -= 0.144462317228317
    rati -= 3.47632646560669
    sbp -= 123.13001251220703
    sbps5 -= 9.002537727355957
    town -= 0.392308831214905

    # Start of Sum
    a = 0

    # Add ethnicity and smoking coefficients
    a += Iethrisk_female[ethrisk]
    a += Ismoke_female[smoke_cat]

    # Add continuous variables contributions
    a += age_1 * -8.1388109247726188
    a += age_2 * 0.79733376689699098
    a += bmi_1 * 0.29236092275460052
    a += bmi_2 * -4.1513300213837665
    a += rati * 0.15338035820802554
    a += sbp * 0.013131488407103424
    a += sbps5 * 0.0078894541014586095
    a += town * 0.077223790588590108

    # Add boolean values contributions
    a += b_AF * 1.5923354969269663
    a += b_atypicalantipsy * 0.25237642070115557
    a += b_corticosteroids * 0.59520725304601851
    a += b_migraine * 0.301267260870345
    a += b_ra * 0.21364803435181942
    a += b_renal * 0.65194569493845833
    a += b_semi * 0.12555308058820178
    a += b_sle * 0.75880938654267693
    a += b_treatedhyp * 0.50931593683423004
    a += b_type1 * 1.7267977510537347
    a += b_type2 * 1.0688773244615468
    a += fh_cvd * 0.45445319020896213

    # Interaction terms
    a += age_1 * (smoke_cat == 1) * -4.7057161785851891
    a += age_1 * (smoke_cat == 2) * -2.7430383403573337
    a += age_1 * (smoke_cat == 3) * -0.86608088829392182
    a += age_1 * (smoke_cat == 4) * 0.90241562369710648

    # Calculate the score
    score = 100.0 * (1 - pow(survivor_female[surv], np.exp(a)))
    return score

def qrisk3_male(age, b_AF, b_atypicalantipsy, b_corticosteroids, b_impotence2, b_migraine, b_ra, b_renal, b_semi, b_sle, b_treatedhyp, b_type1, b_type2, bmi, ethrisk, fh_cvd, rati, sbp, sbps5, smoke_cat, surv, town):
    # Survivor function for males
    survivor_male = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.977268040180206, 0, 0, 0, 0, 0]

    # Ethnicity risk and smoking categories for males
    Iethrisk_male = [0, 0, 0.27719248760308279, 0.47446360714931268, 0.52961729919689371, 0.035100159186299017, -0.35807899669327919, -0.4005648523216514, -0.41522792889830173, -0.26321348134749967]
    Ismoke_male = [0, 0.19128222863388983, 0.55241588192645552, 0.63835053027506072, 0.78983819881858019]

    # Polynomial transformations
    dage = age / 10
    age_1 = dage ** -1
    age_2 = dage ** 3
    dbmi = bmi / 10
    bmi_1 = dbmi ** -2
    bmi_2 = dbmi ** -2 * np.log(dbmi)

    # Centering continuous variables
    age_1 -= 0.234766781330109
    age_2 -= 77.284080505371094
    bmi_1 -= 0.149176135659218
    bmi_2 -= 0.141913309693336
    rati -= 4.300998687744141
    sbp -= 128.57157897949219
    sbps5 -= 8.756621360778809
    town -= 0.52630490064621

    # Start of Sum
    a = 0

    # Add ethnicity and smoking coefficients
    a += Iethrisk_male[ethrisk]
    a += Ismoke_male[smoke_cat]

    # Add continuous variables contributions
    a += age_1 * -17.839781666005575
    a += age_2 * 0.0022964880605765492
    a += bmi_1 * 2.4562776660536358
    a += bmi_2 * -8.3011122314711354
    a += rati * 0.17340196856327111
    a += sbp * 0.012910126542553305
    a += sbps5 * 0.010251914291290456
    a += town * 0.033268201277287295

    # Add boolean values contributions
    a += b_AF * 0.88209236928054657
    a += b_atypicalantipsy * 0.13046879855173513
    a += b_corticosteroids * 0.45485399750445543
    a += b_impotence2 * 0.22251859086705383
    a += b_migraine * 0.25584178074159913
    a += b_ra * 0.20970658013956567
    a += b_renal * 0.71853261288274384
    a += b_semi * 0.12133039882047164
    a += b_sle * 0.4401572174457522
    a += b_treatedhyp * 0.51659871082695474
    a += b_type1 * 1.2343425521675175
    a += b_type2 * 0.85942071430932221
    a += fh_cvd * 0.54055469009390156

    # Calculate the score
    score = 100.0 * (1 - pow(survivor_male[surv], np.exp(a)))
    return score

# Example usage:
age = 45
b_AF = 0
b_atypicalantipsy = 0
b_corticosteroids = 0
b_migraine = 0
b_ra = 0
b_renal = 0
b_semi = 0
b_sle = 0
b_treatedhyp = 0
b_type1 = 0
b_type2 = 0
b_impotence2 = 0
bmi = 25
ethrisk = 2  # Example ethnicity category
fh_cvd = 0
rati = 3.5
sbp = 120
sbps5 = 10
smoke_cat = 1
surv = 10  # Example survival index (for 10-year risk)
town = 0

# Female example
female_score = qrisk3_female(age, b_AF, b_atypicalantipsy, b_corticosteroids, b_migraine, b_ra, b_renal, b_semi, b_sle, b_treatedhyp, b_type1, b_type2, bmi, ethrisk, fh_cvd, rati, sbp, sbps5, smoke_cat, surv, town)
print(f"Female QRISK3 score: {female_score:.2f}%")

# Male example
male_score = qrisk3_male(age, b_AF, b_atypicalantipsy, b_corticosteroids, b_impotence2, b_migraine, b_ra, b_renal, b_semi, b_sle, b_treatedhyp, b_type1, b_type2, bmi, ethrisk, fh_cvd, rati, sbp, sbps5, smoke_cat, surv, town)
print(f"Male QRISK3 score: {male_score:.2f}%")
