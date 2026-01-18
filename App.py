from tkinter import *
from tkinter import messagebox
import burge
import coffe
import cok
import falud
import frie
import milkshak
import momo
import past
import pizz
import te

#Functions

def totalcost():
    global priceofFood,priceofDrinks,priceofCakes,subtotalofItems
    if var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or \
        var6.get() != 0 or var7.get() != 0 or var8.get() != 0 or var9.get() != 0 or var6.get() != 0 or\
        var7.get() != 0 or var8.get() != 0 or var9.get() != 0 or var10.get() != 0 or var11.get() != 0 or\
        var12.get() != 0 or var13.get() != 0 or var14.get() != 0 or var15.get() != 0 :#Check if the entry field is not zero

        #get the number of food items
        item1 = int(e_pizza.get())
        item2 = int(e_fries.get())
        item3 = int(e_burger.get())
        item4 = int(e_pasta.get())
        item5 = int(e_momos.get())
        
        item6 = int(e_coke.get())
        item7 = int(e_coffee.get())
        item8 = int(e_faluda.get())
        item9 = int(e_tea.get())
        item10 = int(e_milkshake.get())
        
        item11 = int(e_oreo.get())
        item12 = int(e_apple.get())
        item13 = int(e_kitkat.get())
        item14 = int(e_vanilla.get())
        item15 = int(e_pineapples.get())

        #calculation part
        priceofFood=(item1*120)+(item2*80)+(item3*120)+(item4*150)+ (item5*100) 

        priceofDrinks=(item6*50)+(item7*40)+ (item8 * 80) + (item9 * 40) + (item10 * 100) 
        
        priceofCakes=(item11*50)+(item12*40)+ (item13 * 60) + (item14 * 50) + (item15 * 40) 

        costoffoodvar.set(str(priceofFood)+ ' Rs')
        costofdrinksvar.set(str(priceofDrinks)+ ' Rs')
        costofcakesvar.set(str(priceofCakes)+ ' Rs')
        
        subtotalofItems=priceofFood+priceofDrinks+priceofCakes
        subtotalvar.set(str(subtotalofItems)+' Rs')

        servicetaxvar.set('50 Rs')

        tottalcost=subtotalofItems+50
        totalcostvar.set(str(tottalcost)+' Rs')

    else:
        messagebox.showerror('Error','No Item Is selected')#displays error when no item is entered

def reset():#reset all values to zero and prepares for the next bill
    e_fries.set('0')
    e_pizza.set('0')
    e_pasta.set('0')
    e_burger.set('0')
    e_momos.set('0')
    
    e_coke.set('0')
    e_coffee.set('0')
    e_faluda.set('0')
    e_tea.set('0')
    e_milkshake.set('0')
    
    e_oreo.set('0')
    e_apple.set('0')
    e_kitkat.set('0')
    e_vanilla.set('0')
    e_pineapples.set('0')
 
    textpizza.config(state=DISABLED)
    textfries.config(state=DISABLED)
    textpasta.config(state=DISABLED)
    textburger.config(state=DISABLED)
    textmomos.config(state=DISABLED)
    
    textcoke.config(state=DISABLED)
    textcoffee.config(state=DISABLED)
    textmilkshake.config(state=DISABLED)
    texttea.config(state=DISABLED)
    textfaluda.config(state=DISABLED)
    
    textoreo.config(state=DISABLED)
    textapple.config(state=DISABLED)
    textkitkat.config(state=DISABLED)
    textvanilla.config(state=DISABLED)
    textpineapples.config(state=DISABLED)

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
   
    costoffoodvar.set('')
    costofdrinksvar.set('')
    costofcakesvar.set('')
    subtotalvar.set('')
    servicetaxvar.set('')
    totalcostvar.set('')

def pizza():
    a=pizz.piz(var1.get())
    if a==1:
        textpizza.config(state=NORMAL)#enabels the entery field to enter number of items
        textpizza.delete(0,END)#deletes the value 0 in the entry field
        textpizza.focus()#the curser is in the respective entery field
    else:
        textpizza.config(state=DISABLED)#keeps the entery field as disabled
        e_pizza.set('0')#the number of items is set zero++

def fries():
    b=frie.fri(var2.get())
    if b==1:
        textfries.config(state=NORMAL)
        textfries.delete(0,END)
        textfries.focus()

    else:
        textfries.config(state=DISABLED)
        e_fries.set('0')


