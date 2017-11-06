from pi.commands.base import PrivacyIdeaBase
import pi.util as util
import json


class Token(PrivacyIdeaBase):
    def __init__(self):
        super().__init__()
        self.pi_username = None
        self.pi_password = None
        self.pi_fqdn = None

    def run(self):
        handler = self.parse_subcommand_
        handler()

    def list(self):
        results = []

        # remove the first item, that's a sub-command
        arg_users = self.request.args[1:]

        # options not yet supported
        # self.request.options)

        for arg_user in arg_users:
            user = {}
            user['name'] = arg_user
            user['tokens'] = []
            try:
                user_tokens=self.get_tokens_(user=arg_user)
                if user_tokens:
                    user_tokens = json.loads(user_tokens.content)

                    # print(json.dumps(user_tokens, indent=4, sort_keys=True))
                    # print(user_tokens['result']['status'])

                    if bool(user_tokens['result']['status']):
                        if 'tokens' in user_tokens['result']['value']:
                            user['tokens'] = user_tokens['result']['value']['tokens']

                results.append(user)

            except Exception as e:
                self.fail(e)

        self.response.content(results, template='token_list').send()

    # received one user as argument
    def reset(self):
        results = []

        # only process the first argument, anything else is discarded

        arg_user = self.request.args[1]

        # options not yet supported
        # future implementation: serial - to reset one specific token failcounter
        # self.request.options)

        user = {'name': arg_user}

        try:
            reset_tokens = self.reset_tokens_(user=arg_user)
            if reset_tokens:
                reset_tokens = json.loads(reset_tokens.content)

                #print(json.dumps(reset_tokens, indent=4, sort_keys=True))

                user['result'] = reset_tokens['result']['status']

            else:
                user['result'] = False

        except Exception as e:
            self.fail(e)

        results.append(user)
        self.response.content(results, template='token_reset').send()

    # for API reference: http://privacyidea.readthedocs.io/en/latest/modules/api/token.html#get--token-
    def get_tokens_(self, user=None, type=None, serial=None, user_fields=None):
        auth_token = self.get_auth_token_()

        url_token_endpoint = "%s/%s" % (self.pi_fqdn, "token")

        params = dict(user=user, type=type, serial=serial, user_fields=user_fields)

        try:
            return util.api_get(url=url_token_endpoint, token=auth_token, params=params)
        except Exception as e:
            self.fail(e)

    # API reference: http://privacyidea.readthedocs.io/en/latest/modules/api/token.html#post--token-reset
    def reset_tokens_(self, user=None, serial=None, realm=None):
        auth_token = self.get_auth_token_()
        url_token_reset_endpoint = "%s/%s" % (self.pi_fqdn, "token/reset")

        params = dict(user=user, serial=serial, realm=realm)

        try:
            return util.api_post(url=url_token_reset_endpoint, token=auth_token, body=params)
        except Exception as e:
            self.fail(e)


    @property
    def parse_subcommand_(self):
        if self.request.args[0] == "list":
            return self.list
        if self.request.args[0] == "reset":
            return self.reset
        self.fail("Unknown subcommand: '%s'" % self.request.args[0])
