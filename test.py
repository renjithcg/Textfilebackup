import os
import sys
import zipfile
import os.path

def Backup():
    if os.path.exists("test.txt"):
        os.remove("test.txt")
    try:
        file = open("./test.txt","w")
        file.write("This is a sentence")
    except IOError:
        print("error")
    else:
        print("successfully Backup")
        file.close()
    if os.path.exists("test.txt"):
        print("File is Ready")
    else:
        print("Not Ready")
    #a=os.path.join(os.getcwd(),"test" + "." + "txt")
    #print(a)
    #return (a)


def zip():
    try:
        jungle_zip = zipfile.ZipFile('./test.txt' + '.zip', 'w')
        jungle_zip.write('./test.txt', compress_type=zipfile.ZIP_DEFLATED)
    except IOError:
        print("not zipped")
    else:
        print("File zipped successfully")
        jungle_zip.close()
        #b=os.path.join(os.getcwd(),"test" + "." + "zip")
        #return (b)
    #print(b)

BACKUP_FILE=Backup()
ZIP_FILE=zip()
#Just for testing
#Just for testing
