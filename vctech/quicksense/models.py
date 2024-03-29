from django.db import models
from accounts.models import UserModel
from django.utils.translation import gettext_lazy as _
from .constants import Constants


class SummarizerModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    credit = models.IntegerField(default=30)
    plan = models.CharField(_("plan"), max_length=100,
                            null=False, blank=False, default=Constants.FREE_PLAN)


class YoutubeModel(models.Model):
    youtubeId = models.CharField(
        _("youtube_id"), max_length=100, null=False, blank=False)
    json_data = models.TextField(default="{}")
