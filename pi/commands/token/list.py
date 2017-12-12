from pi.commands.token.base import TokenBase
import json
import re


class List(TokenBase):
    def __init__(self):
        super().__init__()

    def run(self):
        handler = self.parse_subcommand_
        handler()

    def list(self):
        results = []

        arg_users = self.request.args

        # options not yet supported
        # self.request.options)

        for arg_user in arg_users:
            user = {}

            user['name'] = arg_user
            user['tokens'] = []
            user['result'] = False

            try:
                user_tokens=self.get_tokens(user=arg_user)
                user_tokens = json.loads(user_tokens.content)

                if user_tokens:
                    if bool(user_tokens['result']['status']):
                        if 'tokens' in user_tokens['result']['value']:
                            user['tokens'] = user_tokens['result']['value']['tokens']
                            user['result'] = True
                    else:
                            if user_tokens['result']['error']['code']==905:
                                user['result'] = False

                results.append(user)

            except Exception as e:
                self.fail(e)

        self.response.content(results, template='token_list').send()


    @property
    def parse_subcommand_(self):
        if self.request.args:
            return self.list
        self.fail("This command requires at least one argument and none was passed.")
