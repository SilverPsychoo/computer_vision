import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score, average_precision_score
from sklearn.preprocessing import label_binarize
from sklearn.utils.class_weight import compute_class_weight

# Fijar pseudoaleatoriedad
SEED = 42
np.random.seed(SEED)
tf.random.set_seed(SEED)

# Cargar dataset
df = pd.read_csv("data\Student_performance_data _.csv")

# Target
target_col = "GradeClass"
y_raw = df[target_col]
X = df.drop(columns=[target_col])

# Quitar IDs si hay
X = X.drop(columns=[c for c in X.columns if "id" in c.lower()], errors="ignore")

# One-hot encoding
X = pd.get_dummies(X)

# Codificar etiquetas
le = LabelEncoder()
y = le.fit_transform(y_raw)
class_names = le.classes_.astype(str)

print("Clases:", class_names)
print("Distribución:")
print(y_raw.value_counts())

# Split
X_train, X_temp, y_train, y_temp = train_test_split(
    X, y, test_size=0.3, stratify=y, random_state=SEED
)

X_val, X_test, y_val, y_test = train_test_split(
    X_temp, y_temp, test_size=0.5, stratify=y_temp, random_state=SEED
)

# Escalado
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_val = scaler.transform(X_val)
X_test = scaler.transform(X_test)

# Class weights (CLAVE)
weights = compute_class_weight("balanced", classes=np.unique(y_train), y=y_train)
class_weight = dict(enumerate(weights))

# MODELO (solo uno)
def build_model(input_dim):
    inputs = tf.keras.Input(shape=(input_dim,))
    x = tf.keras.layers.Dense(32, activation="relu")(inputs)
    x = tf.keras.layers.Dropout(0.2)(x)
    x = tf.keras.layers.Dense(16, activation="relu")(x)
    outputs = tf.keras.layers.Dense(len(class_names), activation="softmax")(x)
    return tf.keras.Model(inputs, outputs)

model = build_model(X_train.shape[1])

model.compile(
    optimizer=tf.keras.optimizers.Adam(0.001),
    loss=tf.keras.losses.SparseCategoricalCrossentropy(),
    metrics=["accuracy"]
)

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
    epochs=200,
    batch_size=16,
    callbacks=callbacks,
    class_weight=class_weight,
    verbose=1
)

# Evaluación
test_loss, test_acc = model.evaluate(X_test, y_test, verbose=0)

y_prob = model.predict(X_test)
y_pred = np.argmax(y_prob, axis=1)

# Métricas
precision = precision_score(y_test, y_pred, average="macro")
recall = recall_score(y_test, y_pred, average="macro")
f1 = f1_score(y_test, y_pred, average="macro")

y_test_bin = label_binarize(y_test, classes=np.arange(len(class_names)))
roc_auc = roc_auc_score(y_test_bin, y_prob, average="macro", multi_class="ovr")
pr_auc = average_precision_score(y_test_bin, y_prob, average="macro")

print("\n=== RESULTADOS ===")
print("Loss:", test_loss)
print("Accuracy:", test_acc)
print("Precision:", precision)
print("Recall:", recall)
print("F1:", f1)
print("ROC-AUC:", roc_auc)
print("PR-AUC:", pr_auc)

print("\nMatriz de confusión")
print(confusion_matrix(y_test, y_pred))

print("\nReporte")
print(classification_report(y_test, y_pred, target_names=class_names))

# GRÁFICAS (solo 2)
plt.plot(history.history["loss"], label="Train")
plt.plot(history.history["val_loss"], label="Val")
plt.title("Loss")
plt.legend()
plt.grid()
plt.show()

plt.plot(history.history["accuracy"], label="Train")
plt.plot(history.history["val_accuracy"], label="Val")
plt.title("Accuracy")
plt.legend()
plt.grid()
plt.show()