from rest_framework import serializers
from ..models import Digit
import base64
import uuid
from django.core.files.base import ContentFile

class Base64ImageField(serializers.ImageField):

    def to_internal_value(self, data):
        print('data', data)
        _format, str_img = data.split(';base64')
        print('format',_format)
        print('str_img', str_img)
        print('type str_image', type(str_img))
        decoded_file = base64.b64decode(str_img)
        print('decoded file', type(decoded_file))
        print('type decoded_file', decoded_file)
        fname = f"{str(uuid.uuid4())[:10]}.png"
        print('fname', fname)
        data = ContentFile(decoded_file, name=fname)

        return super().to_internal_value(data)

class DigitSerializer(serializers.ModelSerializer):
    image = Base64ImageField()

    class Meta:
        model = Digit
        fields = ('id', 'image', 'result')