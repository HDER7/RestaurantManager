from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox

operator = ''
price_foods = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
price_drinks = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
price_desserts = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]


def touch_button(num):
    global operator
    operator = operator + num
    calculator_screen.delete(0, END)
    calculator_screen.insert(END, operator)


def clear():
    global operator
    operator = ''
    calculator_screen.delete(0, END)


def calc():
    global operator
    r = str(eval(operator))
    calculator_screen.delete(0, END)
    calculator_screen.insert(0, r)
    operator = ''


def check():
    x = 0
    for c in square_food:
        if food_var[x].get() == 1:
            square_food[x].config(state=NORMAL)
            if square_food[x].get() == '0':
                square_food[x].delete(0, END)
            square_food[x].focus()
        else:
            square_food[x].config(state=DISABLED)
            text_food[x].set('0')
        x += 1

    x = 0
    for c in square_drink:
        if drink_var[x].get() == 1:
            square_drink[x].config(state=NORMAL)
            if square_drink[x].get() == '0':
                square_drink[x].delete(0, END)
            square_drink[x].focus()
        else:
            square_drink[x].config(state=DISABLED)
            text_drink[x].set('0')
        x += 1

    x = 0
    for c in square_dessert:
        if dessert_var[x].get() == 1:
            square_dessert[x].config(state=NORMAL)
            if square_dessert[x].get() == '0':
                square_dessert[x].delete(0, END)
            square_dessert[x].focus()
        else:
            square_dessert[x].config(state=DISABLED)
            text_dessert[x].set('0')
        x += 1


def total():
    subtotal_food = 0
    p = 0
    for c in text_food:
        subtotal_food = subtotal_food + (float(c.get())*price_foods[p])
        p += 1

    subtotal_drink = 0
    p = 0
    for c in text_drink:
        subtotal_drink = subtotal_drink + (float(c.get()) * price_drinks[p])
        p += 1

    subtotal_dessert = 0
    p = 0
    for c in text_drink:
        subtotal_dessert = subtotal_dessert + (float(c.get()) * price_desserts[p])
        p += 1

    subtotal = subtotal_food + subtotal_drink + subtotal_dessert
    tax = subtotal * 0.19
    t = subtotal + tax

    var_cost_food.set(f'$ {round(subtotal_food, 2)}')
    var_cost_drink.set(f'$ {round(subtotal_drink, 2)}')
    var_cost_dessert.set(f'$ {round(subtotal_dessert, 2)}')
    var_subtotal.set(f'$ {round(subtotal, 2)}')
    var_taxes.set(f'$ {round(tax, 2)}')
    var_total.set(f'$ {round(t, 2)}')


def bill():
    text_bill.config(state=NORMAL)
    text_bill.delete(1.0, END)
    num_bill = f'N#-{random.randint(1000,9999)}'
    date = datetime.datetime.now()
    bill_date = f'{date.day}/{date.month}/{date.year} - {date.hour}:{date.minute}'
    text_bill.insert(END, f'Data:\t{num_bill}\t\t{bill_date}\n')
    text_bill.insert(END, f'*'*47)
    text_bill.insert(END, f'Items\t\tAmount\tCost Items\n')
    text_bill.insert(END, f'-'*54)
    x = 0
    for c in text_food:
        if c.get() != '0':
            text_bill.insert(END, f'{food_list[x]}\t\t{c.get()}\t'
                                  f'${int(c.get()) * price_foods[x]}\n')
        x += 1

    x = 0
    for d in text_drink:
        if d.get() != '0':
            text_bill.insert(END, f'{drink_list[x]}\t\t{d.get()}\t'
                                  f'${int(d.get()) * price_drinks[x]}\n')
        x += 1

    x = 0
    for d in text_dessert:
        if d.get() != '0':
            text_bill.insert(END, f'{dessert_list[x]}\t\t{d.get()}\t'
                                  f'${int(d.get()) * price_desserts[x]}\n')
        x += 1
    text_bill.insert(END, f'-'*54)
    text_bill.insert(END, f'Foods Cost:\t\t\t{var_cost_food.get()}\n')
    text_bill.insert(END, f'Drinks Cost:\t\t\t{var_cost_drink.get()}\n')
    text_bill.insert(END, f'Dessert Cost:\t\t\t{var_cost_dessert.get()}\n')
    text_bill.insert(END, f'-'*54)
    text_bill.insert(END, f'Subtotal:\t\t\t{var_subtotal.get()}\n')
    text_bill.insert(END, f'Taxes:\t\t\t{var_taxes.get()}\n')
    text_bill.insert(END, f'Total:\t\t\t{var_total.get()}\n')
    text_bill.config(state=DISABLED)
    text_bill.insert(END, f'*' * 47)


