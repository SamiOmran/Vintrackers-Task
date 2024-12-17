from django.urls import path

from api.views.leads.lead_list_views import LeadListViews
from api.views.leads.lead_detail_views import LeadDetailViews
from api.views.services.service_detail_views import ServiceDetailViews
from api.views.services.service_list_views import ServiceListViews
from api.views.services.service_top_five_view import ServiceTopFiveView
from api.views.vehicles.vehicle_detail_views import VehicleDetailViews
from api.views.vehicles.vehicle_list_views import VehicleListViews
from api.views.vehicles.vehicle_services_cost_view import VehicleServicesCostView

urlpatterns = [
    path('leads/', LeadListViews.as_view()),
    path('leads/<int:lead>', LeadDetailViews.as_view()),

    path('vehicles/', VehicleListViews.as_view()),
    path('vehicles/<int:vehicle>', VehicleDetailViews.as_view()),
    path('vehicles/<int:vehicle>/services-cost', VehicleServicesCostView.as_view()),

    path('services/', ServiceListViews.as_view()),
    path('services/<int:service>', ServiceDetailViews.as_view()),
    path('services/top-services', ServiceTopFiveView.as_view())
]
