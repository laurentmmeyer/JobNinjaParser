import re

from mistletoe import HTMLRenderer

email_replacement_regex = re.compile(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)")
link_replacement_regex = re.compile(r"""<a[\s]+([^>]+)>((?:.(?!\<\/a\>))*.)<\/a>""", re.IGNORECASE | re.VERBOSE)
url_replacement_regex = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
                                   re.MULTILINE)
replacement = '<button class="email_replacement">Jetzt bewerben</button>'


class JobNinjaRenderer(HTMLRenderer):

    # Responsible for handling content
    def render_raw_text(self, token):
        content = token.content
        content = email_replacement_regex.sub(replacement, content)
        content = link_replacement_regex.sub(replacement, content)
        content = url_replacement_regex.sub(replacement, content)
        return content

    def render_link(self, _):
        return replacement
