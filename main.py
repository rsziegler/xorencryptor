from encrypt import *
from filemovement import *

# command format: operation to key
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
    elif do == "nf":
      filemovement.createfile(to)
    elif do == "rf":
      filemovement.readfile(to)
    elif do == "wf":
      text = input("")
      filemovement.writefile(to, text)
    elif do == "df":
      filemovement.deletefile(to)
    elif do == "exit":
      return False
    else:
      print("not a valid operation")
  except:
    print("not valid syntax")
  return True

n = True
while n:
  cmd = input()
  n = execommand(cmd)
