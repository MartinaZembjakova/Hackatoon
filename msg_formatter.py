"""
This file contains the necessary functions and handlers for message formatting.
"""

def Bug (issue, name):
    return "(bug) " + issue + " - " + name + "\n" + "https://jira.solarwinds.com/browse/" + issue

def Closed (issue, name):
    return "(movie) " + issue + " - " + name + "\n" + "https://jira.solarwinds.com/browse/" + issue

if __name__=="__main__":
    print("Start formatting")
    print(Bug("Issue", "Name"))
    print("STOOOOOP")