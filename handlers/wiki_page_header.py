import bleach
import markdown


def markdown_to_html(content):
    return markdown.markdown(content)


def escape_html(text):
    return bleach.clean(text)
