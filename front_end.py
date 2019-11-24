
import sqlalchemy as db
import os



from bottle import route, run, template
mysql_socket = '172.16.238.2:3306'
mysql_password = os.environ["MYSQL_ROOT_PASSWORD"]


def get_rows():
    engine = db.create_engine(F"mysql+mysqldb://root:{mysql_password}@{mysql_socket}/wiki_data?charset=utf8")
    connection = engine.connect()
    metadata = db.MetaData()
    wiki_data_table = db.Table('wiki_data', metadata, autoload=True, autoload_with=engine)
    query = db.select([wiki_data_table])
    result = connection.execute(query)
    return result.fetchall()

@route('/')
def home():
    return template('disp_table', rows=get_rows()[-20:], name='List Of Records')



run(host='0.0.0.0', port=8989, debug=True)




