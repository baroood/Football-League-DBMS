import MySQLdb
Employee_ID = 1
Stadium_ID = 1
Club_ID =1


db=MySQLdb.connect('localhost','root','12345678','Football_League')
cursor = db.cursor()
cursor.execute("""SELECT MAX(Employee_ID) FROM Employee;""")
L=cursor.rowcount
Exists = cursor.fetchall()
cursor.close()
if  int(L)>0:
	for i in Exists:
		Employee_ID = i[0];
else:
	Employee_ID=1


cursor = db.cursor()
cursor.execute("""SELECT MAX(Stadium_ID) FROM Stadiums;""")
L=cursor.rowcount
Exists = cursor.fetchall()
cursor.close()
if  int(L)>0:
	for i in Exists:
		Stadium_ID = i[0];
else:
	Stadium_ID=1


cursor = db.cursor()
cursor.execute("""SELECT MAX(Club_ID) FROM Clubs;""")
L=cursor.rowcount
Exists = cursor.fetchall()
cursor.close()
if  int(L)>0:
	for i in Exists:
		Club_ID = i[0];
else:
	Club_ID=1


def newemployee():
	global Employee_ID
	Employee_ID=Employee_ID+1
	true=0
	db=MySQLdb.connect('localhost','root','12345678','Football_League')
	print("1: Player")
	print("2: Manager")
	print("3: Coach")
	choice = int(input("Enter your choice: "))
	if choice>0 and choice<4:
		First_Name = raw_input('Enter Employee First Name: ')
		Last_Name =raw_input('Enter Employee Last Name: ')
		Salary = raw_input('Enter Salary: ')
		Club_ID_E = raw_input('Enter Club ID :')
	cursor = db.cursor()
	cursor.execute("""SELECT Club_ID FROM Clubs;""")
	l=cursor.rowcount
	exists = cursor.fetchall()
	cursor.close()
	if  int(l)>0:
		for i in exists:
			if i[0] == int(Club_ID_E,10):
				true=1
				break
	if true != 1 and choice>0 and choice<4:
		print("Club Selected Doesn't Exist")
	elif choice == 1:
		Goals=0
		Assists=0
		Tackles=0
		Posotion = raw_input('Enter Player position :')
		try:
			cursor = db.cursor()
			cursor.execute("""INSERT INTO Employee VALUES (%s,%s,%s,%s,%s);""",(Employee_ID,First_Name,Last_Name,Salary,Club_ID_E,))
			cursor.execute("""INSERT INTO Players VALUES (%s,%s,%s,%s,%s);""",(Employee_ID,Goals,Assists,Tackles,Posotion,))
			db.commit()
			print("Added New Player")
			cursor.close()
		except:
			print("Could Not Add To DataBase : Error In Input")
	   		db.rollback()
		db.close()
	elif choice == 2:
		try:
			cursor = db.cursor()
			cursor.execute("""INSERT INTO Employee VALUES (%s,%s,%s,%s,%s);""",(Employee_ID,First_Name,Last_Name,Salary,Club_ID_E,))
			cursor.execute("""INSERT INTO Managers VALUES (%s);""",(Employee_ID,))
			db.commit()
			print("Added New Manger")
			cursor.close()
		except:
	   		print("Could Not Add To DataBase : Error In Input")
	   		db.rollback()
		db.close()
	elif choice == 3:
		try:
			cursor = db.cursor()
			cursor.execute("""INSERT INTO Employee VALUES (%s,%s,%s,%s,%s);""",(Employee_ID,First_Name,Last_Name,Salary,Club_ID_E,))
			cursor.execute("""INSERT INTO Coaches VALUES (%s);""",(Employee_ID,))
			db.commit()
			print("Added New Coach")
			cursor.close()
		except:
	   		print("Could Not Add To DataBase : Error In Input")
	   		db.rollback()
		db.close()
	else:
		print("Wrong Option Selected")
		db.close()