def burger():
    c=burge.bur(var3.get())
    if c==1:
        textburger.config(state=NORMAL)#enabels the entery field to enter number of items
        textburger.delete(0,END)#deletes the value 0 in the entry field
        textburger.focus()#the curser is in the respective entery field

    else:
        textburger.config(state=DISABLED)
        e_burger.set('0')

def pasta():
    d=past.pas(var4.get())
    if d == 1:
        textpasta.config(state=NORMAL)
        textpasta.focus()
        textpasta.delete(0, END)
    elif var4.get() == 0:
        textpasta.config(state=DISABLED)
        e_pasta.set('0')


def momos():
    e=momo.mo(var5.get())
    if e == 1:
        textmomos.config(state=NORMAL)#enabels the entery field to enter number of items
        textmomos.focus()#deletes the value 0 in the entry field
        textmomos.delete(0, END)
    elif var5.get() == 0:
        textmomos.config(state=DISABLED)
        e_momos.set('0')


def coke():
    f=cok.co(var6.get())
    if f == 1:
        textcoke.config(state=NORMAL)
        textcoke.focus()
        textcoke.delete(0, END)
    elif var6.get() == 0:
        textcoke.config(state=DISABLED)
        e_coke.set('0')


def coffee():
    g=coffe.coff(var7.get())
    if g== 1:
        textcoffee.config(state=NORMAL)#enabels the entery field to enter number of items
        textcoffee.focus()#deletes the value 0 in the entry field
        textcoffee.delete(0, END)
    elif var7.get() == 0:
        textcoffee.config(state=DISABLED)
        e_coffee.set('0')


def faluda():
    h=falud.falu(var8.get())
    if h == 1:
        textfaluda.config(state=NORMAL)
        textfaluda.focus()
        textfaluda.delete(0, END)
    elif var8.get() == 0:
        textfaluda.config(state=DISABLED)
        e_faluda.set('0')


def tea():
    i=te.t(var9.get())
    if i == 1:
        texttea.config(state=NORMAL)#enabels the entery field to enter number of items
        texttea.focus()#deletes the value 0 in the entry field
        texttea.delete(0, END)
    elif var9.get() == 0:
        texttea.config(state=DISABLED)
        e_tea.set('0')


def milkshake():
    j=milkshak.milk(var10.get())
    if j == 1:
        textmilkshake.config(state=NORMAL)
        textmilkshake.focus()
        textmilkshake.delete(0, END)
    elif var10.get() == 0:
        textmilkshake.config(state=DISABLED)
        e_milkshake.set('0')
        
def oreo():
    if var11.get() == 1:
        textoreo.config(state=NORMAL)
        textoreo.focus()
        textoreo.delete(0, END)
    elif var11.get() == 0:
        textoreo.config(state=DISABLED)
        e_oreo.set('0')


def apple():
    if var12.get() == 1:
        textapple.config(state=NORMAL)
        textapple.focus()
        textapple.delete(0, END)
    elif var12.get() == 0:
        textapple.config(state=DISABLED)
        e_apple.set('0')


def kitkat():
    if var13.get() == 1:
        textkitkat.config(state=NORMAL)
        textkitkat.focus()
        textkitkat.delete(0, END)
    elif var13.get() == 0:
        textkitkat.config(state=DISABLED)
        e_kitkat.set('0')


def vanilla():
    if var14.get() == 1:
        textvanilla.config(state=NORMAL)
        textvanilla.focus()
        textvanilla.delete(0, END)
    elif var14.get() == 0:
        textvanilla.config(state=DISABLED)
        e_vanilla.set('0')


def pineapples():
    if var15.get() == 1:
        textpineapples.config(state=NORMAL)
        textpineapples.focus()
        textpineapples.delete(0, END)
    elif var15.get() == 0:
        textpineapples.config(state=DISABLED)
        e_pineapples.set('0')        
        

from PIL import Image, ImageTk

#GUI 
root=Tk()

root.geometry('1000x550+0+0')

root.title('Restaurant Billing System')

root.config(bg='black')#Background Color

topFrame=Frame(root,bd=10,relief=RIDGE,bg='white')
topFrame.pack(side=TOP)
labelTitle=Label(topFrame,text='Restaurant Billing System',font=('Georgia',30,'bold'),fg='cyan',bd=9,bg='black',width=20)
labelTitle.grid(row=0,column=0)

#frames

menuFrame=Frame(root,bg='black')
menuFrame.pack(side=TOP)

costFrame=Frame(menuFrame,bg='black',pady=10)#display frame
costFrame.pack(side=BOTTOM)

