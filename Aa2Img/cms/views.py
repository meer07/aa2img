from django.shortcuts import render_to_response
from django.template import RequestContext
from aa2img import aa2img

# Create your views here.
def index(request):
    return render_to_response('index.html', {}, context_instance=RequestContext(request))

def change(request):
    if request.method == "POST":
        texts = request.POST["texts"]
        temp = unicode(texts).split('\n')
        print temp[0]
        #paser = aa2img()
        #paser.outputimg()
        #return render_to_response('index.html', {}, context_instance=RequestContext(request))