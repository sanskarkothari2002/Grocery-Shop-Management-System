from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import PIL.Image, PIL.ImageTk
import mysql.connector
import pushbullet

# new
import smtplib as smt

# Database Design
mydb = mysql.connector.connect(host="localhost", user="root", passwd="root123",database="grocerystore")
my_cursor = mydb.cursor()
LstOfItems = []
my_cursor.execute("SELECT * FROM groceryproducts")
rows =my_cursor.fetchall()
for item in rows:
    LstOfItems.append(item)

toordal=ChanaDal=MoongDal=MasoorDal=UradDal=BasmatiRice=GroundnutOil=SoyabeanOil=MustardOil=500

root = Tk()

class Login:
    def __init__(self,root):
        self.root = root
        self.root.geometry("885x700")  # 885x700
        self.root.resizable(False,False)
        self.bg = PIL.ImageTk.PhotoImage(file=r"D:\Users\jains\Documents\SDP_content\grocerystore.jpg")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        Frame_Login=Frame(self.root,bg="white")
        Frame_Login.place(x=230,y=280,height=300,width=435)

        title=Label(Frame_Login,text="Login Here ",font=("italian",20,"bold"),fg= "#d77337",bg="white").place(x=15,y=30)
        lbl_user=Label(Frame_Login,text="Username",font=("Goudy old style",17,"bold"),fg="gray",bg="white").place(x=35,y=80)
        self.txt_user=Entry(Frame_Login,font=("times new roman",18),bg="lightgray")
        self.txt_user.place(x=60,y=120,width=280,height=35)

        lbl_pass = Label(Frame_Login, text="Password", font=("Goudy old style", 17, "bold"), fg="gray",bg="white").place(x=35, y=165)
        self.txt_pass = Entry(Frame_Login,show="*",font=("times new roman",18),bg="lightgray")
        self.txt_pass.place(x=60, y=205, width=280, height=35)
        login_btn=Button(Frame_Login,command=self.login,text="Login",fg="white",bg="#d77337",font=("times new roman",12)).place(x=160,y=260,width=110)

    global customerName,customerContact,customerEmail,clicked,quantity,resetname
    customerName = StringVar()
    customerContact = StringVar()
    customerEmail = StringVar()
    clicked = StringVar()
    quantity = IntVar()

    def pending(self):
        frame = Frame(root, bg="white")
        frame.place(width=885, height=700)
        ####################### Heading Section #########################
        title = Label(root, text="Retail Shop Management System", bd=11, font=("times new roman", 24, "bold"), fg="white",bg="#4D0039", relief=GROOVE)
        title.pack(fill=X)

        ##################### Customer Details #######################
        Frame_CustomerDetail = Frame(root, bd=4, relief=RIDGE, bg="#4D0039")
        Frame_CustomerDetail.place(x=3, y=63, width=360, height=634)
        Title_detail = Label(Frame_CustomerDetail, text="Customer Detail", font=("times new roman", 22, "bold"),bg="#4D0039",fg="white")
        Title_detail.place(x=60, y=6)



        global txt_name
        lbl_name = Label(Frame_CustomerDetail, text="   Name", font=("times new roman", 16, "bold"), bg="#4D0039",fg="white")
        lbl_name.place(x=-5, y=80)

        txt_name = Entry(Frame_CustomerDetail, font=("times new roman", 16),relief=SUNKEN,textvariable=customerName)
        txt_name.place(x=152, y=80, width=180, height=35)

# -----------------------------------------------------------------------------------------------------------------
        global txt_email
        lbl_mailId = Label(Frame_CustomerDetail, text="   Email Id ", font=("times new roman", 16, "bold"), bg="#4D0039",fg="white")
        lbl_mailId.place(x=-5, y=141)

        txt_email = Entry(Frame_CustomerDetail, font=("times new roman", 16),relief=SUNKEN,textvariable=customerEmail)
        txt_email.place(x=152, y=140, width=180, height=35)
