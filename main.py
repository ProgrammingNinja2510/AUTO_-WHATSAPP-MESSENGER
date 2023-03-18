import pyautogui
import pywhatkit
import speech_recognition as sr
import pyttsx3
import datetime

listener = sr.Recognizer()
engine = pyttsx3.init()

#Assign names for a persons whatsapp number
mobile_phone_list = {
    '1': '+254759131275',#enter contacts 1 number in the empty string
    '2': '',#enter contacts 2 number in the empty string
    '3': '',#enter contacts 3 number in the empty string
    '4': '',#enter contacts 4 number in the empty string
    '5': '',#enter contacts 5 number in the empty string
    '6': '',#enter contacts 6 number in the empty string
    '7': '',#enter contacts 7 number in the empty string
    '8': '',#enter contacts 8 number in the empty string
    '9': '',#enter contacts 9 number in the empty string
    '10':'' #enter contacts 10 number in the empty string
}
#You can add more contacts in the dictionary if you want to

now = datetime.datetime.now()
current_hour= int(now.hour)
current_min= int(now.minute)

def talk(text):
    engine.say(text)
    engine.runAndWait()

   

def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass



def get_message_info():
    how_many_hrs_later=int(input("How many hours later: "))
    talk('To Whom you want to send message')
    name = get_info()
    receiver = mobile_phone_list[name]
    print(receiver)
    current_hour1=current_hour+how_many_hrs_later
    talk('Tell me the text in your message')
    message = get_info()
    pywhatkit.sendwhatmsg(receiver, message,current_hour1,current_min)
    pyautogui.click(1050, 950)
    talk('Your message is sent')
    talk('Do you want to send more messages?')
    send_more = get_info()
    if 'yes' in send_more:

        get_message_info()

get_message_info()
