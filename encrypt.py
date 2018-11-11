from operator import xor

class encrypt:
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




