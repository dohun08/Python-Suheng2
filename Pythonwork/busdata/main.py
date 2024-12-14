from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.responses import StreamingResponse
import matplotlib.pyplot as plt
import csv
import os
import io

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 도메인 허용. 보안을 위해 필요한 도메인만 추가하세요.
    allow_credentials=True,
    allow_methods=["*"],  # 모든 HTTP 메서드 허용 (GET, POST, PUT, DELETE 등)
    allow_headers=["*"],  # 모든 HTTP 헤더 허용
)
site = {}
def CSVdata(n) :
    #uvicorn 으로 할때는 ./traffic_data_20231231.csv 이거
    #docekr 로 할때는 /app/traffic_data_20231231.csv 이거
    f =  open('/app/traffic_data_20231231.csv', mode = 'rt', encoding = 'CP949')
    reader = csv.reader(f, delimiter = ',')
    result = []
    for line in reader:
        gu = line[0]
        site[gu] = (line[3])
        result.append(site)
    f.close()
    
    updated_data = {
    'Category': site['구분1'], 
    'Seoul': site['서울'].strip(),
    'Busan': site['부산'].strip(),
    'Daegu': site['대구'].strip(),
    'Incheon': site['인천'].strip(),
    'Gwangju': site['광주'].strip(),
    'Daejeon': site['대전'].strip(),
    'Ulsan': site['울산'].strip(),
    'Sejong': site['세종'].strip(),
    'Gyeonggi': site['경기'].strip(),
    'Gangwon': site['강원'].strip(),
    'North Chungcheong': site['충북'].strip(),
    'South Chungcheong': site['충남'].strip(),
    'North Jeolla': site['전북'].strip(),
    'South Jeolla': site['전남'].strip(),
    'North Gyeongsang': site['경북'].strip(),
    'South Gyeongsang': site['경남'].strip(),
    'Jeju': site['제주'].strip()
}
    formatted_data = [
    {"name": "서울", "value": int(updated_data['Seoul'])},
    {"name": "경기", "value": int(updated_data['Gyeonggi'])},
    {"name": "부산", "value": int(updated_data['Busan'])},
    {"name": "인천", "value": int(updated_data['Incheon'])},
    {"name": "대구", "value": int(updated_data['Daegu'])},
    {"name": "경상남도", "value": int(updated_data['South Gyeongsang'])},
    {"name": "대전", "value": int(updated_data['Daejeon'])},
    {"name": "충청남도", "value": int(updated_data['South Chungcheong'])},
    {"name": "광주", "value": int(updated_data['Gwangju'])},
    {"name": "경상북도", "value": int(updated_data['North Gyeongsang'])},
    {"name": "울산", "value": int(updated_data['Ulsan'])},
    {"name": "전라남도", "value": int(updated_data['South Jeolla'])},
    {"name": "충청북도", "value": int(updated_data['North Chungcheong'])},
    {"name": "전라북도", "value": int(updated_data['North Jeolla'])},
    {"name": "제주", "value": int(updated_data['Jeju'])},
    {"name": "강원", "value": int(updated_data['Gangwon'])},
    {"name": "세종", "value": int(updated_data['Sejong'])}
]

    if n :
        return formatted_data
    else :
        return updated_data


@app.get('/api/rank')
def main() :
    return CSVdata(1)

sum = 0
@app.get("/api/graph")
async def create_graph(n=0):
    global sum
    # 데이터 예시
    updated_data = CSVdata(0)


    data = {}
    for key, value in updated_data.items():
        if value != "일요일":
            data[key] = int(value)
            sum+=int(value)

    # 차트 생성
    plt.figure(figsize=(10, 6))
    bars = plt.bar(data.keys(), data.values(), label='이용수', color="skyblue")
    plt.yticks(ticks=range(0, max(data.values()) + 100000, 100000),
               labels=range(0, max(data.values()) + 100000, 100000))
    plt.xlabel('지역')
    plt.ylabel('이용수')
    plt.legend()

    # 이미지 저장
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)  # 파일 포인터를 처음으로 되돌림
    plt.close()  # 그래프 닫기
    if n :
        return data
    else :
     return StreamingResponse(buf, media_type="image/png")


@app.get("/api/graph2")
async def create_graph2():
    
    global sum
    # 데이터 예시
    data = await create_graph(1)
    labels = list(data.keys())
    sizes = [value for value in data.values()]

    # 원형 그래프 생성
    textprops = {'fontsize': 18}
    plt.figure(figsize=(18, 14))
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue',
              'mediumseagreen', 'salmon', 'plum', 'tan',
              'skyblue', 'lightpink', 'orange', 'peachpuff',
              'lightgrey', 'lavender', 'powderblue', 'khaki', 'lightyellow']

    plt.pie(sizes, labels=labels, colors=colors,
            autopct=lambda p: '{:.0f}%'.format(p) if p > 5 else '',  # 5% 이하의 퍼센트는 숨김
            startangle=100, textprops={'fontsize': 30},
            labeldistance=1.1)  # 레이블과 원의 중심 간 거리

    plt.axis('equal')  # Equal aspect ratio ensures that pie chart is a circle.

    # 이미지 저장
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)  # 파일 포인터를 처음으로 되돌림
    plt.close()  # 그래프 닫기

    return StreamingResponse(buf, media_type="image/png")