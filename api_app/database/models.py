from sqlalchemy import MetaData, Table, Column, Integer, String

meta = MetaData()
t1 = Table("t1", meta, Column("name", String(50), primary_key=True))

