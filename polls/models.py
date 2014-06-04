import datetime
from django.utils import timezone
from django.db import models

# Create your models here.
class Poll(models.Model):
    def __unicode__(self):
        return self.question
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <now
    was_published_recently.admin_order_field ='pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'published recently?'
    
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('data published')
    
        
class Choice(models.Model):
    def __unicode__(self):
        return self.choice_text
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
