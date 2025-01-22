import firebase_admin
from firebase_admin import credentials, messaging

# Path to your service account JSON file
SERVICE_ACCOUNT_PATH = "key.json"

# Initialize the Firebase Admin SDK
cred = credentials.Certificate(SERVICE_ACCOUNT_PATH)
firebase_admin.initialize_app(cred)

# The device token you want to send the notification to
device_token = "YOUR_DEVICE_TOKEN"

# Create a message payload
message = messaging.Message(
    notification=messaging.Notification(
        title="Hello",
        body="This is a push notification sent from Firebase using Python!"
    ),
    token=device_token,
)

# Send the notification
response = messaging.send(message)

# Print the response
print(f"Successfully sent message: {response}")
