#gspread git: https://github.com/burnash/gspread

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time
import Adafruit_CharLCD as LCD

lcd = LCD.Adafruit_CharLCDPlate()

scope = ['https://spreadsheets.google.com/feeds']

credentials = ServiceAccountCredentials.from_json_keyfile_name('pi-spreadsheet-143506.json', scope)

gc = gspread.authorize(credentials)

focisheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/1037uq5DzMHd1U70a0YlkyrQyR3VwLp-8550KlKvIdvs/edit#gid=0')

bent = focisheet.get_worksheet(0)
kint = focisheet.get_worksheet(1)
katlan = focisheet.get_worksheet(2)

lcd.create_char(1, [31, 21, 10, 4, 4, 10, 17, 31])
lcd.create_char(2, [31, 17, 14, 4, 4, 10, 17, 31])
lcd.create_char(3, [31, 17, 10, 4, 4, 14, 17, 31])
lcd.create_char(4, [31, 17, 10, 4, 4, 10, 21, 31])

lcd.create_char(5, [0, 0, 0, 4, 31, 4, 0, 0])

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

def scrollName(gName, i):
    if len(gName) <= 7:
        return gName
    else:
        return gName[i:i+6]

#print eredmenyek.acell('A1').value

#Cellak szamozasa a listaban 0rol indul, Row, Column formatumban
#Cella szamozasa drivebol 1-rol indul Row, Column formatumban

#print meccsek[2][1]
#bent.update_cell(3, 4, '2:3')

meccsek_bent = bent.get_all_values()
meccsek_kint = kint.get_all_values()
meccsek_katlan = katlan.get_all_values()

print 'asd' + meccsek_bent[10][1] + 'asd'

print 'meccsek bent'

bent_max = len(meccsek_bent)

print 'kint'
kint_max = len(meccsek_kint)
katlan_max = len(meccsek_katlan)

last_update = time.time()

ws_num = 1
game_num = 1

ws_change = True
game_change = True

lcd.message('asd')

while True:
    #10percenkent adatbazis frissitese
    if (time.time()-last_update) >= 600:
        try:
            lcd.clear()
            lcd.message("Adatbazis\nfrissitese")
            meccsek_bent = bent.get_all_values()
            meccsek_kint = kint.get_all_values()
            meccsek_katlan = katlan.get_all_values()

            print 'meccsek bent'

            bent_max = len(meccsek_bent)

            print 'kint'
            kint_max = len(meccsek_kint)
            katlan_max = len(meccsek_katlan)

        except:
            lcd.clear()
            lcd.message('Network error\ntry again later')

        last_update = time.time()

        game_num = 1
        gameNum_change = True

        ws_num = 1
        ws_change = True

    if lcd.is_pressed(LCD.RIGHT):
        if ws_num < 3:
            ws_num += 1
        else:
            ws_num = 1
        print str(ws_num)

        ws_change = True
    elif lcd.is_pressed(LCD.LEFT):
        if ws_num > 1:
            ws_num -= 1
        else:
            ws_num = 3
        print str(ws_num)

        ws_change = True
    elif lcd.is_pressed(LCD.DOWN):
        if game_num < maxWs(ws_num):
            game_num += 1
        else:
            game_num = maxWs(ws_num)

        gameNum_change = True

    elif lcd.is_pressed(LCD.UP):
        if game_num > 1:
            game_num -= 1
        else:
            game_num = 1

        gameNum_change = True

    elif lcd.is_pressed(LCD.SELECT):
        if csapat1 == '-':
            lcd.clear()
            lcd.message("Ez nem egy meccs")

            time.sleep(2)
        else:
            lcd.clear()
            lcd.message(gNameShortener(csapat1))
            lcd.message('\x05')
            lcd.message(gNameShortener(csapat2))

            time.sleep(0.3)

            g1Point = 0
            g2Point = 0

            lcd.set_cursor(1,1)
            lcd.blink(True)
            group = 1
            groupChange = True

            while not lcd.is_pressed(LCD.SELECT):
                lcd.set_cursor(1,1)
                if lcd.is_pressed(LCD.RIGHT):
                    lcd.set_cursor(14,1)
                    group = 2
                elif lcd.is_pressed(LCD.LEFT):
                    lcd.set_cursor(1,1)
                    group = 1
                elif lcd.is_pressed(LCD.UP):
                    if group == 1:
                        g1Point += 1
                    else:
                        g2Point += 1

                    groupChange = True
                elif lcd.is_pressed(LCD.DOWN):
                    if group == 1:
                        if g1Point != 0:
                            g1Point -= 1
                        else:
                            g1Point = 0
                    else:
                        if g2Point != 0:
                            g2Point -= 1
                        else:
                            g2Point = 0

                    groupChange = True
                else:
                    groupChange = False

                if groupChange:
                    lcd.set_cursor(1,1)
                    lcd.message('                ')
                    lcd.set_cursor(1,1)
                    lcd.message(str(g1Point) + '       ' + str(g2Point))

                    if group == 1:
                        lcd.set_cursor(1,1)
                    else:
                        lcd.set_cursor(9,1)

                    groupChange = False

                time.sleep(0.15)

            lcd.blink(False)

            lcd.clear()
            lcd.message('Adatok \nfeltoltese')

            try:
                if ws_num == 1:
                    bent.update_cell(game_num + 2, 4, str(g1Point) + ':' + str(g2Point))
                elif ws_num == 2:
                    kint.update_cell(game_num + 2, 4, str(g1Point) + ':' + str(g2Point))
                else:
                    katlan.update_cell(game_num + 2, 4, str(g1Point) + ':' + str(g2Point))
            except:
                lcd.clear()
                lcd.message('Network error\ntry again later')

        game_num = 1
        gameNum_change = True

        ws_num = 1
        ws_change = True

        time.sleep(0.2)

    if ws_change:
        game_num = 1
        gameNum_change = True

        print getWSNamefromId(ws_num)
        lcd.set_cursor(0,0)
        lcd.message('                ')
        lcd.set_cursor(0,0)
        lcd.message(getWSNamefromId(ws_num))
        ws_change = False

    if gameNum_change:
        if ws_num == 1:
            csapat1 = meccsek_bent[game_num+1][1]
            csapat2 = meccsek_bent[game_num+1][2]

            idopont = meccsek_bent[game_num+1][4]

        elif ws_num == 2:
            csapat1 = meccsek_kint[game_num+1][1]
            csapat2 = meccsek_kint[game_num+1][2]

            idopont = meccsek_bent[game_num+1][4]
        else:
            csapat1 = meccsek_katlan[game_num+1][1]
            csapat2 = meccsek_katlan[game_num+1][2]

            idopont = meccsek_bent[game_num+1][4]

        lcd.set_cursor(11, 0)
        lcd.message(idopont)

        lcd.set_cursor(0, 1)
        lcd.message('                ')
        lcd.set_cursor(0, 1)
        lcd.message(gNameShortener(csapat1) + '\x05' + gNameShortener(csapat2))

        gameNum_change = False