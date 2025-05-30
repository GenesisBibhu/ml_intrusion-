#import joblib
#import numpy as np
#import os

# Path to the trained model file
#
# Load the model
#model = joblib.load(model_path)
#
# #  """
  #  Predicts whether the input indicates an intrusion or not.
#
  #  Args:
  #      input_data (list of float): Features to be passed to the model.
#
  #  Returns:
  #      int: 1 if intrusion, 0 if safe.
  #  """
  #  input_array = np.array(input_data).reshape(1, -1)
   # prediction = model.predict(input_array)
   # return prediction[0]


import joblib
import numpy as np
import os

# Load the trained model
model_path = os.path.join(os.path.dirname(__file__), 'connrf_model.pkl')
model = joblib.load(model_path)

def predict_intrusion(input_data):
    """
    Predicts whether the input data indicates an intrusion.
    
    Parameters:
    input_data (list or array-like): A list of 5 numeric features in the order:
        [ConnectionFrequency, IpReputationScore, Packet_Size, Active_Duration, Flow_Bytes_per_s]

    Returns:
    int: 1 if intrusion is detected, 0 otherwise.
    """
    if not isinstance(input_data, (list, np.ndarray)) or len(input_data) != 5:
        raise ValueError("Input must be a list or array of exactly 5 numeric features.")
    
    input_array = np.array(input_data).reshape(1, -1)
    prediction = model.predict(input_array)
    return int(prediction[0])
