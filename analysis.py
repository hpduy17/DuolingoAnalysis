from duolingo import Duolingo
from pprint import pprint
import json
userList = []
writeFilePath = "C:/duolingodata/french/"
def readfile(filename):
    f = open(filename,"r")
    result = f.read()
    f.close()
    return result

def appendfile(filename, data):
    f = open(filename, "a")
    f.write(data+"\n")
    f.close()

def getUserProfile(username, language_name):
    print("Getting data of ",username, "in language",language_name)
    try:
        duolingo = Duolingo(username)
        lang = duolingo.get_abbreviation_of(language_name)
        try:
            activity = duolingo.get_activity_stream()
            appendfile(writeFilePath+"activity.txt",json.dumps({"key":username, 'data':activity}))
        except:
            print(Exception('activity Fail'))
        try:
            info = duolingo.get_user_info()
            appendfile(writeFilePath + "info.txt", json.dumps({"key": username, 'data': info}))
        except:
            print(Exception('info Fail'))
        try:
            knownskill = duolingo.get_known_topics(lang)
            appendfile(writeFilePath + "knownskill.txt", json.dumps({"key": username, 'data': knownskill}))
        except:
            print(Exception('knownskill Fail'))
        try:
            language_progress = duolingo.get_language_progress(lang)
            appendfile(writeFilePath + "language_progress.txt", json.dumps({"key": username, 'data': language_progress}))
        except:
            print(Exception('language_progress Fail'))
        try:
            setting = duolingo.get_settings()
            appendfile(writeFilePath + "setting.txt", json.dumps({"key": username, 'data': setting}))
        except:
            print(Exception('setting Fail'))
        try:
            streak_info = duolingo.get_streak_info()
            appendfile(writeFilePath + "streak_info.txt", json.dumps({"key": username, 'data': streak_info}))
        except:
            print(Exception('streak_info Fail'))
    except:
        print(Exception('Login Fail'))
if __name__ == '__main__':
    readFilePath = "C:/userlistFrench.txt"
    file  = readfile(readFilePath)
    userList = file.splitlines()
    for u in userList:
        getUserProfile(u, "French")


