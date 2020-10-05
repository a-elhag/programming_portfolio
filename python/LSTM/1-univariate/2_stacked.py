import numpy as np
import keras
from keras.layers import LSTM
from keras.layers import Dense

# split a univariate sequence into samples
def split_sequence(sequence, n_steps):
    X, y = list(), list()
    for i in range(len(sequence)):
        idx_end = i+n_steps
        if idx_end > len(sequence)-1:
            break

        seq_X, seq_y = sequence[i:idx_end], sequence[idx_end]
        X.append(seq_X)
        y.append(seq_y)

    return np.array(X), np.array(y)


row_seq = [10, 20, 30, 40, 50, 60, 70, 80, 90]
n_steps = 3
X, y = split_sequence(row_seq, n_steps)

# [samples, timesteps, features]
n_features = 1
X = X.reshape((X.shape[0], X.shape[1], n_features))

# define model
model = keras.models.Sequential()
model.add(LSTM(50, activation = 'relu',
               return_sequences=True, input_shape=(n_steps, n_features)))
model.add(LSTM(50, activation = 'relu', input_shape=(n_steps, n_features)))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mse')

# fit model
model.fit(X, y, epochs=200, verbose=0)

# predicting
x_input = np.array([70, 80, 90])
x_input = x_input.reshape((1, n_steps, n_features))

yhat = model.predict(x_input, verbose=0)
print(yhat)
