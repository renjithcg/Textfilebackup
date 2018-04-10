import os
import sys
import zipfile

def Backup():
    try:
        file = open("D:\\Renjith\\test.txt","w")
        file.write("This is a sentence")
    except IOError:
        print("error")
    else:
        print("successfully Backup")
        file.close()


def zip():
    try:
        jungle_zip = zipfile.ZipFile('D:\\Renjith\\test.txt' + '.zip', 'w')
        jungle_zip.write('D:\\Renjith\\test.txt', compress_type=zipfile.ZIP_DEFLATED)
    except IOError:
        print("not zipped")
    else:
        print("File zipped successfully")
        jungle_zip.close()

BACKUP_FILE=Backup()
ZIP_FILE=zip()
