# CLASSES AND METHODS
class Person():
    def __init__(self, name, bio, age):
        # your code goes here!
        self.name = name
        self.bio = bio
        self.age = age
       

class Club():
    def __init__(self, name, description):
        # your code goes here!
        self.name = name
        self.description = description
        self.president = None
        self.members = []
    
    def __str__ ():
        return ('%s , %s' % (self.name,self.description))   


    def assign_president(self, person):
        # your code goes here!
        self.president =person



    def recruit_member(self, person):
        # your code goes here!
        for m in self.members:
            if m.name == person.name:
                return False
        self.members.append(person)
        return True
        

               


    def print_member_list(self):
        # your code goes here!
        total_age =0
        avrage_age =0
        for member in self.members:
            total_age += member.age
            avrage_age = total_age / len(self.members) 
            if member == self.president:
                print ('- %s ( %s years old, president) - %s '  % (member.name ,member.age, member.bio ))

            else:
                print ('- %s ( %s years old) - %s '  % (member.name ,member.age, member.bio ))
        print("Average age in this club : %.2f" % avrage_age)


