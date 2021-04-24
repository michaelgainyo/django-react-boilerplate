import os

from bs4 import BeautifulSoup
from django.conf import settings
from django.core.management.base import BaseCommand

index_path = os.path.join(settings.BUILD_DIR, 'index.html')
output_path = os.path.join(settings.TEMPLATES_DIR, 'base-react.html')


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        exists = os.path.exists(index_path)
        if not exists:
            # print or raise error
            return

        html = open(index_path).read()
        soup = BeautifulSoup(html, 'html.parser')

        soup.title.replace_with("{% block head %}{% endblock head %}")

        root = soup.find("div", id="root")
        root.insert_before("{% block body %}")
        root.insert_after("{% endblock body %}")

        style = soup.new_tag('style', type="text/css")
        style.string = "{% block css %}{% endblock css %}"

        soup.head.insert(len(soup.head.contents), style)

        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(str(soup))

        self.stdout.write(
            self.style.SUCCESS(f'Exported file: {output_path}')
        )
