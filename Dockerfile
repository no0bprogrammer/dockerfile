FROM python
WORKDIR /app
COPY hello.py .
CMD ["python","hello.py"]
