import tkinter as tk
root = tk.Tk()

#Vendosja e hapsires se window, titulli i aplikacionit
root.geometry("500x500")
root.title("My First GUI App")

#Me Label e kena vendos titullin.
label = tk.Label(root, text="Welcome to our calcualtor!", font=("Arial", 16), bg = "lightgray")
#Me .pack( e kena vendos qat sen ne window)
label.pack(padx = 20, pady=20)

#Eka kriju ni input prej metodes .Text()
textbox = tk.Text(root, height=3)
#Me .pack( e kena vendos qat sen ne window)
textbox.pack()

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0,weight=1)
buttonframe.columnconfigure(1,weight=1)
buttonframe.columnconfigure(2,weight=1)

#Krijimi i butonave
btn1 = tk.Button(buttonframe, text="1", font=("Arial", 16), bg = "lightgray")
btn1.grid(row = 0, column = 0, sticky=tk.W+tk.E)
btn2 = tk.Button(buttonframe, text="2", font=("Arial", 16), bg = "lightgray")
btn2.grid(row = 0, column = 1, sticky=tk.W+tk.E)
btn3 = tk.Button(buttonframe, text="3", font=("Arial", 16), bg = "lightgray")
btn3.grid(row = 0, column = 2, sticky=tk.W+tk.E)
btn4 = tk.Button(buttonframe, text="4", font=("Arial", 16), bg = "lightgray")
btn4.grid(row = 1, column = 0, sticky=tk.W+tk.E)
btn5 = tk.Button(buttonframe, text="5", font=("Arial", 16), bg = "lightgray")
btn5.grid(row = 1, column = 1, sticky=tk.W+tk.E)
btn6 = tk.Button(buttonframe, text="6", font=("Arial", 16), bg = "lightgray")
btn6.grid(row = 1, column = 2, sticky=tk.W+tk.E)
btn7 = tk.Button(buttonframe, text="7", font=("Arial", 16), bg = "lightgray")
btn7.grid(row = 3, column = 0, sticky=tk.W+tk.E)
btn8 = tk.Button(buttonframe, text="8", font=("Arial", 16), bg = "lightgray")
btn8.grid(row = 3, column = 1, sticky=tk.W+tk.E)
btn9 = tk.Button(buttonframe, text="9", font=("Arial", 16), bg = "lightgray")
btn9.grid(row = 3, column = 2, sticky=tk.W+tk.E)
btn0 = tk.Button(buttonframe, text="0", font=("Arial", 16), bg = "lightgray")
btn0.grid(row = 4, column = 1, sticky=tk.W+tk.E)




buttonframe.pack(fill="x")
root.mainloop()