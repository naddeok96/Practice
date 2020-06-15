'''
This code will open a tdms file, convert it to a numpy array then
save it as a text file
'''
# Imports
from nptdms import TdmsFile as tdms
import numpy as np
import matplotlib.pyplot as plt

# Hyperparameters
file_name = "enter_name_here" # do not add extension and it must be a string object

# Load tdms file
tdms_file = tdms(file_name + ".tdms")

# Convert ECG signal to numpy
ecg_signal = tdms_file.object('Data',' Direct ECG').data

# Save signal
plt.plot(ecg_signal)
plt.show()
np.savetxt("ecg_" + file_name + '.csv', ecg_signal, delimiter=',')
