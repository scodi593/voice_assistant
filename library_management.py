import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia 
import pyjokes
import os
import requests, json , sys
listener = sr.Recognizer()
books_dict = {}
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)

def engine_talk(text):
    engine.say(text)
    engine.runAndWait()
def user_commands():
    try:
    
        with sr.Microphone() as source:
            print("Start Speaking!!")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command

def display_books():
        
        rack_no = 1
        with open("list_of_books.txt") as bk:
            content = bk.readlines()
        for line in content:
            books_dict.update({str(rack_no):{'books_title':line.replace("\n",""),}})
            rack_no =rack_no+ 1 
        print("------------------------List of Books---------------------")
        print("Rack NUMBER","\t", "Title")
        print("----------------------------------------------------------")
        for key, value in books_dict.items():
            print(key,"\t\t", value.get("books_title"))
print(display_books())





books_dict={'ENVIRONMENTAL SCIENCES':{'a':'Environmental Chemistry','b':'Fundamentals of Ecology','c':'WasteWater Treatment','d':'Environmental Studies','e':'Disaster Management'},'ESSENCE OF INDIAN TRADITIONAL KNOWLEDGE':{'a':'Text and Interpretation: The India Tradition','b':'Science in Samskrit','c':'Position paper on Arts, Music, Dance and Theatre','d':'Examinations in Ancient India','e':'Essentials of Indian Philosophy'},'INDIAN CONSTITUTION':{'a':'Introduction to the Constitution of India','b':'Our Parliament','c':'Indian Government and Politics'},'BASIC ELECTRICAL ENGINEERING':{'a':'Basic Electrical Engineering','b':'Fundamentals of Electrical Engineering and Electronics','c':'Utilization of Electric Power and Electric Traction','d':'Basic ElectricalEngineering','e':'Electrical Technology'},'MATHEMATICS-I':{'a':'Advanced Engineering Mathematics','b':'Advanced Engineering Mathematics','c':'Higher Engineering Mathematics','d':'Thomas Calculus','e':'Higher Engineering Mathematics'},'CHEMISTRY':{'a':'Principles of Physical Chemistry','b':'Engineering Chemistry Dhanpat Rai & Sons','c':"Chemistry in Engineering and Technology",'d':'Engineering Chemistry'},'PROGRAMMING FOR PROBLEM SOLVING':{'a': 'Theory and practice of Programming with C','b':'Computer Fundamentals and Programming in C','c':'Programming in ANSI C','d':"The C Programming Language"},'ENGLISH':{'a':'Language and Life: A Skills Approach','b':'English for Engineering','c':'English Language and Communication Skills forEngineers'},'PHYSICS':{'a':'Engineering Physics','b':"Nano Materials",'c':'Engineering Physics','d':'Science of Engineering Materials','e':'Engineering Physics', 'f':'Engineering Physics'},'MATHEMATICS-II':{'a':'Advanced Engineering Mathematics','b':'Advanced Engineering Mathematics','c':'Higher Engineering','d':'Higher Engineering mathematics','e':'A text book of Engineering Mathematics'}
}            
        


def run_alexa():
    command = user_commands()
    print(command)
    if (('number 1'  in command) or ("1" in command)):
        engine_talk('WELCOME TO ENVIRONMENTAL SCIENCES ')
        engine_talk('Loading the rack 1 this is what i found')
        print(books_dict['ENVIRONMENTAL SCIENCES'])
        engine_talk(books_dict['ENVIRONMENTAL SCIENCES'])
    elif (('number 2'  in command) or ("2" in command)):
        engine_talk('WELCOME TO ESSENCE OF INDIAN TRADITIONAL KNOWLEDGE ')
        engine_talk('Loading the rack 2 this is what i found')
        print(books_dict['ESSENCE OF INDIAN TRADITIONAL KNOWLEDGE'])
        engine_talk(books_dict['ESSENCE OF INDIAN TRADITIONAL KNOWLEDGE'])
    elif (('number 3'  in command) or ("3" in command)):
       engine_talk('WELCOME TO MATHEMATICS-I ')
       engine_talk('Loading the rack 3 this is what i found')
       print(books_dict['MATHEMATICS-I'])
       engine_talk(books_dict['MATHEMATICS-I'])
    elif (('number 4'  in command) or ("4" in command)):
        engine_talk('WELCOME TO CHEMISTRY ')
        engine_talk('Loading the rack 4 this is what i found')
        print(books_dict['CHEMISTRY'])
        engine_talk(books_dict['CHEMISTRY'])
    elif (('number 5'  in command) or ("5" in command)):
        engine_talk('WELCOME TO PROGRAMMING FOR PROBLEM SOLVING ')
        engine_talk('Loading the rack 5 this is what i found')
        print(books_dict['PROGRAMMING FOR PROBLEM SOLVING'])
        engine_talk(books_dict['PROGRAMMING FOR PROBLEM SOLVING'])
    elif (('number 6'  in command) or ("6" in command)):
        engine_talk('WELCOME TO INDIAN CONSTITUTION ')
        engine_talk('Loading the rack 6 this is what i found')
        print(books_dict['INDIAN CONSTITUTION'])
        engine_talk(books_dict['INDIAN CONSTITUTION'])
    elif (('number 7'  in command) or ("7" in command)):
        engine_talk('WELCOME TO ENGLISH ')
        engine_talk('Loading the rack 7 this is what i found')
        print(books_dict['ENGLISH'])
        engine_talk(books_dict['ENGLISH'])
    elif (('number 8'  in command) or ("8" in command)):
        engine_talk('WELCOME TO PHYSICS ')
        engine_talk('Loading the rack 8 this is what i found')
        print(books_dict['PHYSICS'])
        engine_talk(books_dict['PHYSICS'])
    elif (('number 9'  in command) or ("9" in command)):
        engine_talk('WELCOME TO MATHEMATICS-II ')
        engine_talk('Loading the rack 9 this is what i found')
        print(books_dict['MATHEMATICS-II'])
        engine_talk(books_dict['MATHEMATICS-II'])
    elif (('number 10'  in command) or ("10" in command)):
        engine_talk('WELCOME TO BASIC ELECTRICAL ENGINEERING ')
        engine_talk('Loading the rack 10 this is what i found')
        print(books_dict['BASIC ELECTRICAL ENGINEERING'])
        engine_talk(books_dict['BASIC ELECTRICAL ENGINEERING'])
    elif 'stop' in command:
        sys.exit()
    else:
        engine_talk('I could not hear you properly')
        

display_books()        
while True:
    run_alexa()