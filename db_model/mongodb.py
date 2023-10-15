import pymongo

MONGO_HOST = 'localhost'
MONGO_COMN = pymongo.MongoClient('mongodb://%s' % (MONGO_HOST)) #로컬호스트로 몽고db 접속한다는 의미!

def conn_mongodb():
    try:
        MONGO_COMN.admin.command('ismaster')
        blog_db = MONGO_COMN.blog_session_db.blog_ab
    except:
        MONGO_COMN = pymongo.MongoClient('mongodb://%s' % (MONGO_HOST))
        blog_db = MONGO_COMN.blog_session_db.blog_ab
    return blog_db

        