def newclub():
	global Stadium_ID
	global Club_ID
	Club_ID=Club_ID+1
	Stadium_ID=Stadium_ID+1
	Games_Won=0
	Games_Lost=0
	db=MySQLdb.connect('localhost','root','12345678','Football_League')
	Club_Name = raw_input('Enter Club Name: ')
	Stadium_Name = raw_input('Enter Stadium Name: ')
	Capacity = raw_input('Enter Stadium Capacity :')
	Location = raw_input('Enter Stadium Location :')
	No_Of_Fans = 0
	No_Of_Fan_Clubs = 0
	try:
		cursor = db.cursor()
		cursor.execute("""INSERT INTO Stadiums VALUES (%s,%s,%s,%s);""",(Stadium_ID,Stadium_Name,Location,Capacity))
		cursor.execute("""INSERT INTO Clubs VALUES (%s,%s,%s,%s,%s);""",(Club_ID,Club_Name,Stadium_ID,Games_Won,Games_Lost))
		cursor.execute("""INSERT INTO Fans VALUES (%s,%s,%s);""",(Club_Name,No_Of_Fans,No_Of_Fan_Clubs))
		db.commit()
		cursor.close()
		print("Added New Club With Stadium")
	except:
		print("Could Not Add To DataBase : Error In Input")
		db.rollback()
	db.close()

def newtournament():
	db=MySQLdb.connect('localhost','root','12345678','Football_League')
	Tournament_Name = raw_input('Enter Tournament Name: ')
	No_Of_Clubs = 0
	Prize_Pool = raw_input('Enter Prize Pool :')
	Duration = raw_input('Enter Duration(in days) :')
	try:
		cursor = db.cursor()
		cursor.execute("""INSERT INTO Tournaments VALUES (%s,%s,%s,%s);""",(Tournament_Name,No_Of_Clubs,Prize_Pool,Duration))
		db.commit()
		cursor.close()
		print("Added New Tournament")
	except:
		print("Could Not Add To DataBase : Error In Input")
		db.rollback()
	db.close()

def club_tour_add():
	db=MySQLdb.connect('localhost','root','12345678','Football_League')
	true =0
	true2 =0
	Club_ID_E = raw_input('Enter Club ID: ')
	Tournaments_Played = raw_input('Enter Tournament Playing: ')
	cursor = db.cursor()
	cursor.execute("""SELECT Club_ID FROM Clubs;""")
	l=cursor.rowcount
	exists = cursor.fetchall()
	cursor.close()
	cursor = db.cursor()
	cursor.execute("""SELECT Tournament_Name FROM Tournaments;""")
	l2=cursor.rowcount
	exists2 = cursor.fetchall()
	cursor.close()
	if int(l)>0:
		for i in exists:
			try:
				if i[0] == int(Club_ID_E,10):
					true=1
					break
			except:
				true=5
	if int(l2)>0:
		for i in exists2:
			if i[0] == Tournaments_Played:
				true2=1
				break
	if true != 1 :
		print('Club does not exist')
	elif true2 == 0:
		print('Tournament does not exist')
	else:
		try:
			cursor = db.cursor()
			cursor.execute("""SELECT No_Of_Clubs FROM Tournaments WHERE Tournament_Name=%s;""",(Tournaments_Played,))
			l1=cursor.rowcount
			exists1 = cursor.fetchall()
			cursor.close()
			if int(l1) > 0:
				for i in exists1:
					Tour_no_of_clubs_val=i[0]+1
			cursor = db.cursor()
			cursor.execute("""UPDATE Tournaments SET No_Of_Clubs = %s WHERE Tournament_Name = %s;""", (Tour_no_of_clubs_val, Tournaments_Played,))
			cursor.execute("""INSERT INTO Tournaments_Played VALUES (%s,%s);""",(Club_ID_E, Tournaments_Played,))
			db.commit()
			cursor.close()
			print("Club has joined Tournament")
		except:
			print("Could Not Add To DataBase : Error In Input")
			db.rollback()
	db.close()
