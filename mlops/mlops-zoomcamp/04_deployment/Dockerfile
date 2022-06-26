FROM agrigorev/zoomcamp-model:mlops-3.9.7-slim

WORKDIR /app
COPY Pip* .

RUN mkdir predictions
RUN python -m pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --system --deploy

COPY [ "./scripts/ride_prediction_prd.py","ride-prediction.py"]

ENTRYPOINT [ "python","./ride-prediction.py" ]