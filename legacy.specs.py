import unittest
import glob
import markdown2
import time

all_test_markdowns = glob.glob("./test-data/*.md")


class LegacyTestCase(unittest.TestCase):
    def test_that_legacy_is_correct(self):
        # given

        # when
        for filename in all_test_markdowns:
            with open(filename) as file:
                old_rendered_html = markdown2.markdown(file.read(),
                                                       extras=['replace_email_by_button', 'replace_link_by_button'])
            with open(filename.replace(".md", ".html")) as html_file:
                old_hmtl = html_file.read()
            # then
            self.assertEqual(old_rendered_html, old_hmtl)

    @unittest.skip("slow")
    def test_that_legacy_is_slow(self):
        # given
        files = []
        for filename in all_test_markdowns:
            with open(filename) as file:
                files.append(file.read())

        start = time.time()

        # when
        for i in range(0, 1000):
            for file in files:
                markdown2.markdown(file, extras=['replace_email_by_button', 'replace_link_by_button'])

        # then
        end = time.time()
        duration = end - start
        message = "It took {}s".format(duration)
        self.assertTrue(duration > 30, message)  # 1 sec


if __name__ == '__main__':
    unittest.main()
