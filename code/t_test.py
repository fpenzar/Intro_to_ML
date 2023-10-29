import numpy as np, scipy.stats as st

h = [10,
     20,
     20,
     20,
     10,
     20,
     20,
     20,
     20,
     20]
ann_errors = np.array([0.20281014,
              0.03983368,
              0.14218998,
              0.67990446,
              0.07951842,
              0.36458257,
              0.21444683,
              0.07517657,
              0.37753469,
              0.1882015])

lambdas = [10,
           1,
           10,
           0.001,
           10,
           10,
           1,
           1,
           1,
           10]
lr_errors = np.array([0.40166299,
             0.11244909,
             0.16395216,
             0.35900188,
             0.20939178,
             0.49028755,
             0.47163486,
             0.27765619,
             0.28006732,
             0.38111609])

baseline_errors = np.array([1.32575258,
                   0.87544597,
                   0.90657379,
                   0.88410836,
                   0.77788476,
                   1.64789031,
                   0.81078369,
                   0.69534558,
                   0.77386508,
                   1.03508353])

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
