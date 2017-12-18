from keras.models import Sequential
from keras.models import Dense
from keras.callbacks import TensorBoard
from keras import optimizers

## Dane wejściowe

LAYERS = [30, 30, 1]
LEARNING_RATE = 0.001
DECAY = 0
MODEL = Sequential()

TENSORBOARD = TensorBoard(log_dir='./logs',
                          histogram_freq=5,
                          batch_size=32,
                          write_graph=True,
                          write_grads=False,
                          write_images=False,
                          embeddings_freq=0,
                          embeddings_layer_names=None,
                          embeddings_metadata=None)

for i in range(0, len(LAYERS)):
    if i == 0:
        MODEL.add(Dense(LAYERS[i], input_dim=2, activation="sigmoid"))
    elif i == len(LAYERS) - 1:
        MODEL.add(Dense(LAYERS[i], activation="linear"))
    else:
        MODEL.add(Dense(LAYERS[i], activation="sigmoid"))

ADAM = optimizers.Adam(lr=LEARNING_RATE, beta_1=0.9, beta_2=0.999, epsilon=1e-8, decay=DECAY)
MODEL.compile(loss='mean_squared_error', optimizer=ADAM, metrics=['accuracy'])
