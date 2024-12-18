from django.urls import path

from api.views.contacts_information.contact_information_detail_views import ContactInformationDetailViews
from api.views.contacts_information.contact_information_list_views import ContactInformationListViews
from api.views.dashboard.lead_created_day_view import LeadCreatedDayView
from api.views.dashboard.total_cost_services_view import TotalCostServicesView
from api.views.dashboard.vehicle_cost_per_lead_view import VehicleCostPerLeadView
from api.views.leads.lead_list_views import LeadListViews
from api.views.leads.lead_detail_views import LeadDetailViews
from api.views.mechanics.count_mechanics_view import CountMechanicsView
from api.views.mechanics.list_vehicles_mechanic_view import ListVehiclesMechanicView
from api.views.mechanics.mechanic_detail_views import MechanicDetailViews
from api.views.mechanics.mechanic_list_views import MechanicListViews
from api.views.services.service_detail_views import ServiceDetailViews
from api.views.services.service_list_views import ServiceListViews
from api.views.services.service_top_five_view import ServiceTopFiveView
from api.views.vehicles.vehicle_detail_views import VehicleDetailViews
from api.views.vehicles.vehicle_list_views import VehicleListViews
from api.views.vehicles.vehicle_services_cost_view import VehicleServicesCostView

urlpatterns = [
    # leads
    path('leads', LeadListViews.as_view()),
    path('leads/<int:lead>', LeadDetailViews.as_view()),

    # vehicles
    path('vehicles', VehicleListViews.as_view()),
    path('vehicles/<int:vehicle>', VehicleDetailViews.as_view()),
    path('vehicles/<int:vehicle>/services-cost', VehicleServicesCostView.as_view()),

    # services
    path('services', ServiceListViews.as_view()),
    path('services/<int:service>', ServiceDetailViews.as_view()),
    path('services/top-services', ServiceTopFiveView.as_view()),

    # mechanics
    path('mechanics', MechanicListViews.as_view()),
    path('mechanics/<int:mechanic>', MechanicDetailViews.as_view()),
    path('mechanics/count-mechanics', CountMechanicsView.as_view()),
    path('mechanics/<int:mechanic>/vehicles', ListVehiclesMechanicView.as_view()),

    # contact information
    path('contacts-information', ContactInformationListViews.as_view()),
    path('contacts-information/<int:contact_info>', ContactInformationDetailViews.as_view()),

    # dashboard
    path('dashboard/total-services-cost', TotalCostServicesView.as_view()),
    path('dashboard/leads-created-per-day', LeadCreatedDayView.as_view()),
    path('dashboard/vehicles-cost-lead/<int:lead>', VehicleCostPerLeadView.as_view())
]
