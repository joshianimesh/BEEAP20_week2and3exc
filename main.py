import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
import tkinter.font as tkFont

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

#sources: 

class App:
    def __init__(self, root):
        # setting title
        root.title("CSV Graphical user interface")
        # setting window size
        width = 600
        height = 500
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
        self.buttonconfig = tk.Frame(root) 
        self.buttonconfig.pack(ipadx=15, ipady=20)
        
        #chartconig for chart frame, frame = neatness 
        self.chartconfig = tk.Frame(root) 
        self.chartconfig.pack(side=tk.BOTTOM, padx=6, pady=7)

        # these canvases are broken, fix them
        self.canvas_config = tk.Canvas(self.chartconfig, cursor = 'dot')
        self.canvas_config.place( relx=0, rely=0, relwidth=0.6, height=0.6)
        self.canvas_config.update() 
        self.fig1 = figure(figsize=(      self.canvas_config.winfo_width() / 100, self.canvas_config.winfo_height() /100   ), dpi=100)
        self.ax1 = self.fig1.add_subplot(111)
        self.chart1 = FigureCanvasTkAgg(self.fig1, self.canvas_config )

        self.canvas_config_1 = tk.Canvas(root, bg = 'white', cursor = 'circle')
        self.canvas_config_1.place( x=310, y=130, width=235, height=142)

        self.canvas_config_2 = tk.Canvas(root, bg = 'cyan')
        self.canvas_config_2.place( x=50, y=290, width=235, height=142)

        self.canvas_config_3 = tk.Canvas(root, )
        self.canvas_config_3.place( x=310, y=290, width=235, height=142)

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
        self.subdf = self.__df.loc[self.__df['COMMUNITY AREA NAME'] == chosen_kaupunki]
        
        def northwest(self):
            
            self.chart1.get_tk_widget().pack(side=tk.BOTTOM,fill=tk.BOTH,expand=True)
            self.ax1.clear()
            janind = self.__subdf.columns.get_loc("KWH JANUARY 2010")
            self.ax1.bar(     range(1, 13),
                    (self.__subdf.iloc[ : ,  range(janind, (janind + 12))  ]).mean()     )
            self.chart1.draw()

        def northeast(self):
          
            self.chart2.get_tk_widget().pack(side=tk.BOTTOM,fill=tk.BOTH,expand=True)
            self.ax2.clear()
            janind = self.__subdf.columns.get_loc("THERM JANUARY 2010")
            self.ax2.bar(    range(1, 13),
                    (self.__subdf.iloc[ : ,  range(janind, (janind + 12))  ]).mean()     )
            self.chart2.draw()
        
        def southwest(self):
          
            self.chart3.get_tk_widget().pack(side=tk.BOTTOM,fill=tk.BOTH,expand=True)
            self.ax3.clear()
            janind = self.__subdf.columns.get_loc("KWH JANUARY 2010")
            self.ax3.plot(     range(1, 13),
                    (self.__subdf.iloc[ : ,  range(janind, (janind + 12))  ]).max(),
                    color='red', marker ='*'    )
            self.ax3.plot(     range(1, 13),
                    (self.__subdf.iloc[ : ,  range(janind, (janind + 12))  ]).mean(),
                    color='blue', marker ='s'    )
            self.chart3.draw()
        
        def southeast(self):   
            self.chart4.get_tk_widget().pack(side=tk.BOTTOM,fill=tk.BOTH,expand=True)
            self.ax4.clear()
            janind = self.__subdf.columns.get_loc("THERM JANUARY 2010")
            self.ax4.plot(     range(1, 13),
                    (self.__subdf.iloc[ : ,  range(janind, (janind + 12))  ]).max(),
                    color='red', marker ='*'    )
            self.ax4.plot(     range(1, 13),
                    (self.__subdf.iloc[ : ,  range(janind, (janind + 12))  ]).mean(),
                    color='blue', marker ='s'    )
            self.chart4.draw()
            
            
            
        northeast(self)
        northwest(self)
        southeast(self)
        southwest(self)

        


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
