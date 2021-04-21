from tkinter import *
import json
from difflib import get_close_matches
from tkinter import messagebox
import pyttsx3

engine=pyttsx3.init()# creating instane of engine class
def wordAudio():
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(enterWordEntery.get())
    engine.runAndWait()
def  meaningaudio():
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(textArea.get(1.0,END))
    engine.runAndWait()



# This part is for functionality
def search():
    data = json.load(open('data.json'))
    word = enterWordEntery.get()
    word = word.lower()
    if word in data:
        meaning = data[word]
        textArea.delete(1.0, END)
        for item in meaning:
            textArea.insert(END, u'\u2022' + item + '\n\n')
    elif len(get_close_matches(word, data.keys())) > 0:
        closeMatch = get_close_matches(word, data.keys())[0]
        print(closeMatch)
        res = messagebox.askyesno('confirm', 'did you mean ' + closeMatch)
        if res == True:
            enterWordEntery.delete(0, END)
            enterWordEntery.insert(END, closeMatch)
            meaning = data[closeMatch]
            textArea.delete(1.0, END)
            for item in meaning:
                textArea.insert(END, u'\u2022' + item + '\n\n')
        else:
            messagebox.showerror('Error', 'The word does not exist please double check it.')
            enterWordEntery.delete(0, END)
            textArea.delete(1.0, END)

    else:
        messagebox.showinfo('information', 'The word does not exist')
        enterWordEntery.delete(0, END)
        textArea.delete(1.0, END)


def clear():
    enterWordEntery.delete(0, END)
    textArea.delete(1.0, END)


def iexit():
    res = messagebox.askyesno('Confirm', 'do you want to exit?')
    if res == True:
        root.destroy()
    else:
        pass


# This for GUI part TK is class of tkinter module
root = Tk()
# To create window for dictionary GUI
root.geometry('1000x626+100+50')
# To give a title too the window
root.title('Talking Dictionary created by Rama')
root.resizable(0, 0)
# using photoimage class we can import the images
bgimage = PhotoImage(file='bg.png')
bgLable = Label(root, image=bgimage)
bgLable.place(x=0, y=0)

enterWordLable = Label(root, text='Enter Word', font=('castellar', 29, 'bold'), fg='red3', bg='whitesmoke')
enterWordLable.place(x=530, y=20)
enterWordEntery = Entry(root, font=('arial', 23, 'bold'), bd=8, relief=GROOVE, justify=CENTER)
enterWordEntery.place(x=510, y=80)

searchImage = PhotoImage(file='search.png')
searchButton = Button(root, image=searchImage, bd=0, bg='whitesmoke', activebackground='whitesmoke', cursor='hand2',
                      command=search)
searchButton.place(x=620, y=150)

micImage = PhotoImage(file='mic.png')
micButton = Button(root, image=micImage, bd=0, bg='whitesmoke', activebackground='whitesmoke', cursor='hand2',command=wordAudio)
micButton.place(x=710, y=153)

MeaningLable = Label(root, text='MEANING', font=('castellar', 29, 'bold'), fg='red3', bg='whitesmoke')
MeaningLable.place(x=580, y=240)

textArea = Text(root, font=('arial', 18, 'bold'), height=8, width=34, bd=8, relief=GROOVE, wrap='word')
textArea.place(x=460, y=300)

microPhoneImage = PhotoImage(file='microphone.png')
microButton = Button(root, image=microPhoneImage, bd=0, bg='whitesmoke', activebackground='whitesmoke', cursor='hand2',command=meaningaudio)
microButton.place(x=530, y=555)

clearImage = PhotoImage(file='clear (1).png')
clearButton = Button(root, image=clearImage, bd=0, bg='whitesmoke', activebackground='whitesmoke', cursor='hand2',
                     command=clear)
clearButton.place(x=660, y=555)

exitImage = PhotoImage(file='exit.png')
exitButton = Button(root, image=exitImage, bd=0, bg='whitesmoke', activebackground='whitesmoke', cursor='hand2',
                    command=iexit)
exitButton.place(x=790, y=555)


def enter_function(event):
    searchButton.invoke()


root.bind('<Return>', enter_function)
root.mainloop()
