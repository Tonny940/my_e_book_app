def validate_file_size(image_object):
    if image_object.size > 5242880:
        raise ValueError('The maximum size of image can be 5MB.')