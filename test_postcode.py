import unittest
import UKpostcode.__init__ as pc


class Testpostcode (unittest.TestCase):
    def test_isvalid(self):
        self.assertTrue(pc.isvalid('AA9A 9AA'))
        self.assertTrue(pc.isvalid('A9A 9AA'))
        self.assertTrue(pc.isvalid('A9 9AA'))
        self.assertTrue(pc.isvalid('A99 9AA'))
        self.assertTrue(pc.isvalid('AA9C 9AA'))
        self.assertTrue(pc.isvalid('AA99 9AA'))
        
        self.assertFalse(pc.isvalid("N29 422SJ"))
        self.assertFalse(pc.isvalid("CFDS 1UQ"))
        self.assertFalse(pc.isvalid("N13 8XL1"))
        self.assertFalse(pc.isvalid("PX4 8L"))
        self.assertFalse(pc.isvalid("CR2 20D"))
        self.assertFalse(pc.isvalid("RGS7 9HW"))
        self.assertFalse(pc.isvalid("HXSW 0ST"))
        self.assertFalse(pc.isvalid("EH1 78J"))
        
    def test_get_inward(self):
        self.assertEqual(pc.get_inward('AA9A 9AA'),'9AA')
        self.assertEqual(pc.get_inward('A9A 9AA'),'9AA')
        self.assertEqual(pc.get_inward('A9 9AA'),'9AA')
        self.assertEqual(pc.get_inward('A99 9AA'),'9AA')
        self.assertEqual(pc.get_inward('AA9 9AA'),'9AA')
        self.assertEqual(pc.get_inward('AA99 9AA'),'9AA')
        
        self.assertRaises(Exception,pc.get_inward,'AA9A 9A')
        self.assertRaises(Exception,pc.get_inward,'AA9A 99A')
        self.assertRaises(Exception,pc.get_inward,'AA9A 999')
        
    def test_get_outward(self):
        self.assertEqual(pc.get_outward('AA9A 9AA'),'AA9A')
        self.assertEqual(pc.get_outward('A9A 9AA'),'A9A')
        self.assertEqual(pc.get_outward('A9 9AA'),'A9')
        self.assertEqual(pc.get_outward('A99 9AA'),'A99')
        self.assertEqual(pc.get_outward('AA9 9AA'),'AA9')
        self.assertEqual(pc.get_outward('AA99 9AA'),'AA99')
    
    def test_get_data(self):
        self.assertRaises(Exception,pc.get_data,'AA9A 9AA')
        self.assertEqual(pc.get_data("NR9 4QJ")["status"], 200)
        
  
                
if __name__ == '__main__':
    unittest.main()
        