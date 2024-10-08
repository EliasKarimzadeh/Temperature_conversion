""" %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    | $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ |
    | $  /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\  $ |
    | $ / @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ \ $ |
    | $ \ @                                                                  @ / $ |
    | $ / @                      ELIAS KARIMZADEH                            @ \ $ |
    | $ \ @                                                                  @ / $ |
    | $ / @              GitHub: github.com/EliasKarimzadeh                  @ \ $ |
    | $ \ @             Linkdin: in/elias-karimzadeh-a7a9b8283               @ / $ |
    | $ / @            Instagram : instagram.com/elyaskarymzade              @ \ $ |
    | $ \ @                                                                  @ / $ |
    | $ / @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ \ $ |        
    | $ \/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/ $ |
    | $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ |
    |%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%|"""
    
import tkinter as tk
elyas = tk.Tk()
from tkinter import ttk
elyas.title('Elias')

result_var = tk.StringVar()



lbl_name_app = tk.Label(  #lbl
    master=elyas,
    text='Convert temperature from Fahrenheit to Celsius'
)

lbl_name_app.grid(
    row=0,
    column=1,
    pady=(10 , 4)
)

lbl_f = ttk.Label(
    master=elyas,
    text='Fahrenheit : ',
)

lbl_c = ttk.Label(
    master=elyas,
    text='Celsius : ',
)

lbl_f.grid(row=1 , column=0 , padx=10 , pady=10)
lbl_c.grid(row=2 , column=0, padx=10 , pady=(0 , 10))


ent_f= ttk.Entry( #ent
    elyas,
    width = 50,
    textvariable=result_var
    
)

lbl_exit = ttk.Label(
    elyas,
    text='Enter Fahrenheit temperature'
) 

ent_f.grid(row=1 , column=1)

def chang(*args):
    try:
        # c = 1.8 f + 32
        celc = (float(result_var.get()) -32) / 1.8
        lbl_exit['text'] = celc
    except ValueError:
        if result_var.get() != '':
            lbl_exit['text'] = 'Enter Valid Number!'
        else: 
            lbl_exit['text'] = 'Enter Fahrenheit temperature'

        

btn_cheng = ttk.Button( #btn
    elyas,
    text='Change!',
    command = chang
)

btn_cheng.grid(row=1 , column=2, padx=20 , pady=10)



lbl_exit.grid(row=2 , column=1, padx=10 , pady=(0 , 10))

elyas.bind('<Return>' ,  chang)

elyas.mainloop()