"""
This file contains application settings and default presets.
"""
import os

# Skype credentials and settings
SKYPE_USENAME = os.environ.get("skype_username")
SKYPE_PASSWORD = os.environ.get("skype_password")
CHAT_INVITE_URL = os.environ.get("invite_url")

# Jira credentials and settings
JIRA_USERNAME = os.environ.get("jira_username")
JIRA_PASSWORD = os.environ.get("jira_password")
JIRA_URL = os.environ.get("jira_url")