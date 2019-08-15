import datetime
import logging

from django.db import models
from .exel_performer import WorkExel

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return f'XML/{filename}'


class InputExel(models.Model):

    current_file = models.FileField()

    def __str__(self):
        return str(self.current_file)


class AversFlat(models.Model):

    file = models.FileField(upload_to=user_directory_path)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        worker_exel = WorkExel(self.file)
        worker_exel.main_perform()

        today = datetime.date.today()
        file_result_path = f'{today}.csv'
        # try:
        #     input_file_instance = InputExel()
        #     logging.warning(f'Making instance')
        #     input_file_instance.current_file = file_result_path
        #     logging.warning(f'Specify field path')
        #     input_file_instance.save()
        #     logging.warning(f'Save')
        # except Exception as e:
        #     logging.warning(f'Error - {e}')