foodFrame=LabelFrame(menuFrame,text='Food',font=('arial',19,'bold'),bd=10,fg='cyan',bg='black')#foood frame
foodFrame.pack(side=LEFT)

drinksFrame=LabelFrame(menuFrame,text='Drinks',font=('arial',19,'bold'),bd=10,fg='cyan',bg='black')#drinks frame
drinksFrame.pack(side=LEFT)

cakesFrame=LabelFrame(menuFrame,text='Pastries',font=('arial',19,'bold'),bd=10,fg='cyan',bg='black')#cake frame
cakesFrame.pack(side=LEFT)

#Variables

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()

var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()

var11 = IntVar()
var12= IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()


e_pizza=StringVar()
e_fries=StringVar()
e_pasta = StringVar()
e_burger = StringVar()
e_momos = StringVar()

e_coke=StringVar()
e_coffee = StringVar()
e_faluda = StringVar()
e_tea = StringVar()
e_milkshake = StringVar()

e_oreo=StringVar()
e_apple = StringVar()
e_kitkat = StringVar()
e_vanilla = StringVar()
e_pineapples = StringVar()



costoffoodvar=StringVar()
costofdrinksvar=StringVar()
costofcakesvar=StringVar()
subtotalvar=StringVar()
servicetaxvar=StringVar()
totalcostvar=StringVar()


e_pizza.set('0')
e_fries.set('0')
e_pasta.set('0')
e_burger.set('0')
e_momos.set('0')

e_coke.set('0')
e_coffee.set('0')
e_faluda.set('0')
e_tea.set('0')
e_milkshake.set('0')

e_oreo.set('0')
e_apple.set('0')
e_kitkat.set('0')
e_vanilla.set('0')
e_pineapples.set('0')



pizza_image = Image.open("pizza.png.png")
resized1_image = pizza_image.resize((40,40))
photo1_image = ImageTk.PhotoImage(image=resized1_image)

fries_image = Image.open("fries.png.png")
resized2_image = fries_image.resize((40,40))
photo2_image = ImageTk.PhotoImage(image=resized2_image)

burger_image = Image.open("burger.png.png")
resized3_image = burger_image.resize((40,40))
photo3_image = ImageTk.PhotoImage(image=resized3_image)

pasta_image = Image.open("pasta.png.png")
resized4_image = pasta_image.resize((40,40))
photo4_image = ImageTk.PhotoImage(image=resized4_image)

momos_image = Image.open("momos.png.png")
resized5_image = momos_image.resize((40,40))
photo5_image = ImageTk.PhotoImage(image=resized5_image)

coke_image = Image.open("coke.png.png")
resized6_image = coke_image.resize((40,40))
photo6_image = ImageTk.PhotoImage(image=resized6_image)

coffee_image = Image.open("coffee.png.png")
resized7_image = coffee_image.resize((40,40))
photo7_image = ImageTk.PhotoImage(image=resized7_image)

faluda_image = Image.open("faluda.png.png")
resized8_image = faluda_image.resize((40,40))
photo8_image = ImageTk.PhotoImage(image=resized8_image)

tea_image = Image.open("tea.png.png")
resized9_image = tea_image.resize((40,40))
photo9_image = ImageTk.PhotoImage(image=resized9_image)

milkshake_image = Image.open("milkshake.png.png")
resized10_image = milkshake_image.resize((40,40))
photo10_image = ImageTk.PhotoImage(image=resized10_image)


oreo_image = Image.open("oreo.png.png")
resized11_image = oreo_image.resize((40,40))
photo11_image = ImageTk.PhotoImage(image=resized11_image)

apple_image = Image.open("apple.png.png")
resized12_image = apple_image.resize((40,40))
photo12_image = ImageTk.PhotoImage(image=resized12_image)

kitkat_image = Image.open("kitkat.png.png")
resized13_image = kitkat_image.resize((40,40))
photo13_image = ImageTk.PhotoImage(image=resized13_image)

vanilla_image = Image.open("vanilla.png.png")
resized14_image = vanilla_image.resize((40,40))
photo14_image = ImageTk.PhotoImage(image=resized14_image)

pineapples_image = Image.open("pineapple.png.png")
resized15_image = pineapples_image.resize((40,40))
photo15_image = ImageTk.PhotoImage(image=resized15_image)


#FOOD

pizza=Checkbutton(foodFrame,text='Pizza',font=('arial',18,'bold'),fg='cyan',bg='black',onvalue=1,offvalue=0,variable=var1,command=pizza)
pizza.grid(row=0,column=0,sticky=W)

