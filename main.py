import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
import tkinter.font as tkFont
from tkinter import *
import os

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.pyplot import figure, Figure 

#sources: 

class App:
     def __init__(self, root):
    # setting title
        root.title("Data graphing application") #Renamed window
        # setting window size
        width = 600
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.button1 = tk.Button(root)
        self.button1["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        self.button1["font"] = ft
        self.button1["fg"] = "#000000"
        self.button1["justify"] = "center"
        self.button1["text"] = "Load CSV" #Changed name of the button to "Load CSV"
        self.button1.place(x=70, y=50, width=70, height=25)
        self.button1["command"] = self.button1_command

        self.dropbox = ttk.Combobox(root)
        self.dropbox.place(x=350, y=50, width=80, height=25)
        self.dropbox.bind("<<ComboboxSelected>>", self.chosen_kaupunki)
        
        self.labelTop = tk.Label(root, text = "Select community")
        self.labelTop.place(x=300, y=20, width=180, height=25)
        
        self.label1 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        self.label1["font"] = ft
        self.label1["fg"] = "#333333"
        self.label1["justify"] = "center"
        self.label1["text"] = "label"
        self.label1.place(x=150, y=50, width= 185, height=25)
        

        # these canvases are broken, fix them
        self.canvas_config = tk.Canvas(root, bg='pink', cursor= 'dot')
        self.canvas_config.place( x=50, y=130, width=250, height=149)
       

        self.canvas_config_1 = tk.Canvas(root, bg='white', cursor= 'circle')
        self.canvas_config_1.place( x=310, y=130, width=250, height=149)
        
        self.canvas_config_2 = tk.Canvas(root, bg='cyan')
        self.canvas_config_2.place( x=50, y=290, width=250, height=149)
        
        
        self.canvas_config_3 = tk.Canvas(root, bg= 'purple')
        self.canvas_config_3.place( x=310, y=290, width=250, height=149)
       
        
    def button1_command(self):
        filePath = fd.askopenfilename(initialdir='.')
        fileName = os.path.basename(filePath)
        self.label1["text"] = fileName  #changes "Label" to name of file
        try:
            self.__df = pd.read_csv(filePath)
            self.__df = self.__df.dropna()
            self.dropbox['values'] = list(self.__df['COMMUNITY AREA NAME'].unique())
        except:
            # quick and dirty, desired behavior would be to show a notification pop up that says
            # "nope!"
            #print('nope')
            self.popUp()
            
      def popUp(self): #function to create popup that says "nope!" in case of an exception
        global pop
        pop = Toplevel(root)
        pop.title("Exception!")
        pop.geometry("100x100")
        pop.config(bg="red")
        popLabel = Label(pop, text ="nope!", bg ="pink", fg="white")
        popLabel.pack(pady=10)
        my_frame = Frame(pop, bg = "white")
        my_frame(pady = 5)
            
     def __comboBoxCb(self, event=None):
        self.__subdf = self.__df.loc[self.__df['COMMUNITY AREA NAME'] == self.dropbox.get()]
        print(self.__subdf.head())
        fig1 = Figure(figsize=(self.canvas_config_2.winfo_width, self.canvas_config_2.winfo_height), dpi=100)
        ax1 = fig1.add_subplot(111)
        self.__subdf.iloc[:, range(self.__subdf.columns.get_loc['KWH JANUARY 2010'], 12)].mean().plot.bar(ax=ax1)
        
        
        
    # desired behavior: select one area, show 4 plots drawn on 4 canvases of that area: 
    # top left: bar chart, average KWH by month
    # top right: bar chart, average THERM by month
    # bottom left and bottom right up to you
    def chosen_kaupunki(self, event=None):
        chosen_kaupunki = self.__GListBox_563.get() 
        print(f"chosen_kaupunki: {chosen_kaupunki}")
        self.__subdf = self.__df.loc[self.__df['COMMUNITY AREA NAME'] == chosen_kaupunki]
        
        figure1 = plt.figure(figsize=(6,5),dpi=80)
        ax1 = figure1.add_subplot(111)
        bar1 = FigureCanvasTkAgg(figure1, root)
        bar1.get_tk_widget().place(x=50, y=130, width=250, height=155)
        kJanIndx = (self.__subdf.columns.get_loc('KWH JANUARY 2010'))
        print(kJanIndx)
        df1 = self.__subdf.iloc[:, range(kJanIndx, kJanIndx+12)].mean().plot.bar(ax=ax1)
        ax1.set_title('KWH avg')
        
        figure1 = plt.figure(figsize=(5,4),dpi=80)
        ax1 = figure1.add_subplot(111)
        bar1 = FigureCanvasTkAgg(figure1, root)
        bar1.get_tk_widget().place(x=310, y=130, width=250, height=155)
        kJanIndx = (self.__subdf.columns.get_loc('THERM JANUARY 2010'))
        print(kJanIndx)
        df1 = self.__subdf.iloc[:, range(kJanIndx, kJanIndx+12)].mean().plot.bar(ax=ax1)
        ax1.set_title('THERM avg') 
        
        figure1 = plt.figure(dpi=80)
        ax1 = figure1.add_subplot(111)
        bar1 = FigureCanvasTkAgg(figure1, root)
        bar1.get_tk_widget().place(x=50, y=295, width=250, height=155)
        kJanIndx = (self.__subdf.columns.get_loc('KWH JANUARY 2010'))
        print(kJanIndx)
        df1 = self.__subdf.iloc[:, range(kJanIndx, kJanIndx+12)].max().plot.bar(ax=ax1)
        ax1.set_title('KWHMaximal') 
        
        figure1 = plt.figure(dpi=80)
        ax1 = figure1.add_subplot(111)
        bar1 = FigureCanvasTkAgg(figure1, root)
        bar1.get_tk_widget().place(x=310, y=295, width=250, height=155)
        ThermFebIndx = (self.__subdf.columns.get_loc('THERM FEBRUARY 2010'))
        print(ThermFebIndx)
        df1 = self.__subdf.iloc[:, range(ThermFebIndx, ThermFebIndx+11)].max().plot.bar(ax=ax1)
        ax1.set_title('THERMmaximal')
        
       
            
            
        


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
