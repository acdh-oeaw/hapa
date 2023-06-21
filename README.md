# HAPA

[![codecov](https://codecov.io/gh/acdh-oeaw/hapa/branch/master/graph/badge.svg?token=BIH9K909AS)](https://codecov.io/gh/acdh-oeaw/hapa)
[![flake8 Lint](https://github.com/acdh-oeaw/hapa/actions/workflows/lint.yml/badge.svg)](https://github.com/acdh-oeaw/hapa/actions/workflows/lint.yml)

## History of Albanian Place-names: Albania

Code repo for the FWF-Project [**Sprachgeschichte der Ortsnamen Albaniens (P 33706)**](https://pf.fwf.ac.at/de/wissenschaft-konkret/project-finder/?search[what]=P%2033706&search[science_discipline_id]=&search[promotion_category_id]=&extended=1)



### building the image

`docker build -t hapa:latest .`
`docker build -t hapa:latest --no-cache .`

### running the image

To run the image you should provide an `.env` file to pass in needed environment variables; see example below:

```
DB_NAME=hapa
DB_USER=hapa
DB_PASSWORD=db_pw
PROJECT_NAME=hapa
SECRET_KEY=randomstring
DEBUG=True
DJANGO_SUPERUSER_USERNAME=user_name
DJANGO_SUPERUSER_PASSWORD=user_pw
VOCABS_DEFAULT_PEFIX=hapa
VOCABS_DEFAULT_PEFIX=en
REDMINE_ID=12345
```

`docker run -it -p 8020:8020 --rm --env-file .env_dev hapa:latest`