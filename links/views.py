from django.shortcuts import render
import json

# Create your views here.
def	links(request):
	f = open('links/links.json', 'r')
	js = json.loads(f.read())
	f.close()
	sortedList = []
	for it in js:
		key = list(it.keys())[0]
		sortedList.append({key: sorted(list(it[key].items()))})
	return	render(request, 'links/main.html', {'links': sortedList})
