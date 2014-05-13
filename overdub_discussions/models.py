from django.db import models

# from core.models import AbstractActivity
from core.models import ActivityCollection, AbstractActivity

class OverdubActivity(AbstractActivity):
	collection = models.ForeignKey(
		ActivityCollection, blank=True, null=True, on_delete=models.SET_NULL, related_name='overdubs')
	media = models.URLField(null=True, blank=True)
	# upload_video = models.FileField(
 #        upload_to='overdub_videos', null=True, blank=True)

	read_after_post = models.BooleanField()