def save():
    info_bill = text_bill.get(1.0, END)
    file = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    file.write(info_bill)
    file.close()
    messagebox.showinfo('Save Bill', 'The bill has been saved')


def reset():
    text_bill.config(state=NORMAL)
    text_bill.delete(0.1, END)
    text_bill.config(state=DISABLED)
    for text in text_food:
        text.set('0')
    for text in text_drink:
        text.set('0')
    for text in text_dessert:
        text.set('0')

    for c in square_food:
        c.config(state=DISABLED)
    for c in square_drink:
        c.config(state=DISABLED)
    for c in square_dessert:
        c.config(state=DISABLED)

    for v in food_var:
        v.set(0)
    for v in drink_var:
        v.set(0)
    for v in dessert_var:
        v.set(0)

    var_cost_food.set('')
    var_cost_drink.set('')
    var_cost_dessert.set('')
    var_subtotal.set('')
    var_taxes.set('')
    var_total.set('')


# Set screen size,title and background color
app = Tk()
app.geometry('1160x615+0+0')
app.resizable(False, False)
app.title('Restaurant Manager')
app.config(bg='burlywood3')

# Top Panel
top_panel = Frame(app, bd=1, relief=FLAT)
top_panel.pack(side=TOP)

# Label title
title_tag = Label(top_panel, text='Facturation system', fg='azure4',
                  font=('Dosis', 58), bg='burlywood3', width=32)
title_tag.grid(row=0, column=0)

# Left panel
left_panel = Frame(app, bd=1, relief=FLAT, width=10)
left_panel.pack(side=LEFT)

# Costs panel
cost_panel = Frame(left_panel, bd=1, relief=FLAT, bg='azure4', padx=128)
cost_panel.pack(side=BOTTOM)

# Food panel
food_panel = LabelFrame(left_panel, text='Food', font=('Dosis', 19, 'bold'),
                        bd=1, relief=FLAT, fg='azure4')
food_panel.pack(side=LEFT)

# Drink panel
drink_panel = LabelFrame(left_panel, text='Drink', font=('Dosis', 19, 'bold'),
                         bd=1, relief=FLAT, fg='azure4')
drink_panel.pack(side=LEFT)

