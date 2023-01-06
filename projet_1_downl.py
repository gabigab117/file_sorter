import pathlib

""" A short example of the use of the Pathlib library.
 The goal is to sort the files in the Downloads folder to distribute them in the folders sorted by file type."""

EXTENSIONS = {".mp4" : "Videos",
              ".avi" : "Videos",
              ".mp3" : "Music",
              ".xlsx" : "Documents",
               ".jpg" : "Pictures",
               ".pdf" : "Documents" }

dossier_trier = pathlib.Path(r"C:\Users\gabri\Downloads")
utilisateur = pathlib.Path(r"C:\Users\gabri")

fichiers = []
for fichier in dossier_trier.iterdir():
    if fichier.is_file():
        fichiers.append(fichier)

for f in fichiers:
    destination = utilisateur / EXTENSIONS.get(f.suffix, "Downloads")
    nouveau = destination / f.name
    f.rename(nouveau)