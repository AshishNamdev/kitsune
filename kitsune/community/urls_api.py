from django.conf.urls import patterns, url

from kitsune.community import api


urlpatterns = patterns(
    '',
    url('^topcontributors/questions/$', api.TopContributorsQuestions.as_view()),
    url('^topcontributors/l10n/$', api.TopContributorsLocalization.as_view()),
)
