import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
import tkinter.font as tkFont

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.pyplot import figure, Figure 

#sources: 

class App:
    def __init__(self, root):
        # setting title
        root.title("CSV Graphical user interface")
        # setting window size
        width = 600
        height = 600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.__GButton_450 = tk.Button(root)
        self.__GButton_450["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        self.__GButton_450["font"] = ft
        self.__GButton_450["fg"] = "#000000"
        self.__GButton_450["justify"] = "center"
        self.__GButton_450["text"] = "Button"
        self.__GButton_450.place(x=70, y=50, width=70, height=25)
        self.__GButton_450["command"] = self.__GButton_450_command

        self.__GListBox_563 = ttk.Combobox(root)
        self.__GListBox_563.place(x=350, y=50, width=80, height=25)
        self.__GListBox_563.bind("<<ComboboxSelected>>", self.chosen_kaupunki)

        self.__GLabel_544 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        self.__GLabel_544["font"] = ft
        self.__GLabel_544["fg"] = "#333333"
        self.__GLabel_544["justify"] = "center"
        self.__GLabel_544["text"] = "label"
        self.__GLabel_544.place(x=150, y=50, width=70, height=25)
        
  # buttonconfig for frame source: https://www.activestate.com/resources/quick-reads/how-to-use-pack-in-tkinter/
        #self.buttonconfig = tk.Frame(root) 
        #self.buttonconfig.pack(ipadx=15, ipady=20)
        
        #chartconig for chart frame, frame = neatness 
        #self.chartconfig = tk.Frame(root) 
        #self.chartconfig.pack(side=tk.BOTTOM, padx=6, pady=7)

        # these canvases are broken, fix them
        self.canvas_config = tk.Canvas(root, bg='pink', cursor= 'dot')
        self.canvas_config.place( x=50, y=130, width=250, height=149)
       

        self.canvas_config_1 = tk.Canvas(root, bg='white', cursor= 'circle')
        self.canvas_config_1.place( x=310, y=130, width=250, height=149)
        
        self.canvas_config_2 = tk.Canvas(root, bg='cyan')
        self.canvas_config_2.place( x=50, y=290, width=250, height=149)
        
        
        self.canvas_config_3 = tk.Canvas(root, bg= 'purple')
        self.canvas_config_3.place( x=310, y=290, width=250, height=149)
       
        
    def __GButton_450_command(self):
        filePath = fd.askopenfilename(initialdir='.')
        try:
            self.__df = pd.read_csv(filePath)
            self.__df = self.__df.dropna()
            self.__GListBox_563['values'] = list(self.__df['COMMUNITY AREA NAME'].unique())
        except:
            # quick and dirty, desired behavior would be to show a notification pop up that says
            # "nope!"
            print('nope')

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
        
       
            
            
        


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()