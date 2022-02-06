import glob
import markdown2

for filename in glob.glob("../test-data/*.md"):
    with open(filename) as file:
        old_md = markdown2.markdown(file.read(), extras=['replace_email_by_button', 'replace_link_by_button'])
        with open(filename.replace(".md", ".html"), "w+") as output:
            output.write(old_md)
