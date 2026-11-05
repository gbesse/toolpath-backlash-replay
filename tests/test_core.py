import unittest,math
from toolpath_backlash_replay.core import run
class DomainTests(unittest.TestCase):
 def test_reversal_deadband(self):
  x=run({'backlash':2,'commands':[0,3,2,1,0]});self.assertEqual([r['output']for r in x['trace']],[0,2,2,2,1])
 def test_zero_backlash(self):
  x=run({'backlash':0,'commands':[0,3,-2]});self.assertEqual(x['command_travel'],x['output_travel'])
 def test_bound(self):
  x=run({'backlash':4,'commands':[0,10,-10,3]});self.assertTrue(all(abs(r['tracking_error'])<=2 for r in x['trace']))
