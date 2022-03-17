import multiprocessing
from bs4 import BeautifulSoup
from queue import Queue, Empty
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin, urlparse
import requests
class MultiThreadCrawler:
	def __init__(self, seed_url):
		self.seed_url = seed_url
		self.root_url = '{}://{}'.format(urlparse(self.seed_url).scheme,urlparse(self.seed_url).netloc)
		self.pool= ThreadPoolExecutor(max_workers=5)
		self.scraped_pages=set([])
		self.crawl_queue=Queue()
		self.crawl_queue.put(self.seed_url)

	def run_web_crawler(self):
		while True:
			try:
				print("\n Name of the current executing process:",multiprocessing.current_process().name, '\n')
				target_url=self.crawl_queue.get(timeout=60)
				if target_url not in self.scraped_pages:
					print("Scraping URL: {}".format(target_url))
					self.scraped_pages.add(target_url)
					job=self.pool.submit(self.scrape_page, target_url)
					job.add_done_callback(self.post_scape_callback)
			except Empty:
				return
			except Exception as e:
				print(e)
				continue

if __name__ == '__main__':
	cc = MultiThreadCrawler("https://www.geeksforgeeks.org/")
	cc.run_web_crawler()
	cc.info()