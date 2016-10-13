#gspread git: https://github.com/burnash/gspread
from Tkinter import *
import ttk
import tkFont
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']

credentials = ServiceAccountCredentials.from_json_keyfile_name('pi-spreadsheet-143506.json', scope)

gc = gspread.authorize(credentials)

focisheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/1037uq5DzMHd1U70a0YlkyrQyR3VwLp-8550KlKvIdvs/edit#gid=0')

bent = focisheet.get_worksheet(0)
kint = focisheet.get_worksheet(1)
katlan = focisheet.get_worksheet(2)
gollov = focisheet.get_worksheet(3)
lapok = focisheet.get_worksheet(4)

win = Tk()

win.geometry("8000x480")

def getWSNamefromId(wsNum):
    if wsNum == 1:
        return meccsek_bent[0][0]
    elif wsNum == 2:
        return meccsek_kint[0][0]
    elif wsNum == 3:
        return meccsek_katlan[0][0]
    else:
        return 'Error'

def maxWs(wsNum):
    if wsNum == 1:
        return bent_max
    elif wsNum == 2:
        return kint_max
    else:
        return katlan_max

def gNameShortener(gName):
    sGrName = ''
    if len(gName) <= 7:
        return gName

    else:
        sGrName += gName[:3]
        sGrName += '.'
        i = len(gName)-3
        j = len(gName)
        sGrName += gName[i:j]

        return sGrName

def exitProgram():
	print("Exit Button pressed")
	win.quit()
	#time.sleep(2)

def eredBeirKezdo():
	for widget in win.winfo_children():
		widget.destroy()

	print "Eredmeny beirasa"

	l = Label(win, text="Hol?", font=listFont)
	l.place(y=60, x=10, width = 150, height = 50)

	exitButt = Button(win, text = 'Exit', font = buttonFont, command = mainScreenLoad)
	exitButt.place(y = 300, x = 650, width = 100, height = 50)

	places = ["Tornacsarnok", "Kinti palya", "Katlan palya"]

	whereList = ttk.Combobox(win, font = listFont, height = 5, width = 25, values = places)
	whereList.place(y=67, x= 160)
	whereList.set('Allitsd be a helyszint!')

	psButt = Button(win, text = "OK", font = buttonFont, height = 2, width = 6, command = Self.Return(whereList.current()) )
	psButt.place(y = 200, x = 150, width = 100, height = 100)

def eredBeir(place):
	for widget in win.winfo_children():
			widget.destroy()

	win.title("Eredmenyek beirasa")

	cim = Label(win, text="Eredmenyek beirasa", font = cimFont)
	cim.pack(side = TOP)

	exitButt = Button(win, text = 'Exit', font = buttonFont, command = mainScreenLoad)
	exitButt.place(y = 300, x = 650, width = 100, height = 50)

	if place == 0:
		meccsList = bent.get_all_values()
	elif place == 1:
		meccsList = kint.get_all_values()
	else:
		meccsList = katlan.get_all_values()

	l = Label(win, text="Melyik meccs?", font=listFont)
	l.place(y=110, x=10, width = 150, height = 50)

	meccs = []
	i = 2
	for i in range(len(meccsList)):
		meccs[i-2] = meccsList[i][1] + ' vs ' + meccsList[i][2]
		i += 1 

	whoList = ttk.Combobox(win, font = listFont, height = 5, width = 25, values = meccs)
	whoList.place(y=117, x= 160)
	whoList.set('Allitsd be a helyszint!')

def mainScreenLoad():
	for widget in win.winfo_children():
			widget.destroy()

	print "Main screen"

	win.title("Main menu")

	cim = Label(win, text="Fomenu", font = cimFont)
	cim.pack(side = TOP)

	eredButt = Button(win, text = "Eredmeny\nbeirasa", font = buttonFont, command = eredBeirKezdo)
	eredButt.place(y = 60, x = 150, width = 170, height = 100)

	golButt = Button(win, text = "Gollovok\nbeirasa", font = buttonFont, height = 2, width = 6)
	golButt.place(y = 60, x = 450, width = 170, height = 100)

	psButt = Button(win, text = "Piros/sarga\n lap", font = buttonFont, height = 2, width = 6)
	psButt.place(y = 200, x = 150, width = 170, height = 100)

	exitButt = Button(win, text = "Exit", font = buttonFont, command = exitProgram, height = 2, width = 6)
	exitButt.place(y = 200, x = 450, width = 170, height = 100)

buttonFont = tkFont.Font(family = 'consolas', size = 20, weight = 'bold')
cimFont = tkFont.Font(family = 'consolas', size = 30, weight = 'bold')
listFont = tkFont.Font(family = 'consolas', size = 16)

#win.title("First gui")

#halihoButton = Button(win, text = "Haliho", font = buttonFont, command = exitProgram, height = 2, width = 6)
#halihoButton.pack(side = BOTTOM)

listaValues = ['Kill me!', 'Haliho', 'kex', 'fapapucs']
lista = ttk.Combobox(win, font = listFont, height = 5, width = 20, values = listaValues)
lista.set('Allitsd be a csapatot!')
lista.pack(side = TOP)

mainScreenLoad()

mainloop()