import os

class filemovement:
  def createfile(path):
    txtfile = open(path, "w+")
    txtfile.close()

  def readfile(readfile):
    txtfile = open(readfile, "r")
    text = txtfile.read()
    print(text)
    txtfile.close()
  
  def writefile(writefile, text):
    txtfile = open(writefile, "w")
    txtfile.write(text)
    txtfile.close()

  def deletefile(delfile):
    try:
      os.remove(delfile)
    except:
      print("the file specified does not exist in this directory")
