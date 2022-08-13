# :feet: Petom :feet:

> \- Pet의 피부사진으로 질병을 **탐지**하여 가능성 있는 질환의 이름과 보편적인 원인, 예방법을 알려주는 웹프로그램  
> \- 반려동물의 피부질환이 의심되는 경우 보호자가 직접 찍은 이미지를 통해 학습된 피부질환을 **탐지**하여 질환 목록을 안내하고 전문병원 치료가 필요할 경우 해당 2차, 3차 병원을 연계할 수 있는 서비스 제공

- 주기능

  1. 반려동물의 피부 사진을 분석해 어떤 질환인지 알려준다
  2. 해당 질환의 보편적인 이유, 예방법을 알려준다

- 생각 중인 추가 기능
  1. 결과를 확인한 유저가 지역을 선택하면 해당 지역의 존재하는 동물병원 중 피부질환을 진료하는 병원의 리스트를 보여준다
  2. 해당 병원의 예약 사이트가 존재하면 링크로 연결해준다 (없다면 대형병원 한 곳을 지정하여 예약사이트로 이동)

## 데이터 수집

- 질환 분석

  > AiHub에 존재하는 데이터 사용 :point_right: [반려동물 피부 질환](https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=561)

- 해당 질환의 보편적인 이유, 예방법

  > 원인이 명확하지 않은 경우가 많기 때문에 간단히 정리하여 저장한 뒤 라벨링하여 보여주거나 데이터 파일을 더 찾아볼 예정

- 동물병원 리스트
  > 공공데이터에서 지역별 [동물병원 현황 데이터](https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=TOTAL&keyword=%EB%8F%99%EB%AC%BC%EB%B3%91%EC%9B%90&detailKeyword=&publicDataPk=&recmSe=&detailText=&relatedKeyword=&commaNotInData=&commaAndData=&commaOrData=&must_not=&tabId=&dataSetCoreTf=&coreDataNm=&sort=&relRadio=&orgFullName=&orgFilter=&org=&orgSearch=&currentPage=1&perPage=10&brm=&instt=&svcType=&kwrdArray=&extsn=&coreDataNmArray=&pblonsipScopeCode=)를 통해 위치, 전화번호, 운영 여부 등을 추출할 예정

## 커밋 메시지 규칙

1. 문장의 끝에 `.` 를 붙이지 않기

2. 이슈 해결 시 커밋 메시지 끝에 이슈 번호 붙이기

   > 예시: issue1 해결 - [#1]

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

## 역할 분담 -- **추가**

| 이름                                       | 역할                    |
| ------------------------------------------ | ----------------------- |
| [홍유리](https://github.com/teraglass)(PM) | 백엔드(Flask, Firebase) |
| 김예은                                     |                         |
| [양지선](https://github.com/Sunnnyyy16)    | 데이터분석               |
