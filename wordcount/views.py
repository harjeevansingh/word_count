# from django.http import HttpResponse


from django.shortcuts import render
import operator


def homepage(request):
	return render(request, 'home.html')

	
def count(request):
	word_dict = {}
	fulltext = request.GET['fulltext']   # 'all_words': all_words
	all_words = fulltext.split()
	for word in all_words:
		if word in word_dict:
			word_dict[word] += 1
		else:
			word_dict[word] = 1
	sorted_dict = sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True)
	return render(request, 'count.html', {'fulltext': fulltext, 'count': len(all_words), 'sorted_dict': sorted_dict})


def about(request):
	return render(request, 'about.html')