def delete_emp():
	true=0
	db=MySQLdb.connect('localhost','root','12345678','Football_League')
	print("1: Player")
	print("2: Manager")
	print("3: Coach")
	choice = int(input("Enter your choice: "))
	if choice>0 and choice<4:
		Employee_ID_E = raw_input('Enter Employee ID: ')
	if choice == 1:
		cursor = db.cursor()
		cursor.execute("""SELECT Employee_ID FROM Players;""")
		l=cursor.rowcount
		exists = cursor.fetchall()
		cursor.close()
		if  int(l)>0:
			for i in exists:
				if i[0] == int(Employee_ID_E,10):
					true=1
					break

		if true != 1 and choice>0 and choice<4:
			print("Player does not Exist")
		else:
			try:
				cursor = db.cursor()
				cursor.execute("""DELETE FROM Players WHERE Employee_ID = %s;""",(Employee_ID_E,))
				cursor.execute("""DELETE FROM Employee WHERE Employee_ID = %s;""",(Employee_ID_E,))
				db.commit()
				print("Deleted a Player")
				cursor.close()
			except:
				print("Could Not Add To DataBase : Error In Input")
		   		db.rollback()
		db.close()
	elif choice == 2:
		cursor = db.cursor()
		cursor.execute("""SELECT Employee_ID FROM Managers;""")
		l=cursor.rowcount
		exists = cursor.fetchall()
		cursor.close()
		if  int(l)>0:
			for i in exists:
				if i[0] == int(Employee_ID_E,10):
					true=1
					break

		if true != 1 and choice>0 and choice<4:
			print("Manager does not Exist")
		else:
			try:
				cursor = db.cursor()
				cursor.execute("""DELETE FROM Managers WHERE Employee_ID = %s;""",(Employee_ID_E,))
				cursor.execute("""DELETE FROM Employee WHERE Employee_ID = %s;""",(Employee_ID_E,))
				db.commit()
				print("Deleted a Manager")
				cursor.close()
			except:
				print("Could Not Add To DataBase : Error In Input")
		   		db.rollback()
		db.close()
	elif choice == 3:
		cursor = db.cursor()
		cursor.execute("""SELECT Employee_ID FROM Coaches;""")
		l=cursor.rowcount
		exists = cursor.fetchall()
		cursor.close()
		if  int(l)>0:
			for i in exists:
				if i[0] == int(Employee_ID_E,10):
					true=1
					break

		if true != 1 and choice>0 and choice<4:
			print("Coach does not Exist")
		else:
			try:
				cursor = db.cursor()
				cursor.execute("""DELETE FROM Coaches WHERE Employee_ID = %s;""",(Employee_ID_E,))
				cursor.execute("""DELETE FROM Employee WHERE Employee_ID = %s;""",(Employee_ID_E,))
				db.commit()
				print("Deleted a Coach")
				cursor.close()
			except:
				print("Could Not Add To DataBase : Error In Input")
		   		db.rollback()
		db.close()
	else:
		print("Sorry Wrong Option")
		db.close()
def deleteclub():
	true=0
	db=MySQLdb.connect('localhost','root','12345678','Football_League')
	Club_ID_E = raw_input('Enter Club ID: ')
	cursor = db.cursor()
	cursor.execute("""SELECT Club_ID FROM Clubs;""")
	l=cursor.rowcount
	exists = cursor.fetchall()
	cursor.close()


	cursor = db.cursor()
	cursor.execute("""SELECT Club_Name FROM Clubs WHERE Club_ID = %s;""",(Club_ID_E,))
	name2 = cursor.fetchall()
	cursor.close()


	cursor = db.cursor()
	cursor.execute("""SELECT Stadium_ID FROM Clubs WHERE Club_ID = %s;""",(Club_ID_E,))
	std_id = cursor.fetchall()
	cursor.close()


	for i in exists:
		if i[0] == int(Club_ID_E,10):
			true=1
			break
	if true == 1:
		for i in name2:
			club_nm=i[0]

	if true == 1:
		for i in std_id:
			stadium_id_temp=i[0]
	
	if true != 1:
			print("Club does not Exist")
	else:
		try:
			cursor = db.cursor()
			cursor.execute("""DELETE FROM Tournaments_Played WHERE Club_ID = %s;""",(Club_ID_E,))
			cursor.close()
			
			cursor = db.cursor()
			cursor.execute("""SELECT Employee_ID FROM Employee WHERE Club_ID = %s;""",(Club_ID_E,))
			emp_id = cursor.fetchall()
			l3=cursor.rowcount
			cursor.close()
			cursor = db.cursor()

			if  int(l3)>0:
				for i in emp_id:
					cursor.execute("""DELETE FROM Players WHERE Employee_ID = %s;""",(i[0],))
					cursor.execute("""DELETE FROM Managers WHERE Employee_ID = %s;""",(i[0],))
					cursor.execute("""DELETE FROM Coaches WHERE Employee_ID = %s;""",(i[0],))
			
			cursor.execute("""DELETE FROM Employee WHERE Club_ID = %s;""",(Club_ID_E,))
			cursor.execute("""DELETE FROM Clubs WHERE Club_ID = %s;""",(Club_ID_E,))
			cursor.execute("""DELETE FROM Stadiums WHERE Stadium_ID = %s;""",(stadium_id_temp,))
			cursor.execute("""DELETE FROM Fans WHERE Club_Name = %s;""",(club_nm,))
			db.commit()
			cursor.close()
			print("Deleted club")
		except:
			print("Could Not Add To DataBase : Error In Input")
			db.rollback()
	db.close()

