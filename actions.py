# UTILS AND FUNCTIONALITY
from data import  population, clubs
from components import Club, Person

my_name = "Rasha "
my_age = 27
my_bio = "hi"
myself = Person(my_name, my_bio, my_age)

def introduction():
    print("Hello, %s. Welcome to our portal." % my_name)

def options():
    # your code goes here!
    
    while True :
        option =input("wold you like to : \n 1- create a new club \n or : \n 2- Browse and join clubs \n or : \n 3- View existing clubs \n or : \n 4- Display members of a club \n or : \n -1 close application \n")
        if option == '1':
            create_club()
        elif option == '2':
            join_clubs()
        elif option == '3':
            view_clubs()
        elif option == '4':
            view_club_members()
        elif option == '-1': 
            quit()
        #return
        else :
            option = input('invalid option enter again ')

def create_club():
    # your code goes here!
    club_name =input("Pick a name for you asesome new club:")
    clube_description = input("what is your club about?")
    club = Club(club_name,clube_description)
    club.recruit_member(myself)
    club.assign_president(myself)
    clubs.append(club)
    print("Enter the numbers of the people you would like to recruit to your new club (-1 to stop :)")
    for i , p in enumerate(population):
        print ("[%s] %s" % (i+1,p.name))
    people_number = input()   
    while int(people_number) != -1:
        if int(people_number)-1  <= len(population):
            club.recruit_member(population[int(people_number)-1])
        else:
            print("incorrect input")
        people_number = input ()
    print("Here's your club:")
    print ( "%s \n %s "%(club.name, club.description))
    club.print_member_list()        
        
    
def view_clubs():
    # your code goes here!
   
    for club in clubs:
        print ("NAME : %s " % club.name)
        print ("DESCRIPTION : %s " % club.description)
        print ("MEMBERS : %s " % len(club.members))

    
def view_club_members():
    # your code goes here!
    view_clubs()
    flag = False
    while not flag:
        club_name = input ("Enter the name of the club whose members you would like to see ")
        for club in clubs:
            if club.name == club_name:
                flag = True
                club.print_member_list()
     
    

def join_clubs():
    # your code goes here!
    view_clubs()
    flag = False
    while not flag:
        club_name = input ("Enter the name of the club you'd like to join :")
        for club in clubs:
            if club.name == club_name:
                flag = True
                if club.recruit_member(myself):
                    print ("%s just joined %s" % (myself.name ,club.name))
                else:
                    print("already exist")
                   

    
    

def application():
    introduction()
    # your code goes here!
    options()
    
