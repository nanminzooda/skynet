# 아나콘다 가상환경 조회

# 가상환경 생성

# 가상환경 실행


#### Python 프로젝트 생성

#### 가상환경 파이썬 버전 바꾸기

```
conda install python=3.7.0 (함부로 띄어쓰기 하면 안됨)
```

#### Django 프로젝트 생성
- django 설치 (pip를 써서 해야 한다)
```
pip install django==2.0.0
```

- django 프로젝트 생성 및 config 생성 (띄어쓰기 함부로 하지않기, 점 꼭 찍기)
```
django-admin startproject config . 
```

- django App 생성
```
python manage.py startapp shop
```

#### Django Flow
- 장고 프로젝트에 대한 사진
- MVT (Model, View(어디로 갈지 알려주는 역할), Template) 구조
- 데이터베이스와 HTML을 매핑해서 응답으로 돌려준다.

- request 요청
```
client >> URLConf(urls.py) >> View(views.py) 
>> (Model(model.py) >> Database) >> Template(*.html)
```

- response 응답
```
Database >> Model(model.py) >> View(views.py) >> Template(*.html) 
>> View(views.py) >> client 
```

- django 실행
```
python manage.py runserver
```

- URLconf(urls.py)
```
# 기본 url 설정 (주소 설정)
path('URL', views.함수) ->(그 함수가 실행됨)

# 그룹 URL 설정
from django.conf.urls import url, include
path('', include(앱이름.urls)),

```

- View(views.py)
```
def 함수명 (reguest):
    # 데이터 베이스 등을 이용한 프로그램 실행 결과
    return HttpResponse()
```

- Template(*.html)
```
<html>
    <!-- html 코드 작성 -->
</html>
```

- 뷰(HTML) 샘플 다운로드
- https://bootstrapmade.com


- 개발 순서 (모르면 이것만 보세요)
```
url.py (url만들기) -> view.py -> html 
```

```
# DB 연동 셋팅
settings.py

# 개발할 때
url.py, view.py, html, model.py
```

```
GET방식 !
http://서버주소:8000/work-pro?category-~!~!

reg -> pro(->여기서 DB로 갑니다) -> works (redirect로 가라)
```

mysql 모듈 설치
```
conda install -n 가상환경명 mysqlclient
```

모델을 이용한 데이터 관리
- makemigrations 명령으로 DB 셋팅 수행을 위한 파일 생성.
```
python manage.py makemigrations
```

- migrate 명령으로 테이블 샛엉
```
python manage.py migrate
```

- 다시한번 말하지만 이게제일 중요 (마지막 마무리!!)
- 
```
# DB 연동 셋팅
settings.py

# 개발할 때
url.py, html, view.py, model.py
M 모델, T 템플릿 (여기가 html), V 뷰

프레임워크 라는 것도, 각 기능에 따라서 코드를 잘라놓은 것입니다. 
```

- 파일을 데이터베이스에서 받아오는 것 ; view.py