import firebase_admin
from firebase_admin import credentials, messaging

# Path to your service account JSON file
SERVICE_ACCOUNT_PATH = "key.json"

# Initialize the Firebase Admin SDK
cred = credentials.Certificate(SERVICE_ACCOUNT_PATH)
firebase_admin.initialize_app(cred)

# The device token you want to send the notification to
device_token = "YOUR_DEVICE_TOKEN"

# Create a message payload with a notification and custom data (for routing)
message = messaging.Message(
    notification=messaging.Notification(
        title="Hello",
        body="This is a push notification sent from Firebase using Python!"
    ),
    data={
        "route": "/details",  # This could be any route your app can navigate to
        "extra_data": "Some additional data here"  # You can add any other custom data you need
    },
    token=device_token,
)

# Send the notification
response = messaging.send(message)

# Print the response
print(f"Successfully sent message: {response}")
