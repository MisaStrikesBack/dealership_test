# python 3.7.3 image
FROM python:3.7.3-alpine
# ensuring console messages are shown
ENV PYTHONUNBUFFERED 1
# setting the working dir
WORKDIR /app
# coping files
COPY . /app
# installing building libs not included in alpine image
RUN pip install --upgrade pip; \
	pip install --upgrade setuptools; \
	set -e; \
	apk add --no-cache --virtual .build-deps \
		postgresql-dev \
		gcc \
		python3-dev \
		musl-dev \
		openldap-dev \
		gcc \
		libc-dev \
		linux-headers \
	; \
	pip install -r requirements.txt; \
	apk del .build-deps;
# running the server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
