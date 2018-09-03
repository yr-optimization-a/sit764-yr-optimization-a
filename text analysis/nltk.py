Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> import nltk
>>> from nltk import word_tokenize
>>> a = "what is daily caloric supply in afganistan"
>>> words = word_tokenize(a)
>>> print words
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(words)?
>>> print(words)
['what', 'is', 'daily', 'caloric', 'supply', 'in', 'afganistan']
>>> import pymysql
>>> connection = pymysql.connect(host='localhost', user='root', passwd='', db='CSV_DB')
>>> cursor = connection.cursor()
>>> for i in words:
	sql = ('select Code from TBL_NAME where Entity=i')
	cursor.execute(sql)
	data = cursor.fetchall()

Traceback (most recent call last):
  File "<pyshell#13>", line 3, in <module>
    cursor.execute(sql)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/cursors.py", line 170, in execute
    result = self._query(query)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/cursors.py", line 328, in _query
    conn.query(q)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/connections.py", line 516, in query
    self._affected_rows = self._read_query_result(unbuffered=unbuffered)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/connections.py", line 727, in _read_query_result
    result.read()
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/connections.py", line 1066, in read
    first_packet = self.connection._read_packet()
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/connections.py", line 683, in _read_packet
    packet.check_error()
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/protocol.py", line 220, in check_error
    err.raise_mysql_exception(self._data)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/err.py", line 109, in raise_mysql_exception
    raise errorclass(errno, errval)
pymysql.err.InternalError: (1054, "Unknown column 'Code' in 'field list'")
>>> print(data)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print(data)
NameError: name 'data' is not defined
>>> for i in words:
	sql = ('select Code from TBL_NAME where Entity=i')
	cursor.execute(sql)
	data = cursor.fetchall()
	print(data)

	
Traceback (most recent call last):
  File "<pyshell#17>", line 3, in <module>
    cursor.execute(sql)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/cursors.py", line 170, in execute
    result = self._query(query)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/cursors.py", line 328, in _query
    conn.query(q)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/connections.py", line 516, in query
    self._affected_rows = self._read_query_result(unbuffered=unbuffered)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/connections.py", line 727, in _read_query_result
    result.read()
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/connections.py", line 1066, in read
    first_packet = self.connection._read_packet()
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/connections.py", line 683, in _read_packet
    packet.check_error()
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/protocol.py", line 220, in check_error
    err.raise_mysql_exception(self._data)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/err.py", line 109, in raise_mysql_exception
    raise errorclass(errno, errval)
pymysql.err.InternalError: (1054, "Unknown column 'Code' in 'field list'")
>>> for i in words:
	sql = ("select Code from TBL_NAME where Entity='i'")
	cursor.execute(sql)
	data = cursor.fetchall()
	print(data)

	
Traceback (most recent call last):
  File "<pyshell#19>", line 3, in <module>
    cursor.execute(sql)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/cursors.py", line 170, in execute
    result = self._query(query)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/cursors.py", line 328, in _query
    conn.query(q)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/connections.py", line 516, in query
    self._affected_rows = self._read_query_result(unbuffered=unbuffered)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/connections.py", line 727, in _read_query_result
    result.read()
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/connections.py", line 1066, in read
    first_packet = self.connection._read_packet()
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/connections.py", line 683, in _read_packet
    packet.check_error()
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/protocol.py", line 220, in check_error
    err.raise_mysql_exception(self._data)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/err.py", line 109, in raise_mysql_exception
    raise errorclass(errno, errval)
pymysql.err.InternalError: (1054, "Unknown column 'Code' in 'field list'")
>>> for i in words:
	sql = ("select Col 4 from TBL_NAME where Clo 1='i'")
	cursor.execute(sql)
	data = cursor.fetchall()
	print(data)

	
