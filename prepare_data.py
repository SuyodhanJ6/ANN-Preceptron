import Preceptron1

class Prepare_Data:
    """
    This class shall be used for Preparing Data. 
    """
    
    def __init__(self):
        pass

    def prepare_data(self, df, target_col="y"):
        """
        Method Name  : prepare_data
        Description  : Splitting data into dependant y and label X.
        OutPut       : Array
        On Failure   : None
        
        Written By: prashantmalge181@gmail.com
        """
        X = df.drop(target_col, axis=1)
        
        y = df[target_col]
        
        return X, y 