import cv2
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import numpy as np

class VideoPlayerApp:
    def __init__(self, root, video_path):
        self.root = root
        self.video_path = video_path
        self.cap = cv2.VideoCapture(video_path)

        if not self.cap.isOpened():
            messagebox.showerror("Error", "No se pudo abrir el video.")
            return

        # Obtener las dimensiones originales del video
        self.frame_width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.frame_height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        # Definir el tamaño máximo del video (por ejemplo, 640px de ancho)
        self.max_width = 640
        aspect_ratio = self.frame_width / self.frame_height
        self.max_height = int(self.max_width / aspect_ratio)

        # Crear un canvas de Tkinter para mostrar el video
        self.canvas = tk.Canvas(root, width=self.max_width, height=self.max_height)
        self.canvas.pack()

        # Botón de recorte
        self.recorte_button = tk.Button(root, text="Recortar", command=self.start_recorte)
        self.recorte_button.pack()

        self.is_playing = False
        self.zoom_area = None

        # Para mostrar el primer frame del video
        self.update_frame()

    def update_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            return

        # Si hay un recorte seleccionado, aplica el recorte
        if self.zoom_area:
            x, y, w, h = self.zoom_area
            frame = frame[y:y+h, x:x+w]

        # Redimensionar el frame para ajustarlo al tamaño máximo
        frame = cv2.resize(frame, (self.max_width, self.max_height))

        # Convertir la imagen de BGR (OpenCV) a RGB (PIL)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(frame_rgb)
        image_tk = ImageTk.PhotoImage(image)

        # Mostrar el frame en el canvas
        self.canvas.create_image(0, 0, anchor=tk.NW, image=image_tk)
        self.canvas.image = image_tk

        if self.is_playing:
            self.root.after(30, self.update_frame)

    def start_recorte(self):
        self.zoom_area = None
        self.select_zoom_area()

    def select_zoom_area(self):
        self.canvas.create_rectangle(0, 0, 200, 200, outline='red', width=2)
        self.canvas.bind("<ButtonPress-1>", self.on_click)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

    def on_click(self, event):
        self.zoom_area = [event.x, event.y, 0, 0]
    
    def on_drag(self, event):
        if self.zoom_area:
            self.zoom_area[2] = event.x - self.zoom_area[0]
            self.zoom_area[3] = event.y - self.zoom_area[1]
            self.update_frame()

    def on_release(self, event):
        if self.zoom_area[2] < 0:  # Si el ancho es negativo, lo corregimos
            self.zoom_area[0] += self.zoom_area[2]
            self.zoom_area[2] = abs(self.zoom_area[2])
        if self.zoom_area[3] < 0:  # Si el alto es negativo, lo corregimos
            self.zoom_area[1] += self.zoom_area[3]
            self.zoom_area[3] = abs(self.zoom_area[3])

        self.canvas.unbind("<ButtonPress-1>")
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")

        # Aquí puedes añadir funcionalidad para guardar el video recortado

    def start_playing(self):
        self.is_playing = True
        self.update_frame()

    def stop_playing(self):
        self.is_playing = False

# Crear la ventana de Tkinter
root = tk.Tk()
root.title("Reproductor de Video con Recorte")

# Ruta al video
video_path = "MURDER DRONES - Episode 2_ Heartbeat(720P_HD).mp4"  # Cambia la ruta al video que desees

# Crear la aplicación de video
app = VideoPlayerApp(root, video_path)

# Botón para reproducir el video
play_button = tk.Button(root, text="Reproducir", command=app.start_playing)
play_button.pack()

# Botón para detener el video
stop_button = tk.Button(root, text="Detener", command=app.stop_playing)
stop_button.pack()

# Iniciar la interfaz de Tkinter
root.mainloop()
