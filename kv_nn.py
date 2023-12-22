from numpy import *
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import SGD
import test

M = 16
# Création du modèle
model = Sequential()

# Ajout de la couche cachée avec 3 neurones
model.add(Dense(units=3, activation='sigmoid'))

# Ajout de la couche de sortie avec 1 neurone
model.add(Dense(units=1, activation='sigmoid'))

# Compilation du modèle avec l'optimiseur SGD (Stochastic Gradient Descent)
model.compile(optimizer=SGD(learning_rate=0.01), loss='binary_crossentropy', metrics=['accuracy'])

# Données d'entraînement factices
X_train = [test.bdserie[0:0+M]]
y_train = [test.bdserie[M]]

model.fit(X_train, y_train, epochs=10)

# Affichage des poids de la première couche après l'entraînement
weights_first_layer, biases_first_layer = model.layers[0].get_weights()
print("Poids de la première couche après rétropropagation du gradient :")
print(weights_first_layer.T)
print(shape(weights_first_layer.T))
print(biases_first_layer)
# Affichage des poids de la deuxième couche après l'entraînement
weights_second_layer, biases_second_layer = model.layers[1].get_weights()
print("\nPoids de la deuxième couche après rétropropagation du gradient :")
print(weights_second_layer.T)
print(shape(weights_second_layer.T))

