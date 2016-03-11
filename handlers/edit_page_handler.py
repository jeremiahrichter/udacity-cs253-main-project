from .handler_class import Handler
from models.page_model import Page

def root_url(url):
    return url.replace('_edit/', '')


class EditPageHandler(Handler):
    def render_edit(self, url, user=None, page=None, error=''):
        self.render('edit.html', url='/_edit' + url, user=user,
                    page=page, error=error)

    def get(self, url):
        if self.user:
            self.render_edit(self.url, user=self.user, page=self.page)
        else:
            self.redirect('/login')

    def post(self, url):
        if not self.user:
            self.redirect('/login')
        else:
            base_url = root_url(self.url)
            content = self.request.get('content') or ''

            if self.v:
                Page.update_content(content, base_url, v=self.v)
                self.redirect(base_url + '?v={}'.format(self.v))
            else:
                Page.update_content(content, base_url)
                self.redirect(base_url)
