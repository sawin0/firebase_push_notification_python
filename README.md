# Firebase Push Notification Sender (Python)

This Python script demonstrates how to send push notifications using Firebase Cloud Messaging (FCM). It uses the Firebase Admin SDK to authenticate with Firebase, construct a notification message, and send it to a specific device.

## Prerequisites

Before using this script, make sure you have the following:

1. **Firebase Project**: A Firebase project set up in the [Firebase Console](https://console.firebase.google.com/).
2. **Firebase Service Account Key**: Download your Firebase service account key in JSON format from the Firebase Console.
3. **Firebase Admin SDK**: The script utilizes the Firebase Admin SDK to send notifications.

### Install Dependencies

The script requires the following Python packages:

- **firebase-admin**: Firebase Admin SDK to interact with Firebase services.

You can install the required dependencies using `pip`:

```bash
pip install firebase-admin
```

## Setup

1. **Download the Service Account Key**:
   - In the Firebase Console, go to **Project Settings** > **Service Accounts**.
   - Generate a new private key and download the JSON file.
   - Save this JSON file somewhere on your machine.

2. **Update the Service Account Path**:
   - In the script, replace the value of `SERVICE_ACCOUNT_PATH` with the path to your downloaded service account JSON file.
   ```python
   SERVICE_ACCOUNT_PATH = "path/to/your/service_account_key.json"
   ```

3. **Set Device Token**:
   - Replace `"YOUR_DEVICE_TOKEN"` with the FCM device token of the device you want to send the notification to. This token is typically generated on the client side (in your mobile app) after registering for push notifications with Firebase.

   ```python
   device_token = "YOUR_DEVICE_TOKEN"
   ```

4. **Notification Content**:
   - The script sends a simple notification with a title and body message. You can modify the `title` and `body` to suit your needs.

   ```python
   title="Hello"
   body="This is a push notification sent from Firebase using Python!"
   ```

## Usage

### Run the Script

Once the setup is complete, you can run the script from the command line or your IDE:

```bash
python send_push_notification.py
```

The script will initialize the Firebase Admin SDK, send a push notification to the specified device, and print a success message with the message ID.

### Example Output

When the notification is successfully sent, you will see output like this:

```bash
Successfully sent message: projects/your-project-id/messages/your-message-id
```

This confirms that the notification was sent to the device.

## Code Explanation

- **Service Account Authentication**: The Firebase Admin SDK is initialized using the credentials provided in the service account JSON file.
- **Message Construction**: A message payload is created with a notification (title and body). The message is then associated with the target device token.
- **Send Notification**: The notification is sent using `messaging.send()`, and the response (message ID) is printed to the console.

### Error Handling

The script doesn't include explicit error handling. In production, you should handle potential errors (e.g., invalid device token, network issues, etc.). You can extend the script by wrapping the `messaging.send()` call in a `try-except` block for more robust error handling.

## Example Error Handling (Optional)

```python
try:
    response = messaging.send(message)
    print(f"Successfully sent message: {response}")
except Exception as e:
    print(f"Error sending message: {e}")
```

### Common Issues:

1. **Invalid Device Token**: Ensure that the device token is correct. Device tokens are unique to each instance of your app and can expire or be rotated.
2. **Service Account Authentication**: Ensure that the service account key JSON file is valid and has the required permissions.
3. **Firebase Permissions**: Make sure that your Firebase project has the correct FCM permissions enabled.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
