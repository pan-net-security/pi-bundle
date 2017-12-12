import urllib
from cog.command import Command
import pi.util as util
import json


class PrivacyIdeaBase(Command):
    def run(self):
        pass

    def __init__(self):
        super().__init__()
        self.pi_username = None
        self.pi_password = None
        self.pi_fqdn = None

    def prepare(self):
        self.pi_username = self.config("pi_username")
        if self.pi_username is None:
            self.fail("Missing dynamic configuration variable 'pi_username'.")

        self.pi_password = self.config("pi_password")
        if self.pi_password is None:
            self.fail("Missing dynamic configuration variable 'pi_password'.")

        self.pi_fqdn = self.config("pi_fqdn")
        if self.pi_fqdn is None:
            self.fail("Missing dynamic configuration variable 'pi_fqdn'.")
        else:
            parsed_url = urllib.parse.urlparse(self.pi_fqdn)

            parsed_url = parsed_url._replace(path="")

            if not parsed_url.scheme:
                parsed_url = parsed_url._replace(scheme="https")

            self.pi_fqdn = parsed_url.geturl()

    def get_auth_token(self):
        """
        http://privacyidea.readthedocs.io/en/latest/modules/api/auth.html#post--auth
        """
        url = self.pi_fqdn
        token_endpoint = ("%s/%s" % (url, "auth"))

        username = self.pi_username
        password = self.pi_password

        auth_data = {'username': username, 'password': password}

        try:
            resp = util.api_post(url=token_endpoint,
                                 body=auth_data,
                                 )
            try:
                resp = json.loads(resp.content)
            except Exception as e:
                self.fail("Failed to acquire PI-Authorization token towards " + self.pi_fqdn + \
                          " with the following response: \n" + str(
                        resp.content))
                return False

            if bool(resp['result']['status']):
                if 'token' in resp['result']['value']:
                    return resp['result']['value']['token']
            else:
                return False

        except util.requests.exceptions.Timeout as e:
            raise
        except util.requests.exceptions.ConnectionError as e:
            raise
        except util.requests.exceptions.InvalidSchema as e:
            raise

    def validate_serial(self, serial=None):
        if serial:
            serial_length = 20
            if len(serial) > serial_length:
                self.fail("The token serial is too long (over " + str(serial_length) + " chars)")
            if not serial.isalnum():
                self.fail("The token serial is not alphanumeric: '" + str(serial) + "'")

    def validate_user(self, user=None):
        if user:
            username_length = 20
            if len(user) > username_length:
                self.fail("The username length is too long (over " + str(username_length) + " chars)")
            if not user.isalnum():
                self.fail("The username is not alphanumeric: '" + str(user) + "'")