######## A script for parsing LOTRO chat files to analyze herbalism flora spawns
import sys,time,os
VERSION="1.1"
(a,b,c,d,e) = sys.version_info

print("Version: "+VERSION+" Python:"+str(a)+"."+str(b)+"."+str(c)+"\n")

from tkinter import *
from tkinter import ttk
from tkinter import filedialog


def resource_path(relative_path):
  """ Get absolute path to resource, works for dev and for PyInstaller """
  base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
  return os.path.join(base_path, relative_path)

class App(Frame):
  def __init__(self, master=None):
    Frame.__init__(self)
    self.pack()
    self.switcher = {
      "Bonemallow...\n": 0,
          "Dusknettle...\n": 1,
          "Eye-of-Night...\n": 2,
          "Evengleam...\n": 3,
          "Mournweed...\n": 4,
          "Wraithscowl...\n": 5,
          "Bell-o-Dale...\n": 6,
          "Buckthorn...\n": 7,
          "Drakewort...\n": 8,
          "Dwarfsbeard...\n": 9,
          "Elfspear...\n": 10,
          "Horsetail...\n": 11,
          "Larkspur...\n": 12,
          "Oxlip...\n": 13,
          "Rock-rose...\n": 14,
          "Southron's Crown...\n": 15,
          "Vetchling...\n": 16
    }   
   
    self.fileToRead = "bigData.txt"
    self.saveToFile = 0
    self.timestampSetting = 1
    
  def createWidgets(self):
    self.hi_there = ttk.Button(self)
    self.hi_there["text"] = "Start Parsing"
    self.hi_there["command"] = self.parseFile
    self.hi_there.grid(row = 0, column = 0, sticky = W, padx = 5) 
    
    self.chooseFile = ttk.Button(self)
    self.chooseFile["text"] = "Choose the file to parse"
    self.chooseFile["command"] = self.pickaFile
    self.chooseFile.grid(row = 0, column = 1,  sticky = W, padx = 5)
    
    self.fileName = Label(self)
    self.fileName["text"] = "bigData.txt The file you choose will be displayed here. This is the default."
    self.fileName.grid(row = 1, column = 0, columnspan=2,  sticky = W, padx = 5)
    
    self.outputBool = Checkbutton(self)
    self.outputBool["text"] = "Save output to file?"
    self.outputBool["command"] = self.setSaveBool
    self.outputBool["variable"] = self.saveToFile
    self.outputBool.deselect()
    self.outputBool.grid(row = 0, column = 2,  sticky = W, padx = 5)
    
    self.timestampBool = Checkbutton(self)
    self.timestampBool["text"] = "Does this logfile contain lines that begin with a timestamp?"
    self.timestampBool["command"] = self.setTimestampBool
    self.timestampBool["variable"] = self.timestampSetting
    self.timestampBool.select()
    self.timestampBool.grid(row = 1, column = 2,  sticky = W, padx = 2)


    self.outputLabel = Label(self,bg="white")
    self.outputLabel["text"] = "Output appears here"
    self.outputLabel.grid(row = 2, column = 0,columnspan = 10 , sticky = W, padx = 2)
    

    
  def pickaFile(self):
    
    self.fileToRead = filedialog.askopenfilename(initialdir = ".",title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
    self.master.update()
    self.fileName["text"]=self.fileToRead

  def setSaveBool(self):
    if self.saveToFile:
      self.saveToFile = 0
    else:
      self.saveToFile = 1
    #print(str(self.saveToFile))  
  
  def setTimestampBool(self):
    if self.timestampSetting:
      self.timestampSetting = 0
    else:
      self.timestampSetting = 1   
    
  def procFlora(self,argument):
    try:
      anInt = self.switcher[argument]
      self.Summaries[anInt]["Count"] += 1
    except:
      anInt = 99
    return anInt
  
  def parseFile(self):
    self.Summaries=[]
    self.Summaries.append({"Name":"Bonemallow","Count":0,"Amber":0,"Sapphire":0,"Gold":0,"Violet":0,"Crimson":0,"Umber":0,"Verdant":0,"Min":0,"Max":0})
    self.Summaries.append({"Name":"Dusknettle","Count":0,"Amber":0,"Sapphire":0,"Gold":0,"Violet":0,"Crimson":0,"Umber":0,"Verdant":0,"Min":0,"Max":0})
    self.Summaries.append({"Name":"Eye-of-Night","Count":0,"Amber":0,"Sapphire":0,"Gold":0,"Violet":0,"Crimson":0,"Umber":0,"Verdant":0,"Min":0,"Max":0})
    self.Summaries.append({"Name":"Evengleam","Count":0,"Amber":0,"Sapphire":0,"Gold":0,"Violet":0,"Crimson":0,"Umber":0,"Verdant":0,"Min":0,"Max":0})
    self.Summaries.append({"Name":"Mournweed","Count":0,"Amber":0,"Sapphire":0,"Gold":0,"Violet":0,"Crimson":0,"Umber":0,"Verdant":0,"Min":0,"Max":0})
    self.Summaries.append({"Name":"Wraithscowl","Count":0,"Amber":0,"Sapphire":0,"Gold":0,"Violet":0,"Crimson":0,"Umber":0,"Verdant":0,"Min":0,"Max":0})
    self.Summaries.append({"Name":"Bell-o-Dale","Count":0,"Amber":0,"Sapphire":0,"Gold":0,"Violet":0,"Crimson":0,"Umber":0,"Verdant":0,"Min":0,"Max":0})
    self.Summaries.append({"Name":"Buckthorn","Count":0,"Amber":0,"Sapphire":0,"Gold":0,"Violet":0,"Crimson":0,"Umber":0,"Verdant":0,"Min":0,"Max":0})
    self.Summaries.append({"Name":"Drakewort","Count":0,"Amber":0,"Sapphire":0,"Gold":0,"Violet":0,"Crimson":0,"Umber":0,"Verdant":0,"Min":0,"Max":0})
    self.Summaries.append({"Name":"Dwarfsbeard","Count":0,"Amber":0,"Sapphire":0,"Gold":0,"Violet":0,"Crimson":0,"Umber":0,"Verdant":0,"Min":0,"Max":0})
    self.Summaries.append({"Name":"Elfspear","Count":0,"Amber":0,"Sapphire":0,"Gold":0,"Violet":0,"Crimson":0,"Umber":0,"Verdant":0,"Min":0,"Max":0})
    self.Summaries.append({"Name":"Horsetail","Count":0,"Amber":0,"Sapphire":0,"Gold":0,"Violet":0,"Crimson":0,"Umber":0,"Verdant":0,"Min":0,"Max":0})
    self.Summaries.append({"Name":"Larkspur","Count":0,"Amber":0,"Sapphire":0,"Gold":0,"Violet":0,"Crimson":0,"Umber":0,"Verdant":0,"Min":0,"Max":0})
    self.Summaries.append({"Name":"Oxlip","Count":0,"Amber":0,"Sapphire":0,"Gold":0,"Violet":0,"Crimson":0,"Umber":0,"Verdant":0,"Min":0,"Max":0})
    self.Summaries.append({"Name":"Rock-rose","Count":0,"Amber":0,"Sapphire":0,"Gold":0,"Violet":0,"Crimson":0,"Umber":0,"Verdant":0,"Min":0,"Max":0})
    self.Summaries.append({"Name":"Southron's Crown","Count":0,"Amber":0,"Sapphire":0,"Gold":0,"Violet":0,"Crimson":0,"Umber":0,"Verdant":0,"Min":0,"Max":0})
    self.Summaries.append({"Name":"Vetchling","Count":0,"Amber":0,"Sapphire":0,"Gold":0,"Violet":0,"Crimson":0,"Umber":0,"Verdant":0,"Min":0,"Max":0})     
 
    count = 0
    nextLine = 0  
    try:
      f = open(self.fileToRead, "r")
      print(self.fileToRead+" was read")
      allLines = f.readlines()
    except Exception as e:
      print(str(e))
      tkstring1 = "You must choose a file to parse"
      print(tkstring1)
      allLines = "Nothing read"
     
    dataline=""
    for line in allLines:
      aline = line.split("]")
      if nextLine:
        if not currentFlora == 99:
          if "You have acquired:" in line:
            if  self.timestampSetting:    #len(aline)==3:
              z = aline[1].split("[")
            else:
              z = aline[0].split("[")
            if z[1][0].isdigit():
              someint = int(z[1][0])                
            else:
              someint = 1
              
              
              
            if "Gold" in line:
              self.Summaries[currentFlora]["Gold"]+= someint
              count += someint
            elif "Violet" in line:  
              self.Summaries[currentFlora]["Violet"]+= someint
              count += someint
            elif "Amber" in line:  
              self.Summaries[currentFlora]["Amber"]+= someint
            elif "Sapphire" in line:  
              self.Summaries[currentFlora]["Sapphire"]+= someint
            elif "Crimson" in line:  
              self.Summaries[currentFlora]["Crimson"]+= someint
              count += someint
            elif "Verdant" in line:  
              self.Summaries[currentFlora]["Verdant"]+= someint
              count += someint
            elif "Umber" in line:  
              self.Summaries[currentFlora]["Umber"]+= someint
              count += someint            
          else:
            nextLine=0
            if self.Summaries[currentFlora]["Min"] == 0:
              self.Summaries[currentFlora]["Min"] = count
            elif count < self.Summaries[currentFlora]["Min"]:
              self.Summaries[currentFlora]["Min"] = count
            if count > self.Summaries[currentFlora]["Max"]:
              self.Summaries[currentFlora]["Max"] = count  
            currentFlora = None
            count = 0
          
    
      if "Taking the contents of " in line:
        nextLine = 1
        if self.timestampSetting:
          try:
            thisLine = aline[1].split("Taking the contents of the ")
          except:
            self.outputLabel.setvar="Timestamp setting appears to not match the file"
        else:
          try:
            thisLine = aline[0].split("Taking the contents of the ")
          except:
            self.outputLabel.setvar="Timestamp setting appears to not match the file"
        try:
          currentFlora = self.procFlora(thisLine[1])
        except:
          self.outputLabel.setvar="Timestamp setting appears to not match the file"
          currentFlora = 99
       
    #print(len(allLines))
    tkstring1 = str(len(allLines))+" lines parsed\n"
    
    try:
      f.close()
    except:
      print("no file to close")
      self.outputLabel["text"]="No file chosen to parse"
      
      return
    if self.saveToFile:
      newFile = open(str(time.time())+".txt", "w")
    Totals = 0
    #print("Name",'\t','\t','\t' ,"Count",'\t' ,"Gold",'\t' ,"Violet"," Amber",'\t' ,"Sapphire","Crimson","Umber" ," Verdant","Min",'\t' ,"Max")
    tkstring2 = str("Name\t\t\tCount\tGold\tViolet\tAmber\tSapphire Crimson Umber\tVerdant\tMin\tMax\n")
    
    string1 = ( '"Name";"Count";"Gold";"Violet";"Amber";"Sapphire";"Crimson";"Umber";"Verdant";"Min";"Max"\n')
    if self.saveToFile:
      newFile.write(string1)
    for lump in self.Summaries:
      #if lump["Count"] > 0:
      #newFile.write(str(lump))
      Totals += lump["Count"]
      #print(lump)
      astring = lump["Name"]+";"+str(lump["Count"])+";"+str(lump["Gold"])+";"+str(lump["Violet"])+";"+str(lump["Amber"])+";"+str(lump["Sapphire"])+";"+str(lump["Crimson"])+";"+str(lump["Umber"])+";"+str(lump["Verdant"])+";"+str(lump["Min"])+";"+str(lump["Max"])+"\n"
      
      if self.saveToFile:
        newFile.write(astring)
      #print(astring)
      
      if lump["Name"] == "Oxlip" or lump["Name"] == "Larkspur" or lump["Name"] == "Horsetail" or lump["Name"] ==  "Elfspear" :
        tkstring2 += str(lump["Name"])+"\t\t\t"+str(lump["Count"])+"\t"+str(lump["Gold"])+"\t"+str(lump["Violet"])+"\t"+str(lump["Amber"])+"\t"+str(lump["Sapphire"])+"\t"+str(lump["Crimson"])+"\t"+str(lump["Umber"])+"\t"+str(lump["Verdant"])+"\t"+str(lump["Min"])+"\t"+str(lump["Max"])+"\n"
        #print(lump["Name"],"\t","\t","\t",lump["Count"],"\t" ,lump["Gold"],"\t",lump["Violet"],"\t",lump["Amber"],"\t",lump["Sapphire"],"\t",lump["Crimson"],"\t",lump["Umber"],"\t",lump["Verdant"],"\t",lump["Min"],"\t",lump["Max"])
      else:
        #print(lump["Name"],"\t","\t",lump["Count"],"\t" ,lump["Gold"],"\t",lump["Violet"],"\t",lump["Amber"],"\t",lump["Sapphire"],"\t",lump["Crimson"],"\t",lump["Umber"],"\t",lump["Verdant"],"\t",lump["Min"],"\t",lump["Max"])
        tkstring2 += (str(lump["Name"])+"\t\t"+str(lump["Count"])+"\t"+str(lump["Gold"])+"\t"+str(lump["Violet"])+"\t"+str(lump["Amber"])+"\t"+str(lump["Sapphire"])+"\t"+str(lump["Crimson"])+"\t"+str(lump["Umber"])+"\t"+str(lump["Verdant"])+"\t"+str(lump["Min"])+"\t"+str(lump["Max"])+"\n")  
    
    
    tkstring3 = str(Totals)+ " plants harvested"
    if Totals == 0:
      tkstring3 += "\nReview your logfile and make sure you have chosen the correct timestamp settings above"
    self.outputLabel["text"] = tkstring1+"\n"+tkstring2+"\n"+tkstring3
    if self.saveToFile:
      newFile.close()  



myapp = App()

myapp.master.title("Parser for LotRO Herbalism Flora by PBNGGames")
myapp.master.geometry("1200x600")
try:
  image_path = resource_path("favicon.ico")
  myapp.master.iconbitmap(image_path)
except:
  print("no icon to show")
myapp.createWidgets()


myapp.mainloop()  
  
  
