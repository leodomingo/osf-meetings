from django.test import TestCase, RequestFactory
from unittest import skip
import mock
import factory
from submissions.models import Submission
# from approvals.models import Approval
# from conferences.models import Conference
from django.contrib.auth.models import User
from test_factories import (UserFactory, SubmissionFactory, ConferenceFactory,
                            SocialAccountFactory, SocialTokenFactory,
                            SocialAppFactory, ApprovalFactory, ResponseFactory)
from serializers import SubmissionSerializer
from views import SubmissionViewSet
# from allauth.socialaccount.models import SocialAccount, SocialToken, SocialApp
# from osf_oauth2_adapter.views import OSFOAuth2Adapter


class TestPermissions(TestCase):

    def setUp(self):
        self.user1 = UserFactory(
            username='user1'
        )
        self.user2 = UserFactory(
            username='user2'
        )
        self.user3 = User.objects.get(username='AnonymousUser')
        self.conference = ConferenceFactory(
            admin=self.user1,
            id='conferenceId'
        )
        self.submission = SubmissionFactory(
            contributor=self.user2,
            conference=self.conference,
            approval=factory.SubFactory(ApprovalFactory, approved=True)
            )

    def test_permissions(self):
        self.assertTrue(self.user1.has_perm('view_submission', self.submission))
        self.assertTrue(self.user2.has_perm('view_submission', self.submission))
        self.assertTrue(self.user3.has_perm('view_submission', self.submission))

        self.assertTrue(self.user1.has_perm('change_submission', self.submission))
        self.assertTrue(self.user2.has_perm('change_submission', self.submission))
        self.assertFalse(self.user3.has_perm('change_submission', self.submission))

        self.assertTrue(self.user1.has_perm('delete_submission', self.submission))
        self.assertTrue(self.user2.has_perm('delete_submission', self.submission))
        self.assertFalse(self.user3.has_perm('delete_submission', self.submission))


class TestSerializers(TestCase):

    def setUp(self):
        self.user = UserFactory(
            username='testUser'
            )
        self.request = RequestFactory().get('./fake_path')
        self.request.query_params = {}
        self.request.user = self.user
        self.submission = SubmissionFactory(
            contributor=self.user,
            conference=factory.SubFactory(ConferenceFactory, id='382',
                                          admin=factory.SubFactory(UserFactory, username='u1'))
            )

    def test_get_links(self):
        serializer = SubmissionSerializer(context={'request': self.request})
        links = serializer.get_links(self.submission)
        self.assertEqual(links['self'], 'http://testserver/submissions/1/')
        self.assertEqual(links['conference'], 'http://testserver/conferences/382/')

    def test_get_can_edit(self):
        serializer = SubmissionSerializer(context={'request': self.request})
        submission2 = SubmissionFactory(
            contributor=factory.SubFactory(UserFactory, username='differentUser'),
            conference=factory.SubFactory(ConferenceFactory, id='234', admin=self.user)
            )
        submission3 = SubmissionFactory(
            contributor=factory.SubFactory(UserFactory, username='differentUser2'),
            conference=factory.SubFactory(ConferenceFactory, id='18',
                                          admin=factory.SubFactory(UserFactory,
                                                                   username='differentUser3'))
            )
        self.assertTrue(serializer.get_can_edit(self.submission))
        self.assertTrue(serializer.get_can_edit(submission2))
        self.assertFalse(serializer.get_can_edit(submission3))


class TestSignals(TestCase):

    def setUp(self):
        self.user1 = UserFactory(
            username='user1'
        )
        self.user2 = UserFactory(
            username='user2'
        )
        self.user3 = User.objects.get(username='AnonymousUser')
        self.conference = ConferenceFactory(
            admin=self.user1,
            id='conferenceId'
        )
        self.submission1 = SubmissionFactory(
            contributor=self.user2,
            conference=self.conference,
            approval=factory.SubFactory(ApprovalFactory, approved=True)
            )
        self.submission2 = SubmissionFactory(
            contributor=self.user2,
            conference=self.conference,
            approval=factory.SubFactory(ApprovalFactory, approved=False)
            )

    def test_add_permissions_approved(self):
        self.submission1.save()
        self.assertTrue(self.user3.has_perm('view_submission', self.submission1))

    def test_add_permissions_rejected(self):
        self.submission2.save()
        self.assertFalse(self.user3.has_perm('view_submission', self.submission2))


class TestViews(TestCase):

    def setUp(self):
        self.user = UserFactory(
            username='testViewsUser',
            id='428'
            )
        self.socialApp = SocialAppFactory()
        self.socialAccount = SocialAccountFactory(
            user=self.user,
            uid='testViewsUser'
            )
        self.socialToken = SocialTokenFactory(
            account=self.socialAccount,
            app=factory.SubFactory(SocialAppFactory),
            token='235387023',
            token_secret='24358103981'
            )
        self.approval = ApprovalFactory(
            id=1,
            approved=True
        )
        self.conference = ConferenceFactory(
            admin=self.user,
            id='conferenceId'
            )
        self.request = RequestFactory().post('./fake_path')
        self.request.user = self.user
        self.request.query_params = {}
        self.contributorData = {'type': 'User', 'username': 'testViewsUser', 'id': '428'}
        self.approvalData = {'type': 'Approval', 'approved': True, 'id': 1}
        self.conferenceData = {'type': 'conferences', 'id': 'conferenceId'}
        self.request.data = {'id': 15, 'node_id': '42u2p', 'title': 'Submission65',
                             'contributor': self.contributorData, 'description':
                             'This is a submission', 'approval': self.approvalData,
                             'conference': self.conferenceData}
        self.views = SubmissionViewSet()

        self.submission1 = SubmissionFactory(
            conference=self.conference,
            contributor=self.user
            )
        self.submission2 = SubmissionFactory(
            conference=self.conference,
            contributor=self.user
            )
        self.submission3 = SubmissionFactory(
            conference=self.conference,
            contributor=self.user
            )

    @skip('This test still needs work')
    # test_create is especially complicated because the create method involves interacting
    # with the socialToken. This data needs to be mocked, but mocking it creates its own
    # set of issues because of the format of the data.  The following code inside the
    # create method is where data needs to be mocked:
    #
    #
    #         response = requests.post(
    #             self.node_url,
    #             data=json.dumps(node),
    #             headers={
    #                 'Authorization': 'Bearer {}'.format(osf_token),
    #                 'Content-Type': 'application/json; charset=UTF-8'
    #             }
    #         )
    #         response_osf = response.json()
    #         serializer.save(
    #             contributor=contributor,
    #             approval=new_approval,
    #             node_id=response_osf['data']['id']
    #         )
    #
    #
    # Right now the test is mocking request.post to return a Response object with the content
    # hardcoded in, but response.json() still isn't returning the correct data. If I had more
    # time, I would look into how to format  this fake data so that the test will work, but
    # my internship is ending right now so someone else has to do it. Sorry :(
    @mock.patch('requests.post')
    def test_create(self, mock_method):
        mock_method.return_value(ResponseFactory(
            content={'data': {'id': 'qjdfy'}}
            ))
        # adapter = OSFOAuth2Adapter(self.request)
        # adapter.complete_login(self.request, self.socialApp, self.socialToken)
        self.views.create(self.request)

    def test_get_queryset(self):
        queryset = self.views.queryset
        self.assertEqual(queryset[0], Submission.objects.all()[0])
        self.assertEqual(queryset[1], Submission.objects.all()[1])
        self.assertEqual(queryset[2], Submission.objects.all()[2])
