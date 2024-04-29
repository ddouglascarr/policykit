import urllib3
from rest_framework.test import APIClient, APITestCase, APIRequestFactory, force_authenticate
from django.contrib.auth.models import User
from django.test.client import MULTIPART_CONTENT

import tests.utils as TestUtils

from policyengine.models import CommunityRole

class APIViewsTestCase(APITestCase):

    def setUp(self):
        self.slack_community, self.user = TestUtils.create_slack_community_and_user()
        self.community = self.slack_community.community
        self.constitution_community = self.community.constitution_community


    def test_get_members(self):
        self.client.force_login(user=self.user, backend="integrations.slack.auth_backends.SlackBackend")
        response = self.client.get('/api/members')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

        user_0 = response.data[0]
        self.assertEqual(user_0['id'], self.user.id)
        self.assertEqual(user_0['name'], 'user1')
        self.assertEqual(len(user_0['roles']), 1)
        self.assertEqual(user_0['roles'][0]['name'], 'fake role')

    def test_put_members_creates_add_user_action(self):
        self.client.force_login(user=self.user, backend="integrations.slack.auth_backends.SlackBackend")
        # create user to assign roles to.
        role = CommunityRole.objects.create(
            role_name="test role", community=self.community)
        user_2 = TestUtils.create_user_in_slack_community(self.slack_community, "user_2")
        user_3 = TestUtils.create_user_in_slack_community(self.slack_community, "user_3")
        
        response = self.client.put(
            '/api/members',
            data={'action': 'assign', 'role': role.id, 'members': [user_2.pk, user_3.pk]},
            format='multipart'
        )
        self.assertEqual(response.status_code, 200)

        test_resp = self.client.get('/api/members')
        self.assertEqual(len(test_resp.data), 3)
        user_2_resp = next(u for u in test_resp.data if u['id'] == user_2.pk)
        user_2_role_ids = [r['id'] for r in user_2_resp['roles']]
        self.assertTrue(set(user_2_role_ids).issuperset({role.id}))
