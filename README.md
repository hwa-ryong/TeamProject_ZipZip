# Python Django 프로젝트
- Server Repository: <a href="https://github.com/pshho/aws-django.git">서버 Git 주소</a>
- Web Page 주소: <a href="http://ec2-3-37-74-149.ap-northeast-2.compute.amazonaws.com/">집집 홈페이지</a>

## <img src="https://github.com/pshho/team3_django_project/assets/128444203/7531dc8b-c696-4c42-b39c-902f873e9dd9" style="width: 40px; height: 25px;" alt="Image"> 프로젝트 소개
* 프로젝트 명: 집집
  > “ 각 집. 또는 모든 집. " 을 뜻하는 순 우리말 - 대한민국 모든 집의 정보와 집과 관련된 핵심적인 내용들을 모아 놓은 홈페이지
* 기획 의도
  > 중장년층 뿐만 아니라 청년들까지도 ‘내 집 마련의 꿈’ 에 대한 열기가 뜨거워지는 만큼 부동산에 관심 있는 사람들과 정보들은 늘어나고 있습니다.
  > 각자가 필요로 하는 정보들을 검색 기능을 사용하여 쉽게 찾을 수 있으며 홈페이지 회원들을 위한 정보 교류가 가능하도록 목표를 두었습니다.
  > <br>**Figma**: <a href="https://www.figma.com/file/zffQCT0SZ5TDC3JORNaqUA/Project_Django_Team-3?type=whiteboard&node-id=0-1&t=Q6DA7FvR7HepJfcw-0">집집 설계</a>

### :mantelpiece_clock: 개발 기간
- 2023.06.19 - 2023.07.02

### :wrench: 개발 환경
- `Python 3.11`
- `HTML | CSS | JavaScript`
- **Framework**: Django
- **Database**: Sqlite3
- **개발 Tool**: VS Code, PyCharm, Figma, Git

### :gear: 주요 기능
#### 1. 로그인/회원가입/마이페이지
- 하나의 페이지에서 로그인과 회원가입(별도 Page Parsing) 구현
- 소셜로그인 기능 구현(구글, 카카오, 네이버)
- 회원가입 시 아이디(영문, 숫자)/사업자 등록증/비밀번호 8자 이상(영, 숫자) 유효성 검사 구현
- 로그인 후 마이페이지를 통해 회원정보 수정, 회원탈퇴, 해당 아이디의 게시판 작성글 확인 기능 구현
<details>
  <summary>마이페이지</summary>
  <p>
    <img src="https://github.com/pshho/team3_django_project/assets/128444203/8b114c60-a997-4ee5-a1bc-926ebb90d887" alt="MyPage">
    <img src="https://github.com/pshho/team3_django_project/assets/128444203/96c0dabd-ddd4-450a-a4b0-7a65a15eb122" alt="MyPage">
  </p>
</details>

<a href="http://ec2-3-37-74-149.ap-northeast-2.compute.amazonaws.com/common/signin/"> > 로그인/회원가입</a>

#### 2. 청약 달력/점수 계산
- 공공데이터포털 한국부동산원이 제공하는 실제 청약 데이터를 API를 통해 각각의 일정을 달력 API 자동으로 추가
- 해당 일정 클릭 시 입주자모집공고 상세정보(공급위치, 규모, 모집공고, 청약접수일, 공급대상, 공급금액 등) 조회 가능
- 청약 가점 계산 함수를 구현하고 무주택기간/부양가족수/청약통장가입기간을 입력받아 계산 후 점수 제공

<a href="http://ec2-3-37-74-149.ap-northeast-2.compute.amazonaws.com/koreaCalendar/"> > 청약 일정</a><br>
<a href="http://ec2-3-37-74-149.ap-northeast-2.compute.amazonaws.com/calculate/calculate/"> > 청약 점수 조회</a>

