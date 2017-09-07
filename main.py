"""
This file contains main function for running the application itself.
"""

from settings import SKYPE_USERNAME
from settings import SKYPE_PASSWORD
from settings import CHAT_INVITE_URL

from skype_service import sendMessage
from skype_service import openChat
from skype_service import logIn

from msg_formatter import Bug
from msg_formatter import Closed


if __name__=="__main__":

    sk = logIn(SKYPE_USERNAME, SKYPE_PASSWORD)
    ch = openChat(sk,CHAT_INVITE_URL)
    msg = Bug("CUST-34979", "Jira is down")
    sendMessage(ch, msg)
    msg = Closed("CUST-34979", "Jira is up")
    sendMessage(ch, msg)
    print("Msgs printed")



    input()