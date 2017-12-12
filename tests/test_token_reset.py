import os
import unittest
import subprocess

class TestCommand(unittest.TestCase):

    fixed_output_prefix = "COG_TEMPLATE: template\nJSON\n"
    bundle_name = 'pi'

    def setUp(self):
        os.environ['pi_username'] = 'admin'
        os.environ['pi_password'] = 'admin'
        os.environ['pi_fqdn'] = 'http://localhost:5000/'
        os.environ['COG_BUNDLE'] = self.bundle_name
        self.maxDiff=None
        pass

    def test_no_argument(self):
        os.environ['COG_COMMAND'] = 'token-reset'
        os.environ['COG_ARGC'] = '0'

        result=subprocess.run(["cog-command"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.assertEqual(result.stderr.decode("utf-8"), 'This command requires at least one argument and none was passed.\n\n')

    def test_non_alphanum_argument(self):
        os.environ['COG_COMMAND'] = 'token-reset'
        os.environ['COG_ARGC'] = '1'
        os.environ['COG_ARGV_0'] = ';'

        result=subprocess.run(["cog-command"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.assertEqual(result.stderr.decode("utf-8"), "The username is not alphanumeric: '" + \
                         os.environ['COG_ARGV_0'] + \
                         "'\n\nError while validating username: Command execution failed" + \
                         "\n\nCommand execution failed\n\n")

if __name__ == '__main__':
    unittest.main()