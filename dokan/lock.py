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
from google.appengine.ext import db

import dokan
from dokan import models

def LockFile(file, processid):	
	def transaction(filekey, processid):
		f = db.get(filekey)
		if not f.locked:
			f.locked = True
			f.locked_by = processid
			return True
		return False
	return db.run_in_transaction(file.key(), processid)

def UnlockFile(file, processid):
	def transaction(filekey, processid):
		f = db.get(filekey)
		if f.locked and f.locked_by == processid:
			f.locked = False
			return True
		return False
	return db.run_in_transaction(file.key(), processid)
	
class LockHandler(webapp.RequestHandler):
	def get(self):
		self.response.out.write("response_code=" + str(dokan.DOKAN_SUCCESS))

class UnlockHandler(webapp.RequestHandler):
	def get(self):
		self.response.out.write("response_code=" + str(dokan.DOKAN_SUCCESS))
		
def main():
    application = webapp.WSGIApplication([('/LockFile.*', LockHandler),
										  ('/UnlockFile.*', UnlockHandler)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
