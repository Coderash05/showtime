
#%%
import tkinter as tk
import mysql.connector as sql
import matplotlib.pyplot as plt
import matplotlib.image as img

window=tk.Tk()
movie_code=0

try:
    conn=sql.connect(host='localhost',user='root',passwd='nanav') #establishing connection with mysql
    if conn.is_connected(): #checking if it is connected to mysql or not
        print('Showtime.com connection successful.')
    else:
        print('Showtime.com connection unsuccessful.')  
        
    print('_________________________________________')
    print('WELCOME TO SHOWTIME.COM')
    c=conn.cursor()
    c.execute('create database if not exists movie;')
    c.execute('use movie;')
    c.execute('create table if not exists movielist(sno int primary key, name varchar(50), rating float(3,2), genre varchar(20), language varchar(10), synopsis varchar(500));')
    c.execute('delete from movielist;')
    c.execute('insert into movielist values(101,"Oppenheimer",8.6,"Biography Drama", "English", "During World War II, Lt. Gen. Leslie Groves Jr. appoints physicist J. Robert Oppenheimer to work on the top-secret Manhattan Project. Oppenheimer and a team of scientists spend years developing and designing the atomic bomb. Their work comes to fruition on July 16, 1945, as they witness the worlds first nuclear explosion, forever changing the course of history.");')
    c.execute('insert into movielist values(102,"Barbie",7.4,"Adventure Comedy", "English", "Barbie and Ken are having the time of their lives in the colorful and seemingly perfect world of Barbie Land. However, when they get a chance to go to the real world, they soon discover the joys and perils of living among humans.");')
    c.execute('insert into movielist values(103,"Across The Spiderverse",8.8,"Animation Action", "English", "Miles Morales catapults across the Multiverse, where he encounters a team of Spider-People charged with protecting its very existence. When the heroes clash on how to handle a new threat, Miles must redefine what it means to be a hero.");')
    c.execute('insert into movielist values(104,"Gadar 2",6.2,"Action Drama", "Hindi", "During the Indo-Pakistani War of 1971, Tara Singh returns to Pakistan to bring his son, Charanjeet, back home.");')
    c.execute('insert into movielist values(105,"Tranformers: Rise of the Beast",6.1,"Action Sci-Fi", "English", "Optimus Prime and the Autobots take on their biggest challenge yet. When a new threat capable of destroying the entire planet emerges, they must team up with a powerful faction of Transformers known as the Maximals to save Earth.");')
    c.execute('insert into movielist values(106,"Mission Impossible: The Dead Reckoning",8.0,"Thriller Adventure", "English", "IMF team must track down a terrifying new weapon that threatens all of humanity if it falls into the wrong hands. With control of the future and the fate of the world at stake, a deadly race around the globe begins. Confronted by a mysterious, all-powerful enemy, Ethan is forced to consider that nothing can matter more than the mission -- not even the lives of those he cares about most.");')
    c.execute('insert into movielist values(107,"Adipurush",3.1,"Action Adventure", "Hindi", "Raghav, the prince of the Ikshvaku dynasty from Kosala, tries to rescue his wife, Janaki, from the demon king Lankesh.");')
    c.execute('insert into movielist values(108,"Kerala Story",7.2,"Drama", "Hindi", "Shalini Unnikrishnan leads an ordinary life as a college student in Kerala until her identity, relationships, dreams and faith dissipate in the abyss of religious terrorism.");')
    c.execute('insert into movielist values(109,"IB71",7.3,"Action Thriller", "Hindi", "Indian intelligence officers embark on a high-stakes mission to counter two enemy nations conspiracy. If things go sideways, they must think on their feet to avoid a disaster.");')
    c.execute('insert into movielist values(110,"RRR",7.8,"Action Drama", "Telugu", "A fearless revolutionary and an officer in the British force, who once shared a deep bond, decide to join forces and chart out an inspirational path of freedom against the despotic rulers.");')
    conn.commit()
    
    #signup section
    c.execute('create table if not exists userdetails(username varchar(30) primary key, password varchar(30) not null, email varchar(30),phoneno bigint(12));')
    c.execute('delete from userdetails;')
    c.execute("insert into userdetails values('niruj1102', '11022006','jnirucompsci@showtime.com',112233);")
    c.execute("insert into userdetails values('mahig0209','02092006','mahikacompsci@showtime.com',223344);")
    c.execute("insert into userdetails values('avanp1512','15122005','avanipcompsci@showtime.com',445566);")
    conn.commit()
    
    usern=None
    
    
            
    def login():
        print('_________________________________________')
        print('LOGIN/ SIGN UP')
        print('Note: Usernames and passwords entered are case sensitive! Please input carefully.')
        
        try:
            global usern
            usern=input('USERNAME: ')
            line="select password from userdetails where username like '"+usern+"' ;"
            c.execute(line)
            data=c.fetchall()
            if len(data)>0:
                while True:
                    pword=input('PASSWORD: ')
                    if pword=='0':
                        print('Quitting ...')
                        break
                    else:
                        if data[0][0]==pword:
                            print('LOGIN SUCCESSFUL!')
                            entry_menu()
                            break
                        else:
                            print('Seems like that is incorrect. Try again: ')
                            print('If you wish to the quit, please type 0')
            else:
                print('\nCreating new account with inputted username!')
                signup()
        except Exception as e:
            print(e)
            login()
            
    def signup():
        print('_________________________________________')
        pword=input('Enter your desired password: ')
        email=input('EMAIL ID: ')
        phoneno=int(input('PHONE NO: '))
        if len(str(phoneno))!=10:
            print('Phone number has to be 10 digit, Please Try Again')
            signup()
        elif pword=='' or email=='' or phoneno==None:
            print('All fields are required, Pease try again')
            signup()
        elif '@' not in email or '.' not in email:
            print('Email format should be: xyz@sample.domain, Please try again')
            signup()
        else:
            values=(usern,pword,email,phoneno)
            line="insert into userdetails values(%s,%s,%s,%s);"
            c.execute(line,values)
            conn.commit()
            print('Account successfully created. Thank you for joining us!')
            entry_menu()
            
    def delete_account():
        decision=input('Are you sure you want to delete this account? (Y/N): ')
        if decision.lower()=='y':
            c.execute('delete from userdetails where username=%s;',(usern,))
            conn.commit()
            print('Account Deleted. Please use Showtime.com again')
        elif decision.lower()=='n':
            entry_menu()
    
    def entry_menu():
        print('__________________________________________')
        try:
            choice=int(input('What would you like to do?\n 1. Find a Movie\n 2. Log Out\n 3. Delete account\nEnter your choice: '))
            if choice==1:
                mainmenu()
            elif choice==2:
                print('Logged out successfully, Please use Showtime.com Again!')
            elif choice==3:
                delete_account()
            else:
                raise Exception
        except:
            print('Invalid input, Please Try Again')
            entry_menu()
            
    
    def display(): # full list of movies
        print('_________________________________________')
        c.execute('select sno, name from movielist;')
        data=c.fetchall()
        print('CODE\t MOVIE')
        for i in data:
            print(i[0],'\t',i[1])
        print()
        print('Enter 100 if you would like to return to Main Menu')
        
        try:
            n=int(input('Enter Movie Code: ' ))
            if n==100:
                mainmenu()
            elif n>100 and n<111:
                global movie_code
                movie_code=n
                movie()
            else:
                print('Please check the code you have entered.')
                display()
                
        except Exception as e:
            print('Invalid Movie Code. Retry.')
            display()
    
