"""
This file contains the necessary functions and handlers for message formatting.
"""
from settings import JIRA_URL

BROWSE_URL = JIRA_URL + '/browse/'


def bug(case, summary):
    return "(bug) " + case + " - " + summary + "\n" + BROWSE_URL + case


def story(case, summary):
    return "(movie) " + case + " - " + summary + "\n" + BROWSE_URL + case


def other_types(case, summary):
    return "(computerrage) " + case + " - " + summary + "\n" + BROWSE_URL + case


def format_message(case, summary, issue_type, status):
    if issue_type == "Story":
        return story(case, summary)
    elif issue_type == "Bug":
        return bug(case, summary)
    else:
        return other_types(case, summary)
