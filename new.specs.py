import unittest
import glob
import time
import mistletoe

from JobNinjaRenderer import JobNinjaRenderer

all_test_markdowns = glob.glob("./test-data/*.md")


class NewProcessorTestCase(unittest.TestCase):
    def test_correctness(self):
        # given
        self.maxDiff = None

        # when
        for filename in all_test_markdowns:
            with open(filename) as file:
                new_rendered_html = mistletoe.markdown(file.read(), JobNinjaRenderer)
            with open(filename.replace(".md", ".correct.html")) as html_file:
                old_html = html_file.read()
            # then
            print("Filename", filename)
            self.assertEqual(new_rendered_html.replace("\n", ""), old_html.replace("\n", ""))

    @unittest.skip("slow")
    def test_speed(self):
        # given
        files = []
        for filename in all_test_markdowns:
            with open(filename) as file:
                files.append(file.read())

        start = time.time()

        # when
        for i in range(0, 1000):
            for file in files:
                mistletoe.markdown(file, JobNinjaRenderer)

        # then
        end = time.time()
        duration = end - start
        message = "It took {}s".format(duration)
        self.assertTrue(duration < 10, message)

if __name__ == '__main__':
    unittest.main()
