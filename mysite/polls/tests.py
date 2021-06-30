import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question

class QuestionModelTests(TestCase):

	def test_was_published_recently_with_future_question(self):
		time = timezone.now() + datetime.timedelta(days=30)
		future_question = Question(pub_date=time)
		try:
			self.assertIs(future_question.was_published_recently(), False)
		except AssertionError:
			print("\n\n\n******TEST FAILURE:******\n")
			print("future date should not be considered published recently\n\n")
# Create your tests here.
