import firebase_admin
from firebase_admin import credentials, messaging

# Path to your service account JSON file
SERVICE_ACCOUNT_PATH = "key.json"

# Initialize the Firebase Admin SDK
cred = credentials.Certificate(SERVICE_ACCOUNT_PATH)
firebase_admin.initialize_app(cred)

# The device token you want to send the notification to
device_token = "f1wXRA_OSa-8KSjM_V_vKY:APA91bEWtM5Oyf8SYiUh7WS54kmxQubl6KWxlTbBaZ6RG6kJcm32vwQjkqKmia60GHDo-quD2NgD72VVdYX9PBsJLv-2yxeR4WaQCozPh0mfLJVVUPIDDWE"

# Create a message payload with a notification and custom data (for routing)
message = messaging.Message(
    notification=messaging.Notification(
        title="Hello",
        body="This is a push notification sent from Firebase using Python!"
    ),
    data={
        "n_action": "rewards",  # This could be any route your app can navigate to
        "extra_data": "Some additional data here"  # You can add any other custom data you need
    },
    token=device_token,
)

# Send the notification
response = messaging.send(message)

# Print the response
print(f"Successfully sent message: {response}")
