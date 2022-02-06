import unittest
import glob

import mistletoe

from JobNinjaRenderer import JobNinjaRenderer

all_test_markdowns = glob.glob("./test-data/*.md")


class NewProcessorTestCase(unittest.TestCase):
    def test_that_new_is_correct(self):
        for filename in all_test_markdowns:
            with open(filename) as file:
                new_rendered_html = mistletoe.markdown(file.read(), JobNinjaRenderer)
            with open(filename.replace(".md", ".html")) as html_file:
                old_html = html_file.read()
        print(old_html)
        print("="*100)
        print(new_rendered_html)
        self.assertEqual(new_rendered_html.replace("\n", ""), old_html.replace("\n", ""))


if __name__ == '__main__':
    unittest.main()
