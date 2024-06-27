import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# 통계량 설정
mean = 0  # 평균
std_dev = 1  # 표준편차

# 히스토그램의 범위 설정
x_min = mean - 3 * std_dev
x_max = mean + 3 * std_dev
x = np.linspace(x_min, x_max, 100)

# 정규 분포의 PDF 계산
pdf = norm.pdf(x, mean, std_dev)

# 히스토그램 그리기
plt.plot(x, pdf, label='Normal Distribution')
plt.xlabel('Value')
plt.ylabel('Density')
plt.title('Histogram Approximation using Normal Distribution')
plt.legend()
plt.show()
