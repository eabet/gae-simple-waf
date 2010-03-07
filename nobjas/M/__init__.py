from google.appengine.ext import db

class Topics(db.Model):
    user     = db.UserProperty()
    title    = db.StringProperty()
    body     = db.TextProperty()
    status   = db.IntegerProperty(default=0)
    created  = db.DateTimeProperty(auto_now_add=True)
    modified = db.DateTimeProperty(auto_now=True)

    def findall(self):
        q = db.GqlQuery("SELECT * FROM Topics WHERE status = :1 ORDER BY created DESC", 0)
        return q.fetch(10)

class Comments(db.Model):
    topic    = db.ReferenceProperty(Topics)
    user     = db.UserProperty()
    body     = db.TextProperty()
    status   = db.IntegerProperty(default=0)
    created  = db.DateTimeProperty(auto_now_add=True)
    modified = db.DateTimeProperty(auto_now=True)
