#graph sheet and stationery
import matplotlib.pyplot as plt
#data
time=[0,5,10,15,20,25,30]
motor_temperature=[30,45,60,75,85,92,95]
efficiency=[92,90,88,85,82,79,75]
#graph1
fig,ax1=plt.subplots()
line1=ax1.plot(time,motor_temperature,color='blue',linestyle='solid',marker='o',label='temperature')
ax1.set_xlabel("Time(seconds)")
ax1.set_ylabel("Temperature(degrees)")
ax1.tick_params(axis='y',labelcolor='blue')
ax1.axhline(y=90,color='red',linestyle='--')
ax1.set_ylim(20,110)
#second graph
ax2=ax1.twinx()
ax2.set_ylabel("Efficiency")
line2=ax2.plot(time,efficiency,color='green',linestyle='solid',marker='s',label='efficiency')
ax2.tick_params(axis='y',labelcolor='green')
ax2.set_ylim(70,100)
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1+lines2, labels1+labels2, loc='upper right')
#Title
plt.title("Motor Thermal vs Efficiency Analysis")
#final command
plt.grid(True,alpha=0.2)
plt.show()

