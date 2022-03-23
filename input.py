import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='172.17.83.2',username='user',password='password',port=9052)
sftp_cient=ssh.open_sftp()
sftp_cient.get('/home/rwadmin/dormant-report', 'dormant-report')

sftp_cient.close()
ssh.close()