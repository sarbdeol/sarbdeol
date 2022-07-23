from pygame import event
import wikipedia
import pyttsx3    # text-to-speech conversion library
import datetime   
import speech_recognition as sr
import os   # portable way of using operating system
import webbrowser   
import sys
import smtplib
import tkinter as tk
from tkinter import messagebox
try:
    import pywhatkit
except:
    print('no internet')
from tkinter import*
from PIL import Image,ImageTk
from translate import Translator  #translate english to hindi
from playsound import playsound
import random
import keyboard
import requests
from bs4 import BeautifulSoup
from time import sleep,time
import pyjokes
from pywikihow import WikiHow,search_wikihow
import pyautogui
#=============create window==========
root=tk.Tk()
root.geometry('500x800+500+100')
root.resizable(False,False)
root.title('Voice Assistant')
root.iconbitmap('assistant.ico')
# top frame
top_frame=Frame(root)

# scroll button
scroll=Scrollbar(top_frame)

# text show

ans=Text(top_frame,width=50,height=33,fg='black',bg='grey',yscrollcommand=scroll.set,wrap=WORD,)
ans.configure(font=("Courier", 10, "roman"))
scroll.pack(side=RIGHT,fill='y')
scroll.config(command=ans.yview)
ans.see(END)
ans.pack()
top_frame.pack(side=TOP)

# bottom frame
bottom_f=Frame(root,width=60)
bottom_f.pack(side=BOTTOM)




#===========pyttsx3===============

# object creation
engine= pyttsx3.init('sapi5')   
# voice rate
rate = engine.getProperty('rate')   # getting details of current speaking rate
                                    #printing current voice rate
engine.setProperty('rate', 150)
#  Voices

voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[1].id)  #changing index, changes voices. o for male
#engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female
#==========read audio===================
def speak(audio):   # text to speech
    global speak   
    
   
    engine.say(audio)
    print(audio)
    try:
        ans.insert(END,'\n>>'+audio)
        ans.see(END)
        root.update()
    except:
        
        root.quit()
    engine.runAndWait()

#================take command============
def takecommand(): #convert voice into text
        r=sr.Recognizer()
        m=sr.Microphone()
        with m as source:
            ans.insert(INSERT,'listening...'+'\n')
            ans.see(END)
            root.update()
            print('listening.....')           
            r.pause_threshold=1
            audio = r.listen(source,timeout=4,phrase_time_limit=5)
            
        try:     #test a block of code for errors
            print('Recognizing...')
            
            query=r.recognize_google(audio,language='en-in')
            
            print(f'you: {query}')
            ans.insert(INSERT,'\t<<' +query)
            ans.see(END)

            root.update()
            
        except Exception as e:    # handle the error
            
            return "none"
        
        return query


def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

def myloc() :
    my="my location"
    url=f'https://www.google.com/search?q=weather+{my}'
    r= requests.get(url)
    data= BeautifulSoup(r.text,"html.parser")
    temp=data.find("div",class_="BNeawe iBp4i AP7Wnd").text
    day=data.find("div",class_="BNeawe tAd8D AP7Wnd").text.split("m",1)  
    speak(f"weather is {day[1]} and {temp}") 

def wish():
    
    hour= int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak('gud morning sir')
        root.update()
    elif hour>12 and hour<18:
        speak('good afternoon sir')
        root.update()
    else :
        speak('good evening sir')
        
        
    #myloc()
def assname():
    
    iname="LAURA" # assistant name
                         
    speak(F"I am your assistant {iname}")
    root.update()
def usrname():
    #global uname
 
    speak("What should i call you sir")
    uname = takecommand().lower()               #user name
    speak("Welcome Mister")
    speak(uname)
    


