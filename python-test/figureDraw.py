import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_list = ["./result/craq_write_rtt_3.txt","./result/craq_write_rtt_9.txt",
             "./result/ttl_write_rtt_3.txt","./result/ttl_write_rtt_9.txt"]
label_list = ["CRAQ Node 3", "CRAQ Node 9", "TTL Node 3", "TTL Node 9"]
title = "accuracy of low IP change frequency"
xlabel_name = "T/s"
ylabel_name = "RTT/ms"
xs_list = []
ys_list = []
y_coefficent = 100
save_name = "../../write_rtt_bold.png"
for i in range(len(file_list)):
    with open(file_list[i], 'r') as fd:
        data_list = fd.readlines()
        x_list = []
        y_list = []
        for j in range(len(data_list)):
            x, y = data_list[j].split(" ")
            x, y = float(x), float(y)
            x_list.append(x)
            y_list.append(y)
        xs_list.append(x_list)
        ys_list.append(y_list)

x = np.arange(0,61,5)
plt.figure(figsize=(8,5))
for i in range(len(xs_list)):
    plt.plot(np.array(xs_list[i]), np.array(ys_list[i])*y_coefficent,linewidth=3,label=label_list[i])

plt.xlabel(xlabel_name, fontsize=15,weight="bold")
plt.ylabel(ylabel_name, fontsize=15,weight="bold")
plt.tick_params(labelsize=13)
plt.legend()
# plt.title(title)
plt.xticks(x,weight="bold")
plt.yticks(weight="bold")
plt.savefig(save_name)
plt.show()