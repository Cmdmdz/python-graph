import json
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import pyplot as plt
import urllib.request as request

def main():
    root = Tk()
    # root.resizable(False, False)
    gui = Window(root)
    gui.root.mainloop()

    return None


# config api
url = 'https://opend.data.go.th/get-ckan/datastore_search?resource_id=219aa5a8-7621-4c63-85d3-64dd1914dff3'

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
        self.root.geometry('1440x880')
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

        figure = plt.figure(figsize=(14, 8), dpi=100)
        chart = FigureCanvasTkAgg(figure, self.root)
        chart.get_tk_widget().grid(row=5, column=0)

        imBaht = []
        exportBaht = []
        year = []

        imBaht1 = []
        exportBaht1 = []
        year1 = []

        for data in records:
            if data['year'] == 2021:
                year.append(data['month_name'])
                imBaht.append(data['import_baht'])
                exportBaht.append(data['export_baht'])
            elif data['year'] == 2022:
                year1.append(data['month_name'])
                imBaht1.append(data['import_baht'])
                exportBaht1.append(data['export_baht'])

        plt.ticklabel_format(style='plain', axis='y')
        plt.plot(year, imBaht, marker='o', label='Import 2021')
        plt.plot(year, exportBaht, marker='o', label='Export 2021')

        plt.plot(year1, imBaht1, marker='o', label='Import 2022')
        plt.plot(year1, exportBaht1, marker='o', label='Export 2022')

        plt.gcf().autofmt_xdate()

        plt.title('BAHT')
        plt.xlabel('MONTH')
        plt.ylabel('IMPORT BAHT : EXPORT BAHT')
        plt.tight_layout()
        plt.legend()

        return None

    # function plot graph us
    def plot_values_us(self):

        figure = plt.figure(figsize=(14, 8), dpi=100)
        chart = FigureCanvasTkAgg(figure, self.root)
        chart.get_tk_widget().grid(row=5, column=0)

        imBaht = []
        exportBaht = []
        year = []

        imBaht1 = []
        exportBaht1 = []
        year1 = []

        for data in records:
            if data['year'] == 2021:
                year.append(data['month_name'])
                imBaht.append(data['import_us'])
                exportBaht.append(data['export_us'])
            elif data['year'] == 2022:
                year1.append(data['month_name'])
                imBaht1.append(data['import_us'])
                exportBaht1.append(data['export_us'])

        plt.ticklabel_format(style='plain', axis='y')
        plt.plot(year, imBaht, marker='o', label='Import 2021')
        plt.plot(year, exportBaht, marker='o', label='Export 2021')

        plt.plot(year1, imBaht1, marker='o', label='Import 2022')
        plt.plot(year1, exportBaht1, marker='o', label='Export 2022')

        plt.gcf().autofmt_xdate()

        plt.title('US')
        plt.xlabel('MONTH')
        plt.ylabel('IMPORT US : EXPORT US')
        plt.tight_layout()
        plt.legend()

        return None

    pass


main()
