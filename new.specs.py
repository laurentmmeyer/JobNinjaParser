import unittest
import glob

import mistletoe

from JobNinjaRenderer import JobNinjaRenderer

all_test_markdowns = glob.glob("./test-data/*.md")


class NewProcessorTestCase(unittest.TestCase):
    def test_that_new_is_correct(self):
        for filename in all_test_markdowns:
            with open(filename) as file:
                old_rendered_html = mistletoe.markdown(file.read(), JobNinjaRenderer)
            with open(filename.replace(".md", ".html")) as html_file:
                old_hmtl = html_file.read()
        self.assertEqual(old_rendered_html, old_hmtl)


if __name__ == '__main__':
    unittest.main()
