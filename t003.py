import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, skew, kurtosis
import matplotlib.font_manager as fm

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'  # Windows의 경우
# plt.rcParams['font.family'] = 'AppleGothic'  # macOS의 경우
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 깨짐 방지

# 데이터 생성
np.random.seed(0)
data_normal = np.random.normal(0, 1, 1000)  # 왜도가 작은 데이터
data_skewed = np.random.exponential(1, 1000)  # 왜도가 큰 데이터

# 왜도와 첨도 계산
normal_skewness = skew(data_normal)
normal_kurtosis = kurtosis(data_normal)
skewed_skewness = skew(data_skewed)
skewed_kurtosis = kurtosis(data_skewed)

# 히스토그램과 정규 분포의 PDF 그리기
fig, axes = plt.subplots(1, 2, figsize=(14, 7))

# 왜도가 작은 데이터
axes[0].hist(data_normal, bins=30, density=True, alpha=0.6, color='g', label='데이터 히스토그램')
xmin, xmax = axes[0].get_xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, np.mean(data_normal), np.std(data_normal))
axes[0].plot(x, p, 'k', linewidth=2, label='정규 분포 PDF')
axes[0].set_title(f'왜도가 작은 데이터\n왜도: {normal_skewness:.2f}, 첨도: {normal_kurtosis:.2f}')
axes[0].set_xlabel('값')
axes[0].set_ylabel('밀도')
axes[0].legend()

# 왜도가 큰 데이터
axes[1].hist(data_skewed, bins=30, density=True, alpha=0.6, color='g', label='데이터 히스토그램')
xmin, xmax = axes[1].get_xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, np.mean(data_skewed), np.std(data_skewed))
axes[1].plot(x, p, 'k', linewidth=2, label='정규 분포 PDF')
axes[1].set_title(f'왜도가 큰 데이터\n왜도: {skewed_skewness:.2f}, 첨도: {skewed_kurtosis:.2f}')
axes[1].set_xlabel('값')
axes[1].set_ylabel('밀도')
axes[1].legend()

plt.tight_layout()
plt.show()
