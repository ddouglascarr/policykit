import rest_framework.serializers as serializers

class CommunityRoleSummarySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(source='__str__')

class MemberSummarySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(source='__str__')
    avatar = serializers.CharField()
    roles = CommunityRoleSummarySerializer(many=True, source='get_roles')

