import unittest
import time


class TestTimeMethods(unittest.TestCase):

    def test_time_function(self):
        current_time = time.time()
        print("time.time(): {0}".format(time.time()))
        print("Current time: ", time.ctime(current_time))
        lst = time.localtime(current_time)
        print("time.localtime(): ", lst)
        lmk = time.mktime(lst)
        print("maketime function: {0}".format(lmk))

        st = time.gmtime(current_time)
        print("time.gmtime(): ", st)
        # print("Struct_time: {0} {1} {2} {3}:{4}:{5} {6}, {7}, {8}, {9}, {10}".format(
        #         st.tm_wday, st.tm_mon, st.tm_mday, st.tm_hour, st.tm_min, st.tm_sec, st.tm_year,
        #         st.tm_zone,  st.tm_isdst, st.tm_gmtoff, st.tm_yday))
        mk = time.mktime(st)
        print("maketime function: {0}".format(mk))

        self.assertEqual(int(lmk), int(current_time))

    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())
    #
    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     with self.assertRaises(TypeError):
    #         s.split(2)


if __name__ == '__main__':
    unittest.main()
