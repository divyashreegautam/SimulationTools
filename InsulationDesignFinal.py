from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import math

root = Tk()
root.geometry("1500x1500")
tkVar1= StringVar(root)

root.title("Insulation design of an electric cable")
root.configure(background='white')

# Heading
label1 = Label(root, text="Insulation design of an electric cable", fg="green", font="Verdana 22 bold italic underline",bg='white'
                                                                                                   )
label1.place(x=120, y=10)

label2 = Label(root, text="Inputs", fg="Black", font="Helvetica 15 underline",bg='white')
label2.place(x=460, y=110)

label3 = Label(root, text="Radius of electric wire, r₁ (mm)", bg='white',fg="blue", font="times 15")
label3.place(x=460, y=150)

scroll1= Scale(root, from_= 0.5, to=10, length = 250,resolution = 0.1, orient=HORIZONTAL, activebackground="orange")
scroll1.configure(background='orange')
scroll1.place(x=460, y=180)

label3 = Label(root, text="Heat transfer coefficient from cladding to ambient, h(W/m^2 C)", bg = 'white',fg="blue", font="times 15")
label3.place(x=748, y=150)

scroll2= Scale(root, from_= 2, to=20, length = 250,resolution = 0.01, orient=HORIZONTAL, activebackground="orange")
scroll2.configure(background='orange')
scroll2.place(x=748, y=180)

label3 = Label(root, text="Select Insulation material(k):", fg="blue", font="times 15",bg='white')
label3.place(x=455, y=235)

choice1 = {'Low Density Polyethene (0.3 W/mK)', 'High Density Polyethene (0.4 W/mK)', 'Polyvinyl Chloride (0.17 W/mK)',
           'Foamed Polyethene (0.25 W/mK)', 'Poly-propylene (0.19 W/mK)', 'Polyamide (0.23 W/mK)',
           'Polyester Elastomer (0.5 W/mK)', 'Polyolefine Elastomer (1.5 W/mK)'}

tkVar1.set('Low Density Polyethene (0.3 W/mK)')
popupMenu1 = OptionMenu(root, tkVar1, *choice1)
popupMenu1.configure(background='orange')
popupMenu1.place(x=455, y=263)


canvas = Canvas(root, width=300, height=180,bg='white')
photo='''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'''
photo=PhotoImage(data=photo)
image = canvas.create_image(0,0, image=photo, anchor=NW)
canvas.place(x=70,y=70)




def lb1():
    if tkVar1.get() == 'Low Density Polyethene (0.3 W/mK)':
        k1 = float(0.3)
    elif tkVar1.get() == 'High Density Polyethene (0.4 W/mK)':
        k1 = float(0.4)
    elif tkVar1.get() == 'Polyvinyl Chloride (0.17 W/mK)':
        k1 = float(0.17)
    elif tkVar1.get() == 'Foamed Polyethene (0.25 W/mK)':
        k1 = float(0.25)
    elif tkVar1.get() == 'Poly-propylene (0.19 W/mK)':
        k1 = float(0.19)
    elif tkVar1.get() == 'Polyamide (0.23 W/mK)':
        k1 = float(0.23)
    elif tkVar1.get() == 'Polyester Elastomer (0.5 W/mK)':
        k1 = float(0.5)
    elif tkVar1.get() == 'Polyolefine Elastomer (1.5 W/mK)':
        k1 = float(1.5)

    h=scroll2.get()
    r1=scroll1.get()

    rad=(k1/h)*100 #Critical radius is in centimeters now

    lb=Label(root,text="Critical radius of insulation %0.2f cm" % rad,bg='white')
    lb.place(x=100,y=305)


def lb2():
    if tkVar1.get() == 'Low Density Polyethene (0.3 W/mK)':
        k1 = float(0.3)
    elif tkVar1.get() == 'High Density Polyethene (0.4 W/mK)':
        k1 = float(0.4)
    elif tkVar1.get() == 'Polyvinyl Chloride (0.17 W/mK)':
        k1 = float(0.17)
    elif tkVar1.get() == 'Foamed Polyethene (0.25 W/mK)':
        k1 = float(0.25)
    elif tkVar1.get() == 'Poly-propylene (0.19 W/mK)':
        k1 = float(0.19)
    elif tkVar1.get() == 'Polyamide (0.23 W/mK)':
        k1 = float(0.23)
    elif tkVar1.get() == 'Polyester Elastomer (0.5 W/mK)':
        k1 = float(0.5)
    elif tkVar1.get() == 'Polyolefine Elastomer (1.5 W/mK)':
        k1 = float(1.5)

    h=scroll2.get()
    r1=scroll1.get()

    thickness=(k1/h)*100 - (r1/10) # Thickness is in centimeters

    lb=Label(root,text="Critical thickness of insulation %0.2f cm" % thickness,bg='white',width=35, height=2)
    lb.place(x=780,y=298)

