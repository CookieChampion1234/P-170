from tkinter import *
from tkinter import ttk
root = Tk()
root.geometry("900x600")
root.title("PERCENTAGE CALCULATION") 
Label1 = Label(root)
Label2 = Label(root)
Label3 = Label(root)


class createElements:
    
   
    
    def __init__(self,language_arts,social):
        self.language_arts = language_arts
        self.social = social
    def percentage(self):
        total = self.language_arts + self.social
        totalj = total * 100
        total_num = totalj / 200
        Label1["text"] = total_num
class createElements1:
    
   
    
    def __init__(self,language_arts,social,maths):
        self.language_arts = language_arts
        self.social = social
        self.maths = maths
    def percentage(self):
        total = self.language_arts + self.social + self.maths
        totalj = total * 100
        total_num = totalj / 200
        Label2["text"] = total_num  
  
        
  
    
class createElements2:
    
   
    
    def __init__(self,language_arts,social,crafts,maths):
        self.language_arts = language_arts
        self.social = social
        self.maths = maths
        self.crafts = crafts
    def percentage(self):
        total = self.language_arts + self.social + self.crafts + self.maths 
        totalj = total * 100
        total_num = totalj / 200
        Label3["text"] = total_num  
        
        
        
blbl = createElements(50,90) 
blbll = createElements1(20,60,100) 
blbllll = createElements2(32,90,67,10) 
btn = Button(root,text="grade 3",command=blbl.percentage)
btn.pack(padx=20,pady= 10)
Label1.pack(padx=20,pady=12)
btn = Button(root,text="grade 5 ",command=blbll.percentage)
btn.pack(padx=20,pady= 13)
Label2.pack(padx=20,pady=14)
btn = Button(root,text="grade 10",command=blbllll.percentage)
btn.pack(padx=20,pady= 15)
Label3.pack(padx=20,pady=16)
root.mainloop()

