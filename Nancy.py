import os
import time
import webbrowser
import speech_recognition as sr
import wikipedia
# import smtplib
import pyttsx3
import datetime
import pyjokes
# import subprocess
engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

# dictionaryForEmail = {
#     "rahul": "rahularyan9898@gmail.com",
#     "sayan": "raysyan222@gmail.com",
#     "dipika":"dipikahait1173@gmail.com",
#     "nandan": "nandandasegre@gmail.com",
# }

# dictionaryForDob = {
#     "rahul": "twenty six june nineteen ninety eight",
#     "sayan": "_______________ nineteen ninety eight",
#     "dipika": "fifteen june nineteen ninety eight"
# }

restrict_search = ["how to have an abortion", "how bombs are made", "hire a Assassin", "process of making drugs", "open xvideos", "find child porn", "process making of gun"]

def speak(text):
    engine.say(text)
    engine.runAndWait()



def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Good Morning")
        print("Good Morning")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
        print("Good Afternoon")

    else:
        speak("Good Evening")
        print("Good Evening")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing...")
            statement = r.recognize_google(audio, language='en-in')
            print(f"user said: {statement} \n")

        except Exception as e:
            speak("Sorry, I can't hear you properly. Can you say again please!")
            return "None"
        return statement

# def sendEmail(to, content):
#     server = smtplib.SMTP('smtp.gmail.com', 465)
#     server.ehlo()
#     server.starttls()
#
#     server.login('mca.vu2020@gmail.com','Vu1@mca20')
#     server.sendmail('mca.vu2020@gmail.com', to, content)
#     server.close()

print("Loading your personal assistant")
speak("Loading your personal assistant")
wishMe()

# The main Function :-

if __name__ == '__main__':

    while True:
        speak("Tell me how can I help you ?")
        statement = takeCommand().lower()
        if statement == 0:
            continue


        if 'who are you' in statement:
            print('I am NANCY your personal assistant.')
            speak('I am NANCY your personal assistant.')


        if 'how are you' in statement:
            print("I am fine, Thank you")
            speak("I am fine, Thank you")
            print("How are you, Sir?")
            speak("How are you, Sir?")

        if 'i am fine' in statement:
            print("It is good to know that you are fine")
            speak("It is good to know that you are fine")

        if 'what can you do for me' in statement:
            print('I am programmed to minor task like opening youtube, browser, gmail and get top headline news from The HINDU')
            speak('I am programmed to minor task like opening youtube, browser, gmail and get top headline news from The HINDU')

        # elif 'change name' in statement:
        #     speak("What would you like to call me, Sir?")
        #     print()

        elif 'reason to create you' in statement:
            print("I was created as a Minor project under the guidance of Mr. Debkumar Bera")
            speak("I was created as a Minor project under the guidance of Mr. Debkumar Bera")

        # elif 'empty recycle bin' in statement:

# Predicting time:-

        elif 'what time is it right now' in statement:
            spTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"the time is {spTime}")
            speak(f"the time is {spTime}")

# For Jokes:-

        elif "tell me a joke" in statement:
            try:
                joke = pyjokes.get_joke()
                print(joke)
                speak(joke)
            except Exception as e:
                print(e)
                speak("Your voice is not clear sir please say that again")

        # elif "birthday" in statement:
        #     try:
        #         print('whose birthday')
        #         speak('whose birthday')
        #         to = takeCommand()
        #         date = dictionaryForDob[to]
        #         speak(date)
        #         print(date)
        #     except Exception as e:
        #         print(e)
        #         speak("Sorry sir I don't know your dath of birth")
# Wikipedia:-

        elif 'wikipedia' in statement:
            speak('serching wikipedia....')
            statement = statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences = 3)
            print("Acording to wikipedia")
            speak("Acording to wikipedia")
            print(results)
            speak(results)

