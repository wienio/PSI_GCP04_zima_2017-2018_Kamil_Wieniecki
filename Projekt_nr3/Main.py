from keras.models import Sequential
from keras.layers.core import Dense
from keras.callbacks import TensorBoard
from keras import optimizers
from prettytable import PrettyTable
from TestData import *

## Dane wejściowe

fill_test_input(0.5)
fill_random_test_input(1000)

LAYERS = [30, 30, 30, 1]
LEARNING_RATE = 0.4
BATCH_SIZE = 20
ERAS = 100000
DECAY = 0
MODEL = Sequential()

LOG_DIR = "./logs-lr" + str(LEARNING_RATE) + "-lay"
for lay in LAYERS:
    LOG_DIR += "-" + str(lay)

TENSORBOARD = TensorBoard(log_dir=LOG_DIR,
                          histogram_freq=5,
                          batch_size=100,
                          write_graph=True,
                          write_grads=False,
                          write_images=True,
                          embeddings_freq=0,
                          embeddings_layer_names=None,
                          embeddings_metadata=None
                          )

for i in range(0, len(LAYERS)):
    if i == 0:
        MODEL.add(Dense(LAYERS[i], input_dim=2, activation="sigmoid"))
    elif i == len(LAYERS) - 1:
        MODEL.add(Dense(LAYERS[i], activation="linear"))
    else:
        MODEL.add(Dense(LAYERS[i], activation="sigmoid"))

ADAM = optimizers.Adam(lr=LEARNING_RATE, beta_1=0.9, beta_2=0.999, epsilon=1e-08, decay=DECAY)
MODEL.compile(loss='mean_squared_error', optimizer=ADAM, metrics=['accuracy'])

MODEL.fit(  test_input,
            test_output,
            epochs=ERAS,
            batch_size=BATCH_SIZE,
            validation_data=(random_input, random_output),
            callbacks=[TENSORBOARD]
            )

RESULTS = MODEL.evaluate(random_input, random_output)

print("\n%s: %.2f%%" % (MODEL.metrics_names[1], RESULTS[1]*100))

print(MODEL.summary())
print("Learning rate =", LEARNING_RATE)

YHAT = MODEL.predict(random_input, verbose=0)
PRETTYTABLE = PrettyTable()
PRETTYTABLE.field_names = ['x1', 'x2', 'PREDICTED', 'EXPECTED']

for i in range(0, len(YHAT)):
    PRETTYTABLE.add_row([random_input[i][0], random_input[i][1], YHAT[i][0], random_output[i]])
print(PRETTYTABLE)

MODEL.save('model-sieci-' + str(LAYERS) +'-lr-' + str(LEARNING_RATE) + '-decay-' + str(DECAY) + '.h5')