fries=Checkbutton(foodFrame,text='Fries',font=('arial',18,'bold'),fg='cyan',bg='black',onvalue=1,offvalue=0,variable=var2,command=fries)
fries.grid(row=1,column=0,sticky=W)

burger=Checkbutton(foodFrame,text='Burger',font=('arial',18,'bold'),fg='cyan',bg='black',onvalue=1,offvalue=0,variable=var3,command=burger)
burger.grid(row=2,column=0,sticky=W)

pasta=Checkbutton(foodFrame,text='Pasta',font=('arial',18,'bold'),fg='cyan',bg='black',onvalue=1,offvalue=0,variable=var4,command=pasta)
pasta.grid(row=3,column=0,sticky=W)

momos=Checkbutton(foodFrame,text='Momos',font=('arial',18,'bold'),fg='cyan',bg='black',onvalue=1,offvalue=0,variable=var5,command=momos)
momos.grid(row=4,column=0,sticky=W)

pizza_label = Label(foodFrame, image=photo1_image)
pizza_label.grid(row=0, column=1,padx=5,pady=5)

fries_label = Label(foodFrame, image=photo2_image)
fries_label.grid(row=1, column=1,padx=5,pady=5)

burger_label = Label(foodFrame, image=photo3_image)
burger_label.grid(row=2, column=1,padx=5,pady=5)

pasta_label = Label(foodFrame, image=photo4_image)
pasta_label.grid(row=3, column=1,padx=5,pady=5)

momos_label = Label(foodFrame, image=photo5_image)
momos_label.grid(row=4, column=1,padx=5,pady=5)

#Entry Fields for Food Items

textpizza=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_pizza)
textpizza.grid(row=0,column=2)

textfries=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_fries)
textfries.grid(row=1,column=2)

textburger=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_burger)
textburger.grid(row=2,column=2)

textpasta = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_pasta)
textpasta.grid(row=3, column=2)

textmomos = Entry(foodFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_momos)
textmomos.grid(row=4, column=2)

#Drinks

coke=Checkbutton(drinksFrame,text='Coke',font=('arial',18,'bold'),fg='cyan',bg='black',onvalue=1,offvalue=0,variable=var6,command=coke)
coke.grid(row=0,column=0,sticky=W)

coffee=Checkbutton(drinksFrame,text='Coffee',font=('arial',18,'bold'),fg='cyan',bg='black',onvalue=1,offvalue=0,variable=var7,command=coffee)
coffee.grid(row=1,column=0,sticky=W)

faluda=Checkbutton(drinksFrame,text='Faluda',font=('arial',18,'bold'),fg='cyan',bg='black',onvalue=1,offvalue=0,variable=var8,command=faluda)
faluda.grid(row=2,column=0,sticky=W)

tea=Checkbutton(drinksFrame,text='Tea',font=('arial',18,'bold'),fg='cyan',bg='black',onvalue=1,offvalue=0,variable=var9,command=tea)
tea.grid(row=3,column=0,sticky=W)

milkshake=Checkbutton(drinksFrame,text='Milkshake',font=('arial',18,'bold'),fg='cyan',bg='black',onvalue=1,offvalue=0,variable=var10,command=milkshake)
milkshake.grid(row=4,column=0,sticky=W)

coke_label = Label(drinksFrame, image=photo6_image)
coke_label.grid(row=0, column=1,padx=5,pady=5)

coffee_label = Label(drinksFrame, image=photo7_image)
coffee_label.grid(row=1, column=1,padx=5,pady=5)

faluda_label = Label(drinksFrame, image=photo8_image)
faluda_label.grid(row=2, column=1,padx=5,pady=5)

tea_label = Label(drinksFrame, image=photo9_image)
tea_label.grid(row=3, column=1,padx=5,pady=5)

milkshake_label = Label(drinksFrame, image=photo10_image)
milkshake_label.grid(row=4, column=1,padx=5,pady=5)

#Entry fields for drink items

textcoke = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_coke)
textcoke.grid(row=0, column=2)

textcoffee = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_coffee)
textcoffee.grid(row=1, column=2)

textfaluda = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_faluda)
textfaluda.grid(row=2, column=2)

texttea = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_tea)
texttea.grid(row=3, column=2)

textmilkshake = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_milkshake)
textmilkshake.grid(row=4, column=2)

#Cakes

oreocake=Checkbutton(cakesFrame,text='Oreo',font=('arial',18,'bold'),fg='cyan',bg='black',onvalue=1,offvalue=0,variable=var11,command=oreo)
oreocake.grid(row=0,column=0,sticky=W)

