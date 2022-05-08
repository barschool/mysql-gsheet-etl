# Mysql - Google Sheets Integration

Small integration script for integrations between Mysql - Google Sheets. 

### Local development
1. Create virtualenv ```python3 -m venv .venv```
1. Activate ```source .venv/bin/activate```
1. Install dependencies ```pip install -r app/requirements.txt```

### Docker
Image: docker.io/barschool/mysql-gsheet

Deploy
```
docker build . -t barschool/mysql-gsheet:latest
docker push barschool/mysql-gsheet:latest
```

