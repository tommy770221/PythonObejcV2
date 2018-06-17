import database
db=database.DataBase()

from database import Database
db=Database()

"兩個同名的類別使用"
from database import Database as DB
db=DB()


from database import Database, Query

"避免使用這個 寫爛code"
from database import *