def deletetour():
	true=0
	db=MySQLdb.connect('localhost','root','12345678','Football_League')
	Tour_Name_E = raw_input('Enter Tournament Name: ')
	cursor = db.cursor()
	cursor.execute("""SELECT Tournament_Name FROM Tournaments;""")
	l=cursor.rowcount
	exists = cursor.fetchall()
	cursor.close()

	for i in exists:
		if i[0] == Tour_Name_E :
			true=1
			break
	if true != 1:
			print("Tournament does not Exist")
	else:
		try:
			cursor = db.cursor()
			cursor.execute("""DELETE FROM Tournaments_Played WHERE Tournaments_Played = %s;""",(Tour_Name_E,))			
			cursor.execute("""DELETE FROM Tournaments WHERE Tournament_Name = %s;""",(Tour_Name_E,))
			db.commit()
			cursor.close()
			print("Deleted Tournament")
		except:
			print("Could Not Add To DataBase : Error In Input")
			db.rollback()
def clubleavetour():
	true1=0
	true2=0
	db=MySQLdb.connect('localhost','root','12345678','Football_League')
	Club_ID_E = raw_input('Enter Club ID: ')
	Tour_Name_E = raw_input('Tournament Name: ')
	cursor = db.cursor()
	cursor.execute("""SELECT Club_ID FROM Clubs;""")
	l1=cursor.rowcount
	exists1 = cursor.fetchall()
	cursor.close()

	cursor = db.cursor()
	cursor.execute("""SELECT Tournament_Name FROM Tournaments;""")
	l2=cursor.rowcount
	exists2 = cursor.fetchall()
	cursor.close()
	if int(l1) > 0:
		for i in exists1:
			if i[0] == int(Club_ID_E) :
				true1=1
				break
	if int(l2) > 0:
		for i in exists2:
			if i[0] == Tour_Name_E :
				true2=1
				break
	if true1 == 0 or true2 == 0:
			print("Club does not play in given tournament")
	else:
		try:
			cursor = db.cursor()
			cursor.execute("""SELECT No_Of_Clubs FROM Tournaments WHERE Tournament_Name=%s;""",(Tour_Name_E,))
			l1=cursor.rowcount
			exists1 = cursor.fetchall()
			cursor.close()
			if int(l1) > 0:
				for i in exists1:
					Tour_no_of_clubs_val=i[0]-1
			cursor = db.cursor()
			cursor.execute("""DELETE FROM Tournaments_Played WHERE Tournaments_Played = %s AND Club_ID = %s;""",(Tour_Name_E,Club_ID_E,))			
			cursor.execute("""UPDATE Tournaments SET No_Of_Clubs = %s WHERE Tournament_Name = %s;""",(Tour_no_of_clubs_val,Tour_Name_E,))			
			db.commit()
			cursor.close()
			print("Deleted Club from Tournament")
		except:
			print("Could Not Add To DataBase : Error In Input")
			db.rollback()
def empchangeclub():
	true=0
	db=MySQLdb.connect('localhost','root','12345678','Football_League')
	Employee_ID_E = raw_input('Enter Employee ID: ')
	cursor = db.cursor()
	cursor.execute("""SELECT Employee_ID FROM Employee;""")
	l=cursor.rowcount
	exists = cursor.fetchall()
	cursor.close()
	if  int(l)>0:
		for i in exists:
			if i[0] == int(Employee_ID_E,10):
				true=1
				break
	if true==1:
		Club_ID_new = raw_input('Enter New Club ID: ') 
		try:
			cursor = db.cursor()
			cursor.execute("""UPDATE Employee SET Club_ID = %s WHERE Employee_ID = %s;""", (Club_ID_new, Employee_ID_E,))	
			db.commit()
			cursor.close()
			print("Employee Changed Club")
		except:
			print("Could Not Add To DataBase : Error In Input")
			db.rollback()
	else:
		print("Employee Does Not Exist")
	db.close()

