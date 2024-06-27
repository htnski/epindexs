import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, skew, kurtosis
import matplotlib.font_manager as fm

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'  # Windows의 경우
# plt.rcParams['font.family'] = 'AppleGothic'  # macOS의 경우
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 깨짐 방지

# 통계량 설정
mean = 0  # 평균
std_dev = 1  # 표준편차
data = np.random.normal(mean, std_dev, 1000)

# 왜도와 첨도 계산
data_skewness = skew(data)
data_kurtosis = kurtosis(data)

# 히스토그램과 정규 분포의 PDF 그리기
plt.hist(data, bins=30, density=True, alpha=0.6, color='g', label='데이터 히스토그램')
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mean, std_dev)
plt.plot(x, p, 'k', linewidth=2, label='정규 분포 PDF')

# 왜도와 첨도 출력
plt.title(f'왜도: {data_skewness:.2f}, 첨도: {data_kurtosis:.2f}')
plt.xlabel('값')
plt.ylabel('밀도')
plt.legend()
plt.show()
