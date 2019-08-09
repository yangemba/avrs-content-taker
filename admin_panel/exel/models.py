from django.db import models
from ..worker.exel_performer import WorkExel


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return f'XML/{filename}'


class AversFlat(models.Model):

    file = models.FileField(upload_to=user_directory_path)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        worker_exel = WorkExel(self.file)
        worker_exel.main_perform()
