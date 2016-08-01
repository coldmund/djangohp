from django.shortcuts import render
import json
import os

# Create your views here.
def	links(request):
	f = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'links.json'), 'r', encoding='utf-8')
	js = json.loads(f.read())
	f.close()
	sortedList = []
	for it in js:
		key = list(it.keys())[0]
		sortedList.append({key: sorted(list(it[key].items()))})
	return	render(request, 'links/main.html', {'links': sortedList})
