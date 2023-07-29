FROM python
RUN pip install flask
WORKDIR /src
COPY . .
EXPOSE 3000
CMD python itil.py
