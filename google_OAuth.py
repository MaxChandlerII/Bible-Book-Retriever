from httplib2 import Http
from oauth2client import client
from oauth2client import file
from oauth2client import tools

SCOPES = 'https://www.googleapis.com/auth/documents.readonly'

class G_OAuth:
    def __init__(self) -> None:
        pass

    def get_credentials():
        """Gets valid user credentials from storage.

        If nothing has been stored, or if the stored credentials are invalid,
        the OAuth 2.0 flow is completed to obtain the new credentials.

        Returns:
            Credentials, the obtained credential.
        """
        store = file.Storage('token.json')
        credentials = store.get()

        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
            credentials = tools.run_flow(flow, store)
        return credentials

    def get_authorized_http():
        '''Gets authorized http using valid credentials from storage

        Calls get_credentials() to get valid credentials

        Returns:
            authorized http
        '''
        credentials = G_OAuth.get_credentials()
        http = credentials.authorize(Http())

        return http