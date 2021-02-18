
from tkinter import*
import random
import time;


root = Tk()
root.geometry("1600x800+0+0")
root.title("Restaurant Manager")

text_Input = StringVar()
operator = ""




Tops = Frame(root, width = 1600, height=50, bg ="powder blue", relief = SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width = 800, height=700, relief = SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width =300, height=700,  relief = SUNKEN)
f2.pack(side=RIGHT)

#===================Time==========================
localtime = time.asctime(time.localtime(time.time()))
#==================Infos=============================
lblInfo = Label(Tops, font=('arial',50, 'bold'), text = "Restaurant Manager" , fg="Steel Blue", bd=10,anchor ='w')
lblInfo.grid(row=0, column=0)

lblInfo = Label(Tops, font=('arial',20, 'bold'), text = localtime , fg="Steel Blue", bd=10,anchor ='w')
lblInfo.grid(row=1, column=0)
#=================================Rechner=====================================

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClearDispay():
    global operator
    operator=""
    text_Input.set("")

def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator=""
    
def Ref():
    x = random.randint(10908, 500876)
    randomRef = str(x)
    rand=randomRef

    CoF = float(Fries)
    CoD = float(Drinks)
    CoFilet = float(Filet)
    CoBurger = float(Burger)
    CoChicken = float(Chicken)
    CoCheese = float(Cheese)

    CostofFries = CoF * 0.99
    CostofDrinks = CoD * 1.00
    CostofFilet = CoFilet * 2.99
    CostofBurger = CoBurger * 2.87
    CostofChicken = CoChicken * 2.89
    CostofCheese = CoCheese * 2.69


    CostofMeal = (CostofFries + CostofDrinks + CostofFilet + CostofBurger + CostofChicken + CostofCheese)

    PayTax = ((CostofFries + CostofDrinks + CostofFilet + CostofBurger + CostofChicken + CostofCheese) * 0.2)

    TotalCost = (CostofFries + CostofDrinks + CostofFilet + CostofBurger + CostofChicken + CostofCheese)

    Ser_Charge = ((CostofFries + CostofDrinks + CostofFilet + CostofBurger + CostofChicken + CostofCheese) / 99)

    Service = Ser_Charge

    OverAllCost = (PayTax + TotalCost + Ser_Charge)

    PaidTax = PayTax

    Ser_Charge = Service
    Cost = CostofMeal
    Tax = PaidTax
    Subtotal = CostofMeal
    global Total
    Total = OverAllCost

    print(Ser_Charge)
    print(Cost)
    print(Tax)
    print(Subtotal)
    print(Total)

def qExit():
    root.destroy()

def Reset():
    rand = 0.0
    Fries = 0.0
    Burger = 0.0
    Filet = 0.0
    Subtotal = 0.0
    Total = 0.0
    Service = 0.0
    Drinks = 0.0
    Tax = 0.0
    Cost = 0.0
    Chicken = 0.0
    Cheese = 0.0
    


txtDisplay = Entry(f2, font =('arial', 20, 'bold'), textvariable = text_Input, bd =30, insertwidth =4, 
                                bg="powder blue", justify = 'right')
txtDisplay.grid(columnspan=4)

btn7 = Button(f2, padx=16, pady=16, bd =8, fg="black", font=('arial',20, 'bold'), text="7", bg="powder blue",
                                 command=lambda: btnClick(7)).grid(row=2, column=0)

btn8 = Button(f2, padx=16, pady=16, bd =8, fg="black", font=('arial',20, 'bold'), text="8", bg="powder blue",
                                 command=lambda: btnClick(8)).grid(row=2, column=1)

btn9 = Button(f2, padx=16, pady=16, bd =8, fg="black", font=('arial',20, 'bold'), text="9", bg="powder blue",
                                 command=lambda: btnClick(9)).grid(row=2, column=2)

Addition = Button(f2, padx=16, pady=16, bd =8, fg="black", font=('arial',20, 'bold'), text="+", bg="powder blue",
#=====================================================================
                                 command=lambda: btnClick("+")).grid(row=2, column=3)
