import os
import webapp2
import cgi

from google.appengine.ext.webapp import template
from google.appengine.ext import ndb


def render_template(handler, templatename, templatevalues):
  path = os.path.join(os.path.dirname(__file__), 'templates/' + templatename)
  html = template.render(path, templatevalues)
  handler.response.out.write(html)

class MainPage(webapp2.RequestHandler):
  def get(self):
    render_template(self, 'index.html', {})

class Demo(webapp2.RequestHandler):
  def get(self):
    render_template(self, 'demo.html', {})

class Contact(webapp2.RequestHandler):
  def get(self):
    render_template(self, 'contact.html', {})

class ConfirmMessage(webapp2.RequestHandler):
  def post(self):
    message = cgi.escape(self.request.get('message'))
    email = cgi.escape(self.request.get('email'))
    render_template(self, 'confirm.html', {
      "email": email, 
      "content": message
      })

class Message(ndb.Model):
  email = ndb.StringProperty()
  content = ndb.StringProperty()

app = webapp2.WSGIApplication([
  ('/', MainPage),
  ('/demo', Demo),
  ('/contact', Contact),
  ('/confirm', ConfirmMessage)
])