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
            arg_user = re.sub('\W+', '', arg_user)
            user['name'] = arg_user
            user['tokens'] = []
            try:
                user_tokens=self.get_tokens(user=arg_user)
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


    @property
    def parse_subcommand_(self):
        if len(self.request.args)>0:
            return self.list
        self.fail("This command requires at least one argument and none was passed.")
