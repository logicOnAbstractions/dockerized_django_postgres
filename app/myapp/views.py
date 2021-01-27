from django.shortcuts import render
from django.views import generic


class IndexView(generic.View):
    template_name = 'myapp/index.html'
    context_object_name = 'dummy'			# not used here, but we can pass a context object as well

    def get(self, request):
        return render(request, self.template_name)