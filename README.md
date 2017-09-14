# Hackatoon 
## Jira on skype

You will need a JIRA account and a special Skype account, that will be added into the chat you want to see your information in. The logon names and passwords will need to be set in enviroment variables.

### Enviroment variables
In windows command line: SET variable_name = "value"

In bash: export variable_name = "value"

#### Variables to be set
You will need to set at least all the variables in settings.py, that do not have default value set.
1. JIRA_URL needs to be set to https://jira.solarwinds.com without the slash at the end.
2. CHAT_INVITE_URL is the entire url the Skype chat generates
3. MAX_RESULTS needs to be high enough so that you don't get more cases than that in the time period.

### Necessary preconditions
You need to have the same time zone on Jira and on your device.
