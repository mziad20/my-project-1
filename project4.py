#تنفيز موقع لمعرفة الوقت
#ُقائمة فارغة لتخزين المستخدمين المسجلين
print("Welcome to the site (your watch)")
users=[]
while True:
    choice=input("do you want (login)or(sign up):")
    if choice == "sign up":
        username = input("new username")
        password = input("new password")
        # تحقق مما إذا كان الاسم غير موجود بالفعل في قائمة المستخدمين
        if any(user.get("username") == username for user in users):
            print("This username already exists")
        else:
            users.append({"username": username, "password": password})
            print("The user has been added successfully")
    elif choice== "login" :
        username=input("username")
        password=input("password")
        # تحقق مما إذا كان الاسم وكلمة السر موجودين في قائمة المستخدمين
        if any(user.get("username") == username and user.get("password") == password for user in users):
            print("Logged in successfully!")
            from tkinter import Label, Tk
            import time

            app_window = Tk()
            app_window.title("Digital Clock")
            app_window.geometry("420x150")
            app_window.resizable(1, 1)

            text_font = ("Boulder", 68, 'bold')
            background = "#f2e750"
            foreground = "#363529"
            border_width = 25

            label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width)
            label.grid(row=0, column=1)


            def digital_clock():
                time_live = time.strftime("%H:%M:%S")
                label.config(text=time_live)
                label.after(200, digital_clock)


            digital_clock()
            app_window.mainloop()
        else:
            print("The username or password is incorrect")

    else:
        break