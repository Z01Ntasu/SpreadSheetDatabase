import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('Spreadsheet-3137bb02fb48.json',scope)

gc = gspread.authorize(credentials)

wks = gc.open('testin table').sheet1
run = True
while run:
	option = input("1.Person erstellen \n2.Person suchen\n3.Programm verlassen\n")
	if  option == "1":
		cell = wks.find("next")
		wks.update_cell(cell.row, cell.col,input("Name?\n") )
		wks.update_cell(cell.row+1, cell.col, input("Nachname?\n"))
		wks.update_cell(cell.row+2, cell.col, input("Alter?\n"))
		wks.update_cell(cell.row+3, cell.col, input("Beruf?\n"))
		wks.update_cell(cell.row, cell.col+1, 'next')
	elif option == "2":
		cell = wks.find(input("Gebe den Vor oder nachnamen ein\n"))
		print("Vorname : ",cell.value)
		print("Nachname : ",wks.cell(cell.row+1, cell.col).value)
		print("Alter : ",wks.cell(cell.row+2, cell.col).value)
		print("Beruf : ",wks.cell(cell.row+3, cell.col).value)
	else:
		run = False
	










#print(wks.get_all_records())
#wks.append_row(['waaaaaaaaa','weeeeeee'])

#print(wks.col_values(1))
#print(wks.cell(1,1).value)