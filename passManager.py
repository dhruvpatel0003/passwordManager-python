import random
import string
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import pyperclip
import json
# from tkinter import password

FONT = ("Arial",10,'bold')
space = ''
new_password = None
data_dict = None

def generate():
        sym = "@#$&*!"
        global space,new_password,data_dict
        word = string.ascii_letters + string.digits + sym
        space = ''
        for i in range(9):
            space += random.choice(word)
        password1.insert(END,f"{space}")
        new_password = space
        pyperclip.copy(new_password)

def save_data():
        new_name = name.get()
        new_email = email.get()
        new_pass = new_password
        data_dict = {
            new_name:  {

            "email": new_email,
            "password": new_password
        }
        }
        try:

            with open("saveData.json", 'r') as file:
                data = json.load(file)
                data.update(data_dict)
            with open('saveData.json', 'w') as file:
                json.dump(data, file, indent=3)

        except:

            with open('saveData.json', 'w') as file:
                json.dump(data_dict,file,indent=3)
            print("Successfully saved")

        email.delete(0,END)
        password1.delete(0,END)
        name.delete(0,END)
        email.focus()
        return

def final():

    if password1.get() == '' or email.get() == '' or name.get() == '':
        messagebox.showinfo('Empty Field','Please enter the all details')
        return
    yes_no = messagebox.askyesno('Information',f"would you like to save this details :\n Email : {email.get()} \n Password : {new_password} ")
    if yes_no:
        save_data()
    else:
        yesno = messagebox.askyesno('','generate password again?')
        if yesno:
            generate()
        else:
            window.destroy()

def search():
    try:
        with open('saveData.json', 'r') as file:
            data = json.load(file)
            emial_data = data[f'{name.get()}']['email']
            pass_data = data[f'{name.get()}']['password']
            messagebox.showinfo('Information',f"emial : {emial_data} \npassword : {pass_data}")
    except KeyError as K:
        messagebox.showerror('Not Found',f'Data does not contain {K}')
        name.delete(1,END)


window = Tk()
window.title('Save email and passwords')
window.resizable(False,False)

lable = Label(text="Keep Safe",font=('Arial',20,'bold'))
lable.grid(row=1,column=1,pady=20,padx=50)

lable_e = Label(text='Email',font=FONT)
lable_e.grid(row=1,column=0)
lable_p = Label(text='Password',font=FONT)
lable_p.grid(row=2,column=0)
lable_n = Label(text='Website',font=FONT)
lable_n.grid(row=0,column=0)

name = Entry(width=40,bd=6)
name.insert(END,'')
name.grid(row=0,column=1,columnspan=2)

email = Entry(width=40,bd=6)
email.insert(END,'')
email.focus()
email.grid(row=1,column=1,columnspan=2)

password1 = Entry(width=40,bd=6)
password1.insert(END,'')
password1.grid(row=2,column=1,columnspan=2)

generate_button = Button(text='Generate',font=FONT,bg='blue',fg='white',activeforeground='blue',activebackground='white',command=generate)
generate_button.grid(row=2,column=2)

search_button = Button(text='search',font=FONT,bg='blue',fg='white',activeforeground='blue',activebackground='white',command=search)
search_button.grid(row=0,column=2)

add_button = Button(text="Add",font=FONT,bg='blue',fg='white',activeforeground='blue',activebackground='white',command=final)
add_button.grid(row=3,column=1,pady=10)

window.mainloop()