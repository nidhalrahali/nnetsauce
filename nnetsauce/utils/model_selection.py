"""Model selection"""

# Authors: Thierry Moudiki
#
# License: BSD 3

# MTS -----

import numpy as np
from sklearn.model_selection import TimeSeriesSplit


class TimeSeriesSplit(TimeSeriesSplit):
    """Time Series cross-validator"""
    
    def __init__(self, n_splits=3, max_train_size=None):
        super().__init__(n_splits=n_splits, 
             max_train_size=max_train_size)
        
    
    def split(self, X, initial_window, horizon=3, fixed_window=False):
        """Generate indices to split data into training and test set.

        Parameters
        ----------
        X : array-like, shape (n_samples, n_features)
            Training data, where n_samples is the number of samples
            and n_features is the number of features.

        initial_window : int, initial number of consecutive values in each 
                         training set sample
        
        horizon : int, number of consecutive values in test set sample
        
        fixed_window : boolean, if False, all training samples start at index 0

        Yields
        ------
        train : ndarray
            The training set indices for that split.

        test : ndarray
            The testing set indices for that split.
        """
        # assert initial_window
        # assert horizon
        # assert fixed_window
        
        n, p = X.shape
        
        # Initialization of indices -----
        
        indices = np.arange(n)
        n_splits = 0   
        
        # train index 
        min_index_train = 0
        max_index_train = initial_window - 1
        
        # test index 
        min_index_test = max_index_train
        max_index_test = initial_window + horizon - 1
        
        
        # Main loop -----
        
        if fixed_window == True: 

            while (max_index_test <= (n-1)):  
                    
                    yield (indices[min_index_train:max_index_train],
                           indices[min_index_test:max_index_test])
                    
                    min_index_train = min_index_train + 1 
                    min_index_test = min_index_test + 1 
                    max_index_train = max_index_train + 1 
                    max_index_test = max_index_test + 1 
                    
                    n_splits = n_splits + 1 
                    
        else: 
            
            while (max_index_test <= (n-1)):  
                    
                    yield (indices[min_index_train:max_index_train],
                           indices[min_index_test:max_index_test])
                    
                    max_index_train = max_index_train + 1 
                    min_index_test = min_index_test + 1 
                    max_index_test = max_index_test + 1                
                    
                    n_splits = n_splits + 1 
        
        
        # set n_splits after (?)
        self.n_splits = n_splits
        self.max_train_size = max_index_train + 1