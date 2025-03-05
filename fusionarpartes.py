import os

def unir_video():
    # Lista de las rutas de las 10 partes del video
    partes = [f"MURDER DRONES - Episode 3/parte_{i+1}.mp4" for i in range(10)]
    
    # Crear un archivo de texto con las rutas de las partes del video
    with open("video_lista.txt", "w") as file:
        for parte in partes:
            file.write(f"file '{parte}'\n")
    
    # Usar ffmpeg para unir las partes
    output_video_path = "video_unido.mp4"
    comando_ffmpeg = f"ffmpeg -f concat -safe 0 -i video_lista.txt -c:v libx264 -c:a aac -strict experimental {output_video_path}"
    
    os.system(comando_ffmpeg)
    print(f"Video unido guardado como: {output_video_path}")
    
    # Eliminar el archivo de texto temporal
    os.remove("video_lista.txt")
    os.remove("video_unido.mp4")

# Ejecutar la función para unir el video
unir_video()
