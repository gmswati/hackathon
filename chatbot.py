from tkinter import *

root = Tk()



root.title('Wonderful dreams')

root.geometry('400x500')



def send():
    #get() returns the entry's current text as a string.
    send="you :"+e.get()
    txt.insert(END,"\n"+send)
    if (e.get()=="hello"):
        txt.insert(END,"\n"+"                            Bot-> hii! how can we help you?")
    elif (e.get()=="hi"):
        txt.insert(END,"\n"+"Bot->                       hello!,How can we help you?")
    elif (e.get()=="what are the languages are you teaching?"):
        txt.insert(END,"\n"+"Bot->                      we teaches programming languages.")
    elif (e.get()=="I want to know about NAVGURUKUL"):
        txt.insert(END,"\n"+"Bot->                      Sure! Navgurukul is NGO where you can learn software Devlopment Course for free")
    elif (e.get()=="Like?"):
        txt.insert(END,"\n"+"Bot->                      Python,Javascript,advannce javascript,Node Js and react.js")
    elif (e.get()=="okay thankyou!"):
        txt.insert(END,"\n"+"Bot->                      for any other query please visit again.")
    else:
        txt.insert(END,"\n"+"Bot->                      please enter again")
    e.delete(0,END)
txt=Text(root)
txt.grid(row=0,column=0,columnspan=2)
e=Entry(root,width=100)
send=Button(root,text="send",command=send).grid(row=1,column=1)
e.grid(row=1,column=0)
# root.title('chatbox')
root.mainloop()     