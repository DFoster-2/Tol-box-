import tkinter as tk
import os

def start_quetion(user):
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
      print ("The Anser is:")
      #print(str("Apps/Qustions/Archive/" + "/" + subject  + "/" + qestion+".txt"))
      with open(str("Apps/Qustions/Archive/" + "/" + subject  + "/" + qestion+".txt"),"r") as qestionAnser:
        anser = qestionAnser.read()
      print(anser)
    else:
      print("we are verry sorry we do not have that qustion 🤔")
      yesorno = input("Would you like to make it? Yes or No ").lower()
      if yesorno == "yes":
        pin = input("pin")
        if pin == "1":
          file = open(str("Apps/Qustions/Archive/" + "/" + subject  + "/" + qestion+".txt"), "x").close()
          text = input("Anser: ")
          text2 = text + str("\nThis is writen by: " + user)
          with open(str("Apps/Qustions/Archive/" + "/" + subject  + "/" + qestion+".txt"), "w") as file:
            file.write(text2)
        else:
          print("wrong pin 😜")
          print("------------------App closed----------------")
          start_quetion("bob")
      else:
        print("ok 👌 closing....")
        print("------------------App closed----------------")
        start_quetion("bob")

def start_quesion_bot():
  root = tk.Tk()

  title = tk.Label(root, text = "Qustions", font=('Helvetica', 16))
  qestion_assc = tk.Entry(root)
  subgect = tk.StringVar()
  folders= [
    "python",
    "sport"
  ]
  subgect.set("Please select")
  subject_assc = tk.OptionMenu(root, subgect, *folders)
  submit = tk.Button(root, text = "Submit", command = lambda: start_quetion("bob") )
  lable1 = tk.Label(root, text = "Subject")
  lable2 = tk.Label(root, text = "Qustion")

  title.grid(row = 0, column= 0, columnspan= 2)
  
  lable1.grid(row = 1, column=0)
  lable2.grid(row = 1, column=1)

  qestion_assc.grid(row = 2, column=1)
  subject_assc.grid(row = 2, column=0)
  
