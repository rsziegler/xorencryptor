from operator import xor

class encrypt:
  @staticmethod
  def decfile(decfile, key):
    txtfile = open(decfile, "r")
    text = txtfile.read().split()
    txtfile.close()

    ascii_conv = []
    enc_conv = []

    for x in text:
      a = ""
      for i in range(len(str(x))):
        s = str(x)
        n = s[i: i+1]
        k = key[i: i+1]
        app = xor(int(n), int(k))
        a = a + str(app)
      enc_conv.append(a)

    for n in enc_conv:
      x = int(n, 2)
      z = x.to_bytes((x.bit_length() + 7) // 8, 'big').decode()
      ascii_conv.append(z)
    txtfile = open(decfile, "w")

    for x in ascii_conv:
      txtfile.write(str(x) + "")

    txtfile.close()

  @staticmethod
  def encfile(encfile, key):
    txtfile = open(encfile, "r")
    text = txtfile.read()
    a_bytes = bytes(text, "ascii")
    txtfile.close()

    bin_conv = []
    enc_conv = []

    for x in a_bytes:
      bin_conv.append("{0:b}".format(x))
    for x in bin_conv:
      a = ""
      for i in range(len(str(x))):
        s = str(x)
        n = s[i: i+1]
        k = key[i: i+1]
        app = xor(int(n), int(k))
        a = a + str(app)
      enc_conv.append(a)

    txtfile = open(encfile, "w")

    for x in enc_conv:
      txtfile.write(str(x) + " ")

    txtfile.close()

class filemovement:
  @staticmethod
  def createfile(path):
    txtfile = open(path, "w+")
    txtfile.close()

  @staticmethod
  def readfile(readfile):
    txtfile = open(readfile, "r")
    text = txtfile.read()
    print(text)
    txtfile.close()
  
  @staticmethod
  def writefile(writefile, text):
    txtfile = open(writefile, "w")
    txtfile.write(text)
    txtfile.close()

class cmdline:
  # command format: operation to key
  @staticmethod
  def execommand(command):
    try:
      commands = command.split()
      do = commands[0]
      if len(commands) == 2:
        to = commands[1]
      elif len(commands) == 3:
        to = commands[1]
        key = commands[2]

      if do == "enc":
        encrypt.encfile(to, key)
      elif do == "dec":
        encrypt.decfile(to, key)
      elif do == "exit":
        return False
      elif do == "nf":
        filemovement.createfile(to)
      elif do == "rf":
        filemovement.readfile(to)
      elif do == "wf":
        text = input("")
        filemovement.writefile(to, text)
      else:
        print("not a valid operation")
    except:
      print("not valid syntax")
    return True