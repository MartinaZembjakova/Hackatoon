"""
This file contains all the necessary functions and handlers for JIRA integration.
"""
import requests

from settings import JIRA_USERNAME, JIRA_PASSWORD, JIRA_URL


def inicalize_session():
    session = requests.Session()
    credentials = {"username": JIRA_USERNAME, "password": JIRA_PASSWORD}
    session.post('https://jira-stage.solarwinds.com/rest/auth/1/session', json=credentials)
    return session


