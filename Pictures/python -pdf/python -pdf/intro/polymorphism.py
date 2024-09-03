'''polymorphism : polyporphism the word means many forms,
polymorphism means same function name being used for different types .the key is the different data type
class 
'''
class cricket:
    def batsman(self):
        print("Dhoni is a best batsman:")
    def bowler(self):
        print("Bumrah is a best bowler in all time:")
class ipl():
    def batsman(self):
        print("Virat kohli is a indian no:1 player in the all time:")
    def bowler(self):
        print("Siraj mia bhai is the best bowler in the rcp")
def display(obj):
    obj.batsman()
    obj.bowler()
    print("Stats are displayed:")
B=cricket()
C=ipl()
display(B)
display(C)
