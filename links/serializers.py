from rest_framework import serializers
from .models import Item

class ItemDetailSerializer(serializers.ModelSerializer):
    share_link = serializers.SerializerMethodField()

    class Meta:
        model = Item
        fields = ['id', 'title', 'description', 'share_link']

    def get_share_link(self, item):
        request = self.context.get('request')
        if request:
            current_domain = request.build_absolute_uri('/')
            return f"{current_domain}item_detail/{item.id}/"
        return ""