#==================Main function=======================
def main():
    running=True
    while running: 
            try:
               import pywhatkit
            except:
               speak('please connect with internet')
               break
            
            ans.insert(INSERT,'\n')
            ans.see(END)

            root.update()
            query=takecommand().lower()

            # All the commands said by user will be
            # stored here in 'query' and will be
            # converted to lower case for easily
            # recognition of command

            # BASIC CONVERSATION
            
            if 'hello' in query or 'hay' in query or 'hey' in query or 'hai' in query:
                speak('Hello sir,how may i help you')

            elif "what's your name" in query or "what is your name" in query or 'your name' in query:
                speak("my name is LAURA.")

            elif "my name" in query:
                usrname()
                
            elif 'who are you' in query :
                speak('i am your assistant sir, How can i help you ')

            elif 'how old are you' in query or 'what is your age' in query :
                speak('age is just a number.But technically is a word.  ')
                
            elif 'good night' in query:
                speak('ok sir ,Talk to you in the morning.')
                break
            elif 'what is love' in query:
                speak("It is 7th sense that destroy all other senses")

            elif "don't listen" in query or "stop listening" in query:
                speak("for how much time you want to stop  from listening commands")
                try:
                    a = int(takecommand())
                    speak(f"Ok take rest for {a} seconds")
                    time.sleep(a)   
                except:
                    speak("speak only integer value ")

            elif "good morning" in query:
                speak("A warm" +query)
                speak("How are you ")
                
            elif 'fine' in query or 'good' in query:
                speak('okay')

            elif "good afternoon" in query:
                speak("How are you ")
                speak(assname) 
            
            elif "will you be my gf" in query or "will you be my bf" in query:  
                speak("I'm not sure about, may be you should give me some time")
    
            elif "how are you" in query:
                speak("I'm fine, glad you me that")
    
            elif "love you" in query:
                speak("It's hard to understand")

            elif 'your birthday' in query or 'you born' in query:
                speak('sir i was programmed on eighth august 2021, and you sir')
                ans.insert(INSERT,'\n')
                root.update()
                query=takecommand().lower()
                if '' in query:
                    speak('ok sir ')
          
            elif 'wait'  in query or 'sleep' in query or 'break' in query:
                speak('ok sir,i am here you can call me anytime ')
                break

            elif 'no thanks' in query or 'ok' in query or 'stop' in query:
                speak('Thanks for using me sir')
                break             
            
            elif "thank you" in query or "thanks" in query:
                speak('welcome sir')   
                break
            elif 'clear' in query:
                speak('ok done')
                ans.delete(1.0,'end')
                

            elif 'who creates you' in query or 'make you'  in query or  'created you' in query or 'develop you'  in query:
                speak('My Creator is Sarabjit Singh ,I give lots of thanks to him')
                root.update()

            elif 'bye' in query or 'close' in query or 'exit' in query or 'quit' in query:
                speak('shutting down ')
                return exit(0) 
            
            elif 'feeling' in query or 'your mood' in query:
                speak('Feeling great, after meeting you sir')

            elif 'bored' in query or 'bore' in query or 'activity' in query or 'nothing to do' in query:
                speak('tell me in which your interest (games) (music) (movies)  ')
                ans.insert(INSERT,'\n')
                root.update()
                query=takecommand().lower()
                if 'games' in query or 'game' in query:
                    speak('i have only lodu to play (if open (YES) or if not ( NO))')
                    ans.insert(INSERT,'\n')
                    root.update()
                    query=takecommand().lower()
                    if 'yes' in query:                    
                        webbrowser.open('https://vipgames.com/play/?affiliateId=wpLudo&forwardto=games/ludo/lobby#/home')
                        sleep(10)
                    elif 'no' in query:
                        root.update()
                        speak('i have Popular Games Online')
                        webbrowser.open('https://www.agame.com/games')
                        break
                    
                elif 'play song' in query or 'movie' in query:
                    speak('which song or movie you want to play')
                    ans.insert(INSERT,'\n')
                    root.update()
                    query=takecommand().lower()
                    if '' in query: 
                        song=query.replace('','')
                        speak('playing '+ song)
                        pywhatkit.playonyt(song)
                        root.update()
                        sleep(5)

            elif 'jokes' in query or 'joke' in query:
                
                engine.setProperty('voice', voices[1].id)
                joke1=pyjokes.get_joke(language='en', category= 'all')
                speak(joke1)
                speak('for more jokes say one more')
                while True:
                    query=takecommand().lower()
                
                    if 'one more' in query:
                        joke1=pyjokes.get_joke(language='en', category= 'all')
                        speak(joke1)
                    else:
                        main()

            #  request module
            
            elif 'temperature' in query:
                try: 
                    url=f'https://www.google.com/search?q={query}'
                    r= requests.get(url)
                    data= BeautifulSoup(r.text,"html.parser")
                    temp=data.find("div",class_="BNeawe iBp4i AP7Wnd").text
                    day=data.find("div",class_="BNeawe tAd8D AP7Wnd").text.split("m",1)
                    
                    speak(f"current {query} is  {day[1]} and {temp}")
                
                except:
                    speak('')
                    break
                    
               
                
            elif 'where i am' in query or 'where we are' in query:
                try:
                    ipadd=requests.get('https://api.ipify.org').text

                    url='https://get.geojs.io/v1/ip/geo/'+ipadd+'.json'
                    geo_req=requests.get(url)
                    geo_data=geo_req.json()
                    city=geo_data['city']
                    country=geo_data['country']
                    print(f'ip address is{ipadd}')
                    speak(f'sir i think we are in {city} city of {country} ')
                except:
                    speak('Due to bad network i cant find sir ')
                    
            elif 'ip address' in query:
                ipadd=requests.get('https://api.ipify.org').text
                speak('your ip address is'+ipadd)

            elif 'weather' in query:
                myloc()
               
                
                  

            #os module 
            elif 'gana' in query or 'song' in query or 'music' in query:
                try:
                    m_dir='C:\\Users\\dell\\Music'
                    songs=os.listdir(m_dir)
                    rd=random.choice(songs)
                    os.startfile(os.path.join(m_dir,rd))
                    
                except:
                    speak("i can't find location of your music ,add your music in new path <C:\\Users\\dell\\Music>")
                  
            
                
                
            elif "write a note" in query:
                speak("What should i write, sir")
                note = takecommand()
                file = open('ass.txt', 'w')
                speak("Sir, Should i include date and time")
                snfm = takecommand()
                if 'yes' in snfm or 'sure' in snfm:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    file.write(strTime)
                    file.write(" :- ")
                    file.write(note)
                    speak('Done sir')
                else:
                    file.write(note)
                    speak('ok i am not include ')
                    speak('done')
            
            elif "show note" in query:
                speak("Showing Notes")
                file = open("ass.txt", "r")
                speak(file.read(2000))

            #keyboard======================
            elif 'run' in query or 'open' in query:
                speak('wait a second sir')
                query=query.replace('open','')
                speak(f'opening {query}')
                keyboard.press_and_release('windows + s')
                sleep(1)
                keyboard.write(query)
                sleep(1)
                keyboard.press_and_release('enter')
                sleep(1)
                 

                   # Webbrowser module ========================
            elif ' open google meet' in  query:
                speak('opening google meet....')
                webbrowser.open('https://meet.google.com')
                root.update()
                
            elif 'open google' in  query:
                speak('Sir, what should i search on google')
                what=takecommand().lower()
                speak('wait a second sir')
                webbrowser.open(f"{what}")
                root.update()
                
            elif 'open gmail' in query:
                speak('opening gmail.....')
                webbrowser.open('https://mail.google.com')
                root.update()
                
            

            elif 'games' in query or 'game' in query:
                speak('i have lodu to play (if open (YES) or if not ( NO))')
                ans.insert(INSERT,'\n')
                root.update()
                query=takecommand().lower()
                if 'yes' in query:                    
                    webbrowser.open('https://vipgames.com/play/?affiliateId=wpLudo&forwardto=games/ludo/lobby#/home')
                    break
                elif 'no' in query:
                    root.update()
                    speak('ok i have more Games Online')
                    webbrowser.open('https://www.agame.com/games')
                    

            #============= pywhatkit module =============
            elif 'youtube' in query :
                
                song=query.replace('youtube','')
                speak('playing '+ song)
                pywhatkit.playonyt(song)
                root.update()
                sleep(5)

            elif 'message new number' in query:  
                speak('speak ten digit of number carefully')
                to=takecommand().lower()
                speak('ok, tell me your message')
                msg=takecommand().lower()
                h=int(datetime.datetime.now().hour)
                m=int(datetime.datetime.now().minute)
                speak('In 95 seconds web.whatsapp.com will open and after 20 seconds message will be delivered')
                pywhatkit.sendwhatmsg(f"+91{to}",msg,h,2+m)

            #== auto module    
            elif 'send a message'  in query:  
                speak('tell me name of your contact ') 
                name=takecommand().lower()  
                speak('what message i send sir') 
                msg=takecommand().lower()
                speak(f'send message to {msg}')
                from auto import whatsappmsg
                whatsappmsg(name,msg)
                speak('done sir')

            elif 'open chat' in query or 'open whatsapp' in query or 'see chat' in  query:
                speak("which chat i open sir")
                chat=takecommand().lower()
                from auto import whatschat
                whatschat(chat)
                speak(f'here is {chat} chat')


            elif 'voice call' in query or 'call' in query:
                speak('tell me a contact name sir')
                vcall=takecommand().lower()
                speak(f'calling {vcall}')
                from auto import whatscall
                whatscall(vcall)
         
            elif 'video call' in query:
                speak('tell me a contact name sir')
                vdcall=takecommand().lower()
                speak('video calling.. {vdcall}')
                from auto import whatsVcall
                whatsVcall(vdcall)
        
            #============= wikipedia module ===========               
            elif 'search' in query or 'find'  in query or 'meaning' in query or 'tell' in query:
                try:
                    person=query.replace('','')
                    info= wikipedia.summary(person,1)
                    speak(f'according to wikipedia, {info}')
                    sleep(5)
                except:
                    speak("sorry i can't find sir")
            
            
            #============ Datetime module=================
            
            elif 'day' in query:
                day=datetime.datetime.today().strftime("%A ")
                speak('Today is : '+day)
                root.update()
            elif 'date' in query:
                date=datetime.datetime.today().strftime('%d %B %Y')
                speak("Today's Date is : "+date)
                root.update()

            elif 'what is the time'  in query or 'tell me the time' in query or 'time' in query:
                h=str(datetime.datetime.now().strftime('%I:%M:%p'))
                speak('Current time is '+h)
                root.update()

                
            
            #==================== translate =============
            elif "translate " in query:          # ONE WORD
                word=query.replace('translate' ,'')
                translator= Translator(from_lang="English",to_lang="Hindi")
                translation = translator.translate(word)
                speak(translation)
                root.update()
                break

            #==psutil=====
            elif 'power' in query or 'battery'in query:
                import psutil
                battery=psutil.sensors_battery()
                percent=battery.percent
                speak(f'sir our system have {percent} percent power ')
            
            #==pywikihow====
            elif 'how to do mode' in query:
                speak("How to do mode is start")
                while True:
                    speak("Please tell me what do you want to know")
                    how=takecommand().lower()
                    try:
                        if 'close' in how or 'exit' in how:
                            speak('How to do mode is closed')
                            break
                        else:
                            max_results=1
                            how_to=search_wikihow(how,max_results)
                            assert len(how_to) ==1
                            how_to[0].print()
                            speak(how_to[0].summary)
                    except:
                        speak("sorry sir, i am not able to find this")

            elif 'screenshot'  in query:
                speak('sir, Please tell me the name for this screenshot file')  
                name=takecommand().lower()
                if 'stop' in name or 'no' in name:
                    main()
                else:
                    speak('please sir hold the screen,i am taking screenshot in three seconds')
                    sleep(1)
                    speak('three')
                    sleep(1)
                    speak('two')
                    sleep(1)
                    speak('one')
                    img=pyautogui.screenshot()
                    img.save(f"{name}.png")
                    speak("i am done sir,the screenshot is saved in our main folder.")


            

            else:
                speak('say that again please!') 
                
                   
   
def img() :  # =========Read the Image=============
    image = Image.open("recbutton.png") 
    # Reszie the image using resize() method
    resize_image = image.resize((120, 120)) 
    img = ImageTk.PhotoImage(resize_image) 
    # create button and attach image
    rebutton = Button(bottom_f,image=img,command=main,bd=0,activebackground='white')
    rebutton.image = img
    rebutton.pack(anchor=CENTER)

    #=========MENU=====================
    main_menu=Menu(root)
    root.config(menu=main_menu)

    # creating file menu
    file_menu=Menu(main_menu)
    main_menu.add_cascade(label='MENU',menu=file_menu)
    def clear():
        speak('clear')
        ans.delete(1.0,'end')     #"1.0" and "end" refer to the first character and 
                                #the last character of the contents in the Text widget
    def exit_1():  # exit function 
        speak('exit')
        root.quit()
    def restart():
        speak('restarting')
        root.destroy()
        os.startfile("LAURADEMO.py")
    


    file_menu.add_command(label='clear',command=clear)
    file_menu.add_command(label='restart',command=restart)
    file_menu.add_command(label='exit',command=exit_1)

if __name__=="__main__":
    
    img()
    wish()
    main()
      
    
    
    root.mainloop()               
              
           
