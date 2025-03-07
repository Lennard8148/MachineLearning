import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import numpy as np
import keras
import tensorflow as tf
import subprocess
from tkinter import filedialog, messagebox, simpledialog
import os

CLASS_NAMES = ['airplane', 'auto', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
MODEL_IMAGE_SIZE = (32, 32)
image_size = (32, 32)
batch_size = 128
saved_accuracy = 0.0

def load_model():
    global model, model_path
    model_path = filedialog.askopenfilename(title="Wähle ein Keras-Modell", filetypes=[("Keras Model", "*.keras")])
    
    if not model_path:
        messagebox.showerror("Fehler", "Modell muss gewählt werden!")
        return
    
    model = tf.keras.models.load_model(model_path)
    model_name = os.path.splitext(os.path.basename(model_path))[0]

    try:
        with open(f'{model_name}-accuracy.txt', 'r') as file:
            saved_accuracy = float(file.read())
    except FileNotFoundError:
        saved_accuracy = 0.0

    accuracy_label.config(text=f'Modell Präzision: {round(saved_accuracy*100)}%')
    model_label.config(text=f"Aktuelles Modell:\n{model_name}")
    messagebox.showinfo("Erfolg", f"Modell erfolgreich geladen: {model_path.split('/')[-1]}")


def classify_image():
    if model is None:
        messagebox.showwarning("Kein Modell", "Bitte wählen Sie zuerst ein Modell aus.")
        return
    
    file_path = filedialog.askopenfilename()
    if not file_path:
        return
    img_model = Image.open(file_path)

    img_UI = img_model.resize((180, 180))
    img_tk = ImageTk.PhotoImage(img_UI)
    panel.configure(image=img_tk)
    panel.image = img_tk

    if img_model.size != (32, 32):
        img_model = img_model.resize(MODEL_IMAGE_SIZE)
    
    img_array = keras.utils.img_to_array(img_model)
    img_array = tf.expand_dims(img_array, 0)

    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions, axis=1)[0]
    score = np.max(predictions)

    result = f'Erkannte Klasse: {CLASS_NAMES[predicted_class]} mit {round(score*100)}% Wahrscheinlichkeit'
    messagebox.showinfo("Ergebnis", result)
    result_label.config(text=result)


def train_new_model():
    model_name = simpledialog.askstring("Neues Modell", "Gib den Namen des neuen Modells ein:")
    if not model_name:
        return

    epochs = simpledialog.askinteger("Trainingseinstellungen", "Gib die Anzahl der Epochen ein (z.B. 10):")
    if not epochs or epochs <= 0:
        messagebox.showerror("Fehler", "Bitte eine gültige Anzahl von Epochen eingeben!")
        return

    messagebox.showinfo("Modelltraining", f'Modell "{model_name}" wird mit {epochs} Epochen trainiert...')

    # https://www.datacamp.com/tutorial/python-subprocess
    result = subprocess.run(
        ["python", "keras-model.py", model_name, str(epochs)],
        stdout=subprocess.PIPE, 
        stderr=subprocess.PIPE, 
        text=True
    )

    if result.returncode == 0:
        messagebox.showinfo("Erfolg", "Training erfolgreich abgeschlossen.")
    else:
        messagebox.showinfo("Fehler", f"Fehler beim Training. Fehlerausgabe: {result.stderr}")


root = tk.Tk()
root.title("Bildklassifikation mit TensorFlow")
root.geometry("800x500")

model_label = tk.Label(root, text="Kein Modell geladen", font=("Arial", 12))
model_label.pack(pady=10)

accuracy_label = tk.Label(root, text=f'Model Präzision: {round(saved_accuracy*100)}%', font=("Arial", 12))
accuracy_label.pack(pady=10)

train_button = tk.Button(root, text="Neues Modell trainieren", command=train_new_model, fg="white", bg="blue")
train_button.pack(pady=10)

switch_button = tk.Button(root, text="Modell wechseln", command=load_model)
switch_button.pack(pady=10)

upload_button = tk.Button(root, text="Bild hochladen & klassifizieren", command=classify_image)
upload_button.pack(pady=10)

panel = tk.Label(root)
panel.pack(pady=20)

result_label = tk.Label(root, text="", font=("Arial", 15))
result_label.pack(pady=20)

load_model()

root.mainloop()
