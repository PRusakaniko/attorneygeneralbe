from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'legislation', views.LegislationViewSet)
router.register(r'departments', views.DepartmentViewSet)
router.register(r'department-images', views.DepartmentImageViewSet)
router.register(r'core-value-items', views.CoreValueItemViewSet)
router.register(r'core-value', views.CoreValueViewSet)
# router.register(r'legal-opinions', views.LegalOpinionViewSet)
router.register(r'publications', views.PublicationViewSet)
router.register(r'news', views.NewsItemViewSet)
router.register(r'events', views.EventViewSet)
router.register(r'headers', views.HeaderViewSet)
router.register(r'banners', views.BannerViewSet)
router.register(r'speeches-and-presentations', views.SpeechesAndPresentationsViewSet)
router.register(r'newsletters', views.NewsLetterViewSet)
# router.register(r'statutes', views.StatutesViewSet)
# router.register(r'gazettes', views.GazetteViewSet)
router.register(r'feedback', views.FeedBackViewSet)
router.register(r'annual-reports', views.AnnualReportViewSet)
router.register(r'monitoring-and-evaluations', views.MonitoringAndEvaluationsViewSet)
router.register(r'about-us', views.AboutUsViewSet)
# router.register(r'notices-and-events-slides', views.NoticesAndEventsSlideViewSet)
# router.register(r'notices-and-events', views.NoticesAndEventsViewSet)
router.register(r'policies', views.PoliciesViewSet)
router.register(r'standard-operation-procedures', views.StandardOperationProceduresViewSet)
router.register(r'forms-and-documents', views.FormsAndDocumentsViewSet)
# router.register(r'practice-directions', views.PrcaticeDirectionsViewSet)
# router.register(r'government-gazettes', views.GovernmentGazettesViewSet)
router.register(r'tenders', views.TendersViewSet)
# router.register(r'regulations', views.RegulationsViewSet)
router.register(r'albums', views.AlbumsViewSet)
router.register(r'album-pictures', views.AlbumPicturesViewSet)
router.register(r'videos', views.VideosViewSet)
router.register(r'overviews', views.OverviewViewSet)  # Use 'overviews' to avoid conflict
router.register(r'secretariate-structure', views.SecretariateStructureViewSet)
router.register(r'documents', views.DocumentsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]