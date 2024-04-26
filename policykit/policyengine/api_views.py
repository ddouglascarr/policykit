from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import get_user
from policyengine.serializers import MemberSummarySerializer

@api_view(['GET', 'POST'])
def members(request):
    from policyengine.models import CommunityPlatform, CommunityUser, Proposal
    user = get_user(request)

    if request.method == 'GET':
        users = CommunityUser.objects.filter(community__community=user.community.community)
        return Response(MemberSummarySerializer(users, many=True).data)
        

    raise NotImplemented
