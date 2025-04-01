col_names = ['과목번호', '과목명', '강의실', '시간수']
list1 = list([['c1', '인공지능개론', 'R1', 3],
          ['c2', '웃음치료', 'R2', 2],
          ['c3', '경영학', 'R3', 3],
          ['c4', '3D디자인', 'R4', 4],
          ['c5', '스포츠경영', 'R2', 2],
          ['c6', '예술의 세계', 'R3', 1]
          ])
import pandas as pd
df = pd.DataFrame(list1, columns=col_names)
df.to_csv('./timetable.csv', header=True, index=False, encoding='utf-8')

df2 = pd.read_csv('./timetable.csv', sep=',')
df2['교수'] = ['김예희', '오정현', '인세훈', '이새봄', '배유진', '이가원']
print(df2)

max_hour = df2.groupby(by=['강의실'],
  as_index=False)['시간수'].max()
max_hour