Traceback (most recent call last):
  File "<pyshell#21>", line 3, in <module>
    cursor.execute(sql)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/cursors.py", line 170, in execute
    result = self._query(query)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/cursors.py", line 328, in _query
    conn.query(q)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/connections.py", line 516, in query
    self._affected_rows = self._read_query_result(unbuffered=unbuffered)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/connections.py", line 727, in _read_query_result
    result.read()
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/connections.py", line 1066, in read
    first_packet = self.connection._read_packet()
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/connections.py", line 683, in _read_packet
    packet.check_error()
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/protocol.py", line 220, in check_error
    err.raise_mysql_exception(self._data)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/err.py", line 109, in raise_mysql_exception
    raise errorclass(errno, errval)
pymysql.err.ProgrammingError: (1064, "You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near '4 from TBL_NAME where Clo 1='i'' at line 1")
>>> for i in words:
	sql = ("select Col 4 from TBL_NAME where Col 1='i'")
	cursor.execute(sql)
	data = cursor.fetchall()
	print(data)

	
Traceback (most recent call last):
  File "<pyshell#23>", line 3, in <module>
    cursor.execute(sql)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/cursors.py", line 170, in execute
    result = self._query(query)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/cursors.py", line 328, in _query
    conn.query(q)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/connections.py", line 516, in query
    self._affected_rows = self._read_query_result(unbuffered=unbuffered)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/connections.py", line 727, in _read_query_result
    result.read()
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/connections.py", line 1066, in read
    first_packet = self.connection._read_packet()
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/connections.py", line 683, in _read_packet
    packet.check_error()
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/protocol.py", line 220, in check_error
    err.raise_mysql_exception(self._data)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/err.py", line 109, in raise_mysql_exception
    raise errorclass(errno, errval)
pymysql.err.ProgrammingError: (1064, "You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near '4 from TBL_NAME where Col 1='i'' at line 1")
>>> for i in words:
	sql = ("select Col4 from TBL_NAME where Col1='i'")
	cursor.execute(sql)
	data = cursor.fetchall()
	print(data)

	
Traceback (most recent call last):
  File "<pyshell#25>", line 3, in <module>
    cursor.execute(sql)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/cursors.py", line 170, in execute
    result = self._query(query)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/cursors.py", line 328, in _query
    conn.query(q)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/connections.py", line 516, in query
    self._affected_rows = self._read_query_result(unbuffered=unbuffered)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/connections.py", line 727, in _read_query_result
    result.read()
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/connections.py", line 1066, in read
    first_packet = self.connection._read_packet()
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/connections.py", line 683, in _read_packet
    packet.check_error()
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/protocol.py", line 220, in check_error
    err.raise_mysql_exception(self._data)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/err.py", line 109, in raise_mysql_exception
    raise errorclass(errno, errval)
pymysql.err.InternalError: (1054, "Unknown column 'Col4' in 'field list'")
>>> for i in words:
	sql = ("select 'Col 4' from TBL_NAME where 'Col 1'='i'")
	cursor.execute(sql)
	data = cursor.fetchall()
	print(data)

	
0
()
0
()
0
()
0
()
0
()
0
()
0
()
>>> a = "what is daily caloric supply in Afganistan"
>>> words = word_tokenize(a)
>>> print(words)
['what', 'is', 'daily', 'caloric', 'supply', 'in', 'Afganistan']
>>> for i in words:
	sql = ("select 'Col 4' from TBL_NAME where 'Col 1'='i'")
	cursor.execute(sql)
	data = cursor.fetchall()
	print(data)

	
0
()
0
()
0
()
0
()
0
()
0
()
0
()
>>> a = "what is daily caloric supply in Africa"
>>> words = word_tokenize(a)
>>> for i in words:
	sql = ("select 'Col 4' from TBL_NAME where 'Col 1'='i'")
	cursor.execute(sql)
	data = cursor.fetchall()
	print(data)

0
()
0
()
0
()
0
()
0
()
0
()
0
()
>>> sql = ("select 'Col 4' from TBL_NAME where 'Col 1'='Africa'")
>>> cursor.execute(sql)
0
>>> sql = ("select Code from calory where Entity='Africa'")
>>> cursor.execute(sql)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    cursor.execute(sql)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/cursors.py", line 170, in execute
    result = self._query(query)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/cursors.py", line 328, in _query
    conn.query(q)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/connections.py", line 516, in query
    self._affected_rows = self._read_query_result(unbuffered=unbuffered)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/connections.py", line 727, in _read_query_result
    result.read()
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/connections.py", line 1066, in read
    first_packet = self.connection._read_packet()
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/connections.py", line 667, in _read_packet
    "Lost connection to MySQL server during query")
