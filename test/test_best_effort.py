import unittest
import ais

class BestEffortTest(unittest.TestCase):

    def testDecodeWithExtraBits(self):
        messages = [
            (1, '181:Kjh01ewHFRPDK1s3IRcn06sd0', 0),  # extra char
            (1, '181:Kjh01ewHFRPDK1s3IRcn06sd0', 2),  # extra char, wrong pad, 4 extra bits
            (5, '533uwnT00000uCCSS00MD5@Dl4h400000080001c8h<25uAn00Q1C1VRBS0000000000000', 0),  # wrong pad
        ]
        for id, body, pad in messages:
            # default value for best_effort is False, so messages with extra bits should fail
            with self.assertRaises(ais.DecodeError):
                _ = ais.decode(body, pad)

            # Set best_effort to True and now it should succeed
            best_effort = True
            msg = ais.decode(body, pad, best_effort)
            self.assertEqual(id, msg['id'])

