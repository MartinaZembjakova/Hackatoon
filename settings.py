"""
This file contains application settings and default presets.
"""
import os

# Skype credentials and settings
SKYPE_USERNAME = os.environ.get("SKYPE_USERNAME")
SKYPE_PASSWORD = os.environ.get("SKYPE_PASSWORD")
CHAT_INVITE_URL = os.environ.get("CHAT_INVITE_URL")

# Jira credentials and settings
JIRA_USERNAME = os.environ.get("JIRA_USERNAME")
JIRA_PASSWORD = os.environ.get("JIRA_PASSWORD")
JIRA_URL = os.environ.get("JIRA_URL")
MAX_RESULTS = int(os.environ.get("MAX_RESULTS", "50"))
PROJECT_NAME = os.environ.get("PROJECT_NAME", "Log & Event Manager")
ISSUE_TYPES = os.environ.get("ISSUE_TYPES", ("Bug", "Story"))
JIRA_SSL_CERTIFICATE = os.environ.get("JIRA_SSL_CERTIFICATE", True)
if JIRA_SSL_CERTIFICATE == "False":
    JIRA_SSL_CERTIFICATE = False

# Others settings
TIMEOUT = int(os.environ.get("TIMEOUT", "300"))
LOG_FILE = os.environ.get("LOG_FILE", "jira2skype.log")
