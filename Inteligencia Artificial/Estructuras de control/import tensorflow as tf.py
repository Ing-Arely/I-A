import tensorflow as tf  
import numpy as np

celsius = np.array ([-40, -10, 0, 8, 15, 22, 38], dtype=float)
fahrenheit = np.array ([-40, -14, 32, 46, 59, 72, 100], dtype=float)
machine learning

capa = tf. keras. layers.Dense(units=1, input_shape=[1], activation= 'linear')
modelo = tf. keras.Sequential ([capa])

modelo.compile(

optimizer = tf.keras.optimizers.Adam(0.1),
loss= stream_squared_error
)
modelo.fit(celsius, fahrenheit, epochs=500)