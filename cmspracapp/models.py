from google.appengine.ext import ndb

# Create your models here.

class Flatpage(ndb.model):
    title = ndb.StringProperty
    content = ndb.TextProperty
    date_created = ndb.DateProperty(auto_now_add=True)


