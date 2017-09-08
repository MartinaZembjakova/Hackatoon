"""
This file contains main function for running the application itself.
"""
from datetime import datetime, timedelta
import threading

from message_formatter import format_message
from jira_service import initialise_session, list_new_issues, close_session, parse_issue
from settings import SKYPE_USERNAME, SKYPE_PASSWORD, CHAT_INVITE_URL, PROJECT_NAME, TIMEOUT, ISSUE_TYPE
from skype_service import send_message, open_chat, login


def main():
    # initialise sessions and establish connections
    skype = login(SKYPE_USERNAME, SKYPE_PASSWORD)
    skype_chat = open_chat(skype, CHAT_INVITE_URL)
    last_check = datetime.now() - timedelta(1)
    session = initialise_session()

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

    close_session(session)


def repeat_checks(last_check, session, skype_chat, stop_event):
    """
    Repeatedly runs checks for new issues.
    :param last_check: date of the last check
    :param session: http session for JIRA API calls
    :param skype_chat: chat to which the messages will be sent
    :param stop_event: flag indicating user will to close the program
    :return: None
    """
    while not stop_event.is_set():
        new_last_check = datetime.now()
        do_check(last_check, session, skype_chat)
        last_check = new_last_check
        stop_event.wait(TIMEOUT)


def do_check(last_check, session, skype_chat):
    """
    Does a single check for new issues.
    :param last_check: date of the last check
    :param session: http sesion for JIRA API calls
    :param skype_chat: chat to which the messages will be sent
    :return: None
    """
    issues = list_new_issues(session, last_check, PROJECT_NAME, ISSUE_TYPE)
    for issue in issues:
        case, summary, issue_type, status = parse_issue(issue)
        message = format_message(case, summary, issue_type, status)
        send_message(skype_chat, message)


def user_input():
    message = ''
    while message != "bye":
        message = input('Type "bye" to exit... ')


if __name__ == "__main__":
    main()
