import pandas as pd
import plotly.express as px

# 엑셀 데이터 불러오기
df = pd.read_excel('수입(2020~2024) & 국산(2023~2024) 자동차 월별 통합.xlsx', sheet_name = 'Sheet2')

# '2020-01'처럼 연-월 형식의 열만 필터링
year_cols = df.columns[1:]

# 데이터를 long format(세로형)으로 변환
df_melted = df.melt(id_vars = 'Brand', value_vars = year_cols, 
                    var_name = 'YearMonth', value_name = 'Sales')
# 막대그래프 그리기
fig = px.bar(
    df_melted,
    x ='YearMonth',
    y ='Sales',
    color ='Brand',
    title ='연월별 브랜드별 판매량 (2020~2024)',
    barmode ='group',  # 같은 월 안에서 브랜드별 막대 나란히
    labels ={'Sales': '판매량(대)', 'YearMonth': '연월'}
)
# 그래프 옵션 조정
fig.update_layout(
    xaxis_tickangle = -45,
    yaxis_tickformat = ','
)
fig.show()