# Dessert panel
dessert_panel = LabelFrame(left_panel, text='Dessert', font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
dessert_panel.pack(side=LEFT)

# Right panel
right_panel = Frame(app, bd=1, relief=FLAT)
right_panel.pack(side=RIGHT)

# Calculator panel
calculator_panel = Frame(right_panel, bd=1, relief=FLAT, bg='burlywood3')
calculator_panel.pack()

# Bill panel
bill_panel = Frame(right_panel, bd=1, relief=FLAT, bg='burlywood3')
bill_panel.pack()

# Button panel
button_panel = Frame(right_panel, bd=1, relief=FLAT, bg='burlywood3')
button_panel.pack()

# Products list
food_list = ['chicken', 'beef', 'salmon', 'kebab', 'hake', 'pizza', 'burger', 'french fries']
drink_list = ['water', 'soda', 'juice', 'coke', 'white wine', 'red wine', 'national beer', 'international beer']
dessert_list = ['ice-cream', 'fruit', 'brownies', 'flan', 'mousse', 'cake', 'cheesecake', 'chocolate']

# Generate items food
food_var = []
square_food = []
text_food = []
count = 0
for food in food_list:
    # Create check buttons
    food_var.append('')
    food_var[count] = IntVar()
    food = Checkbutton(food_panel,
                       text=food.title(),
                       font=('Dosis', 18, 'bold'),
                       onvalue=1,
                       offvalue=0,
                       variable=food_var[count],
                       command=check)
    food.grid(row=count, column=0, sticky=W)

    # Create input square
    square_food.append('')
    text_food.append('')
    text_food[count] = StringVar()
    text_food[count].set('0')
    square_food[count] = Entry(food_panel,
                               font=('Dosis', 18, 'bold'),
                               bd=1,
                               width=6,
                               state=DISABLED,
                               textvariable=text_food[count])
    square_food[count].grid(row=count,
                            column=1)
    count += 1

# Generate items drink
drink_var = []
square_drink = []
text_drink = []
count = 0
for drink in drink_list:
    # Create check buttons
    drink_var.append('')
    drink_var[count] = IntVar()
    drink = Checkbutton(drink_panel,
                        text=drink.title(),
                        font=('Dosis', 18, 'bold'),
                        onvalue=1,
                        offvalue=0,
                        variable=drink_var[count],
                        command=check)
    drink.grid(row=count,
               column=0,
               sticky=W)

    # Create input square
    square_drink.append('')
    text_drink.append('')
    text_drink[count] = StringVar()
    text_drink[count].set('0')
    square_drink[count] = Entry(drink_panel,
                                font=('Dosis', 18, 'bold'),
                                bd=1,
                                width=6,
                                state=DISABLED,
                                textvariable=text_drink[count])
    square_drink[count].grid(row=count,
                             column=1)
    count += 1

# Generate items dessert
dessert_var = []
square_dessert = []
text_dessert = []
count = 0
for dessert in dessert_list:
    # Create check buttons
    dessert_var.append('')
    dessert_var[count] = IntVar()
    dessert = Checkbutton(dessert_panel,
                          text=dessert.title(),
                          font=('Dosis', 18, 'bold'),
                          onvalue=1,
                          offvalue=0,
                          variable=dessert_var[count],
                          command=check)
    dessert.grid(row=count,
                 column=0,
                 sticky=W)

    # Create input square
    square_dessert.append('')
    text_dessert.append('')
    text_dessert[count] = StringVar()
    text_dessert[count].set('0')
    square_dessert[count] = Entry(dessert_panel,
                                  font=('Dosis', 18, 'bold'),
                                  bd=1,
                                  width=6,
                                  state=DISABLED,
                                  textvariable=text_dessert[count])
    square_dessert[count].grid(row=count,
                               column=1)
    count += 1

# cost tags and inputs
var_cost_food = StringVar()
var_cost_drink = StringVar()
var_cost_dessert = StringVar()
var_subtotal = StringVar()
var_taxes = StringVar()
var_total = StringVar()

cost_tag_food = Label(cost_panel, text='Food Cost',
                      font=('Dosis', 12, 'bold'),
                      bg='azure4',
                      fg='white')
cost_tag_food.grid(row=0, column=0)
text_cost_food = Entry(cost_panel,
                       font=('Dosis', 12, 'bold'),
                       bd=1,
                       width=10,
                       state='readonly',
                       textvariable=var_cost_food)
text_cost_food.grid(row=0, column=1, padx=41)

# Drink
cost_tag_drink = Label(cost_panel,
                       text='Drink Cost',
                       font=('Dosis', 12, 'bold'),
                       bg='azure4',
                       fg='white')
cost_tag_drink.grid(row=1, column=0)
text_cost_drink = Entry(cost_panel,
                        font=('Dosis', 12, 'bold'),
                        bd=1,
                        width=10,
                        state='readonly',
                        textvariable=var_cost_drink)
text_cost_drink.grid(row=1, column=1, padx=41)

# Dessert
cost_tag_dessert = Label(cost_panel,
                         text='Dessert Cost',
                         font=('Dosis', 12, 'bold'),
                         bg='azure4',
                         fg='white')
cost_tag_dessert.grid(row=2, column=0)
text_cost_dessert = Entry(cost_panel,
                          font=('Dosis', 12, 'bold'),
                          bd=1,
                          width=10,
                          state='readonly',
                          textvariable=var_cost_dessert)
text_cost_dessert.grid(row=2, column=1, padx=41)

# Subtotal
tag_subtotal = Label(cost_panel,
                     text='Subtotal',
                     font=('Dosis', 12, 'bold'),
                     bg='azure4',
                     fg='white')
tag_subtotal.grid(row=0, column=2)
text_subtotal = Entry(cost_panel,
                      font=('Dosis', 12, 'bold'),
                      bd=1,
                      width=10,
                      state='readonly',
                      textvariable=var_subtotal)
text_subtotal.grid(row=0, column=3, padx=41)

# Taxes
tag_taxes = Label(cost_panel,
                  text='Taxes',
                  font=('Dosis', 12, 'bold'),
                  bg='azure4',
                  fg='white')
tag_taxes.grid(row=1, column=2)
text_taxes = Entry(cost_panel,
                   font=('Dosis', 12, 'bold'),
                   bd=1,
                   width=10,
                   state='readonly',
                   textvariable=var_taxes)
text_taxes.grid(row=0, column=3, padx=41)

# Total
tag_total = Label(cost_panel,
                  text='Total',
                  font=('Dosis', 12, 'bold'),
                  bg='azure4',
                  fg='white')
tag_total.grid(row=2, column=2)
text_total = Entry(cost_panel,
                   font=('Dosis', 12, 'bold'),
                   bd=1,
                   width=10,
                   state='readonly',
                   textvariable=var_total)
text_total.grid(row=0, column=3, padx=41)

# Buttons
buttons = ['Total', 'Bill', 'Save', 'Reset']
c_b = []

columns = 0
for button in buttons:
    button = Button(button_panel,
                    text=button.title(),
                    font=('Dosis', 14, 'bold'),
                    fg='white',
                    bg='azure4',
                    bd=1,
                    width=9)
    c_b.append(button)
    button.grid(row=0, column=columns)
    columns += 1

c_b[0].config(command=total)
c_b[1].config(command=bill)
c_b[2].config(command=save)
c_b[3].config(command=reset)

# Bill area
text_bill = Text(bill_panel,
                 font=('Dosis', 12, 'bold'),
                 bd=1,
                 width=42,
                 height=10,
                 state=DISABLED)
text_bill.grid(row=0, column=0)

# Calculator
calculator_screen = Entry(calculator_panel,
                          font=('Dosis', 16, 'bold'),
                          width=32,
                          bd=1)
calculator_screen.grid(row=0,
                       column=0,
                       columnspan=4)
calc_b = ['7', '8', '9', '+', '4', '5', '6', '-',
          '1', '2', '3', 'x', 'R', 'C', '0', '/']
b_save = []
row = 1
column = 0
for button in calc_b:
    button = Button(calculator_panel,
                    text=button.title(),
                    font=('Dosis', 16, 'bold'),
                    fg='white',
                    bg='azure4',
                    bd=1,
                    width=8)
    b_save.append(button)
    button.grid(row=row, column=column)
    if column == 3:
        row += 1
    column += 1
    if column == 4:
        column = 0

b_save[0].config(command=lambda: touch_button('7'))
b_save[1].config(command=lambda: touch_button('8'))
b_save[2].config(command=lambda: touch_button('9'))
b_save[3].config(command=lambda: touch_button('+'))
b_save[4].config(command=lambda: touch_button('4'))
b_save[5].config(command=lambda: touch_button('5'))
b_save[6].config(command=lambda: touch_button('6'))
b_save[7].config(command=lambda: touch_button('-'))
b_save[8].config(command=lambda: touch_button('1'))
b_save[9].config(command=lambda: touch_button('2'))
b_save[10].config(command=lambda: touch_button('3'))
b_save[11].config(command=lambda: touch_button('*'))
b_save[14].config(command=lambda: touch_button('0'))
b_save[15].config(command=lambda: touch_button('/'))
b_save[13].config(command=clear)
b_save[12].config(command=calc)

# Don't close the window
app.mainloop()
