FROM mysql:8.0.36

ENV MYSQL_ROOT_PASSWORD=root
ENV MYSQL_DATABASE=RP2024

COPY ./data.sql /docker-entrypoint-initdb.d/

CMD ["--default-authentication-plugin=mysql_native_password"]