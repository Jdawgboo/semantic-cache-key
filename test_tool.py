import unittest
from tool import key
class KeyTests(unittest.TestCase):
 def test_stability(self):
  self.assertEqual(key('m',' p ',options={'b':2,'a':1}),key('m','p',options={'a':1,'b':2}));self.assertNotEqual(key('m','a'),key('m','b'))
if __name__=='__main__':unittest.main()
