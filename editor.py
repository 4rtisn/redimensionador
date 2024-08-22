import os
from moviepy.editor import VideoFileClip

input_folder = 'origem/'
output_folder = 'destino/'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

def cortar_video_para_quadrado(video_path, output_path):
    try:
        print(f"Carregando vídeo: {video_path}")
        video = VideoFileClip(video_path)
        largura, altura = video.size
        print(f"Largura: {largura}, Altura: {altura}")

        if largura > altura:
            margem = (largura - altura) // 2
            print(f"Cortando vídeo horizontal: margem = {margem}")
            video_quadrado = video.crop(x1=margem, x2=largura - margem)

        elif altura > largura:
            margem = (altura - largura) // 2
            print(f"Cortando vídeo vertical: margem = {margem}")
            video_quadrado = video.crop(y1=margem, y2=altura - margem)
        else:
            print("Vídeo já é quadrado, sem cortes necessários.")
            video_quadrado = video

        print(f"Salvando vídeo em: {output_path}")
        video_quadrado.write_videofile(output_path, codec="libx264", audio_codec="aac", preset='slow', bitrate="5000k")
        print(f"{output_path} salvo com sucesso!")
        
    except Exception as e:
        print(f"Erro ao processar o vídeo {video_path}: {e}")

extensoes_suportadas = ('.mp4', '.mov', '.avi', '.mkv')

for filename in os.listdir(input_folder):
    file_extension = os.path.splitext(filename)[1].lower() 
    if file_extension in extensoes_suportadas:
        video_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, f"quadrado_{filename}")
        
        print(f"Iniciando o processamento de {filename}...")
        cortar_video_para_quadrado(video_path, output_path)
    else:
        print(f"Arquivo ignorado (não é um vídeo suportado): {filename}")
