import qrcode
import sys
import pandas as pd

FILL_COLOR = 'black'
BACKGROUND_COLOR = 'white'
VERSION = 1
BOX_SIZE = 10
BORDER = 4
ERROR_CORRECTION = qrcode.constants.ERROR_CORRECT_L


def create_qr(text, filename):
    qr = qrcode.QRCode(
        version=VERSION,
        error_correction=ERROR_CORRECTION,
        box_size=BOX_SIZE,
        border=BORDER,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color=FILL_COLOR, back_color=BACKGROUND_COLOR)
    img.save('qrcode/' + filename + '.png')
    print("Creation du QrCode " + text + " terminée")


def generateTable_qr(file, type, columnName, columnText, SheetName):
    count = 0
    if type == "xlsx":
        df = pd.read_excel(file, sheet_name=SheetName)
        for i in df.index:
            create_qr(df[columnText][i], df[columnName][i])
            count += 1
            print("Génération du QrCode " + "" + ": " + str(count) + " / " + str(len(df.index)))
    elif type == "csv":
        df = pd.read_csv(file)
        for i in df.index:
            create_qr(df[columnText][i], df[columnName][i])
            count += 1
            print("Génération du QrCode " + "" + ": " + str(count) + " / " + str(len(df.index)))


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Bienvenue dans le créateur de QR code")
        mode = input("Voulez-vous créer un seul QR code ou Plusieurs QR code ? (1/2) ")
        if mode == "1":
            base = input("Voulez-vous utiliser les paramètres par défaut ou vous les modifiers ? (1/2) ")
            if base == "1":
                text = input("Veuillez entrer le texte à convertir en QR code : ")
                create_qr(text, "result")
            if base == "2":
                text = input("Veuillez entrer le texte à convertir en QR code : ")
                FILL_COLOR = input("Veuillez entrer la couleur de remplissage du QR code : ")
                BACKGROUND_COLOR = input("Veuillez entrer la couleur de fond du QR code : ")
                VERSION = input("Veuillez entrer la version du QR code : ")
                BOX_SIZE = input("Veuillez entrer la taille des cases du QR code : ")
                BORDER = input("Veuillez entrer la taille du bord du QR code : ")
                create_qr(text, "result")
        if mode == "2":
            type = input("Quel est le type de fichier contenant les données ? (XLSX/JSON/CSV) ")
            if type.lower() == "xlsx" or type.lower() == "csv":
                file = input("Veuillez entrer le chemin du fichier contenant les données : ")
                sheetName = input("Veuillez entrer le nom de la feuille Excel : ")
                columnName = input("Veuillez entrer le nom de la colonne contenant les noms : ")
                columnText = input(
                    "Veuillez entrer le nom de la colonne contenant les textes à convertir en QR code : ")
                generateTable_qr(file, type.lower(), columnName, columnText, sheetName)

    else:
        file = sys.argv[1:]
        print("Génération des QR codes d'après la configuration")
