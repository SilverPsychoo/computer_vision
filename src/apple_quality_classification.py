# First part - Imports
import numpy as np
import tensorflow as tf
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.utils.class_weight import compute_class_weight
from sklearn.metrics import roc_auc_score, average_precision_score
from sklearn.metrics import confusion_matrix, classification_report
import matplotlib.pyplot as plt

# Para tener siempre una misma semilla de aletoriedad
SEED = 36
np.random.seed(SEED)
tf.random.set_seed(SEED)

# Cargar el DataSet
data = pd.read_csv("data/apple_quality.csv")

# Eliminar columna ID si existe
if "A_id" in data.columns:
    data = data.drop("A_id", axis=1)

# Convertir variable objetivo
data["Quality"] = (data["Quality"] == "good").astype(int)

# Forzar columnas a numéricas
data = data.apply(pd.to_numeric, errors="coerce")
data = data.dropna()

X = data.drop("Quality", axis=1).values.astype(np.float32)
y = data["Quality"].values.astype(np.int32)

# División de mi DataSet
X_train, X_temp, y_train, y_temp = train_test_split(
    X, y, test_size=0.3, stratify=y, random_state=SEED)

X_val, X_test, y_val, y_test = train_test_split(
    X_temp, y_temp, test_size=0.5, stratify=y_temp, random_state=SEED)

# Scaling
scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_val_s = scaler.transform(X_val)
X_test_s = scaler.transform(X_test)

# Balance de las clases
classes = np.array([0, 1])
cw = compute_class_weight(class_weight='balanced', classes=classes, y=y_train)
class_weigh = {0: float(cw[0]), 1: float(cw[1])}

# Modelo
def build_model(input_dim):
  inputs = tf.keras.Input(shape=(input_dim,))
  x = tf.keras.layers.Dense(128, activation="relu", kernel_regularizer=tf.keras.regularizers.l2(1e-3))(inputs)
  x = tf.keras.layers.Dropout(0.30)(x)
  x = tf.keras.layers.Dense(64, activation="relu")(x)
  x = tf.keras.layers.Dropout(0.20)(x)
  x = tf.keras.layers.Dense(32, activation="relu")(x)
  outputs = tf.keras.layers.Dense(1, activation="sigmoid")(x)
  return tf.keras.Model(inputs, outputs)

model = build_model(X_train_s.shape[1])

# Métricas
metrics = [
    tf.keras.metrics.AUC(curve="ROC", name="auc_roc"),
    tf.keras.metrics.AUC(curve="PR", name="auc_pr"),
    tf.keras.metrics.Recall(name="Recall"),
    tf.keras.metrics.Precision(name="Precision"),
]

# Compilar Modelo
lr = 1e-4
model.compile(
    optimizer=tf.optimizers.Adam(lr),
    loss="binary_crossentropy",
    metrics=metrics
)

# CallBack - EarlyStopping
callbacks = [
    tf.keras.callbacks.EarlyStopping(
        monitor="val_auc_roc",
        mode="max",
        patience=50,
        restore_best_weights=True)
]
model.summary()
history = model.fit(
    X_train_s, y_train,
    validation_data=(X_val_s, y_val),
    epochs=300,
    batch_size=16,
    class_weight=class_weigh,
    verbose=0,
    callbacks=callbacks
)

# Graficación
plt.figure()
plt.plot(history.history["loss"])
plt.plot(history.history["val_loss"])
plt.title("Pérdida")
plt.legend(["Train", "Validation"])
plt.show()

# Evaluación con datos de testing
testing_data_results = model.evaluate(X_test_s, y_test, verbose=1)
print(testing_data_results)

# Probabilidades
y_est_prob = model.predict(X_test_s).ravel()

print("ROC AUC:", roc_auc_score(y_test, y_est_prob))
print("PR AUC:", average_precision_score(y_test, y_est_prob))

# Buscar mejor threshold
thresholds = np.linspace(0.1,0.9,17)

best_f1 = 0
best_threshold = 0.5

for t in thresholds:

    y_pred = (y_est_prob >= t).astype(int)

    report = classification_report(y_test, y_pred, output_dict=True)

    f1 = report["1"]["f1-score"]

    if f1 > best_f1:
        best_f1 = f1
        best_threshold = t

print("Best threshold:", best_threshold)
print("Best F1:", best_f1)

# Predicción final
y_est_bin = (y_est_prob >= best_threshold).astype(int)

print(classification_report(y_test, y_est_bin))

confusion_matrix_table = confusion_matrix(y_test, y_est_bin)
print(confusion_matrix_table)