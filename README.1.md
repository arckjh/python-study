## 어플리케이션 설명

* 문제 이슈
    - 링크 : (https://docs.google.com/document/d/16qUjrB48eCHWqRMCatD7eFmgU_Y6b2E5gkSeAJgr6_c/edit?ts=5dd7a245#)[https://docs.google.com/document/d/16qUjrB48eCHWqRMCatD7eFmgU_Y6b2E5gkSeAJgr6_c/edit?ts=5dd7a245#]
    - 사용자를 유니크키로 데이터를 출력할 때 카드 번호가 다른 사용자일 경우 버그가 발생될 수 있음
    - 시스템 설계/개발인데 데이터를 영속적으로 저장할 수 있는 기능이 필요하다고 판단
    - 시스템 반영
        + 사용자 인식을 사용자 이름 & 카드 번호 2개로 판단
        + 데이터를 영속적으로 저장하는 것은 간단한 파일 RW 기능을 개발함

* 설계 설명
    - system 디렉토리 : 시스템 IO, 파일, 어플리케이션 객체 관리 표준
    - application 디렉토리 : 사용자 IO 및 이벤트 제어
    - domain 디렉토리 : 서비스의 비즈니스 로직 모델링
    - infra 디렉토리 : 데이터 영속화를 위한 인터페이스
    - data 디렉토리 : 프로그램 종료 후 데이터 파일 저장 위치
    - test 디렉토리 : 테스트 스크립트 관리 위치

* 프로그램 실행 (python3 기준)
```
# 가상 환경 설치
cd ~/environment/<mustit-plaform>
python -m venv ./

# 가상 환경 시작
source bin/activate

# 가상 환경의 패키지 설치
pip install -r requirements.txt

# 프로그램 실행(프로그램 실행 유저의 디렉토리 퍼미션 RW 확인)
python bootstrap.py < input.txt

# 테스트코드 실행
pytest test
```