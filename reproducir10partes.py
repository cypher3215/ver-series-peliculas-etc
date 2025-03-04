import cv2
import tkinter as tk
from PIL import Image, ImageTk

# Función para cargar y reproducir las partes del video
def reproducir_video():
    # Lista con las rutas de las 10 partes del video
    partes = [f"partes_video/parte_{i+1}.mp4" for i in range(10)]
    
    # Crear una ventana de Tkinter
    root = tk.Tk()
    root.title("Reproductor de Video")
    
    # Crear un label para mostrar las imágenes
    canvas = tk.Label(root)
    canvas.pack()
    
    # Reproducir las partes del video
    for parte in partes:
        cap = cv2.VideoCapture(parte)  # Abrir la parte del video
        
        if not cap.isOpened():
            print(f"Error al abrir el video: {parte}")
            continue
        
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break  # Si no hay más frames, terminar la reproducción de esta parte
            
            # Convertir el frame a formato RGB para mostrar en tkinter
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame_rgb)
            img = ImageTk.PhotoImage(img)
            
            # Actualizar la imagen en el label
            canvas.configure(image=img)
            canvas.image = img
            
            # Mostrar el frame durante 20 ms (aproximadamente 50 FPS)
            root.update_idletasks()
            root.after(20)
        
        cap.release()  # Liberar el video al terminar

    root.mainloop()

# Ejecutar la función de reproducción
reproducir_video()