"""
This file contains all the necessary functions and handlers for JIRA integration.
"""
import sys

import requests

from settings import JIRA_USERNAME, JIRA_PASSWORD, JIRA_URL, MAX_RESULTS, JIRA_SSL_CERTIFICATE

LOGIN_URL = JIRA_URL + '/rest/auth/1/session'
SEARCH_URL = JIRA_URL + '/rest/api/2/search'


def initialise_session():
    """
    Initialises http session and cookie jar for REST API requests.
    :return: newly created session
    """
    session = requests.Session()
    # FIXME: handle correctly SSL certificates
    session.verify = JIRA_SSL_CERTIFICATE
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
    status = issue['fields']['status']['name']
    return case, summary, issue_type, status


def list_new_issues(session, last_check, project_name, issue_type):
    """
    Retrieves list of issues present in the JIRA for the given project.
    :param session: http session
    :param last_check: date of the last check for new issues
    :param project_name: string with product name
    :param issue_type: string with issue type
    :return: list of json encoded issues
    """
    last_check_formated = last_check.strftime("%Y-%m-%d %H:%M")
    query = 'Project = "{product_name}" AND '.format(product_name=project_name) + \
            'type = "{issue_type}" AND '.format(issue_type=issue_type) + \
            '((created >= "{last_check}") '.format(last_check=last_check_formated) + \
            'OR ' + \
            '(updated >= "{last_check}" '.format(last_check=last_check_formated) + \
            'AND status = "Closed"))'
    parameters = {'jql': query, 'maxResults': MAX_RESULTS}
    response = session.get(SEARCH_URL, params=parameters)
    return response.json()['issues']
