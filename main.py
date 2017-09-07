"""
This file contains main function for running the application itself.
"""
from datetime import datetime, timedelta
from time import sleep

from msg_formatter import format_message
import jira_service
from settings import SKYPE_USERNAME, SKYPE_PASSWORD, CHAT_INVITE_URL, PROJECT_NAME
from skype_service import sendMessage, openChat, logIn


def main():
    skype = logIn(SKYPE_USERNAME, SKYPE_PASSWORD)
    skype_chat = openChat(skype, CHAT_INVITE_URL)
    last_check = datetime.now() - timedelta(1)
    session = jira_service.initialise_session()
    for _ in range(5):
        print("Doing check...")
        new_last_check = datetime.now()
        do_check(last_check, session, skype_chat)
        last_check = new_last_check
        sleep(300)
    jira_service.close_session(session)


def do_check(last_check, session, skype_chat):
    issues = jira_service.list_new_issues(session, last_check, PROJECT_NAME)
    for issue in issues:
        case, summary, issue_type, status = jira_service.parse_issue(issue)
        message = format_message(case, summary, issue_type, status)
        sendMessage(skype_chat, message)


if __name__ == "__main__":
    main()
