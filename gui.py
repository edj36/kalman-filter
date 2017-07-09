import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import tkinter as tk
from tkinter import messagebox as tkMessageBox
from tkinter import filedialog as tkFileDialog
import datetime
from pandas_datareader import data, wb
import numpy as np
import pandas as pd
import kalman

class MainApp(tk.Frame):

    

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.parent.title('DSP FILTER MACHINE')
        self.buttons()
        self.draw([],[],[],'')
        

    ### OK button
    def buttons(self):
        stockVar.set('STOCK')
        stockOptions = tk.OptionMenu(self, stockVar, 'GOOG', 'AAPL', 'BX', 'GS')
        stockOptions.grid(column=4, row=5, sticky='nesw')

        startMonthVar.set('START MM')
        startMonth = tk.OptionMenu(self, startMonthVar, '01','02','03','04',
                                                        '05','06','07','08',
                                                        '09','10','11','12')
        startMonth.grid(column=1, row=5, sticky='nesw')

        startDateVar.set('START DD')
        startDate = tk.OptionMenu(self, startDateVar, '01','02','03','04',
                                                        '05','06','07','08',
                                                        '09','10','11','12',
                                                        '13','14','15','16',
                                                        '17','18','19','20',
                                                        '21','22','23','24',
                                                        '25','26','27','28',
                                                        '29','30','31')
        startDate.grid(column=2, row=5, sticky='nesw')

        startYearVar.set('START YYYY')
        startYear = tk.OptionMenu(self, startYearVar, '2007','2008','2009',
                                                '2010','2011','2012','2013',
                                                '2014','2015','2016','2017')
        startYear.grid(column=3, row=5, sticky='nesw')
        
        endMonthVar.set('END MM')
        endMonth = tk.OptionMenu(self, endMonthVar, '01','02','03','04',
                                                    '05','06','07','08',
                                                    '09','10','11','12')
        endMonth.grid(column=1, row=6, sticky='nesw')

        endDayVar.set('END DD')
        endDay = tk.OptionMenu(self, endDayVar, '01','02','03','04','05','06',
                                                '07','08','09','10','11','12',
                                                '13','14','15','16','17','18',
                                                '19','20','21','22','23','24',
                                                '25','26','27','28','29','30','31')
        endDay.grid(column=2, row=6, sticky='nesw')

        endYearVar.set('END YYYY')
        endYear = tk.OptionMenu(self, endYearVar, '2007','2008','2009','2010',
                                                    '2011','2012','2013','2014',
                                                    '2015','2016','2017')
        endYear.grid(column=3, row=6, sticky='nesw')
        
        self.processButton = tk.Button(self, text='PROCESS', command=self.processButtonClick)
        self.processButton.grid(column=4, row=6, sticky='nesw')


    def processButtonClick(self):
        stock_ticker = stockVar.get()
        start_mm = startMonthVar.get()
        start_dd = startDateVar.get()
        start_yy = startYearVar.get()
        end_mm = endMonthVar.get()
        end_dd = endDayVar.get()
        end_yy = endYearVar.get()
        if stock_ticker == 'STOCK' or start_mm == 'START MM' or start_dd == 'START DD' or start_yy == 'START YYYY' or end_mm == 'END MM' or end_dd == 'END DD' or end_yy == 'END YYYY':
            tkMessageBox.showinfo("ERROR", "You need to choose a value for each option")

        start = datetime.datetime(int(start_yy), int(start_mm), int(start_dd))
        end = datetime.datetime(int(end_yy), int(end_mm), int(end_dd))
        stock = data.DataReader(stock_ticker, 'google', start, end)
        close_price = stock.get('Close')
        kalman_filtered = kalman.kalman_filter(stock)
        self.draw(np.array(close_price.axes)[0],np.array(close_price),kalman_filtered,stock_ticker)

    def draw(self,x,y,k,name):
        self.f = Figure(figsize=(8,5))
        self.a = self.f.add_subplot(111)
        self.a.plot(x,y,label='data')
        self.a.plot(x,k,label='filter')
        self.a.set_title(name)
        self.a.set_xlabel('DATE')
        self.a.set_ylabel('PRICE')
        self.a.legend()
        self.canvas = FigureCanvasTkAgg(self.f, master=self)
        self.canvas.get_tk_widget().grid(column=1,columnspan=4, row=1, rowspan=4, sticky="nesw")

if __name__ == "__main__":
    root = tk.Tk()
    stockVar = tk.StringVar()
    startMonthVar = tk.StringVar()
    startDateVar = tk.StringVar()
    startYearVar = tk.StringVar()
    endMonthVar = tk.StringVar()
    endDayVar = tk.StringVar()
    endYearVar = tk.StringVar()
    root.geometry("960x720+10+10")
    root.resizable(0, 0)
    MainApp(root).pack()
    root.mainloop()
