"""engine: Engine = create_engine(DATABASE_URL)

meta = MetaData()

students = Table(
    'students', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('lastname', String),
)
meta.create_all(engine)
ins = students.insert().values(name='Ravi', lastname='Kapoor')
conn = engine.connect()
conn.execute(students.insert(), [
    {'name': 'Rajiv', 'lastname': 'Khanna'},
    {'name': 'Komal', 'lastname': 'Bhandari'},
    {'name': 'Abdul', 'lastname': 'Sattar'},
    {'name': 'Priya', 'lastname': 'Rajhans'},
])
s = students.select()
result = conn.execute(s)

for row in result:
    print(row)

"""