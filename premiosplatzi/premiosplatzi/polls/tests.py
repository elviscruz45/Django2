import datetime
from django.test import TestCase  # Create your tests here.
from django.utils import timezone

from .models import Question

class QuestionModeltests(TestCase):
    def test_was_publish_recently_with_future_questions(self):
        """was_published_recently return False for questions whose pub_date is in the future"""
        time=timezone.now()+datetime.timedelta(days=30)
        future_question=Question(question_text="Quien es el mejor course Director de Platzi",pub_date=time)
        self.assertIs(future_question.was_published_recently(),False)
        

