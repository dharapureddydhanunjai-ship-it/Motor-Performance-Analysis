import matplotlib.pyplot as plt
time=[0,1,2,3,4,5,6,7,8]
torque=[1.1,2.5,5.6,6.5,7.8,8.3,9.,6,10.2]
plt.plot(time,torque,marker='s',linestyle='solid',label='torque')
plt.xlabel("time(seconds)")
plt.ylabel("torque(N-m)")
plt.title("MOtor Analysis")
plt.axhline(y=8,color='red',linestyle='--')
plt.legend()
plt.grid(True)
plt.show()