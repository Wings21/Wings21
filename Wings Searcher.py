import webbrowser
from googlesearch import search
from tkinter import *

root = Tk()
root.title("Wings Searcher")
root.configure(bg = "#181818")
root.geometry("900x500")
root.resizable(False, False)

def again() :
    try :
        webbrowser.open(s)

    except :
        print('Something went wrong or maybe your network connection is unstable')
        error = Tk()
        error.title("Error 404")
        error.configure(bg = "#181818")
        error.geometry("500x140")
        error.resizable(False, False)
        
        Label(error, text="Something went wrong or maybe your network", bg="#181818", fg="#fff", font=("arial",15)).place(x=40, y=20)
        Label(error, text="connection is unstable", bg="#181818", fg="#fff", font=("arial",15)).place(x=150, y=50)

        Button(error, text="Ok", bg="orange", fg="#fff", activeforeground="#fff", width=8,bd=4,command= error.destroy).place(x=210, y=90)

        error.after(3000, error.destroy)
    
def text_search():

    global s

    no1 = search_text.get()
    no2 = web_name.get()
    no3 = no1+" "+ no2
    
    r.config(text=no3)

    try :
        hmm_text = search_text.get()
        extra = web_name.get()
        ps5 = hmm_text+" "+ extra
        print(ps5)
        text = ps5
        
        for s in search(text, tld = 'com', lang = 'en-in', num = 1, start = 0, stop = 1, pause = 1):
            webbrowser.open(s)

            

        for m1 in search(text, tld = 'com', lang = 'en-in', num = 1, start = 2, stop = 1, pause = 0):
            more1.config(text = m1)

        for m2 in search(text, tld = 'com', lang = 'en-in', num = 1, start = 3, stop = 1, pause = 0):
            more2.config(text = m2)

        for m3 in search(text, tld = 'com', lang = 'en-in', num = 1, start = 4, stop = 1, pause = 0):
            more3.config(text = m3)

        for m4 in search(text, tld = 'com', lang = 'en-in', num = 1, start = 5, stop = 1, pause = 0):
            more4.config(text = m4)

        for m5 in search(text, tld = 'com', lang = 'en-in', num = 1, start = 6, stop = 1, pause = 0):
            more5.config(text = m5)

    except :
        print('Something went wrong or maybe your network connection is unstable')
        error = Tk()
        error.title("Error 404")
        error.configure(bg = "#181818")
        error.geometry("500x140")
        error.resizable(False, False)

        Label(error, text="Something went wrong or maybe your network", bg="#181818", fg="#fff", font=("arial",15)).place(x=40, y=20)
        Label(error, text="connection is unstable", bg="#181818", fg="#fff", font=("arial",15)).place(x=150, y=50)

        Button(error, text="Ok", bg="orange", fg="#fff", activeforeground="#fff", width=8,bd=4,command= error.destroy).place(x=210, y=90)

        error.after(3000, error.destroy)

    search_text.delete(0, END)
    web_name.delete(0, END)

def url() :

    
    
    try :
        u = search_url.get()
        webbrowser.open(u)

    except :
        print('Something went wrong')
        error = Tk()
        error.title("Error 404")
        error.configure(bg = "#181818")
        error.geometry("540x140")
        error.resizable(False, False)

        Label(error, text="Something went wrong maybe the link you are trying ", bg="#181818", fg="#fff", font=("arial",15)).place(x=40, y=20)
        Label(error, text="to visit is broken", bg="#181818", fg="#fff", font=("arial",15)).place(x=200, y=50)

        Button(error, text="Ok", bg="blue", fg="#fff", activeforeground="blue", width=8,bd=4,command= error.destroy).place(x=240, y=90)
        error.after(3000, error.destroy)

    search_url.delete(0, END)


Label(root, text="Recent", bg="#181818", fg="#fff", font=("arial", 15)).place(x=55, y=40)

r = Label(root, bg="#262626", fg="#fff", font=("arial",10), width=20)
r.place(x=10, y=80)
Button(root, text="Search again", fg="#fff", bg="red",activeforeground="red", bd=4, command=again).place(x=50, y=120)

Label(root, text="Wings Searcher", bg="#181818", fg="#fff", font=("arial",30)).place(x=310, y=30)

Label(root, text="Search with text", bg="#181818", fg="#fff",font=("arial",15)).place(x=260, y="100")
search_text = Entry(root, bg="#262626", fg="#fff", font=("arial",10), width=40)
search_text.place(x=200, y=135)
Button(root, text="search", bg="orange", fg="#fff", activeforeground="orange", font=("arial",10), bd=4, command=text_search).place(x=500 ,y=130)

Label(root, text="---OR---", bg="#181818", fg="#fff", font=("arial",10)).place(x=310, y=165)

Label(root, text="Enter a web address(url)", bg="#181818", fg="#fff", font=("arial",15)).place(x=225, y=190)
search_url = Entry(root, width=40, font=("arial",10), bg="#262626", fg="#fff")
search_url.place(x=200, y=230)
Button(root, text="Enter", bg="blue", fg="#fff", activeforeground="blue", font=("arial",10), bd=4, command=url).place(x=500 ,y=225)

Label(root, text="Enter the name of website you", bg="#181818", fg="#fff", font=("arial",12)).place(x=625, y=150)
Label(root, text="want to search on", bg="#181818", fg="#fff", font=("arial",12)).place(x=645, y=170)
Label(root, text="(Optional)", bg="#181818", fg="#fff", font=("arial",8) ).place(x=770, y=172)

web_name = Entry(root, width=30, font=("arial",10), bg="#262626", fg="#fff")
web_name.place(x=625,y=200)


#More
Label(root, text="More Results", bg="#181818", fg="#fff", font=("arial", 20)).place(x=360, y=280)

more1 = Label(root, bg="#262626", fg="#fff", width= 125, height=1)
more1.place(x=10, y=320)

more2 = Label(root, bg="#262626", fg="#fff", width= 125, height=1)
more2.place(x=10, y=350)

more3 = Label(root, bg="#262626", fg="#fff", width= 125, height=1)
more3.place(x=10, y=380)

more4 = Label(root, bg="#262626", fg="#fff", width= 125, height=1)
more4.place(x=10, y=410)

more5 = Label(root, bg="#262626", fg="#fff", width= 125, height=1)
more5.place(x=10, y=440)

root.mainloop()
