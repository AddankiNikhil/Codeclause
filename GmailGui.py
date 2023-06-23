from tkinter import *
import smtplib
master=Tk()
master.title("GmailSender")
master.geometry("350x350")

def send ():
    try :
        user_id=username.get()
        #pass_word="zwizktbggjwrthzs"
        pass_word="gxuabxiapztozioj"
        #pass_word=passw.get()
        sender_address=sender.get()
        subject=sub.get()
        body=bod.get()
        if user_id=="" or pass_word=="" or sender_address=="" :
             notify.config(text="Please enter Redcepients Correctly!",bg="red",fg="white")
        elif body=="":
             notify.config(text="Email cannot be empty!",bg="red",fg="white")
        else:
            final_message="Subject :"+subject+"\n\n"+body
            print(final_message)
            server=smtplib.SMTP("smtp.gmail.com",587)
            server.starttls()
            server.login(user_id,pass_word)
            
            server.sendmail(user_id,sender_address,final_message)
            notify.config(text="Email Sent Succesfully!",bg="Green",fg="white")
            server.quit()
            
        print("email sent")
        
    except Exception as e:
             notify.config(text="Error sending the  Email",bg="red",fg="white")
             print("Except case")
             print(e)
def reset ():
    #print("Reset Button Clicked")
    username.set("")
    passw.set("")
    sender.set("")
    sub.set("")
    bod.set("")


#Field Decleration
head=Label(master,text="EmailSender",font=("Times New Roman",15))
head.grid(row=0,column=1,sticky=N)
Label(master,text="Email").grid(row=1,sticky=W)
Label(master,text="Password").grid(row=2,sticky=W)
Label(master,text="Reciever Mail").grid(row=3,sticky=W)
Label(master,text="Subject").grid(row=4,sticky=W)
Label(master,text="Body").grid(row=5,sticky=W)
#Label(master,text="NOTE:\n If You want to send mail via\n this application please enter the\n password generated in your mail",fg="BLACK").grid(row=7,column=0)
notify=Label(master,text="")
notify.grid(row=8,sticky=N)

#TextField Generation
username=StringVar()
user=Entry(master,textvariable=username,show="#")
user.grid(row=1,column=1,sticky=W)

passw=StringVar()
password=Entry(master,textvariable=passw,show="*")
password.grid(row=2,column=1)

sender=StringVar()
to=Entry(master,textvariable=sender,show="$")
to.grid(row=3,column=1)

sub=StringVar()
Subj=Entry(master,textvariable=sub)
Subj.grid(row=4,column=1)

bod=StringVar()
BodyEntry=Entry(master,textvariable=bod)
BodyEntry.grid(row=5,column=1,sticky=N)

#button addition
B1=Button(master,text="send" ,command=send)
B1.grid(row=8,sticky=W,padx=5,pady=5)

B2=Button(master,text="Reset",command=reset)
B2.grid(row=8,sticky=W,padx=45,pady=45)

master.mainloop()
