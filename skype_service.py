"""
This file contains all the necessary functions and handlers for Skype integration.
"""

from skpy import Skype
import msg_formatter

def logIn():
    return Skype("jira.solarwinds@outlook.com", "3KLi*h!9")
    print("JIRA logged in")

def openChat (sk, chatUrl):
    id = sk.chats.urlToIds(chatUrl)
    sk.chats.sync()
    ch = sk.chats[id["id"]]
    return ch

def sendMessage(chat, msg):
    chat.sendMsg(msg)



if __name__=="__main__":
    sk = logIn()
    ch = openChat(sk,"https://join.skype.com/l8UaczGL8VKq")
    msg = msg_formatter.Bug("CUST-34979", "Jira is down")
    sendMessage(ch, msg)
    msg = msg_formatter.Closed("CUST-34979", "Jira is up")
    sendMessage(ch, msg)
    print("Msgs printed")



    input()