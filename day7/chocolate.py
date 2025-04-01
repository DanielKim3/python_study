import numpy as np
data = np.loadtxt('chocolate_rating.csv', delimiter=',')
print('차원:', data.ndim)
print('모양:', data.shape)
print('원소 수:', data.size)
print(data)

ratings_mean = data[:,3].mean( )
print(ratings_mean)

high_level = data[data[:,3] >= 4]
high_id = high_level[:,0].astype(np.int64)
print('우수 초콜릿 수:', high_id.size)
print(high_id)

high_kakao = high_level[:,2]
unique_values, value_counts = np.unique(high_kakao, return_counts = True)
print(unique_values)
print('카카오 함유량:', unique_values)
print('함유량별 빈도수:', value_counts)

max_index = np.argmax(value_counts)
print(unique_values[max_index])
print('우수 초콜릿', high_id.size, '가지 중', value_counts[max_index],\
  '가지의 카카오 함유량이',unique_values[max_index] * 100,  '%입니다.')
