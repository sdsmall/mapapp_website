import os
import webapp2

from google.appengine.ext.webapp import template


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

app = webapp2.WSGIApplication([
  ('/', MainPage),
  ('/demo', Demo),
  ('/contact', Contact)
])