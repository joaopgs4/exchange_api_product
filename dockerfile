FROM python:3.12-slim
WORKDIR /product
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN chmod +x ./uvicorn.sh
ENV PYTHONPATH=/product/app
CMD ["/bin/bash", "./uvicorn.sh"]
