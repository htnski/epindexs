import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# CSV 파일 로드
df = pd.read_csv('epindex.csv')

# 특정 열 선택
description_series = df['Time']

# 문자열 추출 함수 (MID 함수와 유사)
def mid(string, start, length):
    if isinstance(string, str):
        if start > 0:
            start -= 1
        return string[start:start+length]
    return ''

# 문자열 추출 적용
df['_Year'] = description_series.apply(lambda x: mid(x, 1, 4))
df['_Month'] = description_series.apply(lambda x: mid(x, 5, 2))
df['_Day'] = description_series.apply(lambda x: mid(x, 7, 2))
df['_Hour'] = description_series.apply(lambda x: mid(x, 9, 2))
df['_Min'] = description_series.apply(lambda x: mid(x, 12, 2))
df['_Sec'] = description_series.apply(lambda x: mid(x, 15, 2))

df['gap_sec'] = ''

print("Processing data...")
for index, row in df.iterrows():
    if index > 0:
        rowp = df.iloc[index - 1]

        if row['dir'] == 'Recv' and row['CMD'] == rowp['CMD'] and rowp['dir'] == 'Send':
            recv_time = pd.Timestamp(int(row['_Year']),int(row['_Month']),int(row['_Day']),int(row['_Hour']),int(row['_Min']),int(row['_Sec']))
            send_time = pd.Timestamp(int(rowp['_Year']),int(rowp['_Month']),int(rowp['_Day']),int(rowp['_Hour']),int(rowp['_Min']),int(rowp['_Sec']))
            diff_sec = (recv_time - send_time).total_seconds()
            df.at[index, 'gap_sec'] = int(diff_sec)




    # 매 1000줄마다 "-" 출력
    if index % 1000 == 0:
        print("-", end='', flush=True)        

# 처리 완료 메시지 출력
print("\nProcessing complete.")

# 결과 저장
df.to_csv('epindex00.csv', index=False)

# 결과 출력
print(df.head(5))

'''
#########################################
# 그래프 출력용으로 복사
df2 = df.copy()
# gap_sec 열의 빈 값을 NaN으로 처리
df2['gap_sec'].replace('', np.nan, inplace=True)
# NaN 값을 가진 행 제거
df2.dropna(subset=['gap_sec'], inplace=True)
# gap_sec 열을 정수형으로 변환
df2['gap_sec'] = df2['gap_sec'].astype(int)

# gap_sec 열의 히스토그램 그리기
plt.figure(figsize=(10, 6))
#plt.hist(df2['gap_sec'], bins=30, color='skyblue', edgecolor='black')
plt.hist(df2['gap_sec'], bins=np.arange(df2['gap_sec'].min(), df2['gap_sec'].max() + 1, 1), color='skyblue', edgecolor='black')
plt.title('Histogram of gap_sec')
plt.xlabel('gap_sec')
plt.ylabel('Frequency')
plt.grid(True)
plt.tight_layout()
plt.show()
'''

