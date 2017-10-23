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
        if self.pi_username == None:
            self.fail("Missing dynamic configuration variable 'pi_username'.")

        self.pi_password = self.config("pi_password")
        if self.pi_password == None:
            self.fail("Missing dynamic configuration variable 'pi_password'.")

        self.pi_fqdn = self.config("pi_fqdn")
        if self.pi_fqdn == None:
            self.fail("Missing dynamic configuration variable 'pi_fqdn'.")
        else:
            parsed_url = urllib.parse.urlparse(self.pi_fqdn)

            parsed_url = parsed_url._replace(path="")

            if not parsed_url.scheme:
                parsed_url = parsed_url._replace(scheme="https")

            self.pi_fqdn = parsed_url.geturl()

    def get_auth_token_(self):
        """Retrieve auth token

        :returns: token or None upon error

        **Example Authentication Request**:

        .. sourcecode:: http

           POST /auth HTTP/1.1
           Host: example.com
           Accept: application/json

           username=admin
           password=topsecret

        **Example Authentication Response**:

        .. sourcecode:: http

           HTTP/1.0 200 OK
           Content-Length: 354
           Content-Type: application/json

           {
                "id": 1,
                "jsonrpc": "2.0",
                "result": {
                    "status": true,
                    "value": {
                        "token": "eyJhbGciOiJIUz....jdpn9kIjuGRnGejmbFbM"
                    }
                },
                "version": "privacyIDEA unknown"
           }

        """

        url = self.pi_fqdn
        token_endpoint = ("%s/%s" % (url, "auth"))  # https://<fqdn>/token

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
                self.fail("Failed to acquire PI-Authorization token towards " + self.pi_fqdn + " with the following response: \n" + str(resp.content))
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