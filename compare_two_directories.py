#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Download file resources from remote server to local through paramiko
author: Etienne Rwakineza
time: 2022-04-27
"""

import paramiko
import os
from stat import S_ISDIR as isdir


def down_from_remote(sftp_obj, remote_dir_name, local_dir_name):
    "" "download files remotely" ""
    remote_file = sftp_obj.stat(remote_dir_name)
    if isdir(remote_file.st_mode):
        # Folder, can't download directly, need to continue cycling
        check_local_dir(local_dir_name)
        print('Start downloading folder: ' + remote_dir_name)
        for remote_file_name in sftp.listdir(remote_dir_name):
            sub_remote = os.path.join(remote_dir_name, remote_file_name)
            sub_remote = sub_remote.replace('\\', '/')
            sub_local = os.path.join(local_dir_name, remote_file_name)
            sub_local = sub_local.replace('\\', '/')
            down_from_remote(sftp_obj, sub_remote, sub_local)
    else:
        # Files, downloading directly
        print('Start downloading file: ' + remote_dir_name)
        sftp.get(remote_dir_name, local_dir_name)


def check_local_dir(local_dir_name):
    "" "whether the local folder exists, create if it does not exist" ""
    if not os.path.exists(local_dir_name):
        os.makedirs(local_dir_name)


if __name__ == "__main__":
    "" "program main entry" ""

    # dictionary for IP and directory
dic = {}
dic["10.150.117.26"] = "/home/rwadmin"
dic["10.150.117.27"] = "/home/rwadmin"

# looping through all of IP
for IP in dic.keys():
    # Server connection information
    host_name = IP
    user_name = 'rwadmin'
    password = 'Pr0jeCt@2018!'
    port = 9052
    # Remote file path (absolute path required)
    remote_dir = dic[IP]
    # Local file storage path (either absolute or relative)
    eachIP = os.makedirs(IP)
    #local_dir =  sftp.chdir(eachIP)
    local_dir = ('C:\\Users\\rwakine\\PycharmProjects\\pythonProject1\\'+ str(IP) )
    print(local_dir)
    # Connect to remote server
    t = paramiko.Transport((host_name, port))
    t.connect(username=user_name, password=password)
    sftp = paramiko.SFTPClient.from_transport(t)

    # Remote file start download
    down_from_remote(sftp, remote_dir, local_dir)

    # Close connection
    t.close()