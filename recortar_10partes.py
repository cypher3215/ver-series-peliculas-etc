# para recortar un video completo en 10 partes distintas para ahorrar espacio en los git push
import cv2
import os

def dividir_video(input_video_path, num_partes=10):
    # Abrir el video con OpenCV
    cap = cv2.VideoCapture(input_video_path)

    if not cap.isOpened():
        print("Error al abrir el archivo de video.")
        return

    # Obtener la duración total del video en segundos
    fps = cap.get(cv2.CAP_PROP_FPS)  # Frames por segundo
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))  # Número total de frames
    duracion_video = total_frames / fps  # Duración total en segundos

    # Calcular la duración de cada parte
    duracion_parte = duracion_video / num_partes
    print(f"Duración total del video: {duracion_video:.2f} segundos")
    print(f"Duración de cada parte: {duracion_parte:.2f} segundos")

    # Crear una carpeta para guardar las partes del video
    output_dir = "partes_video"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Dividir el video en partes
    for i in range(num_partes):
        inicio_parte = i * duracion_parte
        fin_parte = (i + 1) * duracion_parte

        # Usar FFmpeg para cortar el video en partes
        output_video_path = os.path.join(output_dir, f"parte_{i+1}.mp4")
        comando_ffmpeg = f"ffmpeg -i \"{input_video_path}\" -ss {inicio_parte} -to {fin_parte} -c:v libx264 -c:a aac -strict experimental \"{output_video_path}\""

        os.system(comando_ffmpeg)
        print(f"Parte {i+1} guardada en: {output_video_path}")

    cap.release()

# Ruta al video
input_video_path = "MURDER DRONES - Episode 5_ Home(720P_HD).mp4"  # Cambia esta ruta a la ubicación de tu video
dividir_video(input_video_path)

# para recortar un video completo en 10 partes distintas para ahorrar espacio en los git push
import cv2
import os

def dividir_video(input_video_path, num_partes=10):
    # Abrir el video con OpenCV
    cap = cv2.VideoCapture(input_video_path)

    if not cap.isOpened():
        print("Error al abrir el archivo de video.")
        return

    # Obtener la duración total del video en segundos
    fps = cap.get(cv2.CAP_PROP_FPS)  # Frames por segundo
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))  # Número total de frames
    duracion_video = total_frames / fps  # Duración total en segundos

    # Calcular la duración de cada parte
    duracion_parte = duracion_video / num_partes
    print(f"Duración total del video: {duracion_video:.2f} segundos")
    print(f"Duración de cada parte: {duracion_parte:.2f} segundos")

    # Crear una carpeta para guardar las partes del video
    output_dir = "partes_video"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Dividir el video en partes
    for i in range(num_partes):
        inicio_parte = i * duracion_parte
        fin_parte = (i + 1) * duracion_parte

        # Usar FFmpeg para cortar el video en partes
        output_video_path = os.path.join(output_dir, f"parte_{i+1}.mp4")
        comando_ffmpeg = f"ffmpeg -i \"{input_video_path}\" -ss {inicio_parte} -to {fin_parte} -c:v libx264 -c:a aac -strict experimental \"{output_video_path}\""

        os.system(comando_ffmpeg)
        print(f"Parte {i+1} guardada en: {output_video_path}")

    cap.release()

# Ruta al video
input_video_path = "MURDER DRONES - Episode 1_ PILOT(720P_HD).mp4"  # Cambia esta ruta a la ubicación de tu video
dividir_video(input_video_path)
