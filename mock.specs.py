import unittest
import markdown2


class MockTestCase(unittest.TestCase):
    def test_module_is_reacting_as_the_legacy_module_with_kwargs(self):
        # given
        text = "Hello [World](https://google.com)"

        # when
        test_object = markdown2.markdown(text, extras=['replace_email_by_button', 'replace_link_by_button'])

        # then
        self.assertEqual(test_object, """<p>Hello <button class="email_replacement">Jetzt bewerben</button></p>\n""")

    def test_module_is_reacting_as_the_legacy_module_with_no_args(self):
        # given
        text = "Hello [World](https://google.com)"

        # when
        test_object = markdown2.markdown(text)

        # then
        self.assertEqual(test_object, """<p>Hello <button class="email_replacement">Jetzt bewerben</button></p>\n""")


if __name__ == '__main__':
    unittest.main()
