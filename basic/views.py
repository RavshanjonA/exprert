from django.views.generic import TemplateView


class Home(TemplateView):
	template_name = 'home.html'


class About(TemplateView):
	template_name = 'about.html'


class Help(TemplateView):
	template_name = 'help.html'


class Blog(TemplateView):
	template_name = 'blog.html'


