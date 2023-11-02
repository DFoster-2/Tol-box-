import tkinter as tk
def none():
  pass
def encript_mesige():
  root_homePage.destroy()
  from .Mesige.encriptMesige import code_incripter; code_incripter()
def decrypt_mesige():
  root_homePage.destroy()
  from .Mesige.decriptMesige import code_incripter; code_incripter()
def start(username):
  global user
  global root_homePage
  user = username
  root_homePage = tk.Tk()
  
  title = tk.Label(root_homePage, text = "Encript / Dectypt", font=('Helvetica', 16))
  imige_Emesige = tk.PhotoImage()
  button_Emesige = tk.Button(root_homePage, text = "Encript a messige", command= encript_mesige)
  
  imige_dmesige = tk.PhotoImage()
  button_dmesige = tk.Button(root_homePage, text = "Decrypt a messige", command= decrypt_mesige)
  
  imige_efile = tk.PhotoImage()
  button_efile = tk.Button(root_homePage, text = "Encript a file", command= none, state=tk.DISABLED)
  
  imige_dfile = tk.PhotoImage()
  button_dfile = tk.Button(root_homePage, text = "Decrypt a file", command= none, state=tk.DISABLED)
  
  
  
  title.grid(row = 0, column= 0, columnspan= 3)
  button_Emesige.grid(row = 1, column= 0)
  button_dmesige.grid(row = 1, column= 1)
  button_efile.grid(row = 1, column= 2)
  button_dfile.grid(row = 2, column= 1)