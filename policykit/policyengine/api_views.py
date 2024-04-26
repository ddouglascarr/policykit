from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import get_user
from policyengine.serializers import MemberSummarySerializer

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def members(request):
    from policyengine.models import CommunityUser
    user = get_user(request)

    if request.method == 'GET':
        users = CommunityUser.objects.filter(community__community=user.community.community)
        return Response(MemberSummarySerializer(users, many=True).data)
        


    raise NotImplemented
