import nltk
import os
from nltk.tokenize import word_tokenize, sent_tokenize
a = 'consumption of calorie in afghanistan in 1967' 
words = (word_tokenize(a))
print(words)
ans = []
import pymysql
connection = pymysql.connect(host='localhost', user='root', passwd='', db='CSV_DB')
cursor = connection.cursor()
for i in words:
    sql = ("select COL4 from tbl_name where Entity=%s and Year=%s")
    que = (i,words[-1])
    cursor.execute(sql,que)
    for data in cursor: 
        ans.append(data)

print(ans)
