import json
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import pyplot as plt
import urllib.request as request
import pandas as pd
from datetime import datetime, timedelta


def main():
    root = Tk()
    root.resizable(False, False)
    gui = Window(root)
    gui.root.mainloop()

    return None


# config api
url = 'https://opend.data.go.th/get-ckan/datastore_search?limit=50&resource_id=219aa5a8-7621-4c63-85d3' \
      '-64dd1914dff3 '

# token api on service data
headers = {'api-key': 'L1jBiz9EWNRPXtsHy1IqVQvHrT0ZS5Yc'}
req = request.Request(url, None, headers)
fileObj = request.urlopen(req).read()
jsonData = json.loads(fileObj)
# get result data from api response
result = jsonData['result']
# get data records
records = result['records']


class Window:
    def __init__(self, root):
        self.root = root
        self.root.geometry('750x750')
        self.amplitude = 1
        self.frequency = 1
        self.vertical_shift = 0
        self.phase_shift = 0

        # button show baht
        btnShowBaht = Button(self.root, text="SHOW BAHT", width=10, command=self.bath)
        btnShowBaht.grid(row=6, column=0)
        self.root.bind("<Return>", self.bath)

        # button show us
        btnShowUs = Button(self.root, text="SHOW US", width=10, command=self.us)
        btnShowUs.grid(row=7, column=0)
        btnShowUs.size()
        self.root.bind("<Return>", self.us)

    # function show graph baht
    def bath(self):
        self.plot_values_baht()
        return plt.show()

    # function show graph us
    def us(self):
        self.plot_values_us()
        return plt.show()

    # function plot graph baht
    def plot_values_baht(self):

        figure = plt.figure(figsize=(6, 6), dpi=100)
        chart = FigureCanvasTkAgg(figure, self.root)
        chart.get_tk_widget().grid(row=5, column=0)

        imBaht = []
        exportBaht = []
        year = []

        for data in records:
            year.append(data['year'])
            imBaht.append(data['import_baht'])
            exportBaht.append(data['export_baht'])

        plt.plot(year, imBaht, marker='o', label='Import BAHT')
        plt.plot(year, exportBaht, marker='o', label='Export BAHT')

        plt.ticklabel_format(useOffset=False)
        plt.title('BAHT')
        plt.xlabel('year')
        plt.ylabel('import baht , export baht')
        plt.tight_layout()
        plt.legend()
        return None

    # function plot graph us
    def plot_values_us(self):

        # laouts graph
        figure = plt.figure(figsize=(6, 6), dpi=100)
        chart = FigureCanvasTkAgg(figure, self.root)
        chart.get_tk_widget().grid(row=5, column=0)

        imUs = []
        exportUs = []
        year = []

        # loob add data to array from records api.
        for data in records:
            year.append(data["year"])
            imUs.append(data['import_us'])
            exportUs.append(data['export_us'])

        plt.plot(year, imUs, marker='o', label='Import US')
        plt.plot(year, exportUs, marker='o', label='Export US')

        plt.ticklabel_format(useOffset=False)
        plt.title('US')
        plt.xlabel('year')
        plt.ylabel('import us , export us')
        plt.tight_layout()
        plt.legend()
        return None

    pass


main()
