from django.test import TestCase
import mock

from mail.mails import create_mailgun_conference_route


class TestMail(TestCase):
    @mock.patch('mail.mails.requests.post')
    def test_create_mailgun_conference_route_poster(self, mock_post):
        create_mailgun_conference_route('this', 'poster')
        mock_post.assert_called_with(
            'https://api.mailgun.net/v3/routes',
            auth=('api', ''),
            data={
                'priority': 0,
                'action': [
                    "forward('http://localhost:8000/mail/inbound/')",
                    'stop()'
                ],
                'expression': "match_recipient('this-poster@osf.io')",
                'description': 'Conference submission by email'
            }
        )

    @mock.patch('mail.mails.requests.post')
    def test_create_mailgun_conference_route_talk(self, mock_post):
        create_mailgun_conference_route('this', 'talk')
        mock_post.assert_called_with(
            'https://api.mailgun.net/v3/routes',
            auth=('api', ''),
            data={
                'priority': 0,
                'action': [
                    "forward('http://localhost:8000/mail/inbound/')",
                    'stop()'
                ],
                'expression': "match_recipient('this-talk@osf.io')",
                'description': 'Conference submission by email'
            }
        )
