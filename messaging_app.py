import csv
from datetime import date
from string import *




class User():

    def __init__(self, username, age):
        self.username = username
        self.age = age


def runnerstart():
    username = input("what is your name?")
    age = 19  # input("what is your age")
    user1 = User(username, age)
    utils = Utils()
    if utils.userexists(user1) == False:
        utils.adduser(user1)
    runnercore(user1)


def runnercore(user):
    choice = -1
    messagemanager = MessageManager()
    while choice != 0:
        choice = int(input("what would you like to do\
            0 = exit\
            1 = send new message\
            2 = view messages with a user\
            3 = log out"))

        if choice == 1:
            recipient = input("who would you like to send this message to? ")
            recipient = (recipient)
            body = input("what is the message you would like to send? ")
            messagemanager.send_new_message(user.username, recipient, body)
        if choice == 2:
            recipient = input("who's message would you like to view? ")
            messagemanager.view_message(user.username, recipient, )
        if choice == 3:
            runnerstart()
    if choice == 0:
        exit()

class Utils():

    def adduser(self, user):
        file = open("users.csv", "a")
        writer = csv.writer(file)
        writer.writerow([user.username, user.age, date.today()])
        file.close()

    def userexists(self, user):
        file = open("users.csv", "r")
        reader = csv.reader(file)
        for line in reader:
            if line[0] == user.username:
                return True
            else:
                return False

    print(userexists)


class MessageManager():

    def send_new_message(self, sender, receiver, messagebody):
        filename = "records/"
        if sender < receiver:  # ascii
            filename += sender + receiver + ".csv"
        else:
            filename += receiver + sender + ".csv"
        file = open(filename, "a")
        writer = csv.writer(file)
        sendeer = "from : " + sender
        receiveer = "to : " + receiver
        writer.writerow([sendeer, receiveer, messagebody, date.today()])
        file.close()

    def view_message(self, sender, receiver):
        filename = "records/"
        if sender < receiver:  # ascii
            filename += sender + receiver + ".csv"
        elif sender > receiver:
            filename += receiver + sender + ".csv"
        else:
            print("you have no conversation with this user")
            runnerstart()
        file = open(filename, "r")
        fullorlast = input("would you like the view the last message(l) or the entire conversation(e)? ")
        if fullorlast == "l":
            reader = csv.reader(file)
            for line in reader:
                print(line)
            file.close()
            # last_message = file.readlines[-1]
            # print(last_message)
        elif fullorlast == "e":
            reader = csv.reader(file)
            for line in reader:
                print(line)
            file.close()
        #     print(file.readlines[0:-1])
        # file.close()


runnerstart()



