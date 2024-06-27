import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_histogram(column_name):
    # CSV 파일 로드
    df2 = pd.read_csv('epindex00.csv')

    #########################################
    ## 그래프 출력용으로 복사
    #df2 = df.copy()

    # gap_sec 열의 빈 값을 NaN으로 처리
    df2[column_name].replace('', np.nan, inplace=True)
    # NaN 값을 가진 행 제거
    df2.dropna(subset=[column_name], inplace=True)
    # gap_sec 열을 정수형으로 변환
    df2[column_name] = df2[column_name].astype(int)

    # gap_sec 열의 히스토그램 그리기
    plt.figure(figsize=(10, 6))
    #plt.hist(df2['gap_sec'], bins=30, color='skyblue', edgecolor='black')
    plt.hist(df2[column_name], bins=np.arange(df2[column_name].min(), df2[column_name].max() + 1, 1), color='skyblue', edgecolor='black')
    plt.title('Histogram of gap_sec')
    plt.xlabel(column_name)
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.tight_layout()
    plt.show()


plot_histogram('gap_sec')