pymysql.err.OperationalError: (2013, 'Lost connection to MySQL server during query')
>>> connection = pymysql.connect(host='localhost', user='root', passwd='', db='CSV_DB')

>>> cursor = connection.cursor()
>>> sql = ("select Code from calory where Entity='Africa'")
>>> cursor.execute(sql)
53
>>> sql = ("select 'Daily caloric supply (FAO (2017)) (kcal/person/day)' from calory where Entity='Africa'")
>>> cursor.execute(sql)
53
>>> data = cursor.fetchall()
>>> print(data)
(('Daily caloric supply (FAO (2017)) (kcal/person/day)',), ('Daily caloric supply (FAO (2017)) (kcal/person/day)',), ('Daily caloric supply (FAO (2017)) (kcal/person/day)',), ('Daily caloric supply (FAO (2017)) (kcal/person/day)',), ('Daily caloric supply (FAO (2017)) (kcal/person/day)',), ('Daily caloric supply (FAO (2017)) (kcal/person/day)',), ('Daily caloric supply (FAO (2017)) (kcal/person/day)',), ('Daily caloric supply (FAO (2017)) (kcal/person/day)',), ('Daily caloric supply (FAO (2017)) (kcal/person/day)',), ('Daily caloric supply (FAO (2017)) (kcal/person/day)',), ('Daily caloric supply (FAO (2017)) (kcal/person/day)',), ('Daily caloric supply (FAO (2017)) (kcal/person/day)',), ('Daily caloric supply (FAO (2017)) (kcal/person/day)',), ('Daily caloric supply (FAO (2017)) (kcal/person/day)',), ('Daily caloric supply (FAO (2017)) (kcal/person/day)',), ('Daily caloric supply (FAO (2017)) (kcal/person/day)',), ('Daily caloric supply (FAO (2017)) (kcal/person/day)',), ('Daily caloric supply (FAO (2017)) (kcal/person/day)',), ('Daily caloric supply (FAO (2017)) (kcal/person/day)',), ('Daily caloric supply (FAO (2017)) (kcal/person/day)',), ('Daily caloric supply (FAO (2017)) (kcal/person/day)',), ('Daily caloric supply (FAO (2017)) (kcal/person/day)',), ('Daily caloric supply (FAO (2017)) (kcal/person/day)',), ('Daily caloric supply (FAO (2017)) (kcal/person/day)',), ('Daily caloric supply (FAO (2017)) (kcal/person/day)',), ('Daily caloric supply (FAO (2017)) (kcal/person/day)',), ('Daily caloric supply (FAO (2017)) (kcal/person/day)',), ('Daily caloric supply (FAO (2017)) (kcal/person/day)',), ('Daily caloric supply (FAO (2017)) (kcal/person/day)',), ('Daily caloric supply (FAO (2017)) (kcal/person/day)',), ('Daily caloric supply (FAO (2017)) (kcal/person/day)',), ('Daily caloric supply (FAO (2017)) (kcal/person/day)',), ('Daily caloric supply (FAO (2017)) (kcal/person/day)',), ('Daily caloric supply (FAO (2017)) (kcal/person/day)',), ('Daily caloric supply (FAO (2017)) (kcal/person/day)',), ('Daily caloric supply (FAO (2017)) (kcal/person/day)',), ('Daily caloric supply (FAO (2017)) (kcal/person/day)',), ('Daily caloric supply (FAO (2017)) (kcal/person/day)',), ('Daily caloric supply (FAO (2017)) (kcal/person/day)',), ('Daily caloric supply (FAO (2017)) (kcal/person/day)',), ('Daily caloric supply (FAO (2017)) (kcal/person/day)',), ('Daily caloric supply (FAO (2017)) (kcal/person/day)',), ('Daily caloric supply (FAO (2017)) (kcal/person/day)',), ('Daily caloric supply (FAO (2017)) (kcal/person/day)',), ('Daily caloric supply (FAO (2017)) (kcal/person/day)',), ('Daily caloric supply (FAO (2017)) (kcal/person/day)',), ('Daily caloric supply (FAO (2017)) (kcal/person/day)',), ('Daily caloric supply (FAO (2017)) (kcal/person/day)',), ('Daily caloric supply (FAO (2017)) (kcal/person/day)',), ('Daily caloric supply (FAO (2017)) (kcal/person/day)',), ('Daily caloric supply (FAO (2017)) (kcal/person/day)',), ('Daily caloric supply (FAO (2017)) (kcal/person/day)',), ('Daily caloric supply (FAO (2017)) (kcal/person/day)',))
>>>  sql = ("select Code from calory where Entity='Africa'")
SyntaxError: unexpected indent
>>> sql = ("select Code from calory where Entity='Africa'")
>>> cursor.execute(sql)
53
>>> data = cursor.fetchall()
>>> print(data)
(('',), ('',), ('',), ('',), ('',), ('',), ('',), ('',), ('',), ('',), ('',), ('',), ('',), ('',), ('',), ('',), ('',), ('',), ('',), ('',), ('',), ('',), ('',), ('',), ('',), ('',), ('',), ('',), ('',), ('',), ('',), ('',), ('',), ('',), ('',), ('',), ('',), ('',), ('',), ('',), ('',), ('',), ('',), ('',), ('',), ('',), ('',), ('',), ('',), ('',), ('',), ('',), ('',))
>>> sql = ("select Code from calory where Entity='Albania'")
>>> cursor.execute(sql)
53
>>> data = cursor.fetchall()
>>> print(data)
(('ALB',), ('ALB',), ('ALB',), ('ALB',), ('ALB',), ('ALB',), ('ALB',), ('ALB',), ('ALB',), ('ALB',), ('ALB',), ('ALB',), ('ALB',), ('ALB',), ('ALB',), ('ALB',), ('ALB',), ('ALB',), ('ALB',), ('ALB',), ('ALB',), ('ALB',), ('ALB',), ('ALB',), ('ALB',), ('ALB',), ('ALB',), ('ALB',), ('ALB',), ('ALB',), ('ALB',), ('ALB',), ('ALB',), ('ALB',), ('ALB',), ('ALB',), ('ALB',), ('ALB',), ('ALB',), ('ALB',), ('ALB',), ('ALB',), ('ALB',), ('ALB',), ('ALB',), ('ALB',), ('ALB',), ('ALB',), ('ALB',), ('ALB',), ('ALB',), ('ALB',), ('ALB',))
>>> connection = pymysql.connect(host='localhost', user='root', passwd='', db='CSV_DB')
>>> cursor = connection.cursor()
>>> sql = ("select Dailcaloricsupply from calory where Entity='Albania'")
>>> cursor.execute(sql)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    cursor.execute(sql)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/cursors.py", line 170, in execute
    result = self._query(query)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/cursors.py", line 328, in _query
    conn.query(q)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/connections.py", line 516, in query
    self._affected_rows = self._read_query_result(unbuffered=unbuffered)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/connections.py", line 727, in _read_query_result
    result.read()
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/connections.py", line 1066, in read
    first_packet = self.connection._read_packet()
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/connections.py", line 683, in _read_packet
    packet.check_error()
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/protocol.py", line 220, in check_error
    err.raise_mysql_exception(self._data)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/err.py", line 109, in raise_mysql_exception
    raise errorclass(errno, errval)
