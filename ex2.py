def generate_password():
    try:
        repeat = int(repeat_entry.get())
        lenght = int(length_entry.get())
    except:
        messagebox.showerror(message="please key in the required")
        return
    if repeat ==1:
        password = random.sample(charecter_string,length)
    else:
        password = random.choice(charecter_string,k=length)

    password=''.join(password)
    password_v=strigVar()
    password="created password: "+str(password)
    password_v.set(password)

    password_label=Entry(password_gen,bd=0,bg=grey85,textvariable=password_v,state='readonly')
    password_label.place(x=10,y=140,height=50,width=320)
