# In locust.py

from locust import HttpUser, task, constant
import random

class QuickstartUser(HttpUser):
	wait_time = constant(0)
	host = "http://128.0.0.1:8000"

	@task
	def test_get_method(self):
		self.client.get("/product")
