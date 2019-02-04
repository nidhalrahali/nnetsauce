"""MTS model"""

# Authors: Thierry Moudiki <thierry.moudiki@gmail.com>
#
# License: MIT

import numpy as np
import sklearn.model_selection as skm
from ..base import Base
from ..utils import matrixops as mo
from ..utils import misc as mx
from ..utils import timeseries as ts


class MTS(Base):
    """MTS model class derived from class Base
    
       Parameters
       ----------
       obj: object
           any object containing a method fit (obj.fit()) and a method predict 
           (obj.predict())
       n_hidden_features: int
           number of nodes in the hidden layer
       activation_name: str
           activation function: 'relu', 'tanh', 'sigmoid', 'prelu' or 'elu'
       a: float
           hyperparameter for 'prelu' or 'elu' activation function
       nodes_sim: str
           type of simulation for the nodes: 'sobol', 'hammersley', 'halton', 
           'uniform'
       bias: boolean
           indicates if the hidden layer contains a bias term (True) or not 
           (False)
       direct_link: boolean
           indicates if the original predictors are included (True) in model's 
           fitting or not (False)
       n_clusters: int
           number of clusters for 'kmeans' or 'gmm' clustering (could be 0: 
               no clustering)
       type_clust: str
           type of clustering method: currently k-means ('kmeans') or Gaussian 
           Mixture Model ('gmm')
       seed: int 
           reproducibility seed for nodes_sim=='uniform'
       type_fit: str
           'regression' or 'classification'
    """
    
    # construct the object -----
    
    def __init__(self, obj,
                 n_hidden_features=5, 
                 activation_name='relu',
                 a=0.01,
                 nodes_sim='sobol',
                 bias=True,
                 direct_link=True, 
                 n_clusters=2,
                 type_clust='kmeans',
                 seed=123): 
                
        super().__init__(n_hidden_features = n_hidden_features, 
                         activation_name = activation_name, a = a,
                         nodes_sim = nodes_sim, bias = bias, 
                         direct_link = direct_link,
                         n_clusters = n_clusters, 
                         type_clust = type_clust, 
                         seed = seed)
        
        self.obj = obj
        self.response = None
        self.lags = None


    def get_params(self):
        
        return super().get_params()

    
    def set_params(self, n_hidden_features=5, 
                   activation_name='relu', 
                   a=0.01,
                   nodes_sim='sobol',
                   bias=True,
                   direct_link=True,
                   n_clusters=None,
                   type_clust='kmeans',
                   seed=123):
        
        super().set_params(n_hidden_features = n_hidden_features, 
                           activation_name = activation_name, a = a,
                           nodes_sim = nodes_sim, bias = bias, 
                           direct_link = direct_link, n_clusters = n_clusters, 
                           type_clust = type_clust, seed = seed)
 
    
    def fit(self, X, **kwargs):
        """Fit MTS model to training data (X, y).
        
        Parameters
        ----------
        X: {array-like}, shape = [n_samples, n_features]
            Training vectors, where n_samples is the number 
            of samples and n_features is the number of features.
        
        y: array-like, shape = [n_samples]
               Target values.
    
        **kwargs: additional parameters to be passed to 
                  self.cook_training_set
               
        Returns
        -------
        self: object
        """
        
        scaled_Z = self.cook_training_set(y = y, X = X, 
                                          **kwargs)
        
        self.obj.fit(scaled_Z, y, **kwargs)
        
        return self

    
    def predict(self, h = 5, **kwargs):
        """Predict on horizon h.
        
        Parameters
        ----------
        h: {integer}
            Forecasting horizon
        
        **kwargs: additional parameters to be passed to 
                  self.cook_test_set
               
        Returns
        -------
        model predictions for a horizon = h: {array-like}
        """
        
        if len(X.shape) == 1:
            
            n_features = X.shape[0]
            new_X = mo.rbind(X.reshape(1, n_features), 
                             np.ones(n_features).reshape(1, n_features))        
            
            if self.type_fit == "regression":
                
                return (self.y_mean + self.obj.predict(self.cook_test_set(new_X, 
                                                                             **kwargs), 
                                                   **kwargs))[0]
                
        else:
            
            if self.type_fit == "regression":
            
                return self.y_mean + self.obj.predict(self.cook_test_set(X, 
                                                                        **kwargs), 
                                               **kwargs)         
        