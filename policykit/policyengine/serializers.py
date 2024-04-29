import rest_framework.serializers as serializers

class CommunityRoleSummarySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(source='__str__')

class MemberSummarySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(source='__str__')
    avatar = serializers.CharField()
    roles = CommunityRoleSummarySerializer(many=True, source='get_roles')

class PutMembersRequestSerializer(serializers.Serializer):
    action = serializers.CharField()  # 'assign' or 'unassign' TODO make this an enum
    role = serializers.IntegerField()  # pk of role to assign
    members = serializers.ListField(child=serializers.IntegerField())  # list of user pks to assign to role