pymysql.err.InternalError: (1054, "Unknown column 'Dailcaloricsupply' in 'field list'")
>>> sql = ("select Dailycaloricsupply from calory where Entity='Albania'")
>>> cursor.execute(sql)
53
>>> data = cursor.fetchall()
>>> print(data)
((Decimal('2223.0'),), (Decimal('2242.0'),), (Decimal('2156.0'),), (Decimal('2270.0'),), (Decimal('2254.0'),), (Decimal('2254.0'),), (Decimal('2262.0'),), (Decimal('2343.0'),), (Decimal('2404.0'),), (Decimal('2415.0'),), (Decimal('2360.0'),), (Decimal('2388.0'),), (Decimal('2432.0'),), (Decimal('2494.0'),), (Decimal('2494.0'),), (Decimal('2680.0'),), (Decimal('2776.0'),), (Decimal('2689.0'),), (Decimal('2607.0'),), (Decimal('2596.0'),), (Decimal('2676.0'),), (Decimal('2664.0'),), (Decimal('2798.0'),), (Decimal('2721.0'),), (Decimal('2565.0'),), (Decimal('2690.0'),), (Decimal('2497.0'),), (Decimal('2594.0'),), (Decimal('2569.0'),), (Decimal('2568.0'),), (Decimal('2572.0'),), (Decimal('2654.0'),), (Decimal('2795.0'),), (Decimal('2877.0'),), (Decimal('2717.0'),), (Decimal('2843.0'),), (Decimal('2725.0'),), (Decimal('2725.0'),), (Decimal('2797.0'),), (Decimal('2734.0'),), (Decimal('2803.0'),), (Decimal('2864.0'),), (Decimal('2772.0'),), (Decimal('2792.0'),), (Decimal('2874.0'),), (Decimal('2855.0'),), (Decimal('2860.0'),), (Decimal('2947.0'),), (Decimal('2993.0'),), (Decimal('3076.0'),), (Decimal('3132.0'),), (Decimal('3184.0'),), (Decimal('3193.0'),))
>>> a = "what is daily caloric supply in Albania"
>>> words = word_tokenize(a))
SyntaxError: invalid syntax
>>> words = word_tokenize(a)
>>> for i in words
SyntaxError: invalid syntax
>>> for i in words:
	sql = ("select Dailycaloricsupply from calory where Entity='i'")
	cursor.execute(sql)
	data = cursor.fetchall()
	print(data)

	
