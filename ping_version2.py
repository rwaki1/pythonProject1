import os
results_file = open("result.txt", "w")
ip_list = ["10.150.91.90","10.150.91.91","10.150.91.89","10.150.94.61","10.150.94.62","10.150.94.63","10.150.94.64","10.150.94.65","10.150.94.66","10.150.95.86","10.150.96.80","10.150.96.145","10.150.96.146","10.150.95.105","10.150.96.81","10.150.96.29","10.150.96.30","10.150.96.27","10.150.96.28","10.150.96.154","10.150.96.117"
]
len(ip_list)
 
#for ip in ipip_list:
 #   ip_list.append("10.150.90." + str(ip))
#print(len(ip_list))
for ip in ip_list:
    response = os.popen(f"ping {ip} -n 1").read()
    if "Received =1" and "Approximate" in response:
        results_file.write(f"UP {ip} Ping Successful" + "\n")
    else:
        results_file.write(f"DOWN {ip} Ping Unsuccessful" + "\n")
results_file.close()
exit()
