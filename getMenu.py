import urllib2
from bs4 import BeautifulSoup as bs
import json
class GetMenu():

	def __init__(self):

		self.fobj = open ("burrp_bangalore.txt","r").readlines()
		
	def _indexdata(self,dic):
		
		with open('menu.json', 'a') as fp:
			json.dump(dic,fp)
			fp.write('\n')

	def _getMenu(self,url):
		print url
		dic = {}
		urlobj  = urllib2.urlopen(url).read()
		
		soup = bs(urlobj)
		for i in range(0,50):
			
			food_items = []
			try :
				
				span_main = soup.find("span",{"id":"menu_0_sec_"+str(i)})
				food_category = span_main.getText()
				for j in range(20):
					try:
			
						div_main = soup.find("span",{"id":"menu_0_sec_"+str(i)+"_dish_"+str(j)})	
						div_main = soup.find("span",{"id":"menu_0_sec_"+str(i)+"_dish_"+str(j)})
						
						food_items.append(div_main.getText())
					
					except:
						
						pass

				# dic[span_main.getText()] = li
				dic.update({food_category:food_items})
				# print dic
			except Exception as e:
				pass
		final_dic ={}
		hotel_id = url.split("/")[-1].strip()
		final_dic[hotel_id] = {"menu":dic}
		print final_dic
		self._indexdata(final_dic)

	def generateUrl(self):
		fobj = self.fobj
		for url in fobj:
			self._getMenu(url)

if __name__ == "__main__":

	ob = GetMenu()
	ob.generateUrl()