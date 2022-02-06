import re

from mistletoe import HTMLRenderer

email_replacement_regex = re.compile(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)")


class JobNinjaRenderer(HTMLRenderer):

    # Responsible for handling emails
    def render_raw_text(self, token):
        if '@' in token:
            return email_replacement_regex.sub('<button class="email_replacement">Jetzt bewerben</button>',
                                               token.content)
        return token.content

    # Responsible for handling links
    def render_link(self, _):
        return '<button class="email_replacement">Jetzt bewerben</button>'