0
()
0
()
0
()
0
()
0
()
0
()
0
()
>>> print(words)
['what', 'is', 'daily', 'caloric', 'supply', 'in', 'Albania']
>>> for i in words:
	sql = ("select Dailycaloricsupply from calory where Entity=i")
	cursor.execute(sql)
	data = cursor.fetchall()
	print(data)

	
Traceback (most recent call last):
  File "<pyshell#78>", line 3, in <module>
    cursor.execute(sql)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/cursors.py", line 170, in execute
    result = self._query(query)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/cursors.py", line 328, in _query
    conn.query(q)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/connections.py", line 516, in query
    self._affected_rows = self._read_query_result(unbuffered=unbuffered)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/connections.py", line 727, in _read_query_result
    result.read()
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/connections.py", line 1066, in read
    first_packet = self.connection._read_packet()
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/connections.py", line 683, in _read_packet
    packet.check_error()
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/protocol.py", line 220, in check_error
    err.raise_mysql_exception(self._data)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/err.py", line 109, in raise_mysql_exception
    raise errorclass(errno, errval)
pymysql.err.InternalError: (1054, "Unknown column 'i' in 'where clause'")
>>> for i in words:
	sql = ("select Dailycaloricsupply from calory where 'Entity' = i")
	cursor.execute(sql)
	data = cursor.fetchall()
	print(data)

	
Traceback (most recent call last):
  File "<pyshell#80>", line 3, in <module>
    cursor.execute(sql)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/cursors.py", line 170, in execute
    result = self._query(query)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/cursors.py", line 328, in _query
    conn.query(q)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/connections.py", line 516, in query
    self._affected_rows = self._read_query_result(unbuffered=unbuffered)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/connections.py", line 727, in _read_query_result
    result.read()
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/connections.py", line 1066, in read
    first_packet = self.connection._read_packet()
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/connections.py", line 683, in _read_packet
    packet.check_error()
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/protocol.py", line 220, in check_error
    err.raise_mysql_exception(self._data)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/err.py", line 109, in raise_mysql_exception
    raise errorclass(errno, errval)
