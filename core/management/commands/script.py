from django.core.management.base import BaseCommand
from core.models import Problem
import bs4, requests
import datetime


class Command(BaseCommand):
    help = 'Scrapes spoj.com to obtain the details of all the listed problems on the aforementioned website.'
    def handle(self, *args, **options):
        self.stdout.write('\nScraping started at %s\n' % str(datetime.datetime.now()))
        count = 0
        problem_name = ''
        problem_code = ''
        problem_score = 0.0
        problem_users = 0
        while count != 3650:
            self.stdout.write('\nScraping problem details for problem %d to %d' %(count + 1, count + 50))
            url = "http://www.spoj.com/problems/classical/sort=6,start=" + str(count)
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36', 'cookie':'inweb_city=Kolkata;'}
            res = requests.get(url, headers = headers)
            res.raise_for_status()
            soup = bs4.BeautifulSoup(res.text, "html.parser")
            problem = soup.select("td['align'] > a")
            href_score = soup.select("td.text-center > a['title']")
            for elements_one, elements_two  in zip(problem, href_score):
                problem_name = elements_one.getText()
                problem_code = elements_one["href"].split("/")[-1]
                problem_score = float(elements_two["title"].split(" ")[1])
                problem_users = int(elements_two.getText())
                obj, created = Problem.objects.update_or_create(code=problem_code, defaults={'name':problem_name, 'code':problem_code, 'users':problem_users, 'score':problem_score})
            count += 50
        self.stdout.write('\nScraping ended at %s\n' % str(datetime.datetime.now()))