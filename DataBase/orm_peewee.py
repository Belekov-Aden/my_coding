import peewee

conn = peewee.PostgresqlDatabase(
    'test2',
    user='postgres',
#     password
    host='localhost',
    port='5432'
)


class Expenses(peewee.Model):
    id = peewee.PrimaryKeyField(unique=True)
    name = peewee.CharField(max_length=100)

    class Meta:
        database = db
        db_table = 'expenses'


class Paymant(peewee.Model):
    ud = peewee.PrimaryKeyField(unique=True)
    amount = peewee.FloatField()
    paymant_date = peewee.DateField
