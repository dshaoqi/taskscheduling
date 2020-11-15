from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('hosts/',views.HostListView.as_view(),name='hosts'),
    path('records/',views.RecordListView.as_view(),name='records'),
    path('steps/',views.StepView,name='steps'),
    path('steps/stepresult',views.StepResultView,name='stepresult'),
    path('flows/',views.FlowView,name='flows'),
    path('flows/flowcommit',views.FlowCommitView,name='flowcommit'),
    path('hosts/<int:host_id>',views.HostDetailView,name='hostdetail'),
    path('flows/<int:flow_id>',views.FlowDetailView,name='flowdetail'),
    
]
