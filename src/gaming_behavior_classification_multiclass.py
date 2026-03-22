import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf 

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.metrics import roc_auc_score, average_precision_score
from sklearn.preprocessing import label_binarize

## Fijar pseudoaleatoriedad
SEED = 42
np.random.seed(SEED)
tf.random.set_seed(SEED)

## Cargar dataset
df = pd.read_csv("data\online_gaming_behavior_dataset.csv")

print(df.head())
print(df.columns)

# Target
target_col = "EngagementLevel"

y_raw = df[target_col]
X = df.drop(columns=[target_col])

# Quitar ID
X = X.drop(columns=["PlayerID"], errors="ignore")

# One-hot
X = pd.get_dummies(X)

# Limpiar datos
X = X.replace([np.inf, -np.inf], np.nan)
X = X.fillna(0)

# Labels
le = LabelEncoder()
y = le.fit_transform(y_raw)
class_names = le.classes_.astype(str)

print("Nombre de clases", class_names)
print("Shape de X:", X.shape)
print("Shape de Y", y.shape)

## División del dataset
X_train, X_temp, y_train, y_temp = train_test_split(
    X, y,
    test_size=0.3,
    random_state=SEED,
    stratify=y
)

X_val, X_test, y_val, y_test = train_test_split(
    X_temp, y_temp,
    test_size=0.5,
    random_state=SEED,
    stratify=y_temp
)

print("Shape del dataset")
print("Train:", X_train.shape, y_train.shape)
print("Val:", X_val.shape, y_val.shape)
print("Test:", X_test.shape, y_test.shape)

# Escalado
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_val = scaler.transform(X_val)
X_test = scaler.transform(X_test)

# Modelo (igual estilo clase)
def build_model(input_dim):

    inputs = tf.keras.Input(shape=(input_dim,))
    x = tf.keras.layers.Dense(
        32,
        activation="relu",
        kernel_regularizer=tf.keras.regularizers.l2(1e-4)
    )(inputs)
    x = tf.keras.layers.Dropout(0.2)(x)
    x = tf.keras.layers.Dense(
        16,
        activation="relu",
        kernel_regularizer=tf.keras.regularizers.l2(1e-4)
    )(x)
    x = tf.keras.layers.Dropout(0.15)(x)
    outputs = tf.keras.layers.Dense(
        len(class_names),
        activation="softmax"
    )(x)
    return tf.keras.Model(inputs, outputs)

model = build_model(X_train.shape[1])

# Compilación
model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
    loss=tf.keras.losses.SparseCategoricalCrossentropy(),
    metrics=["accuracy"]
)

print("\nResumen del modelo")
model.summary()

# Early stopping
callbacks = [
    tf.keras.callbacks.EarlyStopping(
        monitor="val_loss",
        patience=10,
        restore_best_weights=True
    )
]

# Training
history = model.fit(
    X_train, y_train,
    validation_data=(X_val, y_val),
    epochs=300,
    batch_size=32,
    callbacks=callbacks,
    verbose=1
)

# Evaluación
test_loss, test_acc = model.evaluate(X_test, y_test, verbose=0)

print("\n=== RESULTADOS ===")
print("Loss:", test_loss)
print("Accuracy:", test_acc)

# Predicciones
y_prob = model.predict(X_test, verbose=0)
y_pred = np.argmax(y_prob, axis=1)

# Métricas
precision = precision_score(y_test, y_pred, average="macro")
recall = recall_score(y_test, y_pred, average="macro")
f1 = f1_score(y_test, y_pred, average="macro")

y_test_bin = label_binarize(y_test, classes=np.arange(len(class_names)))
roc_auc = roc_auc_score(y_test_bin, y_prob, average="macro", multi_class="ovr")
pr_auc = average_precision_score(y_test_bin, y_prob, average="macro")

print("\nPrecision:", precision)
print("Recall:", recall)
print("F1-score:", f1)
print("ROC-AUC:", roc_auc)
print("PR-AUC:", pr_auc)

print("\n=== MATRIZ DE CONFUSIÓN ===")
print(confusion_matrix(y_test, y_pred))

print("\n=== REPORTE ===")
print(classification_report(y_test, y_pred, target_names=class_names))

# Gráficas
plt.figure(figsize=(10, 4))
plt.plot(history.history["loss"], label="Train loss")
plt.plot(history.history["val_loss"], label="Val loss")
plt.title("Evolución de la pérdida")
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 4))
plt.plot(history.history["accuracy"], label="Train accuracy")
plt.plot(history.history["val_accuracy"], label="Val accuracy")
plt.title("Evolución de la exactitud")
plt.legend()
plt.grid(True)
plt.show()