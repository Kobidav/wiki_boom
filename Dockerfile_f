FROM python:3

WORKDIR /usr/src/app

COPY req.txt ./
RUN pip install --no-cache-dir -r req.txt

COPY front_end.py ./front_end.py
COPY disp_table.tpl ./disp_table.tpl

EXPOSE 8989 8989
CMD [ "python", "front_end.py" ]
