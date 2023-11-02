import os

def start_quetion():
  qestion = input("what is the qustion? ")

  entries = os.listdir("/home/runner/tol-box/Apps/Qustions/Archive/")
  #print(entries)
  lenthOfentries = len (entries)
  string = ""
  for x in range (0, lenthOfentries):
    string = string + "\n" +entries[x]
    #print(string)
  print("Topics:", string) 
  subject = input("What is the subject? ").lower()
  if entries.count(subject) > 0:
    entries = os.listdir("/home/runner/tol-box/Apps/Qustions/Archive/"+ subject)
    lenthOfentries = len (entries)
    string = ""
    qustionsAtMomant = []
    for x in range (0, lenthOfentries):
      temp = entries[x].find(".")
      qustionFromlist = entries[x]
      #print(temp)
      qestioninfile = ""
      for y in range (0, temp):
        qestioninfile = qestioninfile + qustionFromlist[y]
      qustionsAtMomant.append(qestioninfile)
      string = string + "\n" +qestioninfile
      #print(string)
    #print("qustions:", string)
    if qustionsAtMomant.count(qestion) >0:
      print ("hi")
  else:
    pin = input("Pin: ")