# <img src="https://user-images.githubusercontent.com/67316314/189922152-a9327fb4-ca56-4a21-aba4-d71386d67117.svg" width="30"> Petom 

## 주제 선정 이유와 개발 목표


<img src="https://user-images.githubusercontent.com/67316314/190043543-804e79b1-4de9-4edb-90a7-478688912953.jpeg" title="반려견이 동물병원을 찾는 주요 원인- 20위권">

1인 가구 확대로 반려동물을 키우는 가구 수가 증가하면서 반려동물 관련 상품뿐만 아니라 반려동물의 질병 관리 및 케어에 관심이 커지고 있습니다. 반려동물 관련 산업이 성장하며 인공지능을 활용한 펫테크 산업 또한 주목받고 있습니다. 
2018년 농촌진흥청은 반려견의 동물병원 내원 중 예방 접종 외에 가장 큰 원인으로 피부염·습진이라고 발표했습니다. [[출처]](https://www.nias.go.kr/front/soboarddown.do?cmCode=M090814150850297&boardSeqNum=3478&fileSeqNum=2323)
이에 따라 본 팀은 AI 기술을 이용한 반려동물 피부 질환 탐지 기술에 주목하였고 탐지 기술을 이용해 보호자가 반려동물의 피부질환을 조기 발견한다면 적절한 치료를 받을 수 있으리라 생각하였습니다.

PETOM은 보호자가 반려동물의 피부 질환 사진을 업로드해서 피부 질환 증상에 대한 AI 탐지 결과를 확인할 수 있습니다.      
탐지 결과에 따라 보호자가 전문병원 치료가 필요하다고 판단할 경우 거주 지역 주변의 동물병원을 전국 병원 지도를 통해 확인함으로써 치료로 연계할 수 있는 서비스를 제공합니다.


> 1. 반려동물의 피부 사진을 분석해 어떤 증상인지 확인할 수 있습니다. 
> 2. 결과를 확인한 유저가 주변 동물병원의 정보를 지도로 확인할 수 있습니다.
  


## 소개 영상

[![YoutubeVideo](https://user-images.githubusercontent.com/67316314/190053730-d32bb591-5abe-4a8e-93ce-89913581f0ef.png)](https://youtu.be/RowdPnEoWNE)

### 웹사이트 링크

- url : [www.petom.site](http://www.petom.site)


## 아키텍처

<img src="https://user-images.githubusercontent.com/67316314/189929257-e99e8e8f-cb90-4505-b659-d9c95c194023.png"/>   


1. 미란, 결절 증상을 탐지하도록 학습시킨 모델을 petom_weights.pt로 저장하여 프로젝트 내에서 로드하여 사용합니다.    
2. EC2 인스턴스의 Flask 서버가 시작 될 때 모델을 로드하고 사용자가 업로드한 이미지를 byte형식으로 변환하고 이미지 파일로 읽습니다.
3. 탐지 결과를 base64 형식으로 encode한 뒤 utf-8로 decode한 최종 결과를 결과 페이지에 전달하여 사용자가 탐지된 증상을 확인하게 됩니다.

- Colab Notebook 환경에서 AIhub에서 제공하는 반려동물 피부 질환 이미지 데이터를 전처리한 후 YOLOv5의 모델 중 하나인 yolov5n모델에 훈련시켰습니다. 
- 웹의 IP 주소를 petom.site 도메인과 연결시키기 위해 Route 53에 호스팅 영역을 생성해 DNS를 설정했습니다.   


---

## 페이지 구성

1. About

<img src="https://user-images.githubusercontent.com/67316314/189915868-48d07786-6033-495e-932e-cf21669435ee.gif" width="30%"/>   

|                        |  | 
| --------------- | -----------  |
| 경로  | [/templates/about.html](https://github.com/SunTera/Petom/blob/main/templates/about.html)|
| URL   | /, /about  |
| 역할            | Petom에서 사용한 알고리즘과 기대효과, 페이지 구성을 확인할 수 있습니다.|


2. 증상탐지∙결과

<img src="https://user-images.githubusercontent.com/98167266/190056565-5f7b3c41-8701-4726-bb1c-8125c4af75af.gif" width="30%"/>

|                        |  | 
| --------------- | -----------  |
| 경로 (증상탐지) | [/templates/detect.html](https://github.com/SunTera/Petom/blob/main/templates/detect.html)|
| 경로 (결과) | [/templates/result.html](https://github.com/SunTera/Petom/blob/main/templates/result.html)|
| URL   | /detect  |
| 역할            | 증상을 탐지할 이미지를 업로드하면 탐지 결과가 결과 페이지로 전달되어 탐지된 증상을 확인할 수 있습니다.|

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
| [홍유리](https://github.com/teraglass) | 웹페이지 구현, 배포(Flask, AWS), 데이터 전처리      |
| [양지선](https://github.com/Sunnnyyy16)    | 데이터 전처리, 전국 동물병원 지도 시각화 |

