from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from .models import *
from .serializers import *
from django.conf import settings
from django.core.mail import EmailMessage

class LegislationViewSet(viewsets.ModelViewSet):
    """
    API viewset for Legislation.
    """
    queryset = Legislation.objects.all()
    serializer_class = LegislationSerializer

class DepartmentImageViewSet(viewsets.ModelViewSet):
    """
    API viewset for DepartmentImages.
    """
    queryset = DepartmentImage.objects.all()
    serializer_class = DepartmentImageSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    """
    API viewset for Departments.
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class CoreValueItemViewSet(viewsets.ModelViewSet):
    """
    API viewset for CoreValueItem
    """
    queryset = CoreValueItem.objects.all()
    serializer_class = CoreValueItemSerializer

class CoreValueViewSet(viewsets.ModelViewSet):
    """
    API viewset for CoreValueItem
    """
    queryset = CoreValue.objects.all()
    serializer_class = CoreValueSerializer

# class LegalOpinionViewSet(viewsets.ModelViewSet):
#     """
#     API viewset for LegalOpinions.
#     """
#     queryset = LegalOpinion.objects.all()
#     serializer_class = LegalOpinionSerializer

class PublicationViewSet(viewsets.ModelViewSet):
    """
    API viewset for Publications.
    """
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer

class NewsItemViewSet(viewsets.ModelViewSet):
    """
    API viewset for NewsItems.
    """
    queryset = NewsItem.objects.all()
    serializer_class = NewsItemSerializer

class EventViewSet(viewsets.ModelViewSet):
    """
    API viewset for Events.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class HeaderViewSet(viewsets.ModelViewSet):
    queryset = Header.objects.all()
    serializer_class = HeaderSerializer

class BannerViewSet(viewsets.ModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

class SpeechesAndPresentationsViewSet(viewsets.ModelViewSet):
    queryset = SpeechesAndPresentations.objects.all()
    serializer_class = SpeechesAndPresentationsSerializer

class NewsLetterViewSet(viewsets.ModelViewSet):
    queryset = NewsLetter.objects.all()
    serializer_class = NewsLetterSerializer

# class StatutesViewSet(viewsets.ModelViewSet):
#     queryset = Statutes.objects.all()
#     serializer_class = StatutesSerializer

# class GazetteViewSet(viewsets.ModelViewSet):
#     queryset = Gazette.objects.all()
#     serializer_class = GazetteSerializer

class FeedBackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['id', 'name', 'email', 'date', 'reviewed']
    search_fields = ['id', 'name', 'email', 'date', 'reviewed']
    # parser_classes = [MultiPartParser, FormParser]

    def perform_create(self, serializer):
        instance = serializer.save()
        subject = instance.subject
        message = instance.message
        from_email = instance.email
        to_email = settings.EMAIL_HOST_USER
        reply_to_email = instance.email
        name = instance.name
        email_body = f"Name: {name}\nEmail: {reply_to_email}\n\n{message}"

        email = EmailMessage(
            subject=subject,
            body=email_body,
            from_email=to_email,
            to=[to_email],
            reply_to=[reply_to_email]
        )
        email.send()

        return Response(serializer.data)

class AnnualReportViewSet(viewsets.ModelViewSet):
    queryset = AnnualReport.objects.all()
    serializer_class = AnnualReportSerializer

class MonitoringAndEvaluationsViewSet(viewsets.ModelViewSet):
    queryset = MonitoringAndEvaluations.objects.all()
    serializer_class = MonitoringAndEvaluationsSerializer

class AboutUsViewSet(viewsets.ModelViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer

# class NoticesAndEventsSlideViewSet(viewsets.ModelViewSet):
#     queryset = NoticesAndEventsSlide.objects.all()
#     serializer_class = NoticesAndEventsSlideSerializer

# class NoticesAndEventsViewSet(viewsets.ModelViewSet):
#     queryset = NoticesAndEvents.objects.all()
#     serializer_class = NoticesAndEventsSerializer

class PoliciesViewSet(viewsets.ModelViewSet):
    queryset = Policies.objects.all()
    serializer_class = PoliciesSerializer

class StandardOperationProceduresViewSet(viewsets.ModelViewSet):
    queryset = StandardOperationProcedures.objects.all()
    serializer_class = StandardOperationProceduresSerializer

class FormsAndDocumentsViewSet(viewsets.ModelViewSet):
    queryset = FormsAndDocuments.objects.all()
    serializer_class = FormsAndDocumentsSerializer

# class PrcaticeDirectionsViewSet(viewsets.ModelViewSet):
#     queryset = PrcaticeDirections.objects.all()
#     serializer_class = PrcaticeDirectionsSerializer

# class GovernmentGazettesViewSet(viewsets.ModelViewSet):
#     queryset = GovernmentGazettes.objects.all()
#     serializer_class = GovernmentGazettesSerializer

class TendersViewSet(viewsets.ModelViewSet):
    queryset = Tenders.objects.all()
    serializer_class = TendersSerializer

# class RegulationsViewSet(viewsets.ModelViewSet):
#     queryset = Regulations.objects.all()
#     serializer_class = RegulationsSerializer

class AlbumsViewSet(viewsets.ModelViewSet):
    queryset = Albums.objects.all()
    serializer_class = AlbumsSerializer

class AlbumPicturesViewSet(viewsets.ModelViewSet):
    queryset = AlbumPictures.objects.all()
    serializer_class = AlbumPicturesSerializer

class VideosViewSet(viewsets.ModelViewSet):
    queryset = Videos.objects.all()
    serializer_class = VideosSerializer

class OverviewViewSet(viewsets.ModelViewSet):
    queryset = Overview.objects.all()
    serializer_class = OverviewSerializer

class SecretariateStructureViewSet(viewsets.ModelViewSet):
    queryset = SecretariateStructure.objects.all()
    serializer_class = SecretariateStructureSerializer

class DocumentsViewSet(viewsets.ModelViewSet):
    queryset = Documents.objects.all()
    serializer_class = DocumentsSerializer