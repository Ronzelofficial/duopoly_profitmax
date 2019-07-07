from duopCalc import *
import unittest

class MyTest(unittest.TestCase):
   def test_simultaneous_duopoly(self):
     self.assertEqual(simultaneous_duopoly(100-x-y, 1/2*x**2, 1/2*y**2),(25,25,50,937.5,937.5))
     self.assertEqual(simultaneous_duopoly(120-x-y, x**2, y**2),(24,24,72,1152,1152))
     self.assertEqual(simultaneous_duopoly(50-2*x-2*y, x*2+10, y*2+10),(8,8,18,118,118))
     self.assertEqual(simultaneous_duopoly(50-2*x-2*y, x*2+10, y*8+12),(9,6,20,152,60))

   def test_sequential_duopoly(self):
     self.assertEqual(sequential_duopoly(100-x-y, 1/2*x**2, 1/2*y**2),(29,24,47.62,952.38,850.34))
     self.assertEqual(sequential_duopoly(100-x-y, 40*x, y*40),(30,15,55,450,225))
     self.assertEqual(sequential_duopoly(150-x-y, 30*x, y*30),(60,30,60 ,1800,900))
     self.assertEqual(sequential_duopoly(150-x-y, 20*x, y*40),(75,18,57.5 ,2812.5,306.25))

   def test_symmetric_cartel(self):
     self.assertEqual(symmetric_cartel(100-x-y, 1/2*x**2, 1/2*y**2),(20,60,1000))
     self.assertEqual(symmetric_cartel(140-x-y, 20*x, 20*y),(30,80,1800))
     self.assertEqual(symmetric_cartel(150-2*x-y, 20*x**2, 20*y**2),(3,140.43, 244.45))

   def test_folk_theorem(self):
     self.assertEqual(folk_theorem(100-x-y, 1/2*x**2, 1/2*y**2), 0.516)
     self.assertEqual(folk_theorem(140-x-y, 20*x, 20*y), 0.529)

unittest.main()

