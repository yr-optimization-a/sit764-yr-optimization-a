import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
a = "what is daily caloric supply in Albania"
print(word_tokenize(a))
import pymysql
connection = pymysql.connect(host='localhost', user='root', passwd='', db='CSV_DB')
cursor = connection.cursor()
for i in words:
    sql = ("select Dailycaloricsupply from calory where Entity=%s")
    
    cursor.execute(sql,i)
    data = cursor.fetchall()
    print(data)