#### 3. 지도(검색)
- 서울시 실거래(매매), 전/월세 부동산 정보를 Django ORM(데이터베이스)에 저장(대략 4,000건)
- 저장된 각각의 데이터를 위도와 경도값을 통해 지도에 마커(Marker) 생성 및 클러스터화(100, 200, 500, 1000 등의 단위)
- 마커 클릭 시 전/월세가, 매매가, 주소, 법정동명, 계약일, 면적 등의 정보 제공
- 연립다세대/아파트/오피스텔/단독다가구 네 분류의 마커를 통해 정보의 가시성을 높이고 각 분류별로 클릭시 마커를 표시하거나 숨기는 기능 구현
- 지도에서 내 위치 찾기 기능 구현
- 지번명/도로명/일반 건물명으로 검색 기능 구현
- 메인 페이지에서 동일한 검색 시 동일한 기능으로 바로 해당 검색 결과를 지도에 표시하는 기능 구현
- 메인 페이지 검색과 지도에서 검색 시 지도에 마커로 표시되어 있는 건물들이 자동완성으로 표시되게 함

<a href="http://ec2-3-37-74-149.ap-northeast-2.compute.amazonaws.com/map/"> > 집찾기(지도)</a>

#### 4. 계약 관련 정보
- 부동산 계약 관련 필수 정보(부동산매매, 주택, 주택임대차분쟁, 공동주택관리분쟁) 제공
- 우측 하단의 별도의 탭을 통해 가용자금, 정보수집&시세파악, 계약과 관련된 추가 정보를 외부 링크(네이버)와 연결하여 정보 제공
- 매매계약과 관련한 해당 제목 클릭 시 더 상세한 내용을 이미지 형태로 표시하고 숨길 수 있는 기능 구현

<a href="http://ec2-3-37-74-149.ap-northeast-2.compute.amazonaws.com/information/information/"> > 알려드려요</a>

#### 5. 게시판
- 자유게시판, 거래후기 게시판, 인테리어 게시판, 뉴스 4가지 게시판 구성
- 자유게시판과 거래후기 게시판에서 최신순, 추천순으로 글목록 볼 수 있는 기능 구현
- 각 게시글의 댓글 추가, 수정, 삭제와 게시글 추천 기능 구현
- 게시글 추가, 수정, 삭제와 해당 아이디만 수정, 삭제 가능하게 기능 구현
- 댓글도 마찬가지로 해당 아이디만 수정, 삭제 가능하고 로그인 시에만 게시글과 댓글 추가 가능하게 기능 구현
- 인테리어와 뉴스 게시판의 각 글은 웹 크롤링을 통해 외부 링크(네이버 등)와 연결

<a href="http://ec2-3-37-74-149.ap-northeast-2.compute.amazonaws.com/community/board_free/"> > 자유게시판</a><br>
<a href="http://ec2-3-37-74-149.ap-northeast-2.compute.amazonaws.com/review/review_main/"> > 거래후기 게시판</a><br>
<a href="http://ec2-3-37-74-149.ap-northeast-2.compute.amazonaws.com/interior/"> > 인테리어 게시판</a><br>
<a href="http://ec2-3-37-74-149.ap-northeast-2.compute.amazonaws.com/news/news/"> > 뉴스</a><br>

#### 6. 사이드 메뉴/디자인
- 사이드 메뉴탭(집찾기/청약/알려드려요/커뮤니티/고객서비스), 상단 메뉴탭(집찾기/청약/알려드려요/커뮤니티/고객서비스) 구성
- 메인 페이지에서 각 탭에 바로 접속할 수 있는 메인탭 디자인
- 메인 페이지 하단에 현재 인테리어 게시글의 이미지를 슬라이드 효과로 표시(클릭 시 인테리어 게시판으로 연결)
- 반응형 디자인을 통해 모바일과 태블릿 버전 호환
  
<a href="http://ec2-3-37-74-149.ap-northeast-2.compute.amazonaws.com/"> > 메인</a><br>
<a href="http://ec2-3-37-74-149.ap-northeast-2.compute.amazonaws.com/koreaCalendar/"> > 청약 일정(사이드바)</a>

### :people_holding_hands: 구성 멤버
<details>
  <summary>멤버별 역할</summary>
  <p>
    <img src="https://github.com/pshho/team3_django_project/assets/128444203/fde8351a-6709-4135-9c47-f07718e4d8d4" alt="Member">
  </p>
</details>



