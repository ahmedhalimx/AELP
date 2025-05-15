from django.db import models


def get_upload_path(instance, filename):
    return f"uploads/{filename}"


class Course(models.Model):
    class PublishStatus(models.TextChoices):
        PUBLISHED = ('published', 'Published')
        ARCHIVED = ('archived', 'Archived')
        DRAFT = ('draft', 'Draft')

    class AccessRequired(models.TextChoices):
        ANYONE = ('anyone', 'Anyone')
        EMAIL_REQUIRED = ('email_only', 'Email required')

    title = models.CharField(max=100)
    description = models.TextField(blank=True, null=True)
    thumbnail_img = models.ImageField(
        upload_to=get_upload_path,
        blank=True,
        null=True
    )
    access = models.CharField(
        max_length=10,
        choices=AccessRequired.choices,
        default=AccessRequired.ANYONE
    )
    status = models.CharField(
        max_length=10,
        choices=PublishStatus.choices,
        default=PublishStatus.DRAFT
    )
