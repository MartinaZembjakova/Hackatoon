"""
This file contains all the necessary functions and handlers for Skype integration.
"""

from skpy import Skype


def login(username, password):
    """
    Logs a Skype user in.
    :param username: user name of the user to be logged in
    :param password: password for the user to be logged in
    :return: Skype connection object
    """
    return Skype(username, password)


def open_chat(skype, chat_url):
    """
    Opens chat with the given invite URL.
    :param skype: Skype connection object
    :param chat_url: URL of chat that will be used to sent messages into
    :return: Skype chat object
    """
    chat_id = skype.chats.urlToIds(chat_url)
    skype.chats.sync()
    chat = skype.chats[chat_id["id"]]
    return chat


def send_message(chat, message):
    """
    Send the given message to the given chat.
    :param chat: Skype chat object
    :param message: string message
    :return: None
    """
    chat.sendMsg(message)
