from django.db import models
from datetime import datetime

from .validators import validate_video_file_extension


class Recording(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=datetime.now)
    # FileField.storage() to call the file
    # video.url to see the URL
    video = models.FileField(upload_to='videos', validators=[validate_video_file_extension])
