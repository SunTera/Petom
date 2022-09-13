# :feet: Petom :feet:

[www.petom.site](www.petom.site)

> - 반려동물의 피부사진으로 질병을 **탐지**하여 가능성 있는 증상을 알려주는 웹 프로그램입니다.
> - 반려동물의 피부질환이 의심되는 경우 보호자가 직접 찍은 이미지로 피부질환을 **탐지**하여 질환 목록을 안내하고 전문병원 치료가 필요하다고 판단할 경우 보호자가 거주 지역 주변의 동물병원을 전국 병원 지도를 통해 조기치료로 연계할 수 있는 서비스를 제공합니다.

- 주기능

  1. 반려동물의 피부 사진을 분석해 어떤 증상인지 알려준다. (증상 탐지)
  2. 결과를 확인한 유저가 주변 동물병원의 위치정보를 지도로 확인할 수 있다. (병원 지도)

## 아키텍처

## 페이지 구성

- About Page

- 증상탐지∙결과

- 병원지도

## 데이터 출처

- 질환 분석

  > AiHub [반려동물 피부 질환](https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=561)

- 동물병원 리스트
  > 공공데이터포털 [동물병원 현황 데이터](https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=TOTAL&keyword=%EB%8F%99%EB%AC%BC%EB%B3%91%EC%9B%90&detailKeyword=&publicDataPk=&recmSe=&detailText=&relatedKeyword=&commaNotInData=&commaAndData=&commaOrData=&must_not=&tabId=&dataSetCoreTf=&coreDataNm=&sort=&relRadio=&orgFullName=&orgFilter=&org=&orgSearch=&currentPage=1&perPage=10&brm=&instt=&svcType=&kwrdArray=&extsn=&coreDataNmArray=&pblonsipScopeCode=)를 통해 위치, 전화번호, 운영 여부 등을 추출할 예정

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

## 역할 분담

| 이름                                       | 역할                                  |
| ------------------------------------------ | ------------------------------------- |
| [홍유리](https://github.com/teraglass)(PM) | 웹페이지 구현, 배포(Flask, AWS)       |
| [양지선](https://github.com/Sunnnyyy16)    | 데이터분석, 전국 동물병원 지도 시각화 |
| [김예은](https://github.com/kimyeun)       | AI모델개발                            |
