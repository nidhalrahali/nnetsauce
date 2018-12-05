import numpy as np
from numpy import linalg as la
import matrixops as mo


# in alphabetical order
# computes beta_hat = (t(x)%*%x + lam*I)^{-1}%*%t(x)%*%y    
def beta_hat(x, y, lam = 0.1):
    # assert on dimensions
    return np.dot(inv_penalized_cov(x, lam), 
                  mo.crossprod(x, y))


# computes (t(x)%*%x + lam*I)^{-1}
def inv_penalized_cov(x, lam = 0.1):
    # assert on dimensions
    if lam == 0:
        return la.inv(mo.crossprod(x))
    else:
        return la.inv(mo.crossprod(x) + lam*np.eye(x.shape[1]))

    
# beta and Sigma in Bayesian Ridge Regression 1 
# without intercept! without intercept! without intercept!        
def beta_Sigma_hat_rvfl(X, y, 
                        s=0.1, sigma=0.05, 
                        fit_intercept=False,
                        X_star=None, # check when dim = 1 # check when dim = 1
                        return_cov=True):
    
    if len(X.shape) == 1:
        X = X.reshape(-1, 1)
    
    if (X_star is not None):
        if (len(X_star.shape) == 1):
            X_star = X_star.reshape(-1, 1)
    
    n, p = X.shape
    
    if fit_intercept == True:
        X = mo.cbind(np.ones(n), X)
        if X_star is not None:
            X_star = mo.cbind(np.ones(X_star.shape[0]), 
                                      X_star)
        
    s2 = s**2
    lambda_ = (sigma**2)/s2
    
    if return_cov == True:
        
        Cn = inv_penalized_cov(X, lam = lambda_)
        beta_hat_ = np.dot(Cn, mo.crossprod(X, y))
        Sigma_hat_ = s2*(np.eye(X.shape[1]) - np.dot(Cn, mo.crossprod(X))) 
        
        if X_star is None:
            
            return {'beta_hat': beta_hat_, 
                    'Sigma_hat': Sigma_hat_}

        else:
            
            return {'beta_hat': beta_hat_, 
                    'Sigma_hat': Sigma_hat_,
                    'preds': np.dot(X_star, beta_hat_),
                    'preds_std': np.sqrt(np.diag(np.dot(X_star, 
                                         mo.tcrossprod(Sigma_hat_, X_star)) + \
                                        (sigma**2)*np.eye(X_star.shape[0])))
                    }
                    
    else: # return_cov == False
        
        if X_star is None:
            
            return {'beta_hat': beta_hat(X, y, 
                                         lam = lambda_)}
            
        else:
            
            beta_hat_ = beta_hat(X, y, 
                                lam = lambda_)
            
            return {'beta_hat': beta_hat_, 
                    'preds_std': np.dot(X_star, 
                                        beta_hat_)
                    }
            
            
# beta and Sigma in Bayesian Ridge Regression 2
# without intercept! without intercept! without intercept!
def beta_Sigma_hat_rvfl2(X, y, 
                         Sigma=None, 
                         sigma=0.05,
                         fit_intercept=False,
                         X_star=None, # check when dim = 1 # check when dim = 1
                         return_cov=True):
    
    if len(X.shape) == 1:
        X = X.reshape(-1, 1)
   
    n, p = X.shape
    
    if Sigma is None:
        if fit_intercept == True:
            Sigma = np.eye(p + 1)
        else: 
            Sigma = np.eye(p)
    
    if (X_star is not None):
        if (len(X_star.shape) == 1):
            X_star = X_star.reshape(-1, 1)
    
    if fit_intercept == True:
        
        X = mo.cbind(np.ones(n), X)
        Cn = la.inv(np.dot(Sigma, mo.crossprod(X)) + \
                (sigma**2)*np.eye(p + 1))
        
        if X_star is not None:
            X_star = mo.cbind(np.ones(X_star.shape[0]), 
                                      X_star)
    else:
        
        Cn = la.inv(np.dot(Sigma, mo.crossprod(X)) + \
                (sigma**2)*np.eye(p))
        
    temp = np.dot(Cn, mo.tcrossprod(Sigma, X))
    
    if return_cov == True:
        
        if X_star is None:       
            
            return {'beta_hat': np.dot(temp, y), 
                    'Sigma_hat': Sigma - np.dot(temp, np.dot(X, Sigma))}
            
        else:
            
            beta_hat_ = np.dot(temp, y)
            Sigma_hat_ = Sigma - np.dot(temp, np.dot(X, Sigma))
            
            return {'beta_hat': beta_hat_, 
                    'Sigma_hat': Sigma_hat_,
                    'preds': np.dot(X_star, beta_hat_), 
                    'preds_std': np.sqrt(np.diag(np.dot(X_star, 
                                 mo.tcrossprod(Sigma_hat_, X_star)) + \
                                 (sigma**2)*np.eye(X_star.shape[0])))
                    } 
        
    else:
        
        if X_star is None:       
            
            return {'beta_hat': np.dot(temp, y)}
        
        else:
            
            beta_hat_ = np.dot(temp, y)
            
            return {'beta_hat': beta_hat_,
                    'preds': np.dot(X_star, beta_hat_)
                    }