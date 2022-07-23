from logging import exception
from tkinter import *

from PIL import ImageTk,Image
import tkinter.font as font
from tkinter import messagebox
from instascrape import Reel
import time

#'2970217695%3Au9HsJPravNk1u3%3A19'
def download(link):
     try:
          if link:
               SESSIONID='2970217695%3Au9HsJPravNk1u3%3A19'
               headers={
                    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                                   "Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59",
                    "cookie":f'sessionID={SESSIONID}'
               }
               google_reel=Reel(link)
               google_reel.scrape(headers=headers)
               google_reel.download(fp=f".\\reel{int(time.time())}.mp4")
               messagebox.showinfo("status","Reel download successfully Check folder")
          else:
               messagebox.showwarning('Empty Field','Please Enter The Link')
     except exception as e:
          messagebox.showerror("Error","Something went wrong! please try again later")
          print(e)
               

root= Tk()
root.title('Instagram reel downloader')  # title
root.minsize(680,500)
root.maxsize(600,500)
HEIGHT=500
WIDTH= 600
FONT= font.Font(family="Times New Roman",size='18',weight='bold')
canvas= Canvas(root,height=HEIGHT,width=WIDTH)
canvas.pack()

frame=Frame(root,bg='white')
frame.place(relwidth=1,relheight=1)

background_image=ImageTk.PhotoImage(Image.open(r'C:\\Users\\dell\\Desktop\\insta reel download\\image1.jpg'))
background_label= Label(frame,image=background_image)
background_label.place(relx=-0.27,relwidth=0.7,relheight=1)

label1=Label(frame,text='Download instagram reel',font=FONT,bd=5,fg='#011137',bg='white')
label1.place(relx=0.48,rely=0.1,relheight=0.1)

FONT= font.Font(family="Times New Roman",size='12',weight='bold')

label2=Label(frame,text='Enter link address',font=FONT,bd=5,fg='#e52165',bg='white')
label2.place(relx=0.48,rely=0.25,relheight=0.1)

entry=Entry(frame,font=FONT,fg='#fbad50')
entry.place(relx=0.48,rely=0.35,relwidth=0.4,relheight=0.05)

button1=Button(root,text='Download',font=FONT,bg='pink',fg='black',
               activebackground='black',activeforeground='pink',command=lambda:download(entry.get()))
button1.place(relx=0.48,rely=0.45,relheight=0.06,relwidth=0.2)

label3=Label(frame,text='instructions',font=FONT,bd=5,fg='black',bg='white')
label3.place(relx=0.48,rely=0.6,relheight=0.1)

FONT= font.Font(family="Times New Roman",size='10',weight='bold')

TEXT='1. Only Public account Reels Can Be Downloaded \n'\
     '2. Enter the link address of reels from instagram'

label4=Label(frame,text=TEXT,font=FONT,bd=5,fg='#cd486b',justify=LEFT,bg='white')
label4.place(relx=0.48,rely=0.7,relheight=0.1)
root.mainloop()