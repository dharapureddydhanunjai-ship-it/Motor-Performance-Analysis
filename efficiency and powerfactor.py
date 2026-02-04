import matplotlib.pyplot as plt
output_power=[0,500,1000,1500,2000,2500,3000]
efficiency=[0,65,82,88,89,87,84]
power_factor=[0.2,0.45,0.68,0.82,0.88,0.90,0.91]
fig,ax1=plt.subplots()
ax1.set_xlabel("Output Power(in watts)")
ax1.set_ylabel("Efficiency")
line1=ax1.plot(output_power,efficiency,marker='D',linestyle='solid',label='efficiency',color='orange')
ax1.set_ylim(0,100)
ax1.tick_params(axis='y',color='orange')
ax1.annotate('Peak Efficiency (89%)', 
             xy=(2000, 89),        # The arrow points to this data point
             xytext=(2200, 95),    # The text is placed at these coordinates
             arrowprops=dict(facecolor='black', shrink=0.05, width=2))
ax2=ax1.twinx()
ax2.set_ylabel("Power Factor")
line2=ax2.plot(output_power,power_factor,marker='p',linestyle='solid',label='power factor',color='pink')
ax2.set_ylim(0,1)
ax2.tick_params(axis='y',color='pink')
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1+lines2, labels1+labels2, loc='lower right')
plt.title("Induction Motor Performance: Efficiency & Power Factor vs. Load")
plt.grid(True,alpha=0.2)
plt.show()