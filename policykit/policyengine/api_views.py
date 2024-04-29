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
        put_members(user, **req.data)
        return Response({}, status=200)

    raise NotImplemented

def get_members(user):
    from policyengine.models import CommunityUser
    users = CommunityUser.objects.filter(community__community=user.community.community)
    return users

def put_members(user, action, role, members):
    from constitution.models import (PolicykitAddUserRole,
                                     PolicykitRemoveUserRole)

    from policyengine.models import CommunityRole, CommunityUser

    action_model = None
    if action == 'assign':
        action_model = PolicykitAddUserRole()
    elif action == 'revoke':
        action_model = PolicykitRemoveUserRole()
    else:
        raise ValueError('Invalid action')

    action_model.community = user.constitution_community
    action_model.initiator = user
    action_model.role = CommunityRole.objects.filter(pk=role)[0]
    action_model.save(evaluate_action=False)
    action_model.users.set(CommunityUser.objects.filter(id__in=members))
    action_model.save(evaluate_action=True)
