from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import math

root = Tk()

def callback(event):
    print (event.x, event.y)

#---------------------------------------------------------------------------------

c76=Canvas(root,width=300,height=200,bg='white')

c76.create_line(196,7,298,7,width=5,arrow=LAST,fill='black')
x_q1=(196+298)/2 - 40
y_q1=10


c76.create_polygon(0,27,0,97,300,97,300,29,fill='maroon2')
c76.create_polygon(0,97,0,202,300,202,300,97,fill = 'lawn green')


c76.create_line(70,29,70,97,arrow=BOTH,width=2)
c76.create_line(50,98,50,188,arrow=BOTH,width=2)

#------------------------------- Plates --------------------------- 
c76.create_line(0,25,1000,25,width=10,fill='slategray')
c76.create_line(0,195,1000,195,width=10,fill='slategray')
#------------------------------- Plates ---------------------------

y_v1 = (180)/2 - 5
x_v1= 70 +3

x_v2=50+3
y_v2=(180)/2

lb1= Label(c76,text='h2',bg='maroon2')
lb1.place(x=x_v1,y=y_v1-40) 
    
lb2= Label(c76,text='h1        μ₁ =  55cP',bg='lawn green')
lb2.place(x=x_v2,y=y_v2+40)

c76.bind("<Button-1>", callback)
c76.place(x=405,y=40)

lb89=Label(c76,text='U₂',font ='Times',bg='white')
lb89.place(x=160,y=-7)

#---------------------------------------------------------------------------------

root.title("Velocity profile for two immiscible viscous fluids")
root.configure(background='white')

label1 = Label(root, text="Velocity profile for two immiscible viscous fluids", fg="green", font="Helvetica 18 bold italic underline",bg='white'                                                                                                 )
label1.place(x=290, y=0)

label1 = Label(root, text="*1 cp = 0.001 Pa.s", bg='white',fg="red", font="times 15")
label1.place(x=970, y=220)


#---------------------------------------------------------------------------

c3=Canvas(root,height=200,width=220,bg='white')
c3.create_line(111,2,111,600)
label1 = Label(c3, text="Water \n Milk \n Vinegar \n Fruit Juice \n Oil fuel \n Glycerin \n Paraffin \n Honey",
bg='white', fg="black", font="times 15")
label1.place(x=10,y=10)

label2=Label(c3,text="1 cP \n 2 cP \n 12cP \n 55 cP \n 210 cP  \n 648 cP \n 3000 cP  \n  10,000cP"
,bg='white', fg="black", font="times 15")
label2.place(x=120,y=10)
c3.bind("<Button-1>", callback)
c3.place(x=720, y=60)
#----------------------------------------------------------------------------------


label1 = Label(root, text="Viscosity of  fluid, μ₂ (cP): ", bg='white',fg="blue", font="times 15")
label1.place(x=30, y=150)
u= Entry(root, width =10,borderwidth=5, bg='white')
u.place(x=260,y=155)

label1 = Label(root, text="Velocity of upper plate, U₂ (m/s): ", bg='white',fg="blue", font="times 15")
label1.place(x=30, y=120)
v= Entry(root, width =10,borderwidth=5, bg='white')
v.place(x=300,y=120)

#---------------------------------------------------------------

label1 = Label(root, text="Fluid height, h₂ (m)", bg='white',fg="blue", font="times 15")
label1.place(x=30, y=40)

scroll1= Scale(root, from_= 0.0, to = 1, length = 180,resolution = 0.01,orient=HORIZONTAL, activebackground="orange")
scroll1.configure(background='orange')
scroll1.place(x=30, y=70)

button1 = Button(root, text="Solve",width=7, height=1,fg="red",font="times 15",command=lambda:solve())
button1.place(x=300, y=195)

tkVar1= StringVar(root)
choice1 = {'Linear (Ideal)' , 'Parabolic (Actual)'}
tkVar1.set('Linear (Ideal)')
menu = OptionMenu(root, tkVar1, *choice1)
menu.config(font=('Times',(13)), bg='orange', width=15,height = 1)
menu.place(x=50, y=200)

def solve():
    if(tkVar1.get() == 'Parabolic (Actual)'):
        solve_para()
    else:
        solve_linear()

def solve_para():
    nwin=Toplevel()
    nwin.geometry("300x100")
    Label(nwin, text="Please enter value of dP/dx\n Can be positive,0 or negative",font=10).pack()
    e=Entry(nwin)
    e.pack()
    bt=Button(nwin,text='OK',command=lambda:okk()).pack()

    def okk():
        dydx=float(e.get())
        nwin.destroy()
        solve_parabola(dydx)
    
    nwin.mainloop() 

def solve_linear():
    cnvs = Canvas(root, width=300, height=60, bg='yellow')
    label = Label(cnvs,text="Please enter correct values",fg='red',bg='yellow',font = 3)
    label.place(x=10,y=10)
    cnvs.place(x=400,y=400)

    h2=float(scroll1.get())
    h = 1.0 - h2
    viscosity = float(u.get())
    velocity = float(v.get())
    tau1=viscosity * velocity

