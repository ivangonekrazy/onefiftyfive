# INFO-155, Summer 2011

import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

class TemplatedRequestHandler(webapp.RequestHandler):

    def template_response(self, template_file=None, values={}):
        """
        """

        if template_file is None:
            return
                
        # find and open the template file
        this_dir = os.path.dirname(__file__)
        tmpl_file = os.path.join(this_dir, template_file)

        # return the filled out template as the response
        self.response.out.write(template.render(tmpl_file, values))