pymysql.err.InternalError: (1054, "Unknown column 'i' in 'where clause'")
>>> for i in words:
	sql = ("select Dailycaloricsupply from calory where Entity=words[i]")
	cursor.execute(sql)
	data = cursor.fetchall()
	print(data)

	
Traceback (most recent call last):
  File "<pyshell#82>", line 3, in <module>
    cursor.execute(sql)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/cursors.py", line 170, in execute
    result = self._query(query)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/cursors.py", line 328, in _query
    conn.query(q)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/connections.py", line 516, in query
    self._affected_rows = self._read_query_result(unbuffered=unbuffered)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/connections.py", line 727, in _read_query_result
    result.read()
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/connections.py", line 1066, in read
    first_packet = self.connection._read_packet()
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/connections.py", line 683, in _read_packet
    packet.check_error()
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/protocol.py", line 220, in check_error
    err.raise_mysql_exception(self._data)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/err.py", line 109, in raise_mysql_exception
    raise errorclass(errno, errval)
pymysql.err.ProgrammingError: (1064, "You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near '[i]' at line 1")
>>> for i in words:
	sql = ("select Dailycaloricsupply from calory where Entity='words[i]'")
	cursor.execute(sql)
	data = cursor.fetchall()
	print(data)

	
0
()
0
()
0
()
0
()
0
()
0
()
0
()
>>> for i in words:
	sql = ("select Dailycaloricsupply from calory where Entity=(i)")
	cursor.execute(sql)
	data = cursor.fetchall()
	print(data)

	
Traceback (most recent call last):
  File "<pyshell#86>", line 3, in <module>
    cursor.execute(sql)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/cursors.py", line 170, in execute
    result = self._query(query)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/cursors.py", line 328, in _query
    conn.query(q)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/connections.py", line 516, in query
    self._affected_rows = self._read_query_result(unbuffered=unbuffered)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/connections.py", line 727, in _read_query_result
    result.read()
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/connections.py", line 1066, in read
    first_packet = self.connection._read_packet()
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/connections.py", line 683, in _read_packet
    packet.check_error()
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/protocol.py", line 220, in check_error
    err.raise_mysql_exception(self._data)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/err.py", line 109, in raise_mysql_exception
    raise errorclass(errno, errval)
pymysql.err.InternalError: (1054, "Unknown column 'i' in 'where clause'")
>>> for i in words:
	sql = ("select Dailycaloricsupply from calory where Entity='%s'", [i])
	cursor.execute(sql)
	data = cursor.fetchall()
	print(data)

	
Traceback (most recent call last):
  File "<pyshell#88>", line 3, in <module>
    cursor.execute(sql)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/cursors.py", line 170, in execute
    result = self._query(query)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/cursors.py", line 328, in _query
    conn.query(q)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/connections.py", line 515, in query
    self._execute_command(COMMAND.COM_QUERY, sql)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/connections.py", line 765, in _execute_command
    packet = prelude + sql[:packet_size-1]
TypeError: can't concat tuple to bytes
>>> for i in words:
	sql = ("select Dailycaloricsupply from calory where Entity='%s'", (i))
	cursor.execute(sql)
	data = cursor.fetchall()
	print(data)

	
Traceback (most recent call last):
  File "<pyshell#90>", line 3, in <module>
    cursor.execute(sql)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/cursors.py", line 170, in execute
    result = self._query(query)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/cursors.py", line 328, in _query
    conn.query(q)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/connections.py", line 515, in query
    self._execute_command(COMMAND.COM_QUERY, sql)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/connections.py", line 765, in _execute_command
    packet = prelude + sql[:packet_size-1]
TypeError: can't concat tuple to bytes
>>>  for i in words:
	sql = ("select Dailycaloricsupply from calory where Entity='%d'", (i))
	
	cursor.execute(sql)
	data = cursor.fetchall()
	print(data)
	
SyntaxError: unexpected indent
>>> 
>>> for i in words:
	sql = ("select Dailycaloricsupply from calory where Entity='%s'", (i,))
	
	cursor.execute(sql)
	data = cursor.fetchall()
	print(data)

	
