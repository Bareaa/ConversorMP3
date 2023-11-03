from pytube import YouTube
import moviepy.editor as mp
import re
import os

# def download_music():
#     links = input("https://youtu.be/znAoENGZIt4?si=rRiFYEn4fsV4cS5C",
#         "https://youtu.be/44UYbsnEx08?si=BNqP8vrvGRV9dNaU",
#         "https://youtu.be/61x6D8pIvm4?si=GYnYKe9CdkH-bVXO",
#         "https://youtu.be/JMQ9Bu7mO-I?si=otFd54q06hTJf09R",
#         "https://youtu.be/lqCKFZbu78Q?si=BnZ29AnFForJnDYQ",
#         "https://youtu.be/Fq_0_e0hUfE?si=uq9Wp3092eerBqPx",
#         "https://youtu.be/j73pTROq9_A?si=8Fh2oP_dc8_GQuLU",
#         "https://youtu.be/V3qUoiwr5kQ?si=TWWE8LKfwuQArwQv",
#         "https://youtu.be/_Jl-QpJNKiQ?si=hXBRfx4wcikTvQy_",
#         "https://youtu.be/lyWqQ4KzlzQ?si=nSx2j6LfkjVB_LZo",
#         "https://youtu.be/6xVs6vU_b7A?si=L00k7a4QoSQz0cgt",
#         "https://youtu.be/M_To1WP6QHQ?si=iI8txYBDg2ISpAPK",
#         "https://youtu.be/gne9jY-EDm4?si=7w-1OXC6ChHNQfkW",
#         "https://youtu.be/Tbed88ER8W4?si=OGm9nnZ4VWFCqjK3",
#         "https://youtu.be/YcxjBJYvxHI?si=yy72QBDucxITnkLt",
#         "https://youtu.be/fL-K80sj21o?si=ZYQyYZVWK5aQFIg3",
#         "https://youtu.be/SHbGJQGsj8c?si=rBpEEv-wYBB58bEo",
#         "https://youtu.be/dKgtq9__PUc?si=DQfvVENy-aFXEVPE",
#         "https://youtu.be/_oKZsaw-IYI?si=hNZeyzvZXys06s10",
#         "https://youtu.be/YbT9D4wZukg?si=248qho_lwF5hVp2P",
#         "https://youtu.be/KR2lKlFI3qc?si=CRsJWyhRqfcZ2dD1").split()
#     path = input('C:\\Users\\barea\\Downloads\\MusicasMP3')

#     for link in links:
#         yt = YouTube(link)
#         # Fazer o download
#         ys = yt.streams.filter(only_audio=True).first().download(path)
#         # Converter o vídeo (mp4) para mp3
#         for file in os.listdir(path):
#             if re.search('mp4', file):
#                 mp4_path = os.path.join(path, file)
#                 mp3_path = os.path.join(path, os.path.splitext(file)[0] + '.mp3')
#                 new_file = mp.AudioFileClip(mp4_path)
#                 new_file.write_audiofile(mp3_path)
#                 os.remove(mp4_path)
#         print(f"Download Completo para {yt.title}")
def download_music():
    links = [
        "https://youtu.be/9GMjH1nR0ds?si=1l3sO66utTvwkkVk",
        "https://youtu.be/znAoENGZIt4?si=rRiFYEn4fsV4cS5C",
        "https://youtu.be/0ZwsCIfo9n8?si=tjMcLg4ndP7cglwf"
    ]
    path = input('Caminho de download (ex: C:/Users/barea/Downloads/MusicasMP3): ')

    for link in links:
        yt = YouTube(link)
        # Fazer o download
        ys = yt.streams.filter(only_audio=True).first().download(path)
        # Converter o vídeo (mp4) para mp3
        for file in os.listdir(path):
            if re.search('mp4', file):
                mp4_path = os.path.join(path, file)
                mp3_path = os.path.join(path, os.path.splitext(file)[0] + '.mp3')
                new_file = mp.AudioFileClip(mp4_path)
                new_file.write_audiofile(mp3_path)
                os.remove(mp4_path)
        print(f"Download Completo para {yt.title}")

download_music()