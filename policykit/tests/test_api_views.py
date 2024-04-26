from rest_framework.test import APIClient, APITestCase, APIRequestFactory, force_authenticate
from django.test import TestCase
from django.contrib.auth.models import User

import tests.utils as TestUtils

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
