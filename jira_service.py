"""
This file contains all the necessary functions and handlers for JIRA integration.
"""
import sys
from urllib.parse import urljoin

import dateutil.parser
import requests

from settings import JIRA_USERNAME, JIRA_PASSWORD, JIRA_URL

LOGIN_URL = urljoin(JIRA_URL, 'rest/auth/1/session')
SEARCH_URL = urljoin(JIRA_URL, 'rest/api/2/search')


def initialise_session():
    """
    Initialises http session and cookie jar for REST API requests.
    :return: newly created session
    """
    session = requests.Session()
    # FIXME: handle correctly SSL certificates
    session.verify = False
    credentials = {"username": JIRA_USERNAME, "password": JIRA_PASSWORD}
    response = session.post(LOGIN_URL, json=credentials)
    if not response:
        print(response.content, file=sys.stderr)
        raise RuntimeError("Unable to log into JIRA.")
    return session


def close_session(session):
    session.delete(LOGIN_URL)


def parse_issue(issue):
    """
    Parses the given issue and returns only relevant fields
    :param issue: json encoded issue object
    :return: tuple containing relevant info
    """
    case = issue['key']
    summary = issue['fields']['summary']
    issue_type = issue['fields']['issuetype']['name']
    return case, summary, issue_type


def is_new(issue, last_update):
    """
    Returns boolean value whether the issue is newer than the last check.
    :param issue: json encoded issue object
    :param last_update: timestamp of last check
    :return: True if the issue is newer than last check
    """
    creation_date_string = issue['fields']['created']
    creation_date = dateutil.parser.parse(creation_date_string)
    return creation_date >= last_update


def list_new_issues(session, last_check, product_name):
    """
    Retrieves list of issues present in the JIRA for the given project.
    :param session: http session
    :param product_name: string with product name
    :return: list of json encoded issues
    """
    query = ('Product = "{product_name}" AND '.format(),
             'type = "Bug" AND '.format(),
             '((created >= "{last_check}")'.format(),
             'OR',
             '(updated >= "{last_check}" '.format(),
             'AND status = "closed"))')
    query = 'project = "{}"'.format(product_name)
    parameters = {'jql': query}
    response = session.get(SEARCH_URL, params=parameters)
    return response.json()
