import os
from django.core.exceptions import ValidationError


def validate_document_file_extension(value):
    ext = os.path.splitext(value.name)[-1]  # [0] returns path+filename
    # Changed this to from 1 to -1 in case the file had any fake formats in its name
    valid_extensions = ['.pdf', '.doc', '.docx', '.jpg', '.png', '.xlsx', '.xls']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')


def validate_score(value):
    if value > 100 or value < 0:
        raise ValidationError('The scores should be from 0 to 100.')
