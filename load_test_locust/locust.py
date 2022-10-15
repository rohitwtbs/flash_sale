# In locust.py

from locust import HttpUser, task, constant
import random

class QuickstartUser(HttpUser):
        wait_time = constant(0)

    host ="http://127.0.0.1:8000"

    @task
    def test_get_method(self):
        self.client.get("/product")

#   	@task
#    def test_post_method(self):
#        self.client.post("/articles/", {
#			"title" : "A Title",
#			"content" : "content!",
#			"author_name" : "Mario",
#        })
#
#	@task
#	def test_put_method(self):
#		self.client.put("/articles/", {
#			"id" : "3",
#			"title" : "Title is Updated!",
#			"content" : f"Your lucky number: {random.randint(0,9)}!",
#			"author_name" : "Mario 2",
#		})
#        
#    def on_start(self):
#        self.client.post("/login", {"username":"foo", "password":"bar"})
