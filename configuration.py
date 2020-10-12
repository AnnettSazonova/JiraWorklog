import os
import configparser


class Credential ():
    login: str
    api_key: str
    server_url: str

    def __init__(self):
        """Constructor"""
        pass


def init_config():
    """Read or create configuration"""
    credential = Credential ()
    if os.path.isfile ('./config.ini'):
        read_config (credential)
    else:
        _create_config (credential)

    return credential


def read_config(credential: Credential):
    """Read configuration from ini file"""
    config = configparser.ConfigParser ()
    config.sections ()
    config.read ('config.ini')
    credential.login = config['DEFAULT']['Login']
    credential.api_key = config['DEFAULT']['ApiKey']
    credential.server_url = config['DEFAULT']['Server']


def _create_config(credential: Credential):
    """If ini file doesn't exist create one"""
    credential.login = input ('Enter 1st JIRA user name: ')
    credential.api_key = input ('Enter 1st Jira API key: ')
    credential.server_url = input ('Enter 1st Jira URI:')

    credential.login2 = input ('Enter 2nd JIRA user name: ')
    credential.api_key2 = input ('Enter 2nd Jira API key: ')
    credential.server_url2 = input ('Enter 2nd Jira URI:')

    config = configparser.ConfigParser ()
    config['DEFAULT'] = {'Login': credential.login,
                         'ApiKey': credential.api_key,
                         'Server': credential.server_url}
    config['SECOND'] = {'Login': credential.login2,
                         'ApiKey': credential.api_key2,
                         'Server': credential.server_url2}
    with open ('config.ini', 'w') as configfile:
        config.write (configfile)
