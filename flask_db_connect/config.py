db = {
    'host'     : 'localhost',
    'user'     : 'root',
    'password' : 'sjcuec0237',
    'port'     : '3306',
    'database' : 'scof'
}
DB_URL = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8"
DB_info = f"host='{db['host']}', user='{db['user']}', password='{db['password']}', db='{db['database']}', charset='utf8'"