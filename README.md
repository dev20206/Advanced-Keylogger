# Advanced Keylogger Project

This project implements an advanced keylogger in Python, capable of logging keystrokes, capturing clipboard data, recording audio from the microphone, taking screenshots, and gathering system information. The project also includes functionality for encrypting and decrypting sensitive data using the Fernet encryption scheme.

## Files:

1. **keylogger.py**: 
   - This file contains the main implementation of the keylogger. It captures keystrokes, clipboard data, and system information, records audio, takes screenshots, and encrypts the captured data.
   - Usage: Run this script to start the keylogger. It will run in the background and capture data according to the specified parameters.

2. **decryptfile.py**:
   - This script decrypts the encrypted files generated by the keylogger using the Fernet encryption scheme.
   - Usage: Run this script to decrypt the encrypted files. Make sure to provide the correct encryption key.

3. **generatekey.py**:
   - This script generates a new encryption key using the Fernet encryption scheme and saves it to a file.
   - Usage: Run this script to generate a new encryption key and save it to a file. Use this key for encryption and decryption.

## Dependencies:

- `pynput`: Python library for monitoring and controlling input devices such as keyboards and mice.
- `win32clipboard`: Python extension for accessing the Windows clipboard.
- `scipy`: Scientific computing library for working with audio files.
- `sounddevice`: Library for recording audio from the microphone.
- `PIL`: Python Imaging Library for capturing screenshots.
- `cryptography`: Python library for encryption and decryption.

## Setup:

1. Install the required dependencies:
   ```bash
   pip install pynput win32clipboard scipy sounddevice pillow cryptography
   
Run generatekey.py to generate a new encryption key
- python generatekey.py

Update the key variable in keylogger.py with the generated key.

Run keylogger.py to start the keylogger:
- python keylogger.py

Optionally, run decryptfile.py to decrypt the encrypted files:
-python decryptfile.py


