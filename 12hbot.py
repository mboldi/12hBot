#gspread git: https://github.com/burnash/gspread

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time
import Adafruit_CharLCD as LCD

lcd = LCD.Adafruit_CharLCDPlate()

scope = ['https://spreadsheets.google.com/feeds']

credentials = ServiceAccountCredentials.from_json_keyfile_name('pi-spreadsheet-143506.json', scope)

gc = gspread.authorize(credentials)

leltar = gc.open_by_url('https://docs.google.com/spreadsheets/d/1037uq5DzMHd1U70a0YlkyrQyR3VwLp-8550KlKvIdvs/edit#gid=0')

eredmenyek = leltar.get_worksheet(0)

lcd.create_char(1, [31, 21, 10, 4, 4, 10, 17, 31])
lcd.create_char(2, [31, 17, 14, 4, 4, 10, 17, 31])
lcd.create_char(3, [31, 17, 10, 4, 4, 14, 17, 31])
lcd.create_char(4, [31, 17, 10, 4, 4, 10, 21, 31])

def load():
	lcd.clear()
	lcd.message('\x01')
	time.sleep(0.5)
	lcd.clear()
	lcd.message('\x02')
	time.sleep(0.5)
	lcd.clear()
	lcd.message('\x03')
	time.sleep(0.5)
	lcd.clear()
	lcd.message('\x04')


#print eredmenyek.acell('A1').value

meccsek = eredmenyek.get_all_values()

print meccsek[2][1]
eredmenyek.update_cell(3, 4, '2:3')

