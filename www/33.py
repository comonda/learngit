#import time, uuid, functools, threading, logging
# def next_id(t = None):

#     if t is None:
#         t = time.time()
#     return '%015d%s000' % (int(t * 1000), uuid.uuid4().hex)
# print uuid.uuid4().hex
# print next_id()
# print id(next_id())
# print hex(id(next_id()))

# def create_engine(user, password, database, host='127.0.0.1', port = 3306, **kw):
# #    import mysql.connector
#
#     paramas = dict(user=user, password = password, database=database, host=host, port=port)
#     defaults = dict(use_unicode=True, charset='utf8', collation='utf-8_general_ci', autocommit=False)
#     for k, v in defaults.iteritems():
#         paramas[k] = kw.pop(k, v)
#         print paramas[k]
#     paramas.update(kw)
#     print paramas
#
# create_engine('comon','gloryn','mysql')



from models import User, Blog, Comment

from transwarp import db

import time

db.create_engine(user='root', password='364834547', database='awesome')

u = User(name='Test3', email='test@example.com3', password='12345678902', image='about:blank')

u.insert()

print 'new user id:', u.id

u1 = User.find_first('where email=?', 'test@example.com')
print 'find user\'s name:', u1.name

# u1.delete()
#
# time.sleep(1)
# u2 = User.find_first('where email=?', 'test@example.com')
# print 'find user:', u2