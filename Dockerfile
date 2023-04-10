FROM python
WORKDIR ./app
COPY expenses.py middleware.py server.py db.db ./app
ENTRYPOINT ["/app/server.py"]