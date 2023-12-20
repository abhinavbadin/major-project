import tkinter
from tkinter import *
import math
import random
from threading import Thread 
from collections import defaultdict
from tkinter import ttk
from tkinter import filedialog
import matplotlib.pyplot as plt
import numpy as np
import time

global vehicles
global labels
global vehicle_x
global vehicle_y
global canvas
attacks = []
global text
global emmision
global fuel
global vehicle_distance

def getAttacks():
    attacker = random.randint(2, 6)
    while len(attacks) < attacker:
        att = random.randint(1, 8)
        if att not in attacks and att != 5:
            attacks.append(att)
    print(attacks)        
            
            

def calculateDistance(vehicle_x,vehicle_y,i):
    distance = 0
    if i < len(vehicle_x)-1:
        x1 = vehicle_x[i]
        y1 = vehicle_y[i]
        x2 = vehicle_x[i+1]
        y2 = vehicle_y[i+1]
        distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return distance

def startTrafficSimulation(vehicle_x,vehicle_y,canvas,vehicles,labels,text,emmision,fuel,vehicle_distance):
    class SimulationThread(Thread):
        def __init__(self,vehicle_x,vehicle_y,canvas,vehicles,labels,text,emmision,fuel,vehicle_distance): 
            Thread.__init__(self) 
            self.vehicle_x = vehicle_x
            self.vehicle_y = vehicle_y
            self.canvas = canvas
            self.vehicles = vehicles
            self.labels = labels
            self.text = text
            self.text.delete('1.0', END)
            self.flag = True
            self.emmision = emmision
            self.fuel = fuel
            self.vehicle_distance = vehicle_distance
        def run(self):
            start = 0
            while(self.flag):
                count = 0
                start = start + 1
                for i in range(len(vehicle_x)):
                    if vehicle_x[i] > 1200:
                        count = count + 1
                if count == len(vehicle_x):
                    self.flag = False
                for i in range(len(vehicle_x)):
                    x = 0
                    k = 0
                    if i in attacks and start > 4:
                        x = vehicle_x[i]
                        if i < 5:
                            x = x + 18
                        else:
                            x = x - 18
                        self.emmision[i] = self.emmision[i] + (random.randint(40, 70)/100)
                        self.fuel[i] = self.fuel[i] + (random.randint(50, 80)/100)
                        self.vehicle_distance[i] = self.vehicle_distance[i] + 18
                        k = 1
                    else:
                        x = vehicle_x[i]
                        if i < 5:
                            x = x + 20
                        else:
                            x = x - 20
                        self.emmision[i] = self.emmision[i] + (random.randint(30, 40)/100)
                        self.fuel[i] = self.fuel[i] + (random.randint(40, 70)/100)
                        self.vehicle_distance[i] = self.vehicle_distance[i] + 20
                    vehicle_x[i] = x
                    canvas.delete(vehicles[i])
                    canvas.delete(labels[i])
                    if vehicle_x[i] < 1250 and i < 5:
                        if k == 0:
                            name = canvas.create_oval(vehicle_x[i],vehicle_y[i],vehicle_x[i]+40,vehicle_y[i]+40, fill="blue")
                            lbl = canvas.create_text(vehicle_x[i]+20,vehicle_y[i]-10,fill="darkblue",font="Times 10 italic bold",text="V"+str(i))
                            labels[i] = lbl
                            vehicles[i] = name
                        if k == 1:
                            name = canvas.create_oval(vehicle_x[i],vehicle_y[i],vehicle_x[i]+40,vehicle_y[i]+40, fill="red")
                            lbl = canvas.create_text(vehicle_x[i]+20,vehicle_y[i]-10,fill="red",font="Times 10 italic bold",text="V"+str(i))
                            labels[i] = lbl
                            vehicles[i] = name    
                        distance = calculateDistance(vehicle_x,vehicle_y,i)
                        if distance > 129 and distance < 132:
                            self.text.insert(END,"Vehicle "+str(i)+" current distance to its preceding vehicle is : "+str(distance)+" & preceding normal vehicle maintaining safe distance\n")
                        if distance > 0 and distance < 125:
                            self.text.insert(END,"Vehicle "+str(i)+" current distance to its preceding vehicle is : "+str(distance)+" & preceding is attack vehicle & not maintaining safe distance\n")
                    if vehicle_x[i] > 50 and i > 4:
                        if k == 0:
                            name = canvas.create_oval(vehicle_x[i],vehicle_y[i],vehicle_x[i]+40,vehicle_y[i]+40, fill="blue")
                            lbl = canvas.create_text(vehicle_x[i]+20,vehicle_y[i]-10,fill="darkblue",font="Times 10 italic bold",text="V"+str(i))
                            labels[i] = lbl
                            vehicles[i] = name
                        if k == 1:
                            name = canvas.create_oval(vehicle_x[i],vehicle_y[i],vehicle_x[i]+40,vehicle_y[i]+40, fill="red")
                            lbl = canvas.create_text(vehicle_x[i]+20,vehicle_y[i]-10,fill="red",font="Times 10 italic bold",text="V"+str(i))
                            labels[i] = lbl
                            vehicles[i] = name    
                        distance = calculateDistance(vehicle_x,vehicle_y,i)
                        if distance > 129 and distance < 132:
                            self.text.insert(END,"Vehicle "+str(i)+" current distance to its preceding vehicle is : "+str(distance)+" & preceding normal vehicle maintaining safe distance\n")
                        if distance > 0 and distance < 125:
                            self.text.insert(END,"Vehicle "+str(i)+" current distance to its preceding vehicle is : "+str(distance)+" & preceding is attack vehicle & not maintaining safe distance\n")
                            
                canvas.update()
                time.sleep(0.5)
            print(self.emmision)
            print(self.fuel)
            self.text.delete('1.0', END)
            self.text.insert(END,"Simulation Completed")
    newthread = SimulationThread(vehicle_x,vehicle_y,canvas,vehicles,labels,text,emmision,fuel,vehicle_distance) 
    newthread.start()


