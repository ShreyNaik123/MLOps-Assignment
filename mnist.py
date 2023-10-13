import tensorflow as tf
from tensorflow.keras import layers
import os
print(tf.__version__)

dataset = tf.keras.datasets.mnist

(X_train, y_train), (X_test,y_test) = dataset.load_data()

X_train = X_train/255
X_test = X_test/255


input_layer = layers.Input(X_train.shape[1:])
x = layers.Flatten()(input_layer)
output_layer = layers.Dense(10, activation='softmax')(x)

model = tf.keras.Model(inputs=input_layer, outputs=output_layer)

model.compile(optimizer=tf.keras.optimizers.Adam(),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

history = model.fit(X_train, y_train, epochs=10, batch_size=128,validation_data=(X_test, y_test))

# Save weights
weights_path = os.path.join("weights", "model_weights.h5")

model.save_weights(weights_path)

print(f"Model weights saved to {weights_path}")