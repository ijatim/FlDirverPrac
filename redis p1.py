import redis

r_connection = redis.Redis(host='localhost',
                           port=3306,
                           password='Nk[vhd;s1374')



r_connection.set('foo', 'bar')
#value = r_connection.get('foo')
#print(value)