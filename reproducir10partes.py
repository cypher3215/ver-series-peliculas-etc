import os 

os.system("pip install python-vlc")
import tkinter as tk
import vlc
import time

class VideoPlayerApp:
    def __init__(self, root, video_paths):
        self.root = root
        self.video_paths = video_paths  # Lista de partes de video
        self.current_video = 0  # Índice para controlar qué video se está reproduciendo
        
        # Crear instancia de vlc.MediaPlayer
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()

        # Crear el contenedor de video en el canvas de Tkinter
        self.canvas = tk.Canvas(root, width=640, height=360)
        self.canvas.pack()

        # Crear un contenedor de video en Tkinter
        self.embed = self.canvas.winfo_id()
        self.player.set_xwindow(self.embed)

        # Reproducir el primer video
        self.play_video()

    def play_video(self):
        video_path = self.video_paths[self.current_video]
        media = self.instance.media_new(video_path)
        self.player.set_media(media)

        # Reproducir video
        self.player.play()

        # Mientras el video esté en reproducción
        self.monitor_video()

    def monitor_video(self):
        while self.player.get_state() != vlc.State.Ended:
            if self.player.get_state() == vlc.State.Playing:
                # Hacer que el video se reproduzca en segundo plano
                self.root.after(10, self.monitor_video)
                return
            time.sleep(0.1)

        # Cuando el video termine, se pasa al siguiente
        self.current_video += 1
        if self.current_video < len(self.video_paths):
            self.play_video()
        else:
            print("Todos los videos han terminado.")

    def stop_video(self):
        self.player.stop()

# Crear la ventana de Tkinter
root = tk.Tk()
root.title("Reproductor de Video con Audio")

# Rutas de los videos (puedes añadir hasta 10 videos aquí)
video_paths = [f"murderdrones-capitulo1/parte_{i+1}.mp4" for i in range(10)]  # Lista de rutas

# Crear la aplicación de video
app = VideoPlayerApp(root, video_paths)

# Botón para detener el video
stop_button = tk.Button(root, text="Detener", command=app.stop_video)
stop_button.pack()

# Iniciar la interfaz de Tkinter
root.mainloop()
