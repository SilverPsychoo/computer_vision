import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, classification_report

## Fijar pseudoaleatoriedad
SEED = 42
np.random.seed(SEED)
tf.random.set_seed(SEED)


## Cargar datasets
iris = load_iris()
X = iris.data.astype(np.float32) # Características
y = iris.target.astype(np.int32) # Etiquetas
class_names = iris.target_names # Nombre de las clases

print("Nombre de las clases", class_names)
print("Forma de X:", X.shape)
print("Shape de Y", y.shape)


# División del dataset
# Datos de entrenamiento (70%), datos temporales (30%)
X_train, X_temp, y_train, y_temp = train_test_split(
    X, y,
    test_size = 0.3,
    random_state = SEED,
    stratify = y
)
# Datos del testing y validation (50% del 30%)
X_val, X_test, y_val, y_test = train_test_split(
    X_temp, y_temp,
    test_size = 0.5,
    random_state = SEED,
    stratify = y_temp
)

print("Shape del dataset")
print("Train:", X_train.shape, y_train.shape)
print("Val:", X_val.shape, y_val.shape)
print("Test:", X_test.shape, y_test.shape)

# Normalización - (Escalado)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_val = scaler.transform(X_val)
X_test = scaler.transform(X_test)

# Construcción del modelo
def build_model(input_dim):
    inputs = tf.keras.Input(shape=(input_dim,))
    x = tf.keras.layers.Dense(
        64,
        activation = "relu",
        kernel_regularizer = tf.keras.regularizers.l2(1e-4)
        )(inputs)
    x = tf.keras.layers.Dropout(0.25)(x)
    x = tf.keras.layers.Dense(
        32,
        activation = "relu",
        kernel_regularizer = tf.keras.regularizers.l2(1e-4)
        )(inputs)
    x = tf.keras.layers.Dropout(0.20)(x)
    outputs = tf.keras.layers.Dense(
        3,
        activation = "softmax",
        )(x)
    return tf.keras.Model(inputs, outputs)

model = build_model(X_train.shape[1])
model.summary()

lr = 0.01
# Compilación de modelo 
model.compile(
    optimizer = tf.keras.optimizers.Adam(learning_rate = lr),
    loss = tf.keras.losses.SparseCategoricalCrossentropy(),
    metrics = ["accuracy"]
)

print("\nResumen del modelo \t")
model.summary()

# Callbacks
callbacks = [
    tf.keras.callbacks.EarlyStopping(
        monitor="val_loss",
        mode ="max", patience=10,
        restore_best_weights=True)
]

# Training
history = model.fit(
    X_train, y_train,
    validation_data = (X_val, y_val),
    epochs = 150,
    batch_size = 16,
    verbose = 1
)

# Evaluación de los datos de testing
test_loss, test_acc = model.evaluate(X_test, y_test, verbose=0)

print("Resultados")
print("Pérdida testing:", test_loss )
print("Accuracy testing:", test_acc)