import matplotlib.pyplot as plt
import numpy

plt.plot([1, 2, 3], [4, 5, 6])
plt.show()

plt.plot([5, 3, 4, 2, 5, 6])
plt.plot([10, 4, 3, 2, 8, 4])
plt.show()


# 객체 지향 방식으로 그리기
y1=[1, 3, 2, 4, 1, 3]
y2=[4, 5, 6, 2, 5, 2]
fig, axes= plt.subplots(1, 2)

axes[0].plot(y1, label='00')
axes[0].plot(y2, label='11')
axes[0].legend(loc=(0.5, 0.5))

axes[1].plot(y1)

axes[1].plot(y2)
fig.tight_layout()

plt.show()
