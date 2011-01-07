#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util

import time
import dokan

class InfoHandler(webapp.RequestHandler):
	def get(self):
		response = ""
		response += "filename=" + self.request.get("filename") + ","
		response += "length=0,"
		response += "creation_ticks=" + str(long(time.time())) + ","
		response += "lastaccess_ticks=" + str(long(time.time())) + ","
		response += "lastwrite_ticks=" + str(long(time.time())) + ","
		response += "attributes=128"
		
		self.response.out.write(response)

def main():
    application = webapp.WSGIApplication([('/FileInfo.*', InfoHandler)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
