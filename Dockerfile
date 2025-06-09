FROM apify/actor-python

COPY . ./

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "scraper.py"]
