#csv 라이브러리 가져오기
import csv
#CSV 파일 불러오기
f = open('weather.csv', 'w', newline = '')
#CSV 파일 작성할 준비하기
wr = csv.writer(f)
#데이터를 한 행씩 작성하기
wr.writerow(['날짜', '요일', '날씨', '최저기온', '최고기온', '강수량'])
wr.writerow(['20230101', '월', '맑음', '-4.3', '3.8', '0'])
wr.writerow(['20230102', '화', '맑음', '-7.4', '0.4', '0'])
wr.writerow(['20230103', '수', '맑음', '-9.0', '0.6', '0'])
#f 변수의 자원 반환하기
f.close( )
