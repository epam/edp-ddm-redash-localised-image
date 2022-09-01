FROM redash/redash:8.0.2.b37747 as source

FROM python:3.9.6 as local
COPY --from=source /app/client/dist/app.*.js /app/
COPY . /app
WORKDIR /app
RUN pip install pipenv
RUN pipenv install
RUN pipenv run python main.py

FROM source
COPY --from=local /app/app.*.js /app/client/dist/.
