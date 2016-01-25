from .handler_class import Handler
from models.page_model import Page


def root_url(url):
    return url.replace('_edit/', '')


class EditPageHandler(Handler):
    def render_edit(self, url, user=None, page=None, error=''):
        self.render('edit.html', url='/_edit' + url, user=user,
                    page=page, error=error)

    def get(self, url):
        page = Page.by_url(url)
        if self.user:
            self.render_edit(url, user=self.user, page=page)
        else:
            self.render('display.html', url=url, page=page)

    def post(self, url):
        if not self.user:
            self.render('display.html', url=url)
        else:
            base_url = root_url(url)
            content = self.request.get('content') or ''
            page = Page.find_page(base_url)
            if page.update_content(content):
                self.redirect(base_url)
            else:
                error = 'An error occurred during submission, please try again!'
                self.render_edit(url, user=self.user, page=page, error=error)
