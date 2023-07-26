import firebase_admin
from firebase_admin import credentials, messaging
from .models import FCMToken
import requests
import json
def send_fcm_notification(fcm_token, title, message):
    # Get the FCM token associated with the user from the database
    
    # Initialize Firebase Admin SDK (replace '/path/to/serviceAccountKey.json' with your actual service account key path)
    serverToken = 'AAAA2ItrorI:APA91bH2lxWX15M__JURVwJkX8erwz1PW5slVex1HiiDxxdatS6ItOKxGi_y9KYkDG2UMZsMHf6qlrLzsAbUNmGCZLiZUOXO0DfzvWKtG3AjtdsoeV8FWr1VbJV92jGxMOogJ7XKsEU_'
            #deviceToken = 'fCGE9X4MYCXUwRoAgkVEjr:APA91bGmuPDtCfx9un8ueAzT2T3t_28UlmHOls89eJY10a4O5WtQSvCmvzeaZQtberUt_o26CRwzjWni9C_muUp8gH4JQqQfLmdC7dkIBUgAegDSXwbdRaGSTFIfv-u-DXKNsK5kRT-v'

    headers = {
            'Content-Type': 'application/json',
            'Authorization': 'key=' + serverToken,
        }

    body = {
            'notification': {'title': title,
                                'body': message
                                },
            'to':
                fcm_token,
            'priority': 'high',
            #   'data': dataPayLoad,
            }
    response = requests.post("https://fcm.googleapis.com/fcm/send",headers = headers, data=json.dumps(body))
    print(response.status_code)

    print(response.json())