Traceback (most recent call last):
  File "<pyshell#94>", line 4, in <module>
    cursor.execute(sql)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/cursors.py", line 170, in execute
    result = self._query(query)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/cursors.py", line 328, in _query
    conn.query(q)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/connections.py", line 515, in query
    self._execute_command(COMMAND.COM_QUERY, sql)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/connections.py", line 765, in _execute_command
    packet = prelude + sql[:packet_size-1]
TypeError: can't concat tuple to bytes
>>> for i in words:
	sql = ("select Dailycaloricsupply from calory where Entity=?")
	
	cursor.execute(sql,i)
	data = cursor.fetchall()
	print(data)

	
Traceback (most recent call last):
  File "<pyshell#96>", line 4, in <module>
    cursor.execute(sql,i)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/cursors.py", line 168, in execute
    query = self.mogrify(query, args)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/cursors.py", line 147, in mogrify
    query = query % self._escape_args(args, conn)
TypeError: not all arguments converted during string formatting
>>> for i in words:
	sql = ("select Dailycaloricsupply from calory where Entity='%s'")
	
	cursor.execute(sql,i)
	data = cursor.fetchall()
	print(data)

	
Traceback (most recent call last):
  File "<pyshell#98>", line 4, in <module>
    cursor.execute(sql,i)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/cursors.py", line 170, in execute
    result = self._query(query)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/cursors.py", line 328, in _query
    conn.query(q)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/connections.py", line 516, in query
    self._affected_rows = self._read_query_result(unbuffered=unbuffered)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/connections.py", line 727, in _read_query_result
    result.read()
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/connections.py", line 1066, in read
    first_packet = self.connection._read_packet()
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/connections.py", line 683, in _read_packet
    packet.check_error()
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/protocol.py", line 220, in check_error
    err.raise_mysql_exception(self._data)
  File "/Users/parth/Library/Python/3.7/lib/python/site-packages/pymysql/err.py", line 109, in raise_mysql_exception
    raise errorclass(errno, errval)
pymysql.err.ProgrammingError: (1064, "You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'what''' at line 1")
>>> for i in words:
	sql = ("select Dailycaloricsupply from calory where Entity=%s")
	
	cursor.execute(sql,i)
	data = cursor.fetchall()
	print(data)

	
0
()
0
()
0
()
0
()
0
()
0
()
53
((Decimal('2223.0'),), (Decimal('2242.0'),), (Decimal('2156.0'),), (Decimal('2270.0'),), (Decimal('2254.0'),), (Decimal('2254.0'),), (Decimal('2262.0'),), (Decimal('2343.0'),), (Decimal('2404.0'),), (Decimal('2415.0'),), (Decimal('2360.0'),), (Decimal('2388.0'),), (Decimal('2432.0'),), (Decimal('2494.0'),), (Decimal('2494.0'),), (Decimal('2680.0'),), (Decimal('2776.0'),), (Decimal('2689.0'),), (Decimal('2607.0'),), (Decimal('2596.0'),), (Decimal('2676.0'),), (Decimal('2664.0'),), (Decimal('2798.0'),), (Decimal('2721.0'),), (Decimal('2565.0'),), (Decimal('2690.0'),), (Decimal('2497.0'),), (Decimal('2594.0'),), (Decimal('2569.0'),), (Decimal('2568.0'),), (Decimal('2572.0'),), (Decimal('2654.0'),), (Decimal('2795.0'),), (Decimal('2877.0'),), (Decimal('2717.0'),), (Decimal('2843.0'),), (Decimal('2725.0'),), (Decimal('2725.0'),), (Decimal('2797.0'),), (Decimal('2734.0'),), (Decimal('2803.0'),), (Decimal('2864.0'),), (Decimal('2772.0'),), (Decimal('2792.0'),), (Decimal('2874.0'),), (Decimal('2855.0'),), (Decimal('2860.0'),), (Decimal('2947.0'),), (Decimal('2993.0'),), (Decimal('3076.0'),), (Decimal('3132.0'),), (Decimal('3184.0'),), (Decimal('3193.0'),))
>>> 
