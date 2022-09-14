#pip install pytube

from pytube import YouTube

link = input("Entrez le lien de la vidéo YouTube : ")
yt = YouTube(link)  
ys = yt.streams.get_highest_resolution()   
print("Téléchargement..") 
ys.download("Downloads\Vidéos téléchargées")  # Modifiez ce chemin pour choisir où télécharger la vidéo
print("Téléchargement terminé !")
