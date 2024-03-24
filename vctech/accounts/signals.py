from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import UserModel
from quicksense.models import SummarizerModel


@receiver(post_save, sender=UserModel)
def create_item_for_new_user(sender, instance, created, **kwargs):
    if created:
        SummarizerModel.objects.create(user=instance, credit=30)
