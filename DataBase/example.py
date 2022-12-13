import psycopg2

conn = psycopg2.connect(
    dbname='market',
    user='postgres',
    password='4.100.20.1001.Aden',
    host='localhost',
    port='5432'
)

cur = conn.cursor()


def print_from_db(execute):
    cur.execute(execute)
    c = cur.fetchall()
    print(c)

# print_from_db('SELECT MAX(followers) FROM users')
# print_from_db('SELECT COUNT(*) FROM users')
# print_from_db('SELECT * FROM users WHERE followers = (SELECT MAX(followers) FROM users)')
# print_from_db('SELECT AVG(followers) FROM users')
# print_from_db('SELECT * FROM users ORDER BY login')
# print_from_db('SELECT * FROM users ORDER BY email')
# print_from_db('SELECT * FROM users ORDER BY country')
# print_from_db('SELECT user_id,login FROM users')

# print_from_db("SELECT * FROM users\
#               WHERE(login LIKE '%as%' OR login LIKE '%cg%'\
#               OR login LIKE '%si%' OR login LIKE '%am%' OR login LIKE '%qwe%' OR login LIKE '%er%'\
#               OR login LIKE '%ka%' OR login LIKE '%an%')\
#               ")

# print_from_db("SELECT * FROM users\
#               WHERE (login LIKE '%lol'\
#               OR login LIKE '%kan'\
#               OR login LIKE '%ck'\
#               OR login LIKE '%ie.'\
#               OR login LIKE '%ig')\
#               ")

# print_from_db("SELECT * FROM users\
#               WHERE (login LIKE 'a%'\
#               OR login LIKE 'b%'\
#               OR login LIKE 'c%'\
#               OR login LIKE 'M%'\
#               OR login LIKE 'D%'\
#               OR login LIKE 'A%')\
#               ")

# print_from_db("SELECT * FROM users WHERE profession = 'Senior Programmer'\
#               AND country = 'Israel'\
#               ")

# print_from_db('SELECT * FROM users WHERE email IS NULL')
# print_from_db("SELECT * FROM users WHERE ( address LIKE 'Chui%' AND email IS NULL")
# print_from_db("SELECT login,phone_number, profession FROM users WHERE profession = 'Web Developer' ")
# print_from_db("SELECT country FROM users WHERE profesiion = 'Unemployed'")
# print_from_db("SELECT * FROM users WHERE (email LIKE '%.ru' AND profession = 'Developer') ORDER BY login DESC")
# print_from_db("DELETE FROM users WHERE (password = '12345' OR password = 'user123б' OR password = 'qwerty')")

# print_from_db("SELECT COUNT(product_name) FROM narodnii WHERE product_name = 'piyaz'")
# print_from_db("DELETE FROM narodnii WHERE day_to_expire > 5")
