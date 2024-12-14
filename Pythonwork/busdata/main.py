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
    f =  open('./한국교통안전공단_대중교통 이용인원 현황_20231231.csv', mode = 'rt', encoding = 'CP949')
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

@app.get("/api/data/{image_name}")
def get_image(image_name: str):
    # images 폴더의 경로를 설정합니다.
    image_path = os.path.join("images", image_name)
    print(image_path)
    # 파일이 존재하는지 확인합니다.
    if os.path.isfile(image_path):
        return FileResponse(image_path, media_type='image/png')
    else:
        return {"error": "Image not found."}
    
    
@app.get("/api/graph")
async def create_graph():
    # 데이터 예시
    updated_data = CSVdata(0)


    data = {}
    for key, value in updated_data.items():
        if value != "일요일":
            data[key] = int(value)

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

    return StreamingResponse(buf, media_type="image/png")