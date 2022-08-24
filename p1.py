from inspect import Attribute
from tkinter import *
from tkinter import messagebox
import os
pw=Tk()
pw.geometry("900x400")
pw.title("Simple Shop Management System")
pw.configure(bg='black')
var=-1
fname="ssm.dat"
tempfname="ssml.dat"


def bmsg():
    messagebox.showinfo("button","button pressed")

def display(Li):
    V=list(Li.split("#"))
    enitemname.delete(0,END)
    enItemPrice.delete(0,END)
    enItemQuantity.delete(0,END)
    enItemCategory.delete(0,END)
    enItemDiscount.delete(0,END)
    enitemname.insert(0,str(V[0]))
    enItemPrice.insert(1,str(V[1]))
    enItemQuantity.insert(2,str(V[2]))
    enItemCategory.insert(3,str(V[3]))
    enItemDiscount.insert(4,str(V[4]))

def additem():
    global var
    num_lines=0
    with open(fname,'r') as myfile:
        for line in myfile:
            num_lines+=1
    var=num_lines-1
    e1=enitemname.get().strip()
    e2=enItemPrice.get().strip()
    e3=enItemQuantity.get().strip()
    e4=enItemCategory.get().strip()
    e5=enItemDiscount.get().strip()
    f=open(fname,'a+')
    f.write('{0}#{1}#{2}#{3}#{4}\n'.format(str(e1),str(e2),str(e3),str(e4),str(e5)))
    f.close()
    enitemname.delete(0,END)
    enItemPrice.delete(0,END)
    enItemQuantity.delete(0,END)
    enItemCategory.delete(0,END)
    enItemDiscount.delete(0,END)
    messagebox.showinfo("","Item "+e1+" added successfully")

lbheading =Label(pw,text="Shop Management System ",bg='black',fg="white",font=("Times",30))
lbItemName =Label(pw,text="Item Name ",bg='red',relief="ridge",fg="white",font=("Times",12),width=20)
enitemname =Entry(pw, font=("Times",12))
btTest= Button(pw, text="Add Item", bg="white", fg="black" ,width=20, font=("Times",12),command=additem)

lbItemPrice=Label(pw,text="Item Price",bg='red',relief="ridge",fg="white",font=("Times",12),width=20)
enItemPrice=Entry(pw,font=("Times",12))
#btTest2= Button(pw, text="Enter", bg="white", fg="black" ,width=20, font=("Times",12),command=additem)

lbItemQuantity=Label(pw,text="Item Quantity",bg='red',relief="ridge",fg="white",font=("Times",12),width=20)
enItemQuantity=Entry(pw,font=("Times",12))
#btTest3= Button(pw, text="Enter", bg="white", fg="black" ,width=20, font=("Times",12),command=additem)

lbItemCategory=Label(pw,text="Item Category",bg='red',relief="ridge",fg="white",font=("Times",12),width=20)
enItemCategory=Entry(pw,font=("Times",12))
#btTest4= Button(pw, text="Enter", bg="white", fg="black" ,width=20, font=("Times",12),command=additem)

lbItemDiscount=Label(pw,text="Item Discount",bg='red',relief="ridge",fg="white",font=("Times",12),width=20)
enItemDiscount=Entry(pw,font=("Times",12))
#btTest5= Button(pw, text="Enter", bg="white", fg="black" ,width=20, font=("Times",12),command=additem)

def firstItem():
    global var
    var=0
    f=open(fname)
    f.seek(var)
    c=f.readline()
    f.close()
    display(c)

btTest6= Button(pw, text="View first Item", bg="white", fg="black" ,width=20, font=("Times",12),command=firstItem)

def ViewLastItem():
    global var
    var=0
    f=open(fname)
    x=f.read().splitlines()
    f.close()
    last_line=x[-1]
    num_lines=0
    with open(fname) as f8:
        for lines in f8:
            num_lines+=1

    var=num_lines-1
    #print(var)
    try:
      display(last_line)
    except:
        messagebox.showinfo("record finished","sorry... no more records")
    
btTest2= Button(pw, text="View last Item", bg="white", fg="black" ,width=20, font=("Times",12),command=ViewLastItem)

def viewPreviousItem():
    global var
    var=var-1
    if var<0:
        messagebox.showinfo("","No previous recrord")
        var=var+1
        return
    f=open(fname)
    f.seek(var)
    try:
        c=f.readlines()
        f.close()
        x=c[var]
        display(x)
    except:
         messagebox.showinfo("","No previous recrord")
         f.close()



