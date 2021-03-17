import feedparser
import webbrowser
from tkinter import Tk, ttk, Listbox


class TkHref(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.state = ('zoomed')
        self.t2l = dict()
        self.urls = {
            'Top News': 'http://www.moneycontrol.com/rss/MCtopnews.xml',
            'Latest News': 'http://www.moneycontrol.com/rss/latestnews.xml',
            'Most Popular': 'http://www.moneycontrol.com/rss/MCtopnews.xml',
            'Business News': 'http://www.moneycontrol.com/rss/MCtopnews.xml',
            'Brokerage Recommendations': 'http://www.moneycontrol.com/rss/brokeragerecos.xml',
            'Buzzing Stocks': 'http://www.moneycontrol.com/rss/buzzingstocks.xml',
            'Market Reports': 'http://www.moneycontrol.com/rss/marketreports.xml',
            'Global News': 'http://www.moneycontrol.com/rss/internationalmarkets.xml',
            'Market Edge': 'http://www.moneycontrol.com/rss/marketedge.xml',
            'Technicals': 'http://www.moneycontrol.com/rss/technicals.xml',
            'Results': 'http://www.moneycontrol.com/rss/results.xml'
        }

        self.l01 = ttk.Label(self, text='Hyperlinks in Tkinter')
        self.h01 = ttk.Separator(self, orient='horizontal')
        self.c01 = ttk.Combobox(self, values=[*self.urls.keys()])
        self.b01 = ttk.Button(self, text='Get News', command=self.fetch)
        self.lb0 = Listbox(self, foreground='blue', width=80, height=15)
        self.lb0.bind('<<ListboxSelect>>', self.selected)

        self.l01.grid(row=0, column=0, columnspan=2)
        self.h01.grid(row=1, column=0, columnspan=2, sticky='ew')
        self.c01.grid(row=2, column=0)
        self.b01.grid(row=2, column=1)
        self.lb0.grid(row=3, column=0, columnspan=2, sticky='ew')

    def fetch(self):
        try:
            f = feedparser.parse(self.urls[self.c01.get()])
            for i in f.entries:
                self.t2l[i.title] = i.link
                self.lb0.insert('end', i.title)

        except Exception as e:
            print(e)

    def selected(self, something):
        print(something)
        webbrowser.open_new(self.t2l[self.lb0.get(self.lb0.curselection())])


if __name__ == '__main__':
    app = TkHref()
    app.mainloop()
