from pi.commands.token.base import TokenBase
import json


class Delete(TokenBase):
    def __init__(self):
        super().__init__()

    def run(self):
        handler = self.parse_subcommand_
        handler()

    def delete(self):
        results = []

        token_serials = self.request.args

        # options not yet supported
        # future implementation: serial - to delete tokens based on user

        for token_serial in token_serials:
            delete_result={}

            delete_result['serial'] = token_serial

            try:
                delete_token = self.delete_tokens(serial=token_serial)

                if delete_token:
                    delete_token = json.loads(delete_token.content)

                    if delete_token['result']['status']:
                        delete_result['result'] = delete_token['result']['value']

                else:
                    delete_token['result'] = 0

            except Exception as e:
                self.fail(e)

            results.append(delete_result)

        self.response.content(results, template='token_delete').send()

    @property
    def parse_subcommand_(self):
        if self.request.args:
            return self.delete
        self.fail("This command requires at least one argument and none was passed.")