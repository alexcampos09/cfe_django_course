from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'newsletter.views.home', name='home'),
    url(r'^contact$', 'newsletter.views.contact', name='contact'),
    url(r'^about$', 'trydjango18.views.about', name='about'),
    url(r'^cats$', 'trydjango18.views.cats', name='cats'),
    url(r'^pokemon$', 'trydjango18.views.pokemon', name='pokemon'),
    url(r'^sushi$', 'trydjango18.views.sushi', name='sushi'),
    url(r'^gym$', 'trydjango18.views.gym', name='gym'),
    url(r'^tiktak$', 'trydjango18.views.tiktak', name='tiktak'),
    url(r'^todo$', 'trydjango18.views.todo', name='todo'),
    url(r'^coffee$', 'trydjango18.views.coffee', name='coffee'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
