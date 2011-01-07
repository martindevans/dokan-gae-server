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

import dokan
from dokan import models

class CreateHandler(webapp.RequestHandler):
	def get(self):
		filepath = self.request.get("filepath")
		access = int(self.request.get("access"))			
		share = int(self.request.get("share"))
		mode = int(self.request.get("mode"))
		options = int(self.request.get("options"))
		processid = int(self.request.get("processid"))
		
		if not (mode in dokan.FILE_MODE):
			self.response.out.write("response_code=" + str(dokan.DOKAN_ERROR) + ",message=" + str(mode) + " is not a valid filemode option")
			return
		if not options in dokan.FILE_OPTIONS:
			self.response.out.write("response_code=" + str(dokan.DOKAN_ERROR) + ",message=" + str(options) + " is not a valid fileoptions option")
			return
		
		self.response.out.write("response_code=" + str(dokan.DOKAN_SUCCESS))

def main():
    application = webapp.WSGIApplication([('/CreateFile.*', CreateHandler)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