# ---------------------------------------------------------------------------------------------------------------------------------------


        global txt_contact
        lbl_contact = Label(Frame_CustomerDetail, text="   Contact no. ", font=("times new roman", 16, "bold"), bg="#4D0039",fg="white")
        lbl_contact.place(x=-5, y=201)

        txt_contact = Entry(Frame_CustomerDetail, font=("times new roman", 16),relief=SUNKEN,textvariable=customerContact)
        txt_contact.place(x=152, y=200, width=180, height=35)
# ------------------------------------------------------------------------------------------------------------------------------------------

        add_ncustomrers= Button(Frame_CustomerDetail,text="Add Detail",font=("arial", 16, "bold"),bg="lightgray",command=self.customerDetail)
        add_ncustomrers.place(x=90,y=275,width=180)
# --------------------------------------------------------------------------------------------------------------------------------------------
        global file1
        file1 = open("customerdetail.txt", "a")
        file1.write("\n\t   Name\t\t\tEmail\t\tPhoneno")

    ####################### offer ###########################
        # welcomeImg = Frame(Frame_CustomerDetail)
        # welcomeImg.place(x=10,y=335,width=330,height=280)
        # lbl_avail_offer1 = Label(welcomeImg,text="OFFERS",font=("arial",16,"bold"))
        # lbl_avail_offer1.place(x=120,y=5)


        ###################### Product Details ##############################
        Frame_ProductSelection = Frame(root, bd=4, relief=RIDGE, bg="#4D0039")
        Frame_ProductSelection.place(x=366, y=63, width=516, height=130)

        Title_product = Label(Frame_ProductSelection, text="Products ", font=("tmes new roman", 16,"bold"), bg="#4D0039",fg="white")
        Title_product.place(y=15)
        dropbox = OptionMenu(Frame_ProductSelection, clicked, *LstOfItems)
        dropbox.place(x=100, y=15, width=210, height=35)

        lbl_Quantity = Label(Frame_ProductSelection, text="Quantity  ", font=("times new roman", 16,"bold"), bg="#4D0039",fg="white")
        lbl_Quantity.place(x=320, y=15)
        txt_Quantity = Entry(Frame_ProductSelection,font=("times new roman", 14), bg="lightgray",relief=SUNKEN,textvariable=quantity)
        txt_Quantity.place(x=420, y=15, width=70, height=30)

        # creating a button to add item to cart for management of bill
        Addbtn = Button(Frame_ProductSelection, text="Add item", font=("arial",16,"bold"),bg="lightgray",command=self.additem)
        Addbtn.place(x=45, y=75, width=99, height=35)

        Resetbtn = Button(Frame_ProductSelection, text="Reset", font=("arial",16,"bold"),bg="lightgray",command=self.reset)
        Resetbtn.place(x=175, y=75, width=83, height=35)

        BillGeneratebtn = Button(Frame_ProductSelection,text="Generate Bill",font=("arial",16,"bold"), bg="lightgray",command=self.billgenrate)
        BillGeneratebtn.place(x=295, y=75, width=143, height=35)

        ####################### Billing Section #########################
        billframe = Frame(root,relief=GROOVE,bd=6)
        billframe.place(x=366, y=195, width=516, height=505)
        billlabel = Label(billframe,text="Bill Area",font=("arial",16,"bold"),relief = GROOVE,bd = 7)
        billlabel.pack(fill=X)
        scroll_Y = Scrollbar(billframe,orient = VERTICAL)
        scroll_Y.pack(side=RIGHT,fill=Y)
        global textArea
        textArea = Text(billframe, yscrollcommand=scroll_Y)
        scroll_Y.configure(command=textArea.yview)
        textArea.pack()
        self.welcome()

    def login(self):
        if self.txt_pass.get()=="" or self.txt_user.get()=="":
            messagebox.showerror("ERROR", f"All fields are mandatory",parent=self.root)
        elif self.txt_user.get()=="admin1" and self.txt_pass.get()=="VIT2906":
            messagebox.showinfo("Welcome", f"Welcome {self.txt_user.get()}",parent=self.root)
            # self.stock()
            self.pending()
        else:
           messagebox.showerror("ERROR",f"Invalid Credentials",parent=self.root)

    def customerDetail(self):
        file1.write("\n\t------------------------------------------------------------------------------------")
        file1.write(f"\n\t{txt_name.get()}\t {txt_email.get()}\t {txt_contact.get()}")
        print("details are added sucessfully")

    global price
    price=[]
    def additem(self):
        global toordal,ChanaDal,MoongDal,MasoorDal,UradDal,BasmatiRice,GroundnutOil,SoyabeanOil,MustardOil
        if clicked.get()=='':
            print("please select the item")
        if "ToorDal" in clicked.get():
            if (quantity.get()<=toordal):
                textArea.insert(END,f'\n{" Toor Dal"}\t\t     {quantity.get()} Kg\t\t     {150*quantity.get()}')
                price.append(150*quantity.get())
                toordal-=quantity.get()
            else:
                messagebox.showerror("ERROR",f"stock is not available only at present : {str(toordal)} Kg",parent=self.root)
        if "ChanaDal" in clicked.get():
            if (quantity.get()<=ChanaDal):
                textArea.insert(END, f'\n{" Chana Dal"}\t\t     {quantity.get()} Kg\t\t     {125 * quantity.get()}')
                price.append(125 * quantity.get())
                ChanaDal -= quantity.get()
            else:
                messagebox.showerror("ERROR",f"stock is not available only at present : {str(ChanaDal)} Kg",parent=self.root)
        if "MoongDal" in clicked.get():
            if (quantity.get()<=MoongDal):
                textArea.insert(END, f'\n{" Moong Dal"}\t\t     {quantity.get()} Kg\t\t     {146 * quantity.get()}')
                price.append(146 * quantity.get())
                MoongDal -= quantity.get()
            else:
                messagebox.showerror("ERROR",f"stock is not available only at present : {str(MoongDal)} Kg",parent=self.root)
        if "MasoorDal" in clicked.get():
            if (quantity.get()<=MasoorDal):
                textArea.insert(END, f'\n{" Masoor Dal"}\t\t     {quantity.get()} Kg\t\t     {135 * quantity.get()}')
                price.append(135 * quantity.get())
                MasoorDal -= quantity.get()
            else:
                messagebox.showerror("ERROR",f"stock is not available only at present : {str(MasoorDal)} Kg",parent=self.root)
        if "UradDal" in clicked.get():
            if (quantity.get()<=UradDal):
                textArea.insert(END, f'\n{" Urad Dal"}\t\t     {quantity.get()} Kg\t\t     {175 * quantity.get()}')
                price.append(175 * quantity.get())
                UradDal -= quantity.get()
            else:
                messagebox.showerror("ERROR",f"stock is not available only at present : {str(UradDal)} Kg",parent=self.root)
        if "BasmatiRice" in clicked.get():
            if (quantity.get()<=BasmatiRice):
                textArea.insert(END, f'\n{" Basmati Rice"}\t\t     {quantity.get()} Kg\t\t     {125 * quantity.get()}')
                price.append(125 * quantity.get())
                BasmatiRice -= quantity.get()
            else:
                messagebox.showerror("ERROR",f"stock is not available only at present : {str(BasmatiRice)} Kg",parent=self.root)
        if "GroundnutOil" in clicked.get():
            if (quantity.get()<=GroundnutOil):
                textArea.insert(END, f'\n{" Groundnut Oil"}\t\t     {quantity.get()} Kg\t\t     {220 * quantity.get()}')
                price.append(220 * quantity.get())
                GroundnutOil -= quantity.get()
            else:
                messagebox.showerror("ERROR",f"stock is not available only at present : {str(GroundnutOil)} Kg",parent=self.root)
        if "SoyabeanOil" in clicked.get():
            if (quantity.get()<=SoyabeanOil):
                textArea.insert(END, f'\n{" Soyabean Oil"}\t\t     {quantity.get()} Kg\t\t     {169 * quantity.get()}')
                price.append(169 * quantity.get())
                SoyabeanOil -= quantity.get()
            else:
                messagebox.showerror("ERROR",f"stock is not available only at present : {str(SoyabeanOil)} Kg",parent=self.root)
        if "MustardOil" in clicked.get():
            if (quantity.get()<=MustardOil):
                textArea.insert(END, f'\n{" Mustard Oil"}\t\t     {quantity.get()} Kg\t\t     {195 * quantity.get()}')
                price.append(195 * quantity.get())
                MustardOil -= quantity.get()
            else:
                messagebox.showerror("ERROR",f"stock is not available only at present : {str(MustardOil)} Kg",parent=self.root)

    def stock(self):
        API_Key = "o.FcirDOAoBuEgelVGZeU72k3lhBM0PipJ"
        file = open("stock.txt", mode="a")
        file.write("\n--------- Current Stock ---------")
        file.write(f"\n Toordal: {toordal} Kg")
        file.write(f"\n Chanadal: {ChanaDal} Kg")
        file.write(f"\n MoongDal: {MoongDal} Kg")
        file.write(f"\n MasoorDal: {MasoorDal} Kg")
        file.write(f"\n BasmatiRice: {BasmatiRice} Kg")
        file.write(f"\n GroundnutOil: {GroundnutOil} Kg")
        file.write(f"\n SoyabeanOil: {SoyabeanOil} Kg")
        file.write(f"\n MustardOil: {MustardOil} Kg")
        file.close()
        # ---- Reading -----#
        file = open("stock.txt", mode="r")
        text = file.read()
        pb = pushbullet.Pushbullet(API_Key)
        push = pb.push_note('Remember', text)

        print("Notification send")

    def welcome(self):

        textArea.delete(1.0, END)
        textArea.insert(END, "\t    Shree Balagi Oil And Sales")
        textArea.insert(END, "\n\n Bill No. ")
        textArea.insert(END, "\n Customer Name:   " + customerName.get())
        textArea.insert(END, "\n Phone no. :   " + customerContact.get())
        textArea.insert(END, f"\n =======================================")
        textArea.insert(END, "\n   Item\t\t    Quantity   \t\t     Price")
        textArea.insert(END, f"\n =======================================\n")
        textArea.configure(font=("arial",15,"bold"))

    def billgenrate(self):
        if(txt_name.get()==""):
            messagebox.showerror("Error","please enter your details in detail section",parent=self.root)
        else:
          global tex
          tex = textArea.get(10.0,(10.0+float(len(price))))
          self.welcome()
          textArea.insert(END,tex)
          textArea.insert(END,"========================================")
          textArea.insert(END,f"\n\t\tTotal Amount:  {sum(price)} Rs")


          bill=textArea.get(1.0,END)

         # bill sending to user part
          object = smt.SMTP("smtp.gmail.com", 587)
          object.starttls()

          object.login("sanskar.kothari20@vit.edu", "12011067")

          subject = "Invoice"
          body = bill

          message = "Subject:{}\n\n{}".format(subject, body)
          object.sendmail("sanskar.kothari20@vit.edu",customerEmail.get(), message)
          print("Bill on respective candidate mail id send sucessfully")
          object.quit()

         # self.stock()

    def reset(self):
        print("Reseting your bill area and customer details")
        textArea.delete(3.0, END)
        txt_name.delete(0,END)
        txt_email.delete(0,END)
        txt_contact.delete(0,END)
        self.welcome()

obj = Login(root)

root.mainloop()