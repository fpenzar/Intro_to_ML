import numpy as np, scipy.stats as st

h = [20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 10.0]
ann_errors = np.array([0.8107708692550659, 0.39075276255607605, 0.8707024455070496, 0.8381874561309814, 0.24542424082756042, 0.24991504848003387, 0.49130159616470337, 0.22714824974536896, 0.5132558941841125, 0.48146501183509827])

lambdas = [10.0, 10.0, 1.0, 1.0, 10.0, 10.0, 1.0, 10.0, 10.0, 1.0]
lr_errors = np.array([0.6094261058805718, 0.2132922267969456, 0.5611793438773491, 0.6093703731147087, 0.2014942513288549, 0.1688532606947013, 0.23264255743535825, 0.13833495816475644, 0.1824120388047476, 0.18560740124989875])

baseline_errors = np.array([1.9051489154424734, 1.0220299429582904, 0.9817857042272544, 0.792193192540003, 0.6967674805334072, 0.9891891309728749, 0.4361199849885119, 0.951097223226031, 0.4987140223513846, 1.214402728900416])

# set alpha
alpha = 0.05

## COMPARE ANN and LR
# h0 => mean(ann_errors) == mean(lr_errors)
# h1 => mean(ann_errors) != mean(lr_errors)

z = ann_errors - lr_errors
# Confidence interval
CI = st.t.interval(1-alpha, len(z)-1, loc=np.mean(z), scale=st.sem(z))
# p-value
p = 2*st.t.cdf( -np.abs( np.mean(z) )/st.sem(z), df=len(z)-1) 

print(f"Confidence interval for mean difference (ANN and LR): {CI}")
print(f"p-value ANN and LR: {p}")


## COMPARE ANN and baseline
# h0 => mean(ann_errors) == mean(baseline_errors)
# h1 => mean(ann_errors) != mean(baseline_errors)

z = ann_errors - baseline_errors
# Confidence interval
CI = st.t.interval(1-alpha, len(z)-1, loc=np.mean(z), scale=st.sem(z))
# p-value
p = 2*st.t.cdf( -np.abs( np.mean(z) )/st.sem(z), df=len(z)-1) 

print(f"Confidence interval for mean difference (ANN and baseline): {CI}")
print(f"p-value ANN and baseline: {p}")


## COMPARE baseline and LR
# h0 => mean(baseline_errors) == mean(lr_errors)
# h1 => mean(baseline_errors) != mean(lr_errors)

z = lr_errors - baseline_errors
# Confidence interval
CI = st.t.interval(1-alpha, len(z)-1, loc=np.mean(z), scale=st.sem(z))
# p-value
p = 2*st.t.cdf( -np.abs( np.mean(z) )/st.sem(z), df=len(z)-1) 

print(f"Confidence interval for mean difference (baseline and LR): {CI}")
print(f"p-value baseline and LR: {p}")