def matchstats():
	db=MySQLdb.connect('localhost','root','12345678','Football_League')

	won_id = raw_input('Enter Club ID of winning club: ')
	lost_id = raw_input('Enter Club ID of losing club: ')
	cursor = db.cursor()
	cursor.execute("""SELECT Games_Won FROM Clubs WHERE Club_ID=%s;""",(won_id,))
	l1=cursor.rowcount
	exists1 = cursor.fetchall()
	cursor.close()
	true1=0
	true2=0

	cursor = db.cursor()
	cursor.execute("""SELECT Games_Lost FROM Clubs WHERE Club_ID=%s;""",(lost_id,))
	l2=cursor.rowcount
	exists2 = cursor.fetchall()
	cursor.close()
	if int(l1) > 0:
		for i in exists1:
			true1=1
			won_val=i[0]+1

	if int(l2) > 0:
		for i in exists2:
			true2=1
			lost_val=i[0]+1

	if true1 == 0 or true2 == 0:
			print("Invalid Club ID's")
	else: 
		cursor = db.cursor()
		cursor.execute("""UPDATE Clubs SET Games_Won = %s WHERE Club_ID = %s;""", (won_val, won_id,))
		cursor.execute("""UPDATE Clubs SET Games_Lost = %s WHERE Club_ID = %s;""", (lost_val, lost_id,))
		db.commit()
		cursor.close()

	while(1):
		print("1: Player_ID")
		print("2: No More Stats To Be Added")
		choice = int(input("Enter your choice: "))
		if choice == 1:
			true3=0 
			Player_ID_E = raw_input('Enter Employee ID of Player: ')
			cursor = db.cursor()
			cursor.execute("""SELECT Employee_ID FROM Players;""")
			l3=cursor.rowcount
			exists = cursor.fetchall()
			cursor.close()
			if  int(l3)>0:
				for i in exists:
					print(i[0])
					if i[0] == int(Player_ID_E,10):
						true=1
						break
			if true != 1:
				print('Invalid player ID ')
			else:
				true4=0
				true5=0
				true6=0

				Goals_E = raw_input('Enter Goals scored: ')
				Assists_E = raw_input('Enter Assists: ')
				Tackles_E = raw_input('Enter Tackles : ')
				

				cursor = db.cursor()
				cursor.execute("""SELECT Goals FROM Players WHERE Employee_ID = %s;""",(Player_ID_E,))
				l4=cursor.rowcount
				goals1 = cursor.fetchall()
				cursor.close()
				if int(l4) > 0:
					for i in goals1:
						true4=1
						goals_val=i[0]+int(Goals_E,10)
				

				cursor = db.cursor()
				cursor.execute("""SELECT Assists FROM Players WHERE Employee_ID = %s;""",(Player_ID_E,))
				l5=cursor.rowcount
				Assists1 = cursor.fetchall()
				cursor.close()
				if int(l5) > 0:
					for i in Assists1:
						true5=1
						Assists_val=i[0]+int(Assists_E,10)
				

				cursor = db.cursor()
				cursor.execute("""SELECT Tackles FROM Players WHERE Employee_ID = %s;""",(Player_ID_E,))
				l6=cursor.rowcount
				Tackles1 = cursor.fetchall()
				cursor.close()
				if int(l6) > 0:
					for i in Tackles1:
						true6=1
						Tackles_val=i[0]+int(Tackles_E,10)


				cursor = db.cursor()
				cursor.execute("""UPDATE Players SET Goals = %s WHERE Employee_ID = %s;""", (goals_val, Player_ID_E,))
				cursor.execute("""UPDATE Players SET Assists = %s WHERE Employee_ID = %s;""", (Assists_val, Player_ID_E,))
				cursor.execute("""UPDATE Players SET Tackles = %s WHERE Employee_ID = %s;""", (Tackles_val, Player_ID_E,))
				db.commit()
				cursor.close()

		else:
			break