btTest3= Button(pw, text="view previous item", bg="white", fg="black" ,width=20, font=("Times",12),command= viewPreviousItem)

def viewNextItem():
    global var
    var+=1
    f=open(fname)
    f.seek(var)
    try:
        c=f.readlines()
        f.close()
        xyz=c[var]
        display(xyz)
    except:
         var-=1
         messagebox.showinfo("","No Next Record")

btTest4= Button(pw, text="view next item", bg="white", fg="black" ,width=20, font=("Times",12),command= viewNextItem)


def DeleteItem():
    global var
    e1=enitemname.get()
    with open(fname) as f, open(tempfname,"w") as working:
        for line in f:
           if str(e1) not in line:
              working.write(line)
    os.remove(fname)
    os.rename(tempfname,fname)
    enitemname.delete(0,END)
    enItemPrice.delete(0,END)
    enItemQuantity.delete(0,END)
    enItemCategory.delete(0,END)
    enItemDiscount.delete(0,END)
    messagebox.showinfo("","record deleted successfully")

btTest5= Button(pw, text="Delete Record", bg="white", fg="black" ,width=20, font=("Times",12),command= DeleteItem)
 
def SearchItem():
    i=0
    e11=enitemname.get()
    with open(fname) as f3:
        for line in f3:
            i=i+1
            if e11.lower() in line.lower():
                break
    try:
        display(line)
    except:
         messagebox.showinfo("","Error End Of File")

btTest7= Button(pw, text="Search Record", bg="white", fg="black" ,width=20, font=("Times",12),command= SearchItem)
       
def UpdateItem():
    e1=enitemname.get().strip()
    e2=enItemPrice.get().strip()
    e3=enItemQuantity.get().strip()
    e4=enItemCategory.get().strip()
    e5=enItemDiscount.get().strip()
    with open(fname) as f1,open(tempfname,"w") as working:
        for line in f1:
            if str(e1) not in line:
                working.write(line)
            else:
                working.write('{0}#{1}#{2}#{3}#{4}\n'.format(str(e1),str(e2),str(e3),str(e4),str(e5)))
    os.remove(fname)
    os.rename(tempfname,fname)              
    messagebox.showinfo("","Record Updated Successfully")       

btTest8= Button(pw, text="Update Record", bg="white", fg="black" ,width=20, font=("Times",12),command= UpdateItem)

def clear():
    enitemname.delete(0,END)
    enItemPrice.delete(0,END)
    enItemQuantity.delete(0,END)
    enItemCategory.delete(0,END)
    enItemDiscount.delete(0,END)

btTest9= Button(pw, text="Clear", bg="white", fg="black" ,width=20, font=("Times",12),command= clear)

lbheading.grid(row=0,columnspan=5)
lbItemName.grid(row=1,column=0, sticky=E, padx=10, pady=10)
enitemname.grid(row=1,column=1, sticky=E, padx=10, pady=10)
lbItemPrice.grid(row=2,column=0, sticky=E, padx=10, pady=10)
enItemPrice.grid(row=2,column=1, sticky=E, padx=10, pady=10)
lbItemQuantity.grid(row=3,column=0, sticky=E, padx=10, pady=10)
enItemQuantity.grid(row=3,column=1, sticky=E, padx=10, pady=10)
lbItemCategory.grid(row=4,column=0, sticky=E, padx=10, pady=10)
enItemCategory.grid(row=4,column=1, sticky=E, padx=10, pady=10)
lbItemDiscount.grid(row=5,column=0, sticky=E, padx=10, pady=10)
enItemDiscount.grid(row=5,column=1, sticky=E, padx=10, pady=10)
btTest.grid(row=1,column=2, sticky=E, padx=10, pady=10)
btTest2.grid(row=2,column=2, sticky=E, padx=10, pady=10)
btTest3.grid(row=3,column=2, sticky=E, padx=10, pady=10)
btTest4.grid(row=4,column=2, sticky=E, padx=10, pady=10)
btTest5.grid(row=5,column=2, sticky=E, padx=10, pady=10)
btTest6.grid(row=1,column=3, sticky=E, padx=10, pady=10)
btTest7.grid(row=2,column=3, sticky=E, padx=10, pady=10)
btTest8.grid(row=3,column=3, sticky=E, padx=10, pady=10)
btTest9.grid(row=4,column=3, sticky=E, padx=10, pady=10)

pw.mainloop()

