import datetime
import os
import time

import requests
import sqlalchemy as db
import sqlalchemy_utils as db_utils

mysql_socket = '172.16.238.2:3306'
mysql_password = os.environ["MYSQL_ROOT_PASSWORD"]


def create_table(engine, metadata):
    wiki_data_table = db.Table('wiki_data', metadata,
                               db.Column('pk', db.Integer(), primary_key=True),
                               db.Column('id', db.Integer()),
                               db.Column('ns', db.String(255), nullable=False),
                               db.Column('title', db.String(1000)),
                               db.Column('time', db.String(50)),
                               )
    metadata.create_all(engine)  # Creates the table
    return wiki_data_table


def get_wiki_random_paged():
    url = "https://en.wikipedia.org/w/api.php?action=query&list=random&rnnamespace=0&rnlimit=8&format=json"
    get_json_request = requests.get(url)
    if get_json_request.status_code:
        random_site_list = get_json_request.json()['query']['random']
        for member in random_site_list:
            member['time'] = datetime.datetime.now().strftime('%H:%M:%S %d.%m.%Y')
        return random_site_list
    return "Error"


print(get_wiki_random_paged())


def put_rows():
    engine = db.create_engine(F"mysql+mysqldb://root:{mysql_password}@{mysql_socket}/wiki_data?charset=utf8")
    if not db_utils.database_exists(engine.url):
        db_utils.create_database(engine.url)
    connection = engine.connect()
    metadata = db.MetaData()
    create_table(engine, metadata)
    wiki_data_table = db.Table('wiki_data', metadata, autoload=True, autoload_with=engine)
    query = db.insert(wiki_data_table)
    connection.execute(query, get_wiki_random_paged())
    connection.close()


while True:
    try:
        put_rows()
        time.sleep(300)
    except Exception as e:
        print("Error: ", e)
