import requests
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


coinbase_api = 'https://api.pro.coinbase.com'


def entry_point_function(request):
    '''List all individual steps as disparate function calls'''
    result = {}
    request_json = request.get_json()
    result['request'] = request_json
    # result.update(get_coinbase_test())
    result.update(get_coinbase_time())
    result.update(google_sheets_quickstart())
    return result


def get_coinbase_test():
    response = requests.get(coinbase_api)
    try:
        return {'coinbase_test': response.json()['message']}
    except Exception as e:
        print(e)


def get_coinbase_time():
    response = requests.get(coinbase_api + '/time')
    try:
        coinbase_time = {}
        response_json = response.json()
        coinbase_time['coinbase_epoch'] = response_json['epoch']
        coinbase_time['coinbase_iso'] = response_json['iso']
        return coinbase_time
    except Exception as e:
        print(e)


def google_sheets_quickstart():
    # If modifying these scopes, delete the file token.pickle.
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

    # The ID and range of a sample spreadsheet.
    SAMPLE_SPREADSHEET_ID = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'
    SAMPLE_RANGE_NAME = 'Class Data!A2:E'

    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])

    if not values:
        result = {'google_sheets': 'No data found'}
    else:
        result = {
            'google_sheets': [{'Name': row[0], 'Major': row[4]} for row in values]
        }
    return result