def cmd():
   plot1()
   lb1()

def cmd2():
   plot2()
   lb2()


def plot1():
    #fetching k value
    if tkVar1.get() == 'Low Density Polyethene (0.3 W/mK)':
        k1 = float(0.3)
    elif tkVar1.get() == 'High Density Polyethene (0.4 W/mK)':
        k1 = float(0.4)
    elif tkVar1.get() == 'Polyvinyl Chloride (0.17 W/mK)':
        k1 = float(0.17)
    elif tkVar1.get() == 'Foamed Polyethene (0.25 W/mK)':
        k1 = float(0.25)
    elif tkVar1.get() == 'Poly-propylene (0.19 W/mK)':
        k1 = float(0.19)
    elif tkVar1.get() == 'Polyamide (0.23 W/mK)':
        k1 = float(0.23)
    elif tkVar1.get() == 'Polyester Elastomer (0.5 W/mK)':
        k1 = float(0.5)
    elif tkVar1.get() == 'Polyolefine Elastomer (1.5 W/mK)':
        k1 = float(1.5)




    r1=scroll1.get()
    h=scroll2.get()

    Q = []
    r2 = []

    crit_thickness=k1/h #in meters

    r1=0.001*r1 #r1 is converted in millimeters
   
    rA=r1

    t = 0.0001 # Thickness of one layer of insulation in meters

    N= 10 * (crit_thickness/t) # *2 has to be done instead of 10

    N=int(N)


    for i in range(0,N,1):
        rA = (r1 + (i * t))
        rC=rA*100
        r2.append(rC)


        QA = 70 / (math.log(rA / r1) / (2 * 3.14 * 1000 * k1) + 1 / (h * 2 * 3.14 * rA * 1000))
        Q.append(QA)


    fig = Figure(figsize=(6,3.5))
    a = fig.add_subplot(111)
    a.plot(r2,Q,color='red')

    a.set_xlabel('r₂(cm)',color='green',labelpad=0)
    a.set_ylabel('Q (watts)',color='green')


    canvas1 = Canvas(root, width=7.5, height=4.5)
    canvas1 = FigureCanvasTkAgg(fig, master=root)
    canvas1.get_tk_widget().place(x=40,y=295)
    canvas1.draw()

def plot2():
    #fetching k value
    if tkVar1.get() == 'Low Density Polyethene (0.3 W/mK)':
        k1 = float(0.3)
    elif tkVar1.get() == 'High Density Polyethene (0.4 W/mK)':
        k1 = float(0.4)
    elif tkVar1.get() == 'Polyvinyl Chloride (0.17 W/mK)':
        k1 = float(0.17)
    elif tkVar1.get() == 'Foamed Polyethene (0.25 W/mK)':
        k1 = float(0.25)
    elif tkVar1.get() == 'Poly-propylene (0.19 W/mK)':
        k1 = float(0.19)
    elif tkVar1.get() == 'Polyamide (0.23 W/mK)':
        k1 = float(0.23)
    elif tkVar1.get() == 'Polyester Elastomer (0.5 W/mK)':
        k1 = float(0.5)
    elif tkVar1.get() == 'Polyolefine Elastomer (1.5 W/mK)':
        k1 = float(1.5)
    

    r1=scroll1.get()
    h=scroll2.get()

    Q = []
    r2 = []

    crit_thickness=k1/h #in meters

    r1=0.001*r1 #r1 is converted in millimeters
   
    rA=r1

    t = 0.0001 # Thickness of one layer of insulation in meters

    N= 10 * (crit_thickness/t) # *2 has to be done instead of 10

    N=int(N)


    for i in range(0,N,1):
        rC=i*t*100
        r2.append(rC)

        rA = (r1 + (i * t))

        QA = 70 / (math.log(rA / r1) / (2 * 3.14 * 1000 * k1) + 1 / (h * 2 * 3.14 * rA * 1000))
        Q.append(QA)



    fig = Figure(figsize=(6,3.5))
    a = fig.add_subplot(111)
    a.plot(r2,Q,color='red')


    a.set_xlabel('t (cm)',color='green',labelpad=0)	
    a.set_ylabel('Q (watts)',color='green')

    canvas2 = Canvas(root, width=7.5, height=3.5)
    canvas2 = FigureCanvasTkAgg(fig, master=root)
    canvas2.get_tk_widget().place(x=660,y=298)
    canvas2.draw() 
  

button2 = Button(root, text="Plot r₂ wrt Q",width=11, height=1,fg="green",command=lambda:cmd())
button2.place(x=150, y=270)

button3 = Button(root, text="Plot Q wrt t", fg="green",width=11, height=1,command=lambda:cmd2())
button3.place(x=860, y=260)

root.state('zoomed')

root.mainloop()
