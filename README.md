```shell
python3.7m -m venv .venv

pip install django==3.2.25
pip install djongo==1.3.6
pip install pymongo==3.12.1

django-admin startproject config .
```

settings.py
```python
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'test_kgs',
        'ENFORCE_SCHEMA': False,
        'CLIENT': {
            'host': '10.0.0.112',
            'port': 2400,
        }
    }
}
LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'
```