import os
results_file = open("result.txt", "w")
ip_list = []
len(ip_list)
for ip in range(1, 256):
    ip_list.append("10.150.95." + str(ip))
print(len(ip_list))
for ip in ip_list:
    response = os.popen(f"ping {ip} -n 2").read()
    if "Received =1" and "Approximate" in response:
        results_file.write(f"UP {ip} Ping Successful" + "\n")
    else:
        results_file.write(f"DOWN {ip} Ping Unsuccessful" + "\n")
results_file.close()
exit()
