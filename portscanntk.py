from tkinter import *
from tkinter.ttk import Frame
from tkinter import messagebox
import socket

#Chase Brown
#3.25.17
#ip port scanning python with tkkinter gui

def portScan(ip,port):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #set client = to socket ip and port for easier use
        client.connect((ip, port))  #attempt to connect to the ip and port
        return True             #return true if it connects else return none
    except:
        return None

class portscan(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.title("Python Port Scanner")       #Title of window
        #set the frame dimentions and pack the parent window
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.resizable(width=False,height=False)

        #get screen dimensions and center window
        xoffset = int(self.winfo_screenwidth()/2-1280/2)
        yoffset = int(self.winfo_screenheight()/2-800/2)
        self.geometry("%dx%d+%d+%d" % (1280, 800, xoffset, yoffset))    #set geometry of window

        self.frames = {}
        for F in (Welcome, MainMenu):       #The two windows used in program sets the page
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Welcome")          #call show_frame to display the welcome window

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()                     #raise that window frame
        self.title(frame.title)             #rename the window title to the title in def Welcome

    def changeTitle(self, newTitle):
        self.title(newTitle)

class Welcome(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self,parent)
        self.controller = controller        #set the controller
        self.title = "Welcome"              #ttile of the window
        #menu File
        mb = Menubutton(self, text="File", relief=RAISED)       #menu button
        mb.grid(column=0, row=0)        #place in the window it will appear
        mb.menu = Menu(mb, tearoff=0)   #set the button as a menu
        mb["menu"] = mb.menu            #menu with about and exit program which are commands
        mb.menu.add_command(label="About.?", command=self.about)        #calls the about message box
        mb.menu.add_separator()
        mb.menu.add_command(label="Exit Program", command=self.quit)    #exits the program

        self.w_header = Label(self, text="Python Port Scanner", font=("Helvetica", 32, "bold")) #header
        self.but_start = Button(self, text="START", font=("Helvetica", 24, "bold"), width=30,
                                command=self.start, relief=RAISED, bd=5)    #start button
        #Formatting of the window
        self.columnconfigure(3, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(4, weight=2)
        self.w_header.grid(column=2, row=2)
        self.but_start.grid(column=2, row=3)

    def about(self):
        messagebox.showinfo("About", "Chase Brown")     #messagebox when File<About.? is selected

    def start(self):
        self.controller.show_frame("MainMenu")          #opens up the next window mainmenu


class MainMenu(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.title = "Main Menu"

        #menu File
        mb = Menubutton(self, text="File", relief=RAISED)
        mb.grid(column=0, row=0)
        mb.menu = Menu(mb, tearoff=0)
        mb["menu"] = mb.menu
        mb.menu.add_command(label="About.?", command=self.about)
        mb.menu.add_separator()
        mb.menu.add_command(label="Exit Program", command=self.quit)
        #menu Help
        mb2 = Menubutton(self, text="Help", relief=RAISED)
        mb2.grid(column=1, row=0)
        mb2.menu = Menu(mb2, tearoff=0)
        mb2["menu"] = mb2.menu
        mb2.menu.add_command(label="Scanner Help", command=self.help)

        #labels for the ip beginning and ending port entry boxes
        self.window_label = Label(self, text="To begin your port scan pleae fill in the boxes below",
                                  font=("Helvetica", 26, "bold"))
        self.lab_ip = Label(self, text="Ip:", font=("Helvetica", 12, "bold"))
        self.lab_firstport = Label(self, text="Begining Port:", font=("Helvetica", 12, "bold"))
        self.lab_secondport = Label(self, text="Ending Port:", font=("Helvetica", 12, "bold"))
        self.ent_ip = Entry(self, font=("Helvetica", 16, "bold"), width=15)     #ip entry box
        self.ent_firstport = Entry(self, font=("Helveticta", 16, "bold"), width=10)     #beginning port entry box
        self.ent_secondport = Entry(self, font=("Helvetica", 16, "bold"), width=10)     #ending port entry box
        #lambda command to call scan that gets the inputs that are entered in the window boxes with .get()
        self.but_scan = Button(self, text="Scan", font=("Helvetic", 12, "bold"),
                               command=lambda: self.scan(self.ent_ip.get(), self.ent_firstport.get(),
                                                         self.ent_secondport.get()), relief=RAISED, bd=5, width=10)
        self.win_text = Text(self, height= 20, width=150)

        #WINDOW FORMATTING AND PLACEMENT
        self.window_label.grid(columnspan=13, row=1, pady=20)

        self.columnconfigure(2, weight=1)       #add buffer space between left side and ip

        self.lab_ip.grid(column=3, row=2, pady=10)              #place the ip and ip input box
        self.ent_ip.grid(column=4, row=2, pady=10, padx=10)

        self.columnconfigure(5, weight=1)  # add space between ip: and beginningport:
        self.lab_firstport.grid(column=6, row=2, pady=10)       #place the firstport title and input box
        self.ent_firstport.grid(column=7, row=2, pady=10, padx=10)

        self.columnconfigure(8, weight=1)  # space between ports and scan button
        self.lab_secondport.grid(column=9, row=2, pady=10)      #place the secondport title and input box
        self.ent_secondport.grid(column=10, row=2, pady=10, padx=10)

        self.but_scan.grid(column=11, row=2, pady=20)        #place button middle of screen under entries

        self.columnconfigure(12, weight=2)  # add buffer space between ports input and right side

        self.win_text.grid(columnspan=13, row=3, pady=10)

    def help(self):
        messagebox.showinfo("Help", "Enter a valid ip number along with a Beginning port \n"
                                    "that is greater than 0 and less than or equal to 65000.\n"
                                    "IP ex: 192.168.10.1")

    def about(self):
        messagebox.showinfo("About", "Chase Brown")

    def scan(self, ip, fport, sport):
        self.ent_ip.delete(0, 'end')
        self.ent_firstport.delete(0, 'end')
        self.ent_secondport.delete(0, 'end')
        #ip fport and sport are passed in as strings because of .get() for the entries
        #convert the variables fport and sport to ints to use as compares
        if int(fport) < 1 or int(fport) > 65000:
            self.ent_firstport.insert(0, "invalid")     #if the input is not valid then it clears the entries and prints
                                                        #invalid in the window that is not valid
        elif int(sport) < 1 or int(sport) > 65000:
            self.ent_secondport.insert(0, "invalid")
        else:
            self.win_text.insert(INSERT, "ports open on ")      #formatting for the print to the text box
            self.win_text.insert(INSERT, ip)
            self.win_text.insert(INSERT, " from  ")
            self.win_text.insert(INSERT, fport)
            self.win_text.insert(INSERT, " to ")
            self.win_text.insert(INSERT, sport)
            self.win_text.insert(INSERT, "\n")
            for port in range(int(fport), int(sport)):
                var = portScan(ip, port)
                if var == TRUE:
                    self.win_text.insert(INSERT, "Open port: ")
                    self.win_text.insert(INSERT, port)
                    self.win_text.insert(INSERT, "\n")

if __name__ == "__main__":
    app = portscan()
    app.mainloop()