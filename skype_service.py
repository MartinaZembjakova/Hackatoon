"""
This file contains all the necessary functions and handlers for Skype integration.
"""

from skpy import Skype

def logIn(username, password):
    return Skype(username, password)
    print("JIRA logged in")

def openChat (sk, chatUrl):
    id = sk.chats.urlToIds(chatUrl)
    sk.chats.sync()
    ch = sk.chats[id["id"]]
    return ch

def sendMessage(chat, msg):
    chat.sendMsg(msg)
