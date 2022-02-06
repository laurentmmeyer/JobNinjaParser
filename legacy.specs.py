import unittest
import glob
import markdown2
import time

all_test_markdowns = glob.glob("./test-data/*.md")


class LegacyTestCase(unittest.TestCase):
    def test_that_legacy_is_correct(self):
        for filename in all_test_markdowns:
            with open(filename) as file:
                old_rendered_html = markdown2.markdown(file.read(),
                                                       extras=['replace_email_by_button', 'replace_link_by_button'])
            with open(filename.replace(".md", ".html")) as html_file:
                old_hmtl = html_file.read()
        self.assertEqual(old_rendered_html, old_hmtl)

    def test_that_legacy_is_slow(self):
        start = time.time()
        for i in range(0, 100):
            for filename in all_test_markdowns:
                with open(filename) as file:
                    markdown2.markdown(file.read(), extras=['replace_email_by_button', 'replace_link_by_button'])
        end = time.time()
        self.assertTrue(end - start > 1)  # 1 sec


if __name__ == '__main__':
    unittest.main()
