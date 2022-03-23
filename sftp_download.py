import paramiko

#list of IPs
IPs=["172.17.83.2","172.17.83.35","172.17.83.36",]





for ip in IPs:
    try:
        file_name=ip+".csv"
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=ip,username='rwadmin',password='Pr0jeCt@2018!',port=9052)
        sftp_cient=ssh.open_sftp()
        sftp_cient.get('/home/rwadmin/dormant-report', file_name)

        sftp_cient.close()
        ssh.close()
        print("Sucess : ", ip)
    except:
        print("There is a problem : ", ip)

