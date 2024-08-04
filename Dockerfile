FROM python:3.9-slim

COPY . ./serverbook

WORKDIR serverbook


RUN pip install -i https://pypi.mirrors.ustc.edu.cn/simple/  -r requirements.txt

EXPOSE 8888

CMD ["python", "main.py"]
