import mysql.connector
import tkinter  as tk
from tkinter import *
my_w = tk.Tk()
my_w.geometry("400x250")
my_connect = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="priyanshu",
  database="python"
)
my_conn = my_connect.cursor()
my_conn.execute("SELECT * FROM passenger limit 0,20")
i=0
for passenger in my_conn:
    for j in range(len(passenger)):
        e = Entry(my_w, width=10, fg='red')
        e.grid(row=i+1, column=j)
        e.insert(END, passenger[j])
    i=i+1
my_w.mainloop()