#-----------------------------------------------------------------
#
#               x1,y1----------x4,y4
#                 |             |
#                 |             |
#                 |             |
#               x2,y2----------x3,y3
#
#------------------------------------------------------   
    
    h0 = 18 * h * 10
    c2=Canvas(root,width=300,height=300,bg='white')
    c2.create_polygon(0,22,0,187- h0 +15,300,187 - h0 + 15,300,22, fill='maroon2')
    c2.create_polygon(0,187 - h0 + 15, 0,202,300,202,300,187 - h0+15, fill='lawn green')

#------------------------------- Plates --------------------------- 
    c2.create_line(0,25,1000,25,width=10,fill='slategray')
    c2.create_line(0,202,1000,202,width=10,fill='slategray')
    #------------------------------- Plates ---------------------------
    
    c2.create_line(196,14,298,14,width=5,arrow=LAST,fill='black')
    x_q1=(196+298)/2 - 40
    y_q1=10
    lb89=Label(c2,text='U₂ = %.1f m/s' %velocity,bg='white')
    lb89.place(x=115,y=0)

    c2.create_line(70,25,70,180 - h0 + 22,arrow=BOTH,width=2)
    c2.create_line(50,180-h0 + 22,50,198,arrow=BOTH,width=2)


    #---------------------------------------------------------------

    y_v1 = (180 - h0 + 3)/2 +2
    x_v1= 70 +3

    x_v2=50+3
    y_v2=(180 - h0 + 176)/2 + 7

    lb1= Label(c2,text=' h2 = %.2f m            μ = %.2f' %(1-h,viscosity),bg='maroon2')
    lb1.place(x=x_v1,y=y_v1) 
    
    
    lb2= Label(c2,text='h1 = %.2f m                 μ₁ = 55.00 cP' %(h),bg='lawn green')
    lb2.place(x=x_v2,y=y_v2)

    c2.bind("<Button-1>", callback)
    c2.place(x=405,y=40)


#--------------------------------------------------------------         

    canvas = Canvas(root, width=1300, height=500, bg='white')
    canvas.place(x=10,y=250)
    canvas.create_polygon((70,(368-h*320) -10,70,368,545,368,545,(368-h*320) -10), fill='lawn green')
    canvas.create_polygon((70,33,70,(368-h*320) -10,545,(368-h*320) -10,545,33), fill='maroon2')

# -------------------------Boundary diagram-------------------
    canvas.create_line(70, 368, 545, 368 , width =15, fill='gainsboro')
    canvas.create_line(70, 33, 545, 33 , width =15, fill='gainsboro')
    canvas.create_line(70, 360, 70, 40 , width =3, fill='gainsboro')
    canvas.create_line(545, 360, 545, 40 , width =3, fill='gainsboro')

    canvas.create_line(70, 360 , 60, 360 , width = 1, fill='black')
    lb= Label(canvas, text='0.0',bg = 'white',font=("Times")).place(x=30,y=345)
    canvas.create_line(70, 296 , 60, 296 , width = 1, fill='black')
    lb= Label(canvas, text='0.2',bg = 'white',font=("Times")).place(x=30,y=280)
    canvas.create_line(70, 232 , 60, 232 , width = 1, fill='black')
    lb= Label(canvas, text='0.4',bg = 'white',font=("Times")).place(x=30,y=215)
    canvas.create_line(70, 168 , 60, 168 , width = 1, fill='black')
    lb= Label(canvas, text='0.6',bg = 'white',font=("Times")).place(x=30,y=150)
    canvas.create_line(70, 104 , 60, 104 , width = 1, fill='black')
    lb= Label(canvas, text='0.8',bg = 'white',font=("Times")).place(x=30,y=90)
    canvas.create_line(70, 40 , 60, 40 , width = 1, fill='black')
    lb= Label(canvas, text='1.0',bg = 'white',font=("Times")).place(x=30,y=25)
    canvas.create_line(71,360,544,41,width=3)

    canvas.create_line(71,211,295,211,width=2,arrow=LAST)
    canvas.create_line(71,297,161,297,width=2,arrow=LAST)
    canvas.create_line(71,150,386,150,width=2,arrow=LAST)
    canvas.create_line(71,265,207,265,width=2,arrow=LAST)
    canvas.create_line(71,75,491,75,width=2,arrow=LAST)
    canvas.create_line(71,322,125,322,width=2,arrow=LAST)
    canvas.create_line(71,107,448,108,width=2,arrow=LAST)
    canvas.create_line(71,180,343,180,width=2,arrow=LAST)
    canvas.create_line(71,232,261,232,width=2,arrow=LAST)
    canvas.create_line(71,107,448,108,width=2,arrow=LAST)
    canvas.create_line(71,42,540,42,width=2,arrow=LAST)
    canvas.bind("<Button-1>", callback)