def generate():
    global vehicle_distance
    global emmision
    global fuel
    global vehicles
    global labels
    global vehicle_x
    global vehicle_y
    global text
    global canvas
    emmision = []
    fuel = []
    vehicles = []
    vehicle_x = []
    vehicle_y = []
    labels = []
    vehicle_distance = []
    getAttacks()
    x = 10
    y = 150
    for i in range(0,5):
        vehicle_x.append(x)
        vehicle_y.append(y)
        name = canvas.create_oval(x,y,x+40,y+40, fill="blue")
        lbl = canvas.create_text(x+20,y-10,fill="darkblue",font="Times 10 italic bold",text="V"+str(i))
        labels.append(lbl)
        vehicles.append(name)
        emmision.append(0)
        fuel.append(0)
        vehicle_distance.append(0)
        x = x + 150
    x = 1150
    y = 340
    for i in range(5,10):
        vehicle_x.append(x)
        vehicle_y.append(y)
        name = canvas.create_oval(x,y,x+40,y+40, fill="blue")
        lbl = canvas.create_text(x+20,y-10,fill="darkblue",font="Times 10 italic bold",text="V"+str(i))
        labels.append(lbl)
        vehicles.append(name)
        emmision.append(0)
        fuel.append(0)
        vehicle_distance.append(0)
        x = x - 150
    

def startSimulation():
    global vehicle_distance
    global vehicles
    global labels
    global vehicle_x
    global vehicle_y
    global text
    global canvas
    startTrafficSimulation(vehicle_x,vehicle_y,canvas,vehicles,labels,text,emmision,fuel,vehicle_distance)

def calculateSeverity():
    global vehicles
    severity = len(attacks) / len(vehicles)
    text.delete('1.0', END)
    text.insert(END,'Cyber Attack Impact Severity : '+str(severity))

def fuelGraph():
    global emmision
    global fuel
    plt.figure(figsize=(10,6))
    plt.grid(True)
    plt.xlabel('Vehicles')
    plt.ylabel('Fuel & Emission Increases')
    plt.plot(emmision, 'ro-', color = 'blue')
    plt.plot(fuel, 'ro-', color = 'red')
    plt.legend(['Emission', 'Fuel Consumption'], loc='upper left')
    #plt.xticks(wordloss.index)
    plt.title('Cyber Attack Impact on Fuel & Emission Consumption Graph')
    plt.show()

def speedGraph():
    global vehicle_distance
    bars = ('0','1','2','3','4','5','6','7','8','9')
    for i in range(len(vehicle_distance)):
        vehicle_distance[i] = vehicle_distance[i]/100
    y_pos = np.arange(len(bars))
    plt.bar(y_pos, vehicle_distance)
    plt.xticks(y_pos, bars)
    plt.show()
    

def Main():
    global canvas
    global vehicle_list
    global text
    global emmision
    root = tkinter.Tk()
    root.geometry("1300x1200")
    root.title("Impact Evaluation of Cyber-attacks on Traffic Flow of Connected and Automated Vehicles")
    root.resizable(True,True)
    font1 = ('times', 12, 'bold')

    canvas = Canvas(root, width = 1200, height = 400)
    canvas.create_line(0, 100,1200, 100,fill='black',width=3)
    canvas.create_line(0, 390,1200, 390,fill='black',width=3)
    canvas.pack()

    text=Text(root,height=14,width=120)
    scroll=Scrollbar(text)
    text.configure(yscrollcommand=scroll.set)
    text.place(x=10,y=450)

    font = ('times', 14, 'bold')
    title = Label(root, text='Impact Evaluation of Cyber-attacks on Traffic Flow of Connected and Automated Vehicles')
    title.config(bg='violet red', fg='white')  
    title.config(font=font)           
    title.config(height=3, width=120)       
    title.place(x=0,y=5)

    font1 = ('times', 12, 'bold')
    generateButton = Button(root, text="Generate Traffic", command=generate)
    generateButton.place(x=1000,y=450)
    generateButton.config(font=font1)

    startButton = Button(root, text="Start Simulation", command=startSimulation)
    startButton.place(x=1000,y=500)
    startButton.config(font=font1)

    severityButton = Button(root, text="Calculate Attack Impact Severity", command=calculateSeverity)
    severityButton.place(x=1000,y=550)
    severityButton.config(font=font1)

    fuelButton = Button(root, text="Cyber Attack Impact on Fuel & Emission Consumption Graph", command=fuelGraph)
    fuelButton.place(x=1000,y=600)
    fuelButton.config(font=font1)

    speedButton = Button(root, text="Average Speed Graph", command=speedGraph)
    speedButton.place(x=1000,y=650)
    speedButton.config(font=font1)
    
    root.config(bg='steel blue')
    root.mainloop()
   
 
if __name__== '__main__' :
    Main ()
    
