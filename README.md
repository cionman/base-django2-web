## base-django2-web

### 1. 적용 기능
- pipenv 적용
- mysql 서버 연결
- 환경설정 분리(development, production)
- django-debug-toolbar
- django-extension 
- 레이아웃 분리
- INSTALLED_APPS 기존 설치랑 추가 설치된 앱 분리
- django-bootstrap3
- 개발환경 쿼리 로깅
- 사용자 모델 - 인증, 프로필 수정, 패스워드 변경 기능
- 개발 환경 static file 자동 refresh
- static 파일관리 whitenoise
- 실서버 서버 구동용 gunicorn 설치

# 2. 프로젝트 시작시 설정 필요

1. 프로젝트 클론 
2. pipenv 설치 

```bash
pip install pipenv
```

3. 환경별 install
    - 개발환경
    ```bash
    pipenv install --dev
    ```
    - 실서버환경
    ```bash
    pipenv install
    ```

4. 환경설정 (development, production) 분리에 따른 시스템 환경변수 설정
    - 개발
    ```bash
    export DJANGO_SETTINGS_MODULE=project.settings.development
    ```
    - 실서버
    ```bash
    export DJANGO_SETTINGS_MODULE=project.settings.production
    ```

5. 프로젝트 루트에 `server_info.json` 파일 만들기
    - 데이터베이스 정보 등 secret한 정보를 git에 올리지 않고 분리하기 위함

```json
{
    "production" : {
        "SECRET_KEY" : "키입력",
        "DATABASES" : {
            "default": {
                "ENGINE": "django.db.backends.mysql",
                "NAME": "slowalk_django",
                "USER": "데이터베이스 계정",
                "PASSWORD": "데이터베이스 암호",
                "HOST": "데이터베이스 호스트 정보",
                "PORT": "포트정보"
            }
        }
    }
}
```

6. 데이터베이스 마이그레이션

```bash
python manage.py makemigrations
python manage.py makemigrations accounts
python manage.py migrate
```

7. 기본 관리자 페이지 계정 생성
    - 기본 admin url - [http://127.0.0.1:8000/sl-admin/](http://127.0.0.1:8000/sl-admin/)
    
```bash
python manage.py createsuperuser
```

### TODO 보완 필요

- FBV 예제, CBV 예제(FormView, ListView, DetailView)
- 폼처리, Validatior 사용
- 이미자파일 처리, 섬네일만들기, pilkit사용
- ToastUI Editor달기
- 테스트 코드 작성
- django rest framework 적용
- humanize 필터 적용
- 트랜잭션처리
- Django Admin Interface 적용(https://djangopackages.org/grids/g/admin-styling/)
- Django Admin Editor 적용