#---------------------------------------------------------------------------
    x1=[]
    x2=[]
    Q=[]

    y1=viscosity
    y2=55

    N=100 -int(scroll1.get() * 100)
    visc = int(u.get())


    for i in range(0,N,1):
        x1.append(i*0.01)
        Q.append(55)

    for i in range(N-1,100,1):
        x1.append(i*0.01)
        Q.append(visc)

    fig = Figure(figsize=(7,3.5))
    a = fig.add_subplot(111)
    a.plot(x1,Q,color='red')

    a.set_xlabel('y (m)',color='green',labelpad=0) 
    a.set_ylabel('τ (Pa)',color='green')


    canvas2 = Canvas(c2, width=7.5, height=3.5)
    canvas2 = FigureCanvasTkAgg(fig, master=root)
    canvas2.get_tk_widget().place(x=610,y=260)
    canvas2.draw()

#----------------------------------------------------------------------#

def solve_parabola(dydx):
    cnvs = Canvas(root, width=300, height=50, bg='yellow')
    label = Label(cnvs,text="Please enter correct values",fg='red',bg='yellow',font =3)
    label.place(x=10,y=10)
    cnvs.place(x=400,y=400)

    canvas = Canvas(root, width=1300, height=500, bg='white')
    canvas.place(x=10,y=250)

    h2=float(scroll1.get())
    h = 1.0 - h2
    viscosity = float(u.get())
    velocity = float(v.get())
    tau1=viscosity * velocity

    h0 = 18 * h * 10
    c2=Canvas(root,width=300,height=300,bg='white')
    c2.create_polygon(0,22,0,187- h0 +15,300,187 - h0 + 15,300,22, fill='maroon2')
    c2.create_polygon(0,187 - h0 + 15, 0,202,300,202,300,187 - h0+15, fill='lawn green')

#------------------------------- Plates --------------------------- 
    c2.create_line(0,25,1000,25,width=10,fill='slategray')
    c2.create_line(0,202,1000,202,width=10,fill='slategray')
    #------------------------------- Plates ---------------------------
    
    c2.create_line(196,14,298,14,width=5,arrow=LAST,fill='black')
    x_q1=(196+298)/2 - 40
    y_q1=10
    lb89=Label(c2,text='U₂ = %.1f m/s' %velocity,bg='white')
    lb89.place(x=115,y=0)

    c2.create_line(70,25,70,180 - h0 + 22,arrow=BOTH,width=2)
    c2.create_line(50,180-h0 + 22,50,198,arrow=BOTH,width=2)


    #---------------------------------------------------------------

    y_v1 = (180 - h0 + 3)/2 +2
    x_v1= 70 +3

    x_v2=50+3
    y_v2=(180 - h0 + 176)/2 + 7

    lb1= Label(c2,text=' h2 = %.2f m            μ = %.2f' %(1-h,viscosity),bg='maroon2')
    lb1.place(x=x_v1,y=y_v1) 
    
    
    lb2= Label(c2,text='h1 = %.2f m                 μ₁ = 55.00 cP' %(h),bg='lawn green')
    lb2.place(x=x_v2,y=y_v2)

    c2.bind("<Button-1>", callback)
    c2.place(x=405,y=40)


    #-----------------------------------Parabolic Graph -------------------

    xp=[]
    yp=[]  
    xt=[]
    yt=[] 


    P1 = - dydx / (110*velocity)
    P2 = ((55/viscosity)* (1 + P1*(1-(2*h2))-1))/(1-2*h2)

    for temp in range(0,100,1):
        y = temp * 0.01

        if(y<=h2):
            P = P1
        else:
            P = P2
        u_v = y + P*y*(1-y)
        xp.append(u_v)
        yp.append(y)


    for tmp in range(0,100,1):
        if(y<=h2):
            P = P1
        else:
            P = P2        
        y = tmp*0.01
        tau = (viscosity * velocity) + ((viscosity * P * velocity) * (1- (2*y)))
        xt.append(tau)
        yt.append(y)


#-----------------------------------PLOTTING---------------------------------

    fig = Figure(figsize=(6,3.5))
    at = fig.add_subplot(111)

    at.plot(xt,yt,color='red')

    at.set_xlabel('τ (Pa)',color='blue',labelpad=0) 
    at.set_ylabel('y/h',color='blue')


    canvas2 = Canvas(canvas, width=6, height=3.5)
    canvas2 = FigureCanvasTkAgg(fig, master=root)
    canvas2.get_tk_widget().place(x=630,y=260)
    canvas2.draw()  


    fig = Figure(figsize=(6,3.5))
    ap = fig.add_subplot(111)

    ap.plot(xp,yp,color='red')

    ap.set_xlabel('u/U',color='blue',labelpad=0) 
    ap.set_ylabel('y/h',color='blue')


    canvas2 = Canvas(canvas, width=6, height=3.5)
    canvas2 = FigureCanvasTkAgg(fig, master=root)
    canvas2.get_tk_widget().place(x=30,y=260)
    canvas2.draw()

#-----------------------------------------------------------------
#
#               x1,y1----------x4,y4
#                 |             |
#                 |             |
#                 |             |
#               x2,y2----------x3,y3
#
#------------------------------------------------------   

root.state('zoomed')

root.mainloop()
