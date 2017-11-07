import urllib
from pi.commands.base import PrivacyIdeaBase
import pi.util as util
import json


class TokenBase(PrivacyIdeaBase):
    def run(self):
        pass

    def __init__(self):
        super().__init__()
        self.pi_username = None
        self.pi_password = None
        self.pi_fqdn = None

    # for API reference: http://privacyidea.readthedocs.io/en/latest/modules/api/token.html#get--token-
    def get_tokens(self, user=None, type=None, serial=None, user_fields=None):
        self.validate_serial(serial=serial)
        self.validate_user(user=user)

        auth_token = self.get_auth_token()

        url_token_endpoint = "%s/%s" % (self.pi_fqdn, "token")

        params = dict(user=user, type=type, serial=serial, user_fields=user_fields)

        try:
            return util.api_get(url=url_token_endpoint, token=auth_token, params=params)
        except Exception as e:
            self.fail(e)

    # API reference: http://privacyidea.readthedocs.io/en/latest/modules/api/token.html#post--token-reset
    def reset_tokens(self, user=None, serial=None, realm=None):
        self.validate_user(user)
        self.validate_serial(serial)

        auth_token = self.get_auth_token()
        url_token_reset_endpoint = "%s/%s" % (self.pi_fqdn, "token/reset")

        params = dict(user=user, serial=serial, realm=realm)

        try:
            return util.api_post(url=url_token_reset_endpoint, token=auth_token, body=params)
        except Exception as e:
            self.fail(e)

    # API reference: http://privacyidea.readthedocs.io/en/latest/modules/api/token.html#delete--token-(serial)
    def delete_tokens(self, user=None, serial=None, realm=None):
        self.validate_serial(serial=serial)
        self.validate_user(user=user)

        auth_token = self.get_auth_token()
        url_token_delete_endpoint = "%s/%s/%s" % (self.pi_fqdn, "token", serial)

        if user:
            params = dict(user=user, serial=serial, realm=realm)
        else:
            params = None

        try:
            return util.api_delete(url=url_token_delete_endpoint, token=auth_token, body=params)
        except Exception as e:
            self.fail(e)