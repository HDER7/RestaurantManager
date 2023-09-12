from tkinter import *

# Set screen size,title and background color
app = Tk()
app.geometry('1020x630+0+0')
app.resizable(False, False)
app.title('Restaurant Manager')
app.config(bg='burlywood3')

# Top Panel
top_panel = Frame(app, bd=1, relief=FLAT)
top_panel.pack(side=TOP)

# Label title
title_tag = Label(top_panel, text='Facturation system', fg='azure4',
                  font=('Dosis', 58), bg='burlywood3', width=28)
title_tag.grid(row=0, column=0)

# Left panel
left_panel = Frame(app, bd=1, relief=FLAT)
left_panel.pack(side=LEFT)

# Costs panel
cost_panel = Frame(left_panel, bd=1, relief=FLAT, bg='azure4', padx=189)
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
                       font=('Dosis', 19, 'bold'),
                       onvalue=1,
                       offvalue=0,
                       variable=food_var[count])
    food.grid(row=count, column=0, sticky=W)

    # Create input square
    square_food.append('')
    text_food.append('')
    text_food[count] = StringVar()
    text_food[count].set('0')
    square_food[count] = Entry(food_panel,
                               font=('Dosis', 19, 'bold'),
                               bd=1,
                               width=8,
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
                        font=('Dosis', 19, 'bold'),
                        onvalue=1,
                        offvalue=0,
                        variable=drink_var[count])
    drink.grid(row=count,
               column=0,
               sticky=W)

    # Create input square
    square_drink.append('')
    text_drink.append('')
    text_drink[count] = StringVar()
    text_drink[count].set('0')
    square_drink[count] = Entry(drink_panel,
                                font=('Dosis', 19, 'bold'),
                                bd=1,
                                width=8,
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
                          font=('Dosis', 19, 'bold'),
                          onvalue=1,
                          offvalue=0,
                          variable=dessert_var[count])
    dessert.grid(row=count,
                 column=0,
                 sticky=W)

    # Create input square
    square_dessert.append('')
    text_dessert.append('')
    text_dessert[count] = StringVar()
    text_dessert[count].set('0')
    square_dessert[count] = Entry(dessert_panel,
                                  font=('Dosis', 19, 'bold'),
                                  bd=1,
                                  width=8,
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

app.mainloop()