btn4 = Button(f2, padx=16, pady=16, bd =8, fg="black", font=('arial',20, 'bold'), text="4", bg="powder blue",
                                 command=lambda: btnClick(4)).grid(row=3, column=0)

btn5 = Button(f2, padx=16, pady=16, bd =8, fg="black", font=('arial',20, 'bold'), text="5", bg="powder blue",
                                 command=lambda: btnClick(5)).grid(row=3, column=1)

btn6 = Button(f2, padx=16, pady=16, bd =8, fg="black", font=('arial',20, 'bold'), text="6", bg="powder blue",
                                 command=lambda: btnClick(6)).grid(row=3, column=2)

Substraction = Button(f2, padx=16, pady=16, bd =8, fg="black", font=('arial',20, 'bold'), text="-", bg="powder blue",
                                 command=lambda: btnClick("-")).grid(row=3, column=3)
#=================================================================================
btn1 = Button(f2, padx=16, pady=16, bd =8, fg="black", font=('arial',20, 'bold'), text="1", bg="powder blue",
                                 command=lambda: btnClick(1)).grid(row=4, column=0)

btn2 = Button(f2, padx=16, pady=16, bd =8, fg="black", font=('arial',20, 'bold'), text="2", bg="powder blue",
                                 command=lambda: btnClick(2)).grid(row=4, column=1)

btn3 = Button(f2, padx=16, pady=16, bd =8, fg="black", font=('arial',20, 'bold'), text="3", bg="powder blue",
                                 command=lambda: btnClick(3)).grid(row=4, column=2)

Multiply = Button(f2, padx=16, pady=16, bd =8, fg="black", font=('arial',20, 'bold'), text="*", bg="powder blue",
                                 command=lambda: btnClick("*")).grid(row=4, column=3)
#===================================================================================

btn0 = Button(f2, padx=16, pady=16, bd =8, fg="black", font=('arial',20, 'bold'), text="0", bg="powder blue").grid(row=5, column=0)
                               
btnClaer = Button(f2, padx=16, pady=16, bd =8, fg="black", font=('arial',20, 'bold'), text="C", bg="powder blue",command=btnClearDispay).grid(row=5, column=1)
                                 
btnEquals = Button(f2, padx=16, pady=16, bd =8, fg="black", font=('arial',20, 'bold'), text="=", bg="powder blue", command=btnEqualsInput).grid(row=5, column=2)
                                 
Division = Button(f2, padx=16, pady=16, bd =8, fg="black", font=('arial',20, 'bold'), text="/", bg="powder blue",
                        command=lambda: btnClick("/")).grid(row=5, column=3)
                                 

#================================================Restaurant Infos 1================================================

rand = 1
Fries = 2
Burger = 3
Filet = 4
Chicken =5
Cheese = 6

lblReference =Label(f1, font =('arial', 16, 'bold'), text="Reference", bd=16, anchor='w')
lblReference.grid(row=0,  column=0)
txtReference =Entry(f1, font =('arial', 16, 'bold'), textvariable =rand, bd=10, insertwidth=4,
                bg="powder blue", justify = 'right')
txtReference.grid(row=0,  column=1)

lblFries =Label(f1, font =('arial', 16, 'bold'), text="Large Fries", bd=16, anchor='w')
lblFries.grid(row=1,  column=0)
txtFries =Entry(f1, font =('arial', 16, 'bold'), textvariable =Fries, bd=10, insertwidth=4,
                bg="powder blue", justify = 'right')
txtFries.grid(row=1,  column=1)

lblBurger =Label(f1, font =('arial', 16, 'bold'), text="Burger_Meal", bd=16, anchor='w')
lblBurger.grid(row=2,  column=0)
txtBurger =Entry(f1, font =('arial', 16, 'bold'), textvariable =Burger, bd=10, insertwidth=4,
                bg="powder blue", justify = 'right')
txtBurger.grid(row=2,  column=1)

lblFilet =Label(f1, font =('arial', 16, 'bold'), text="Filet_o_Meal", bd=16, anchor='w')
lblFilet.grid(row=3,  column=0)
txtFilet =Entry(f1, font =('arial', 16, 'bold'), textvariable =Filet, bd=10, insertwidth=4,
                bg="powder blue", justify = 'right')
