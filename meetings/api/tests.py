from django.test import TestCase
from unittest import skip


class TestCheckLoggedIn(TestCase):

    @skip('Test with authenticated user (this may duplicate CurrentUserView)')
    def test_user_authenticated(self):
        pass

    @skip('Test with unauthenticated user')
    def test_user_unauthenticated(self):
        pass


class TestCurrentUserView(TestCase):

    @skip('Test with authenticated user')
    def test_user_authenticated(self):
        pass

    @skip('Test with unauthenticated user')
    def test_user_unauthenticated(self):
        pass


class TestUserDetail(TestCase):

    @skip('Test that correct user is returned')
    def test_get(self):
        pass


class TestAuthenticateUser(TestCase):

    @skip('Use several test cases to show that user is authenticated')
    def test_post(self):
        pass
