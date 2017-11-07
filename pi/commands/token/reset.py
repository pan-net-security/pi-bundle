from pi.commands.token.base import TokenBase
import json
import re


class List(TokenBase):
    def __init__(self):
        super().__init__()

    def run(self):
        handler = self.parse_subcommand_
        handler()

    def reset(self):
        results = []

        # currently supporting just one argument
        arg_user = self.request.args[1]
        arg_user = re.sub('\W+', '', arg_user)

        # options not yet supported
        # future implementation: serial - to reset one specific token failcounter
        # self.request.options)

        user = {'name': arg_user}

        try:
            reset_tokens = self.reset_tokens(user=arg_user)
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

    @property
    def parse_subcommand_(self):
        if len(self.request.args)>0:
            return self.reset
        self.fail("This command requires at least one argument and none was passed.")