import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from obspy import read
import numpy as np
import pandas as pd
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
# Load the trained model
model = load_model('/home/boomermath/keras_nasa/quake_detector_model(proximity)-CNN.h5')
stream = read("XB.ELYSE.02.BHV.2022-01-02HR04_evid0006.mseed")
trace = stream[0]

data = trace.data
sampling_rate = trace.stats.sampling_rate

n_samples = len(data)
time_rel = np.arange(0, n_samples / sampling_rate, 1 / sampling_rate)

test_file = "/home/boomermath/keras_nasa/XB.ELYSE.02.BHV.2022-01-02HR04_evid0006.csv"
test_df = pd.read_csv(test_file)

test_df['proximity'] = [0] * len(test_df.index)

# Prepare the test data similar to how you prepared the training data
test_X = test_df[['proximity', 'velocity(c/s)']].values

# Reshape X for CNN (samples, time_steps, features)
time_steps = 501  # Adjust according to your model's time step requirement
X_test = []
for i in range(len(test_X) - time_steps):
    X_test.append(test_X[i:i + time_steps])

X_test = np.array(X_test)

# Make predictions
predictions = model.predict(X_test)
low_indices = np.where(predictions.flatten() < 10)[0]

# Plot the results
plt.figure(figsize=(15, 5))

# Plot all predictions
plt.plot(test_df['rel_time(sec)'][time_steps:], predictions, label='All Predictions', alpha=0.3)

# Plot low predictions (< 0.1)
plt.scatter(test_df['rel_time(sec)'][low_indices + time_steps], predictions, 
            color='blue', zorder=5)

# Plot styling
plt.xlabel('Time (seconds)')
plt.ylabel('Prediction Probability')
plt.legend()
plt.grid(True)

# Show plot
plt.savefig('predictions.png')