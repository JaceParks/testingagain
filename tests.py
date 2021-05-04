import unittest
import thisfunc

class testfunctions(unittest.TestCase):
    def test_cube(self):
        #should not fail
        self.assertEqual(thisfunc.cube(1),1)
        self.assertEqual(thisfunc.cube(3),27)
        self.assertEqual(thisfunc.cube(10),1000)
        self.assertEqual(thisfunc.cube(-3),-27)

        #should fail
        self.assertEqual(thisfunc.cube(-3),-4)
        self.assertEqual(thisfunc.cube(5),100)
        self.assertEqual(thisfunc.cube(11.11),33)

    def test_avg(self):
        #should not fail
        self.assertEqual(thisfunc.avg([5,5,5]),5)
        self.assertEqual(thisfunc.avg([50,100,150]),100)
        self.assertEqual(thisfunc.avg([1,1,1,1,1,1,1,1,1,1,1,1,1,1]),1)

        #should fail
        self.assertEqual(thisfunc.avg([1,-1,12]),0)
        self.assertEqual(thisfunc.avg([56000,33123,312312312,3123123]),-312312)
        self.assertEqual(thisfunc.avg([123,333213,312312312,31,3123131]),500)

    def test_full(self):
        #should not fail
        self.assertEqual(thisfunc.full("jace","parks"),"jace parks")
        self.assertEqual(thisfunc.full("Martin","Luther"),"Martin luther")
        self.assertEqual(thisfunc.full("James","Harden"),"James Harden")

        #should fail
        self.assertEqual(thisfunc.full("james","franco"),"Seth rogen")
        self.assertEqual(thisfunc.full("Harley","quinn"),"The joker")
        self.assertEqual(thisfunc.full("Donald","Glover"),"Childish Gambino")    


if __name__ == "__main__":
    unittest.main()