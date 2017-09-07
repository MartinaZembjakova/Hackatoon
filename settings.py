"""
This file contains application settings and default presets.
"""
import os

# Skype credentials and settings
SKYPE_USERNAME = os.environ.get("SKYPE_USERNAME")
SKYPE_PASSWORD = os.environ.get("SKYPE_PASSWORD")
CHAT_INVITE_URL = os.environ.get("INVITE_URL")

# Jira credentials and settings
JIRA_USERNAME = os.environ.get("JIRA_USERNAME")
JIRA_PASSWORD = os.environ.get("JIRA_PASSWORD")
JIRA_URL = os.environ.get("JIRA_URL")