import paramiko
import time
from getpass import getpass
import datetime
import os
dateTimeStamp = time.strftime('%y-%m-%d-%H-%M-%S')

SAVE_FILE = open('switch' +"_" + dateTimeStamp + ".txt" , 'w')

print(SAVE_FILE)