from rest_framework.serializers import ModelSerializer, SerializerMethodField
from base.models import Room, User, Topic

class RoomSerializer(ModelSerializer):
    participants = SerializerMethodField()
    host = SerializerMethodField()
    topic = SerializerMethodField()

    class Meta:
        model = Room
        fields = '__all__'

    def get_participants(self, obj):
        return [participant.username for participant in obj.participants.all()]
    
    def get_host(self, obj):
        return obj.host.username

    def get_topic(self, obj):
        return obj.topic.name


# from rest_framework.serializers import ModelSerializer
# from base.models import Room, User

# class RoomSerializer(ModelSerializer):
#     class Meta:
#         model = Room
#         fields = '__all__'