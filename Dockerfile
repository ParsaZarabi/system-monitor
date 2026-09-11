FROM python:3.12-slim

LABEL maintainer="Parsa Zarabi <zarabiparsa@gmail.com>"

WORKDIR /app


# copy dependency file first — leverages layer caching
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt


# copy application code last (changes most often)
COPY monitor.py .

# log directory mounted as volume at runtime
RUN mkdir -p /var/log/monitor
ENV LOG_PATH=/var/log/monitor/system_monitor.log
ENV TZ=Asia/Tehran
# force immediate stdout flush — required for docker logs
ENV PYTHONUNBUFFERED=1


# continuous mode inside container (no cron needed!)
CMD [ "python", "monitor.py", "--watch" ]