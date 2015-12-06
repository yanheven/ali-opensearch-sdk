# -*- encoding: utf-8 -*-
from opensearchsdk.apiclient import api_base


class AppManager(api_base.Manager):
    """Application resource manage class"""
    def list(self, page=None, page_size=None):
        """
        get application list with given page and page size.
        :param page:
        :param page_size:
        :return: app list
        """
        body = {}
        if page is not None:
            body['page'] = str(page)
        if page_size is not None:
            body['page_size'] = str(page_size)

        return self.send_get(body)

    def create(self, name, template):
        """
        create a application from a given template.
        :param name: application name
        :param template: template name
        :return:application name
        """
        body = dict(action='create', template=template)
        spec_url = '/' + name

        return self.send_post(body, spec_url)

    def delete(self, name):
        """
        delete a application by name.
        :param name: application name
        :return: status messsage
        """
        body = dict(action='delete')
        spec_url = '/' + name

        return self.send_post(body, spec_url)

    def get(self, name):
        """
        get detail of a application by name.
        :param name: application name
        :return: application detail
        """
        body = dict(action='status')
        spec_url = '/' + name

        return self.send_post(body, spec_url)
