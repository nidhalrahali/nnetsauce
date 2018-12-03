import numpy as np
import psdcheck as psdx
import matrixops as mo
import misc as mx
import lmfuncs as lmf 
from sklearn import datasets
import matplotlib.pyplot as plt  

# Basic tests


# 1 - matrix_ops -----

A = 2*np.eye(4)

print("1 - matrix_ops ----- \n")
print("A = ")
print(A)
print("\n")
print("mo.crossprod(A) = ")
print(mo.crossprod(A))
print("\n")
print("mo.tcrossprod(A) = ")
print(mo.tcrossprod(A))
print("\n")
print("mo.crossprod(A, np.eye(4)) = ")
print(mo.crossprod(A, np.eye(4)))
print("\n")
print("mo.tcrossprod(A, np.eye(4)) = ")
print(mo.tcrossprod(A, np.eye(4)))
print("\n")
print("mo.cbind(A, A)")
print(mo.cbind(A, A))
print("\n")
print("mo.rbind(A, A)")
print(mo.rbind(A, A))
print("\n")

# 2 - misc -----

x = {"a": 3, "b": 5}
y = {"c": 1, "d": 4}

print("2 - misc ----- \n")
print("x")
print(x)
print("y")
print(y)
print("\n")
print(mx.merge_two_dicts(x, y))
print("\n")


# 3 - psd_check -----

print("3 - psd_check ----- \n")

print("Test for isPD")
print(psdx.isPD(A))
print("\n")
print("Test for nearestPD")
print(psdx.nearestPD(A))
print("\n")


# 4 - psd_check -----

diabetes = datasets.load_diabetes()

# define X and y
X = diabetes.data 
y = diabetes.target

print("lmf.beta_hat(X, y, lam = 0.1)")
print(lmf.beta_hat(X, y, lam = 0.1))
print("\n")
print("lmf.inv_penalized_cov(X, lam = 0.1)")
print(lmf.inv_penalized_cov(X, lam = 0.1))
print("\n")

# 5 - lm_funcs -----

# fit training set 

import numpy as np

sigma = 0.3 
s = 0.1
n_points = 25 

np.random.seed(1223)
x = np.linspace(1, 25, num=n_points)
y = 20*np.random.rand(n_points) - 10

print("4 - Bayesian Ridge ----- \n")

print('----- beta_Sigma_hat: fit_intercept = True, return_cov = True')
print("\n")
print(lmf.beta_Sigma_hat_rvfl(x = x, y = y,
                              s = s, sigma = sigma,
                              fit_intercept = True,
                              return_cov = True))
print("\n")

print('----- beta_Sigma_hat: fit_intercept = True, return_cov = False')
print("\n")
print(lmf.beta_Sigma_hat_rvfl(x = x, y = y,
                              s = s, sigma = sigma,
                              fit_intercept = True,
                              return_cov = False))
print("\n")

print('----- beta_Sigma_hat: fit_intercept = False, return_cov = False')
print("\n")
print(lmf.beta_Sigma_hat_rvfl(x = x, y = y,
                              s = s, sigma = sigma,
                              fit_intercept = False,
                              return_cov = False))
print("\n")

print('----- beta_Sigma_hat: fit_intercept = False, return_cov = True')
print("\n")
print(lmf.beta_Sigma_hat_rvfl(x = x, y = y,
                              s = s, sigma = sigma,
                              fit_intercept = False,
                              return_cov = True))
print("\n")

print('----- beta_Sigma_hat: fit_intercept = True, return_cov = True, x_star')
print("\n")
print(lmf.beta_Sigma_hat_rvfl(x = x, y = y, x_star = x,
                              s = s, sigma = sigma,
                              fit_intercept = True,
                              return_cov = True))
print("\n")

print('----- beta_Sigma_hat: fit_intercept = True, return_cov = False, x_star')
print("\n")
print(lmf.beta_Sigma_hat_rvfl(x = x, y = y, x_star = x,
                              s = s, sigma = sigma,
                              fit_intercept = True,
                              return_cov = False))
print("\n")

print('----- beta_Sigma_hat: fit_intercept = False, return_cov = False, x_star')
print("\n")
print(lmf.beta_Sigma_hat_rvfl(x = x, y = y, x_star = x,
                              s = s, sigma = sigma,
                              fit_intercept = False,
                              return_cov = False))
print("\n")

print('----- beta_Sigma_hat:  fit_intercept = False, return_cov = True, x_star')
print("\n")
print(lmf.beta_Sigma_hat_rvfl(x = x, y = y, x_star = x,
                              s = s, sigma = sigma,
                              fit_intercept = False,
                              return_cov = True))
print("\n")

## without intercept

fit_obj = lmf.beta_Sigma_hat_rvfl(x = x, y = y, x_star = x,
                                  s = s, sigma = sigma,
                                  fit_intercept = False,
                                  return_cov = True)

y_hat = fit_obj['preds']
y_std = fit_obj['std']

plt.scatter(x, y, color='black')
plt.fill_between(x, y_hat - 1.96*y_std,  
                 y_hat + 1.96*y_std, 
                 color = 'gray', 
                 alpha = 0.4)
plt.plot(x, y_hat)
plt.title('fits vs obs')
plt.xlabel('x')
plt.ylabel('fits')
plt.show()

# 5 - lm_funcs -----

diabetes = datasets.load_diabetes()

# define X and y
X = diabetes.data 
y = diabetes.target

fit_obj = lmf.beta_Sigma_hat_rvfl(x = X[0:350,:], y = y[0:350], 
                                  x_star = X[350:442,:],
                                  s = s, sigma = sigma,
                                  fit_intercept = True,
                                  return_cov = True)

y_hat = fit_obj['preds']
y_std = fit_obj['std']

x = range(92)

plt.scatter(x, y[350:442], color='black')
plt.fill_between(x, y_hat - 1.96*y_std,  
                 y_hat + 1.96*y_std, 
                 color = 'gray', 
                 alpha = 0.4)
plt.plot(x, y_hat)
plt.title('fits vs obs')
plt.xlabel('x')
plt.ylabel('fits')
plt.show()