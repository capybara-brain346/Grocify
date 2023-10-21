from tkinter import *
from tkinter import messagebox
from csv import DictWriter
from PIL import Image
import pandas as pd

class FruitApp:

    def SignIn(self):
        self.root.destroy()
        self.root = Tk()
        self.root.title('The Fruit App')
        self.root.iconbitmap("fruit.ico")
        self.root.geometry('500x700+500+100')
        self.root.config(bg='#aedcd2')

        user_label = Label(self.root, text='Enter Username ->', font=('Product Sans', 18))
        user_label.pack(pady=50)

        signin_entry_username = Entry(self.root, width=25, font=('Product Sans', 16))
        signin_entry_username.pack(pady=10)

        pass_label = Label(self.root, text='Enter Password ->', font=('Product Sans', 18))
        pass_label.pack(pady=50)

        signin_entry_password = Entry(self.root, width=25, font=('Product Sans', 16))
        signin_entry_password.pack(pady=10)
        signin_entry_username.get()
        signin_entry_password.get()

        def logmatch():
            userData = pd.read_csv('users2.csv')
            df = pd.DataFrame(userData)
            log_match = (len(df[(df.username == signin_entry_username.get()) &
                                (df.password == signin_entry_password.get())]) > 0)
            if log_match:
                FruitApp.database(self)
            else:
                messagebox.showinfo('Grocify','Username Or Password Is Wrong!\nPlease Try Again')

        signin_button = Button(self.root, text='Sign In', font=('Product Sans', 18), width=10,command=logmatch)
        signin_button.pack(pady=40)

        back_welcomescreen = Button(self.root,text='Back',font=('Product Sans',18),width=10,command=FruitApp)
        back_welcomescreen.pack(pady=10)



    def pay(self):

        self.root = Tk()
        self.root.title('Grocify')
        self.root.iconbitmap("fruit.ico")
        self.root.geometry('500x700+500+100')
        self.root.config(bg='#aedcd2')
        option_label = Label(self.root,text='Please Choose Payment Option:',font=('Product Sans',18),bg='#d7ede8')
        option_label.pack(pady=30)
        def qr():
            img = Image.open("paisa bhej.png")
            img.show()



        pay_qr = Button(self.root,text='QR Code',font=('Product Sans',16),bg='#d7ede8',command=qr)
        pay_qr.pack(pady=10)

        def upi():
            upi_label = Label(self.root,text='UPI ID -> 9168088565@ybl',font=('Product Sans',16),bg='#d7ede8')
            upi_label.pack()

        pay_upi = Button(self.root,text='UPI',font=('Product Sans',16),bg='#d7ede8',command=upi)
        pay_upi.pack(pady=10)


        self.root.mainloop()



    def database(self):
        self.root.destroy()
        self.root = Tk()
        self.root.title('Grocify')
        self.root.iconbitmap("fruit.ico")
        self.root.geometry('500x700+500+100')
        self.root.config(bg='#aedcd2')

        fruitdf = pd.DataFrame(pd.read_csv('fruit.csv'))

        for i in range(len(fruitdf)):
            Fruit_Label_Data = fruitdf.iloc[i]
            Fruit_Label_ID = Label(self.root, text=Fruit_Label_Data['ID'], font=('Product Sans', 16), bg='#d7ede8')
            Fruit_Label_Name = Label(self.root, text=Fruit_Label_Data['Fruit'], font=('Product Sans', 16), bg='#d7ede8')
            Fruit_Label_Price = Label(self.root, text=f"₹{Fruit_Label_Data['Price(₹)']}", font=('Product Sans', 16),
                                      bg='#d7ede8')

            Fruit_Label_ID.grid(row=i, column=0)
            Fruit_Label_Name.grid(row=i, column=1)
            Fruit_Label_Price.grid(row=i, column=2)

        quantity_indicator = Label(self.root,text='X KGs',font=('Product Sans',18),bg='#d7ede8')
        quantity_indicator.grid(row=0,column=4)

        Quantity_Selection1 = Spinbox(self.root, from_=0, to=50, font=('Product Sans', 16), width=5,increment=0.5)
        Quantity_Selection1.grid(row=0, column=3)
        Quantity_Selection2 = Spinbox(self.root, from_=0, to=50, font=('Product Sans', 16), width=5,increment=0.5)
        Quantity_Selection2.grid(row=1, column=3)
        Quantity_Selection3 = Spinbox(self.root, from_=0, to=50, font=('Product Sans', 16), width=5,increment=0.5)
        Quantity_Selection3.grid(row=2, column=3)
        Quantity_Selection4 = Spinbox(self.root, from_=0, to=50, font=('Product Sans', 16), width=5,increment=0.5)
        Quantity_Selection4.grid(row=3, column=3)
        Quantity_Selection5 = Spinbox(self.root, from_=0, to=50, font=('Product Sans', 16), width=5,increment=0.5)
        Quantity_Selection5.grid(row=4, column=3)
        Quantity_Selection6 = Spinbox(self.root, from_=0, to=50, font=('Product Sans', 16), width=5,increment=0.5)
        Quantity_Selection6.grid(row=5, column=3)
        Quantity_Selection7 = Spinbox(self.root, from_=0, to=50, font=('Product Sans', 16), width=5,increment=0.5)
        Quantity_Selection7.grid(row=6, column=3)
        Quantity_Selection8 = Spinbox(self.root, from_=0, to=50, font=('Product Sans', 16), width=5,increment=0.5)
        Quantity_Selection8.grid(row=7, column=3)
        Quantity_Selection9 = Spinbox(self.root, from_=0, to=50, font=('Product Sans', 16), width=5,increment=0.5)
        Quantity_Selection9.grid(row=8, column=3)
        Quantity_Selection10 = Spinbox(self.root, from_=0, to=50, font=('Product Sans', 16), width=5,increment=0.5)
        Quantity_Selection10.grid(row=9, column=3)
        Quantity_Selection11 = Spinbox(self.root, from_=0, to=50, font=('Product Sans', 16), width=5,increment=0.5)
        Quantity_Selection11.grid(row=10, column=3)
        Quantity_Selection12 = Spinbox(self.root, from_=0, to=50, font=('Product Sans', 16), width=5,increment=0.5)
        Quantity_Selection12.grid(row=11, column=3)
        Quantity_Selection13 = Spinbox(self.root, from_=0, to=50, font=('Product Sans', 16), width=5,increment=0.5)
        Quantity_Selection13.grid(row=12, column=3)
        Quantity_Selection14 = Spinbox(self.root, from_=0, to=50, font=('Product Sans', 16), width=5,increment=0.5)
        Quantity_Selection14.grid(row=13, column=3)
        Quantity_Selection15 = Spinbox(self.root, from_=0, to=50, font=('Product Sans', 16), width=5,increment=0.5)
        Quantity_Selection15.grid(row=14, column=3)
        Quantity_Selection16 = Spinbox(self.root, from_=0, to=50, font=('Product Sans', 16), width=5,increment=0.5)
        Quantity_Selection16.grid(row=15, column=3)
        Quantity_Selection17 = Spinbox(self.root, from_=0, to=50, font=('Product Sans', 16), width=5,increment=0.5)
        Quantity_Selection17.grid(row=16, column=3)
        Quantity_Selection18 = Spinbox(self.root, from_=0, to=50, font=('Product Sans', 16), width=5,increment=0.5)
        Quantity_Selection18.grid(row=17, column=3)
        Quantity_Selection19 = Spinbox(self.root, from_=0, to=50, font=('Product Sans', 16), width=5,increment=0.5)
        Quantity_Selection19.grid(row=18, column=3)
        Quantity_Selection20 = Spinbox(self.root, from_=0, to=50, font=('Product Sans', 16), width=5,increment=0.5)
        Quantity_Selection20.grid(row=19, column=3)

        def quantity():

            qt_lst = list(map(float, [Quantity_Selection1.get(), Quantity_Selection2.get(), Quantity_Selection3.get(),
                                      Quantity_Selection4.get(), Quantity_Selection5.get(),Quantity_Selection6.get(),
                                      Quantity_Selection7.get(), Quantity_Selection8.get(),Quantity_Selection9.get(),
                                      Quantity_Selection10.get(),Quantity_Selection11.get(), Quantity_Selection12.get(),
                                      Quantity_Selection13.get(),Quantity_Selection14.get(), Quantity_Selection15.get(),
                                      Quantity_Selection16.get(), Quantity_Selection17.get(), Quantity_Selection18.get()
                                      , Quantity_Selection19.get(), Quantity_Selection20.get()]))

            print(qt_lst)
            print('\n')

            def cart_screen():
                global f_l
                self.root.destroy()
                root = Tk()
                root.title('Grocify')
                root.iconbitmap("fruit.ico")
                root.geometry('500x700+500+100')
                root.config(bg='#aedcd2')

                mycart = pd.DataFrame()
                for i_f in Flat_R_lst:
                    ID_sort = fruitdf.loc[[i_f], ['ID', 'Fruit', 'Price(₹)']]
                    mycart = pd.concat([mycart, ID_sort])

                mycart = mycart.sort_values(by='ID')

                non_zero = [s for s in qt_lst if s != 0]

                for d in range(len(mycart)):
                    mycart.iloc[d, 2] *= non_zero[d]

                mycart['Quantity'] = non_zero

                cart_label = Label(root, text='Fruits:', font=('Product Sans', 18), bg='#d7ede8')
                cart_label.grid(row=0, column=0)
                cart_price_label = Label(root, text='Price:', font=('Product Sans', 18), bg='#d7ede8')
                cart_price_label.grid(row=0, column=1)
                cart_quantity_label = Label(root, text='Quantity', font=('Product Sans', 18), bg='#d7ede8')
                cart_quantity_label.grid(row=0, column=2)

                for f_l in range(len(mycart)):
                    mycart_fruit_data = mycart.iloc[f_l]
                    mycart_fruit_label = Label(root, text=mycart_fruit_data.loc['Fruit'], font=('Product Sans', 16),bg='#d7ede8')
                    mycart_fruit_label.grid(row=f_l + 1, column=0)
                    mycart_price_label = Label(root, text=f"₹{mycart_fruit_data.loc['Price(₹)']}", font=('Product Sans', 16),bg='#d7ede8')
                    mycart_price_label.grid(row=f_l + 1, column=1)
                    mycart_quantity_label = Label(root, text=mycart_fruit_data.loc['Quantity'],font=('Product Sans', 16), bg='#d7ede8')
                    mycart_quantity_label.grid(row=f_l + 1, column=2)

                price_sum = mycart['Price(₹)'].sum(axis=0)
                total_price_label = Label(root,text=f"Total Price: ₹{price_sum}",font=('Product Sans',18),bg='#d7ede8')
                total_price_label.grid(row=f_l+2,column=2)
                a = Label(root, text=' ', font=('Product Sans', 20), bg='#aedcd2')
                a.grid(row=f_l+3,column=2)
                pay_button = Button(root,text='Place Order',font=('Product Sans',16),bg='#d7ede8',command=self.pay)
                pay_button.grid(row=f_l+4,column=2)


                root.mainloop()

            R = {n: rep[n] for rep in [{}] for i, n in enumerate(qt_lst)if rep.setdefault(n, []).append(i) or len(rep[n]) == 1}
            del R[0]
            print(R)

            Flat_R_lst = [val for f in R.values() for val in f]

            print(Flat_R_lst)

            cart_screen()

        blank = Label(self.root, text='', pady=5, bg='#aedcd2')
        blank.grid(row=20, column=2)
        continue_button = Button(self.root, text='Continue', font=('Product Sans', 18), command=quantity)
        continue_button.grid(row=21, column=2)

        self.root.mainloop()



    def signup(self):
        self.root.destroy()
        self.root = Tk()
        self.root.title('Grossify')
        self.root.iconbitmap("fruit.ico")
        self.root.geometry('500x700+500+100')
        self.root.config(bg='#aedcd2')

        firstname_label = Label(self.root,text='Enter Your First Name:',font=('Product Sans', 16), bg='#d7ede8')
        firstname_label.pack(pady=15)
        firstname_data = Entry(self.root,width=25)
        firstname_data.pack(pady=15)

        lastname_label = Label(self.root,text='Enter Your Last NAme:',font=('Product Sans', 16), bg='#d7ede8')
        lastname_label.pack(pady=15)
        lastname_data = Entry(self.root, width=25)
        lastname_data.pack(pady=15)

        age_label = Label(self.root,text='PLease Enter Your Age:',font=('Product Sans', 16), bg='#d7ede8')
        age_label.pack(pady=15)
        age_data = Entry(self.root,width=25)
        age_data.pack(pady=15)

        options = ['M','F']
        menu = StringVar()
        menu.set('Please Select Your Gender:')

        gender_data = OptionMenu(self.root,menu,*options)
        gender_data.pack(pady=15)

        username_label = Label(self.root,text= 'Please Enter Your Username:',font=('Product Sans', 16), bg='#d7ede8')
        username_label.pack(pady=15)
        username_data = Entry(self.root,width=25)
        username_data.pack(pady=15)

        password_label = Label(self.root,text='Please Enter Your Password:',font=('Product Sans', 16), bg='#d7ede8')
        password_label.pack(pady=15)
        password_data = Entry(self.root, width=25)
        password_data.pack(pady=15)


        def register():
            userData = pd.read_csv('users2.csv')
            log_match = (len(userData[(userData.username == username_data.get())]) > 0)
            null_check = (firstname_data.get() == 0 or lastname_data.get() == 0 or age_data.get() == 0 or
                          username_data.get() == 0 or password_data.get() == 0)
            if log_match:
                messagebox.showinfo('Grocify','Username Already Exists!')
                self.signup()
            elif null_check:
                messagebox.showinfo('Grocify','Please Do Not Leave Any Field Empty!')
                self.signup()
            else:
                reg_dict = {'firstname': firstname_data.get(), 'lastname': lastname_data.get(), 'username':
                 username_data.get(), 'password': password_data.get(), 'age': age_data.get(), 'sex': menu.get()}
                with open('users2.csv', 'a') as newlog_data:
                    dictw_newlog_data = DictWriter(newlog_data, fieldnames=reg_dict.keys())
                    dictw_newlog_data.writerow(reg_dict)
                newlog_data.close()
                self.database()

        register_button = Button(self.root,text='Register',font=('Product Sans',18),width = 10,command=register)
        register_button.pack(pady=20)
        back_button = Button(self.root,text='Back',font=('Product Sans',18),width = 10,command=self.welcome_screen)
        back_button.pack(pady=20)

        self.root.mainloop()



    def welcome_screen(self):
        self.root = Tk()
        self.root.title('Grossify')
        self.root.iconbitmap("fruit.ico")
        self.root.geometry('500x600+500+100')

        background = PhotoImage(file='background_image.png')
        background_img_label = Label(self.root, image=background)
        background_img_label.place(x=0, y=0)

        welcome_text_label = Label(self.root, text='Welcome To The Fruit App :)', fg='black', bg='white')
        welcome_text_label.pack(pady=100)
        welcome_text_label.config(font=('Product Sans', 20))

        signin_button = Button(self.root, text='Sign In', fg='black', bg='white', command=self.SignIn)
        signin_button.pack()
        signin_button.config(font=('Product Sans', 18))

        signup_button = Button(self.root, text='Register', fg='black', bg='white',command=self.signup)
        signup_button.pack(pady=20)
        signup_button.config(font=('Product Sans', 18))

        self.root.mainloop()



f = FruitApp()
if __name__ == '__main__':
    f.welcome_screen()
