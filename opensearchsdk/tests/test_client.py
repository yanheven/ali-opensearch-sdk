# from testtools import TestCase
#
# from opensearchsdk import client
#
#
# class ClientTest(TestCase):
#     def test_client_get_reset_timings(self):
#         cs = client.Client('base_url', 'public_key', 'private_key')
#         self.assertEqual(0, len(cs.get_timing()))
#         cs.client.time.append("somevalue")
#         self.assertEqual(1, len(cs.get_timing()))
#         self.assertEqual("somevalue", cs.get_timing()[0])
#
#         cs.reset_timing()
#         self.assertEqual(0, len(cs.get_timing()))
