# python 3.7.3 image
FROM python:3.7.3-alpine
# ensuring console messages are shown
ENV PYTHONUNBUFFERED 1
# setting the working dir
WORKDIR /app
# coping files
COPY . /app
# update pip
CMD ["pip", "install", "--upgrade", "pip"]
# installing building libs not included in alpine image
RUN set -e; \
	apk add --no-cache --virtual .build-deps \
		gcc \
		libc-dev \
		linux-headers \
	; \
	pip install -r requirements.txt; \
	apk del .build-deps;
# running the server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
