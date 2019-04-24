from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import get_user_model
from django.utils import timezone
User = get_user_model()
import uuid
from bs4 import BeautifulSoup






class Stories(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE, default=2)
	title = models.CharField(max_length=100)
	pub_date = models.DateTimeField(default=timezone.now)
	body = RichTextUploadingField()
	family_uuid = models.UUIDField(default=uuid.uuid4)
	image = models.ImageField(upload_to="images/", blank=True, null=True)
	parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)


	def __str__(self):
		return self.title

	def summary(self):
		html = self.body[:50]
		soup = BeautifulSoup(html, "html.parser" )
		text = soup.get_text()

		return text + "..."
