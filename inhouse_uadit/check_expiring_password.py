
import paramiko
p = paramiko.SSHClient()
cred = open("cred.csv","r")
for i in cred.readlines():
    line=i.strip()
    ls =line.split(",")

    #ip=ls[0].split(",")

    print(ls)
    # # ['10.150.117.26', 'rwadmin', 'Pr0jeCt@2018!']
    # # ['10.150.117.27', 'rwadmin', 'Pr0jeCt@2018!']
    # # ['10.150.117.28', 'rwadmin', 'Pr0jeCt@2018!']
    p.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    p.connect("%s"%ls[0],port =9052, username = "%s"%ls[1], password="%s"%ls[2])
    stdin, stdout, stderr = p.exec_command("sudo chage -l appadmin;lastlog |grep appadmin")
    opt = stdout.readlines()
    opt ="".join(opt)
    print(opt)
    temp=open("%s.txt"%ls[0],"w")
    temp.write(opt)
    temp.close()
cred.close()
p.close()