txtFilet.grid(row=3,  column=1)

lblChicken =Label(f1, font =('arial', 16, 'bold'), text="Chicken Meal", bd=16, anchor='w')
lblChicken.grid(row=4,  column=0)
txtChicken =Entry(f1, font =('arial', 16, 'bold'), textvariable = Chicken, bd=10, insertwidth=4,
                bg="powder blue", justify = 'right')
txtChicken.grid(row=4,  column=1)

lblCheese =Label(f1, font =('arial', 16, 'bold'), text="Cheese Meal", bd=16, anchor='w')
lblCheese.grid(row=5,  column=0)
txtCheese =Entry(f1, font =('arial', 16, 'bold'), textvariable = Cheese, bd=10, insertwidth=4,
                bg="powder blue", justify = 'right')
txtCheese.grid(row=5,  column=1)
#================================================Restaurant Infos 2================================================

Total = 7
Service = 8
Drinks = 9
Tax = 10
Cost = 11
Chicken = 12
Cheese = 13
SubTotal = 14

lblDrinks =Label(f1, font =('arial', 16, 'bold'), text="Drinks", bd=16, anchor='w')
lblDrinks.grid(row=0,  column=2)
txtDrinks =Entry(f1, font =('arial', 16, 'bold'), textvariable =Drinks, bd=10, insertwidth=4,
                bg="#ffffff", justify = 'right')
txtDrinks.grid(row=0,  column=3)

lblCost =Label(f1, font =('arial', 16, 'bold'), text="Cost of Meal", bd=16, anchor='w')
lblCost.grid(row=1,  column=2)
txtCost =Entry(f1, font =('arial', 16, 'bold'), textvariable =Cost, bd=10, insertwidth=4,
                bg="#ffffff", justify = 'right')
txtCost.grid(row=1,  column=3)

lblStateTax =Label(f1, font =('arial', 16, 'bold'), text="State Tax", bd=16, anchor='w')
lblStateTax.grid(row=2,  column=2)
txtStateTax =Entry(f1, font =('arial', 16, 'bold'), textvariable =Tax, bd=10, insertwidth=4,
                bg="#ffffff", justify = 'right')
txtStateTax.grid(row=2,  column=3)

lblService =Label(f1, font =('arial', 16, 'bold'), text="Service_Charge", bd=16, anchor='w')
lblService.grid(row=3,  column=2)
txtService =Entry(f1, font =('arial', 16, 'bold'), textvariable =Service, bd=10, insertwidth=4,
                bg="#ffffff", justify = 'right')
txtService.grid(row=3,  column=3)

lblSubTotal =Label(f1, font =('arial', 16, 'bold'), text="Sub Total", bd=16, anchor='w')
lblSubTotal.grid(row=4,  column=2)
txtSubTotal =Entry(f1, font =('arial', 16, 'bold'), textvariable = SubTotal , bd=10, insertwidth=4,
                bg="#ffffff", justify = 'right')
txtSubTotal.grid(row=4,  column=3)

lblTotal =Label(f1, font =('arial', 16, 'bold'), text=" Total", bd=16, anchor='w')
lblTotal.grid(row=5,  column=2)
txtTotal =Entry(f1, font =('arial', 16, 'bold'), textvariable =Total, bd=10, insertwidth=4,
                bg="#ffffff", justify = 'right')
txtTotal.grid(row=5,  column=3)
S
#==================================Button==================
btnTotal = Button(f1, padx=16, pady =16, fg="black",font =('arial', 16, 'bold'),width=10,
                text="Total", bg= "powder blue",command = Ref).grid(row=7, column=1)

btnReset = Button(f1, padx=16, pady =16, fg="black",font =('arial', 16, 'bold'),width=10,
                text="Reset", bg= "powder blue",command =Reset).grid(row=7, column=2)

btnExit = Button(f1, padx=16, pady =16, fg="black",font =('arial', 16, 'bold'),width=10,
                text="Exit", bg= "powder blue",command =qExit).grid(row=7, column=3) 



root.mainloop()