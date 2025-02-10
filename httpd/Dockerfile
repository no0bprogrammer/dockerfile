#choosing base images as oracle linux
FROM oraclelinux:8.3
# update the OS to the latest patch
RUN yum update -y && \
    yum install httpd -y
# Changing the working directory
WORKDIR /var/www/html/
RUN echo "hello from the index file">index.html && \
    echo "Hello from the trainer page "> trainer.html && \
    echo "hello from the training page "> training.html

CMD ["httpd","-DFOREGROUND"]
