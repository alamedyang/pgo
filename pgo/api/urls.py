from django.urls import path

from pgo.api.routers import pgo_router
from pgo.api.views import BreakpointCalcAPIView, GoodToGoAPIView


pgo_api_urls = pgo_router.urls
pgo_api_urls.extend((
    path('breakpoint-calc/', BreakpointCalcAPIView.as_view(), name='breakpoint-calc'),
    path('good-to-go/', GoodToGoAPIView.as_view(), name='good-to-go'),
))
