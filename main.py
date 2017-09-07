"""
This file contains main function for running the application itself.
"""
from datetime import datetime, timedelta
from time import sleep
import threading

from msg_formatter import format_message
import jira_service
from settings import SKYPE_USERNAME, SKYPE_PASSWORD, CHAT_INVITE_URL, PROJECT_NAME, TIMEOUT
from skype_service import sendMessage, openChat, logIn


def main():
    # initialise sessions and establish connections
    skype = logIn(SKYPE_USERNAME, SKYPE_PASSWORD)
    skype_chat = openChat(skype, CHAT_INVITE_URL)
    last_check = datetime.now() - timedelta(1)
    session = jira_service.initialise_session()

    # stopping flag
    stop_event = threading.Event()
    # worker thread
    checking_thread = threading.Thread(target=repeat_checks, args=(last_check, session, skype_chat, stop_event))
    checking_thread.start()
    # wait for user input in main thread
    user_input()

    # at this point user typed in bye and wants to exit
    stop_event.set()
    checking_thread.join()

    jira_service.close_session(session)


def repeat_checks(last_check, session, skype_chat, stop_event):
    while not stop_event.is_set():
        new_last_check = datetime.now()
        do_check(last_check, session, skype_chat)
        last_check = new_last_check
        stop_event.wait(TIMEOUT)


def do_check(last_check, session, skype_chat):
    issues = jira_service.list_new_issues(session, last_check, PROJECT_NAME)
    for issue in issues:
        case, summary, issue_type, status = jira_service.parse_issue(issue)
        message = format_message(case, summary, issue_type, status)
        sendMessage(skype_chat, message)


def user_input():
    message = ''
    while message != "bye":
        message = input('Type "bye" to exit... ')


if __name__ == "__main__":
    main()
