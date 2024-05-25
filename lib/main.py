from tkinter import *
from PIL import Image, ImageTk
import customtkinter as ctk
import mysql.connector

ctk.set_appearance_mode("dark")


class MainApp:
    def __init__(self, app):
        self.db = mysql.connector.connect(
            host="localhost", port=4306, user="root", password="", database="py_employee")
        self.mycursor = self.db.cursor()

        app.after(0, lambda: app.state('zoomed'))
        app.title("THE COMPANY PROFILE")
        self.HomePage(app)
        # self.Registration_Page(app)
        # self.ToDoPage(app)

    def check_details(self, app):
        emp_username_entry = self.emp_username_entry
        emp_password_entry = self.emp_password_entry

        self.entered_user_id = emp_username_entry.get()
        self.entered_password = emp_password_entry.get()

        self.mycursor.execute(
            "SELECT * FROM employee_details WHERE USERNAME = '" + self.entered_user_id+"' AND PASSWORD = '" + self.entered_password + "'")
        self.username_check = self.mycursor.fetchone()

        if self.username_check is None:
            print("INVALID")
            self.HomePage(app)
        else:
            print("SUCCESS")
            self.ToDoPage(app)

    def HomePage(self, app):
        self.clear_frame(app)
        self.BackgroundImage1(app)

        main_frame = ctk.CTkFrame(app, fg_color="white")
        main_frame.place(relx=0.5, rely=0.5, anchor="center",
                         relwidth=0.5, relheight=0.6)

        left_frame = ctk.CTkFrame(main_frame, fg_color="white")
        left_frame.place(relx=0, rely=0, relwidth=0.5, relheight=1)

        right_frame = ctk.CTkFrame(main_frame, fg_color="white")
        right_frame.place(relx=0.5, rely=0, relwidth=0.5, relheight=1)

        self.load_img(left_frame)

        right_frame.pack_propagate(0)
        login_txt = ctk.CTkLabel(right_frame, text="Log in", font=(
            "0xProto", 24), text_color='black')
        login_txt.pack(padx=10, pady=10)

        emp_username_label = ctk.CTkLabel(
            right_frame, text="Enter username", font=("0xProto", 12), text_color='black')
        emp_username_label.pack(padx=10, pady=10)
        self.emp_username_entry = ctk.CTkEntry(
            right_frame, width=300, bg_color="white")
        self.emp_username_entry.pack(padx=10, pady=10)

        emp_password_label = ctk.CTkLabel(
            right_frame, text="Enter Password", font=("0xProto", 12), text_color='black')
        emp_password_label.pack(padx=10, pady=10)
        self.emp_password_entry = ctk.CTkEntry(
            right_frame, width=300, bg_color="white")
        self.emp_password_entry.pack(padx=10, pady=10)

        login_button = ctk.CTkButton(right_frame, text="LOG IN", font=(
            "0xProto", 12), command=lambda: self.check_details(app))

        login_button.place(x=130, y=280)

        signup_button = ctk.CTkButton(right_frame, text="SIGN UP", font=(
            "0xProto", 12), command=lambda: self.Registration_Page(app))
        signup_button.place(x=130, y=320)

        left_frame.bind("<Configure>", lambda event: self.load_img(left_frame))

    def Registration_Page(self, app):
        self.clear_frame(app)
        self.BackgroundImage2(app)

        frame = Frame(app, bg="BLACK")
        frame.place(relx=0.5, rely=0.5, anchor="center", height=700, width=700)

        label = Label(frame, text="EMPLOYEE REGISTRATION FORM",
                      font=("0xProto", 24), bg="BLACK", fg="WHITE")
        label.place(relx=0.5, rely=0.1, anchor="center")

        name_label = Label(frame, text="EMPLOYEE NAME", font=(
            "0xProto", 16), bg="BLACK", fg="WHITE")
        name_label.place(relx=0.3, rely=0.25, anchor="center")
        self.emp_name = Entry(frame, width=14, font=("0xProto", 14))
        self.emp_name.place(relx=0.7, rely=0.25, anchor="center")

        employee_id_label = Label(frame, text="EMPLOYEE ID", font=(
            "0xProto", 16), bg="BLACK", fg="WHITE")
        employee_id_label.place(relx=0.3, rely=0.35, anchor="center")
        self.emp_employee_id = Entry(frame, width=14, font=("0xProto", 14))
        self.emp_employee_id.place(relx=0.7, rely=0.35, anchor="center")

        employee_username_label = Label(frame, text="EMPLOYEE USERNAME", font=(
            "0xProto", 16), bg="BLACK", fg="WHITE")
        employee_username_label.place(relx=0.3, rely=0.45, anchor="center")
        self.emp_employee_username = Entry(
            frame, width=14, font=("0xProto", 14))
        self.emp_employee_username.place(relx=0.7, rely=0.45, anchor="center")

        employee_password_label = Label(frame, text="EMPLOYEE PASSWORD", font=(
            "0xProto", 16), bg="BLACK", fg="WHITE")
        employee_password_label.place(relx=0.3, rely=0.55, anchor="center")
        self.emp_employee_password = Entry(
            frame, width=14, font=("0xProto", 14))
        self.emp_employee_password.place(relx=0.7, rely=0.55, anchor="center")

        signup_button = ctk.CTkButton(frame, text="SIGN UP", font=(
            "0xProto", 12), command=lambda: self.registration_helper(app))
        signup_button.place(relx=0.50, rely=0.75, anchor="center")

        home_button = ctk.CTkButton(frame, text="HOME", font=(
            "0xProto", 12), command=lambda: self.HomePage(app))
        home_button.place(relx=0.50, rely=0.85, anchor="center")

    # name,id,username,password

    def ToDoPage(self, app):
        self.clear_frame(app)
        self.BackgroundImage3(app)

    def LandingPage(self):
        pass

    def registration_helper(self, app):
        self.employee_name = self.emp_name.get()
        self.employee_id = self.emp_employee_id.get()
        self.username = self.emp_employee_username.get()
        self.password = self.emp_employee_password.get()

        print(self.employee_name, self.employee_id,
              self.username, self.password)

        self.mycursor.execute(
            'INSERT INTO employee_details (`EMPLOYEE_NAME`, `EMPLOYEE_ID`, `USERNAME`, `PASSWORD`) VALUES(%s,%s,%s,%s)', (self.employee_name, self.employee_id, self.username, self.password))

        self.db.commit()
        print("\nSUCCESS ADDED TO DB\n")
        self.Registration_Page(app)

    def load_img(self, frame):
        self.original_img = Image.open(
            "C://Users//AKHI//Desktop//PYTHON WORKS//PY TODO//assets//images//frame_image.png")
        frame_width = frame.winfo_width()
        frame_height = frame.winfo_height()

        resized_img = self.original_img.resize((frame_width, frame_height))
        self.tk_img = ImageTk.PhotoImage(resized_img)

        self.img_label = Label(frame, image=self.tk_img, borderwidth=0)
        self.img_label.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.img_label.image = self.tk_img

    def BackgroundImage1(self, app):
        img = Image.open(
            "C://Users//AKHI//Desktop//PYTHON WORKS//PY TODO//assets//images//main_bg.png")
        img = img.resize((1920, 1080))
        img = ctk.CTkImage(light_image=img, size=(1920, 1080))
        im = ctk.CTkLabel(app, image=img, text="")
        im.image = img
        im.place(x=0, y=0)

    def BackgroundImage2(self, app):
        img = Image.open(
            "C://Users//AKHI//Desktop//PYTHON WORKS//PY TODO//assets//images//trekking.png")
        img = img.resize((1920, 1080))
        img = ctk.CTkImage(light_image=img, size=(1920, 1080))
        im = ctk.CTkLabel(app, image=img, text="")
        im.image = img
        im.place(x=0, y=0)

    def BackgroundImage3(self, app):
        img = Image.open(
            "C://Users//AKHI//Desktop//PYTHON WORKS//PY TODO//assets//images//dehr.jpg")
        img = img.resize((1920, 1080))
        img = ctk.CTkImage(light_image=img, size=(1920, 1080))
        im = ctk.CTkLabel(app, image=img, text="")
        im.image = img
        im.place(x=0, y=0)

    def clear_frame(self, app):
        for widget in app.winfo_children():
            widget.destroy()


app = ctk.CTk()
MainApp(app)
app.mainloop()
