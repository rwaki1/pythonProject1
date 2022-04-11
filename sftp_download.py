import paramiko

#list of IPs
IPs=["10.150.95.61","10.150.95.62","10.150.95.63","10.150.95.64","10.150.95.65","10.150.95.66"]

for ip in IPs:
    try:
        file_name=ip+".csv"
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=ip,username='rwadmin',password='Exchange@2017!',port=9052)
        sftp_cient=ssh.open_sftp()
        sftp_cient.get('/home/rwadmin/dormant-report', file_name)

        sftp_cient.close()
        ssh.close()
        print("Sucess : ", ip)
    except:
        print("There is a problem : ", ip)

