# <img src="https://user-images.githubusercontent.com/67316314/189922152-a9327fb4-ca56-4a21-aba4-d71386d67117.svg" width="30"> Petom 

반려동물의 피부사진으로 질병을 **탐지**하여 가능성 있는 증상을 알려주는 웹 프로그램입니다.   

반려동물의 피부질환이 의심되는 경우 보호자가 직접 찍은 이미지로 피부질환을 **탐지**하여 질환 목록을 안내하고 전문병원 치료가 필요하다고 판단할 경우 보호자가 거주 지역 주변의 동물병원을 전국 병원 지도를 통해 조기치료로 연계할 수 있는 서비스를 제공합니다.


1. 반려동물의 피부 사진을 분석해 어떤 증상인지 확인할 수 있습니다. 
2. 결과를 확인한 유저가 주변 동물병원의 위치정보를 지도로 확인할 수 있습니다.
  
  ---

## 소개 영상

[![YoutubeVideo](이미지 썸네일.jpg)](유튜브 주소) -- 추가

### 웹사이트 링크

- url : [www.petom.site](http://www.petom.site)

---

## 아키텍처

<img src="https://user-images.githubusercontent.com/67316314/189929257-e99e8e8f-cb90-4505-b659-d9c95c194023.png"/>   


1. 미란, 결절 증상을 탐지하도록 학습시킨 모델을 .pt 파일로 저장하여 프로젝트 내에서 로드하여 사용합니다.    
2. EC2 인스턴스의 Flask 서버가 시작 될 때 모델을 로드하고 사용자가 업로드한 이미지를 byte형식으로 변환하여 이미지 파일로 읽습니다.
3. 로드한 모델을 이용해 탐지한 후 결과를 base64 형식으로 encode한 뒤 utf-8로 decode한 이미지를 결과 페이지에 전달하여 사용자가 결과를 확인하게 됩니다.

- Colab Notebook 환경에서 YOLOv5의 모델 중 하나인 yolov5n모델에 AIhub에서 제공하는 반려동물 피부 질환 이미지 데이터를 전처리한 후 훈련시켰습니다. 
- 웹의 DNS 주소를 petom.site 도메인과 연결시키기 위해 Route 53에 호스팅 영역을 설정했습니다.   



---

## 페이지 구성

1. About Page
<img src="https://user-images.githubusercontent.com/67316314/189915868-48d07786-6033-495e-932e-cf21669435ee.gif" width="30%"/>   

|                        |  | 
| --------------- | -----------  |
| 경로  | [/templates/about.html](https://github.com/SunTera/Petom/blob/main/templates/about.html)|
| URL   | /, /about  |
| 역할            | Petom에서 사용한 알고리즘과 기대효과, 페이지 구성을 확인할 수 있습니다.|


2. 증상탐지∙결과

3. 병원지도   
<img src="https://user-images.githubusercontent.com/67316314/189904236-bf8f6ae7-c709-4c52-8cd0-71fad4d2c10e.gif" width="30%"/>   

|                        |  | 
| --------------- | -----------  |
| 경로  | [/templates/hospital.html](https://github.com/SunTera/Petom/blob/main/templates/hospital.html)|
| URL   | /hospital  |
| 역할            | 전국 동물병원을 시각화한 지도를 통해 병원의 주소와 전화번호를 확인할 수 있습니다.|

---

## 데이터 출처

- 반려동물 피부 질환 이미지

  > AiHub [반려동물 피부 질환](https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=561)

- 전국 동물병원 리스트
  > 공공데이터포털 [동물병원 현황 데이터](https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=TOTAL&keyword=%EB%8F%99%EB%AC%BC%EB%B3%91%EC%9B%90&detailKeyword=&publicDataPk=&recmSe=&detailText=&relatedKeyword=&commaNotInData=&commaAndData=&commaOrData=&must_not=&tabId=&dataSetCoreTf=&coreDataNm=&sort=&relRadio=&orgFullName=&orgFilter=&org=&orgSearch=&currentPage=1&perPage=10&brm=&instt=&svcType=&kwrdArray=&extsn=&coreDataNmArray=&pblonsipScopeCode=)

---

## 커밋 메시지 규칙

1. 문장의 끝에 `.` 를 붙이지 않기

2. 이슈 해결 시 커밋 메시지 끝에 이슈 번호 붙이기

   > 예시: issue1 해결 [#1]

3. 형식

   > [타입]: [내용] [이슈 번호]

   - 예시

     > docs: add 메소드 설명 주석 추가 [#1]
     >
     > refactor: 인증 메소드 수정 [#2]

4. 타입 종류

   > \- docs : 문서 작성
   >
   > \- fix : 버그 대처
   >
   > \- refactor : 코드 수정 / 리팩터링
   >
   > \- chore : 간단한 수정
   >
   > \- feature : 새로운 기능
   >
   > \- test : 테스트 추가
   
---

## 역할 분담

| 이름                                       | 역할                                  |
| ------------------------------------------ | ------------------------------------- |
| [홍유리](https://github.com/teraglass) | 웹페이지 구현, 배포(Flask, AWS)       |
| [양지선](https://github.com/Sunnnyyy16)    | 데이터분석, 전국 동물병원 지도 시각화 |

