from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import get_user
from policyengine.serializers import MemberSummarySerializer, PutMembersRequestSerializer

@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def members(request):
    user = get_user(request)

    if request.method == 'GET':
        return Response(
            MemberSummarySerializer(get_members(user), many=True).data
        )

    if request.method == 'PUT':
        req = PutMembersRequestSerializer(data=request.data)
        if not req.is_valid():
            return Response(req.errors, status=400)
        put_members(*req.data)
        return Response({}, status=200)

    raise NotImplemented

def get_members(user):
    from policyengine.models import CommunityUser
    users = CommunityUser.objects.filter(community__community=user.community.community)
    return users

def put_members(action, role, members):
    pass
