import requests
import json

# OpenWeatherMap API 키 (실제 사용 시 본인의 API 키로 교체해야 합니다)
api_key = "YOUR_API_KEY_HERE"

# 서울의 위도와 경도
lat = 37.532600
lon = 127.024612

# API 엔드포인트 URL
url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=minutely,hourly,daily,alerts&appid={api_key}&units=metric"

# API 요청 보내기
response = requests.get(url)

# 응답 확인
if response.status_code == 200:
    # JSON 형식으로 데이터 파싱
    data = json.loads(response.text)
    
    # 필요한 정보 추출
    current_weather = data['current']
    temp = current_weather['temp']
    feels_like = current_weather['feels_like']
    pressure = current_weather['pressure']
    humidity = current_weather['humidity']
    weather_description = current_weather['weather'][0]['description']
    
    # 결과 출력
    print(f"서울의 현재 날씨:")
    print(f"기온: {temp}°C")
    print(f"체감 온도: {feels_like}°C")
    print(f"기압: {pressure} hPa")
    print(f"습도: {humidity}%")
    print(f"날씨 설명: {weather_description}")
else:
    print("날씨 정보를 가져오는데 실패했습니다.")


