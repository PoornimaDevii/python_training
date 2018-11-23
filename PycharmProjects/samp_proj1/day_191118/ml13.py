# Dimensionality reduction

# pertains to unsupervised learning -> one or more features are considered as one important feature

# Correlation

from scipy.stats import pearsonr

print(pearsonr([1,2,3],[1,2,3.1]))
print(pearsonr([1,2,3],[3,2,1]))
print(help(pearsonr))