def updatefan():
	db=MySQLdb.connect('localhost','root','12345678','Football_League')
	true=0
	Club_Name_E = raw_input('Enter Club Name: ')
	cursor = db.cursor()
	cursor.execute("""SELECT Club_Name FROM Clubs""")
	l1=cursor.rowcount
	name2 = cursor.fetchall()
	cursor.close()
	if int(l1)>0:
		for i in name2:
			if i[0] == Club_Name_E:
				true =1
	if true != 1:
		print("Club Does Not Exist")
	else:
		Fans_E = raw_input('Change In Fans: ')
		Fan_Club_E = raw_input('Change In Fan Clubs: ')
		cursor = db.cursor()
		cursor.execute("""SELECT No_Of_Fans FROM Fans WHERE Club_Name = %s;""",(Club_Name_E,))
		l2=cursor.rowcount
		Fans1 = cursor.fetchall()
		cursor.close()
		if int(l2) > 0:
			for i in Fans1:
				Fans_val=i[0]+int(Fans_E,10)


		cursor = db.cursor()
		cursor.execute("""SELECT No_Of_Fan_Clubs FROM Fans WHERE Club_Name = %s;""",(Club_Name_E,))
		l3=cursor.rowcount
		Fansclub1 = cursor.fetchall()
		cursor.close()

		if int(l3) > 0:
			for i in Fansclub1:
				Fanclubs_val=i[0]+int(Fan_Club_E,10)
		if Fanclubs_val >= 0 and Fans_val >= 0 :
			cursor = db.cursor()
			cursor.execute("""UPDATE Fans SET No_Of_Fans = %s WHERE Club_Name = %s;""", (Fans_val, Club_Name_E,))
			cursor.execute("""UPDATE Fans SET No_Of_Fan_Clubs = %s WHERE Club_Name = %s;""", (Fanclubs_val, Club_Name_E,))
			db.commit()
			cursor.close()
		else :
			print("Invalid Input")	



def report():
	db=MySQLdb.connect('localhost','root','12345678','Football_League')
	cursor = db.cursor()
	cursor.execute("""SELECT Club_Name FROM Fans WHERE No_Of_Fans = (SELECT max(No_Of_Fans) FROM Fans);""")
	L=cursor.rowcount
	Exists = cursor.fetchall()
	cursor.close()
	print
	print('Most popular club is:')
	if  int(L)>0:
		for i in Exists:
			most_popular_club=i[0]
			print(most_popular_club)


	cursor = db.cursor()
	cursor.execute("""SELECT concat(First_Name, " " ,Last_Name) FROM Employee WHERE Employee_ID = (SELECT Employee_ID FROM Players WHERE Goals = (SELECT max(Goals) FROM Players));""")
	L=cursor.rowcount
	Exists = cursor.fetchall()
	cursor.close()
	if  int(L)>0:
		print
		print('Player with most Goals:')
		for i in Exists:
			most_goals_player=i[0]
			print(most_goals_player)
	else:
		print('Insufficient data')
	
	cursor = db.cursor()
	cursor.execute("""SELECT concat(First_Name, " " ,Last_Name) FROM Employee WHERE Employee_ID = (SELECT Employee_ID FROM Players WHERE Assists = (SELECT max(Assists) FROM Players));""")
	L=cursor.rowcount
	Exists = cursor.fetchall()
	cursor.close()
	if  int(L)>0:
		print
		print('Player with most Assists:')
		for i in Exists:
			most_assists_player=i[0]
			print(most_assists_player)
	else:
		print('Insufficient data')
	
	cursor = db.cursor()
	cursor.execute("""SELECT concat(First_Name, " " ,Last_Name) FROM Employee WHERE Employee_ID = (SELECT Employee_ID FROM Players WHERE Tackles = (SELECT max(Tackles) FROM Players));""")
	L=cursor.rowcount
	Exists = cursor.fetchall()
	cursor.close()
	if  int(L)>0:
		print
		print('Player with most Tackles:')
		for i in Exists:
			most_Tackles_player=i[0]
			print(most_Tackles_player)
	else:
		print('Insufficient data')

	


while True:
	print("1: Add Employee")
	print("2: Add Club")
	print("3: Add Tournament")
	print("4: Add club to Tournament")
	print("5: Delete Employee")
	print("6: Delete Club")
	print("7: Delete Tournament")
	print("8: Club Leaves Tournament")
	print("9: Employee Changes Club")
	print("10: Match Takes Place")
	print("11: Update Fan Clubs")
	print("12: For report")
	print("13: Exit")
	choice = int(input("Enter your choice: "))

	if choice == 1:
		newemployee()

	elif choice == 2:
	 	newclub()

	elif choice == 3:
		newtournament()

	elif choice == 4:
		club_tour_add()

	elif choice == 5:
		delete_emp()

	elif choice == 6:
		deleteclub()

	elif choice == 7:
		deletetour()

	elif choice == 8:
		clubleavetour()

	elif choice == 9:
		empchangeclub()

	elif choice == 10:
		matchstats()

	elif choice == 11:
		updatefan()

	elif choice == 12:
		report()

	elif choice == 13:
		break;
	else:
		print('Invalid input')

	print 
	print("--------------------------------------------------------------------------")
	print

print('Ba Bye!')