applecake=Checkbutton(cakesFrame,text='Apple',font=('arial',18,'bold'),fg='cyan',bg='black',onvalue=1,offvalue=0,variable=var12,command=apple)
applecake.grid(row=1,column=0,sticky=W)

kitkatcake=Checkbutton(cakesFrame,text='Kitkat',font=('arial',18,'bold'),fg='cyan',bg='black',onvalue=1,offvalue=0,variable=var13 ,command=kitkat)
kitkatcake.grid(row=2,column=0,sticky=W)

vanillacake=Checkbutton(cakesFrame,text='Vanilla',font=('arial',18,'bold'),fg='cyan',bg='black',onvalue=1,offvalue=0,variable=var14,command=vanilla)
vanillacake.grid(row=3,column=0,sticky=W)

pineapplescake=Checkbutton(cakesFrame,text='pineapples',font=('arial',18,'bold'),fg='cyan',bg='black',onvalue=1,offvalue=0,variable=var15 ,command=pineapples)
pineapplescake.grid(row=4,column=0,sticky=W)

oreo_label = Label(cakesFrame, image=photo11_image)
oreo_label.grid(row=0, column=1,padx=5,pady=5)

apple_label = Label(cakesFrame, image=photo12_image)
apple_label.grid(row=1, column=1,padx=5,pady=5)

kitkat_label = Label(cakesFrame, image=photo13_image)
kitkat_label.grid(row=2, column=1,padx=5,pady=5)

vanilla_label = Label(cakesFrame, image=photo14_image)
vanilla_label.grid(row=3, column=1,padx=5,pady=5)

pineapples_label = Label(cakesFrame, image=photo15_image)
pineapples_label.grid(row=4, column=1,padx=5,pady=5)

#entry fields for cakes

textoreo = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_oreo)
textoreo.grid(row=0, column=2)

textapple = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_apple)
textapple.grid(row=1, column=2)

textkitkat = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_kitkat)
textkitkat.grid(row=2, column=2)

textvanilla = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_vanilla)
textvanilla.grid(row=3, column=2)

textpineapples = Entry(cakesFrame, font=('arial', 18, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_pineapples)
textpineapples.grid(row=4, column=2)


#Cost display 

labelCostofFood=Label(costFrame,text='Cost of Food',font=('arial',16,'bold'),bg='black',fg='cyan')
labelCostofFood.grid(row=0,column=0)

textCostofFood=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costoffoodvar)
textCostofFood.grid(row=0,column=1,padx=41)

labelCostofDrinks=Label(costFrame,text='Cost of Drinks',font=('arial',16,'bold'),bg='black',fg='cyan')
labelCostofDrinks.grid(row=1,column=0)

textCostofDrinks=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costofdrinksvar)
textCostofDrinks.grid(row=1,column=1,padx=41)

labelCostofCakes=Label(costFrame,text='Cost of Cakes',font=('arial',16,'bold'),bg='black',fg='cyan')
labelCostofCakes.grid(row=2,column=0)

textCostofCakes=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costofcakesvar)
textCostofCakes.grid(row=2,column=1,padx=41)

labelSubTotal=Label(costFrame,text='Sub Total',font=('arial',16,'bold'),bg='black',fg='cyan')
labelSubTotal.grid(row=0,column=2)

textSubTotal=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=subtotalvar)
textSubTotal.grid(row=0,column=3,padx=41)

labelServiceTax=Label(costFrame,text='Service Tax',font=('arial',16,'bold'),bg='black',fg='cyan')
labelServiceTax.grid(row=1,column=2)

textServiceTax=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=servicetaxvar)
textServiceTax.grid(row=1,column=3,padx=41)

labelTotalCost=Label(costFrame,text='Total Cost',font=('arial',16,'bold'),bg='black',fg='cyan')
labelTotalCost.grid(row=2,column=2)

textTotalCost=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=totalcostvar)
textTotalCost.grid(row=2,column=3,padx=41)

#Buttons

buttonTotal=Button(costFrame,text='Total',font=('arial',14,'bold'),bg='black',fg='cyan',bd=3,padx=5,command=totalcost)
buttonTotal.grid(row=0,column=4)

buttonReset=Button(costFrame,text='Reset',font=('arial',14,'bold'),bg='black',fg='cyan',bd=3,padx=5,command=reset)
buttonReset.grid(row=1,column=4)

root.mainloop()#Terminate GUI