# Webbrowsers:-

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com/")
            print("Youtube is open now")
            speak("Youtube is open now")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com/")
            print("google is open now")
            speak("google is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("https://mail.google.com/")
            print("gmail is open now")
            speak("gmail is open now")
            time.sleep(5)

        elif 'open stack overflow' in statement:
            print("Here you go to stack over flow.Happy coding")
            speak("Here you go to stack over flow.Happy coding")
            webbrowser.open("stackoverflow.com")

        # elif 'mail' in statement:
        #     try:
        #         speak('whom to send')
        #         to = takeCommand()
        #         to = dictionaryForEmail[to]
        #         print(to)
        #         speak("what should i say")
        #         content = takeCommand()
        #         sendEmail(to, content)
        #         speak("Email has been sent")
        #     except Exception as e:
        #         print(e)
        #         speak("Sorry sir i am unable to send the mail")

# For News

        elif 'show me latest news' in statement:
            news = webbrowser.open_new_tab("https://www.thehindu.com/latest-news/")
            print('Here are some latest news from the hindu')
            speak('Here are some latest news from the hindu')
            time.sleep(5)

# Serching data from web:-

        elif 'search' in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

# For restrict_search

        # elif 'search' in statement:
        #     if statement != restrict_search:
        #         statement = statement.replace("search", "")
        #         webbrowser.open_new_tab(statement)
        #     else:
        #         print("This is comes under restric search as per indian government rule.")
        #         speak("This is comes under restric search as per indian government rule.")
        #         break

        # elif 'search' in statement:
        #     try:
        #         statement = statement.replace("search","")
        #         webbrowser.open_new_tab(statement)
        #     except Exception as e:
        #         statement = restrict_search
        #         print("This is comes under restric search as per indian government rule.")
        #         speak("This is comes under restric search as per indian government rule.")
        #         break


        # elif "porn" in statement or "sex" in statement:
        #     print("This word comes under a restriction word")
        #     speak("This word comes under a restriction word")
        #     break
# restrict_search = ["how to have an abortion", "how bombs are made", "hire a Assassin","process of making drugs", "open xvideos", "find child porn", ]

        elif statement in restrict_search:
            print("Sorry, This is comes under restric search as per indian government rule.")
            speak("Sorry, This is comes under restric search as per indian government rule.")
            print("This may be risky for you")
            speak("This may be risky for you")
            break

# open powerpoint:-

        elif 'open powerpoint presentation' in statement:
            print("Opening power point presentation")
            speak("Opening power point presentation")
            # power = r"C:\\Users\\rahul\\OneDrive\\Desktop\\Nancy\\Speech_Recognition with protected search.pptx"
            power = r"C:\\Users\\rahul\\OneDrive\\Desktop\\Speech_Recognition with protected search.pptx"
            os.startfile(power)

# for holding:-
        elif "don't listen me" in statement or "stop listening" in statement:
            print("For how much time you want to stop me from listening command")
            speak("For how much time you want to stop me from listening command")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

# For Stop running command:-

        elif "exit" in statement or "good bye" in statement or "ok bye" in statement:
            print("Thanks for giving me your valuable time")
            speak("Thanks for giving me your valuable time")
            print("Your personal assistant NANCY is shutting down, Good Bye")
            speak("Your personal assistant NANCY is shutting down, Good Bye")
            # break
            exit()

        # elif 'exit' in statement:
        #     print("Thanks for giving me your valuable time")
        #     speak("Thanks for giving me your valuable time")
        #     exit()



        # elif 'sleep' in statement:
        #     print("Your system is going to sleep mode.")
        #     speak("Your system is going to sleep mode.")
        #     subprocess.call("shutdown/h")

        elif 'log off' in statement or 'sign out' in statement:
            try:
                print('Are you sure to log off your system')
                speak('Are you sure to log off your system')
                choice = takeCommand()
                os.system("shutdown /l")
                time.sleep(7)
            except Exception as e:
                speak('Sorry Sir, I am unable to sign out')

        # elif 'log off' in statement or 'sign out' in statement:
        #     speak("sign out")
        #     subprocess.call(["shutdown /l"])
        #     time.sleep(5)
