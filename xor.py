# Importing Libraries
import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import joblib
from matplotlib.colors import ListedColormap
plt.style.use("fivethirtyeight") 
import prepare_data
import Preceptron1

class Solution:
    """
    This Class shall be used for Predecting The value.
    
    Written By: prashantmalge181@gmail.com
    """
    def __init__(self):
        pass
    
    def xorPredict(self, XOR):
        """
        Method Name  : xorPredict
        Description  : Predict the XOR table using preceptron.
        OutPut       : --
        On Failure   : None
        
        Written By: prashantmalge181@gmail.com
        """
        df_XOR = pd.DataFrame(XOR)

        print(df_XOR)


        X, y = prepare_data.Prepare_Data.prepare_data(self, df_XOR)

        ETA = 0.1 # 0 and 1
        EPOCHS = 10

        model_and = Preceptron1.Perceptron(eta=ETA, epochs=EPOCHS)
        model_and.fit(X, y)

        _ = model_and.total_loss()

        # Saving Model
        model_and.save(filename="xor.model", model_dir="model_xor")

    

# # How to use and Model
# reload_model_and = Preceptron1.Perceptron().load(filepath="model/xor.model")
# print(f"Predicted Values is : {reload_model_and.predict(X=[[1,1]])}")
"""
    Type : Array
"""

XOR = {
    "x1": [0,0,1,1],
    "x2": [0,1,0,1],
    "y" : [0,1,1,0]
}

o = Solution()
print(o.xorPredict(XOR))