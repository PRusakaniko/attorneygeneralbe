from rest_framework import serializers
from .models import *

class LegislationSerializer(serializers.ModelSerializer):
  """
  Serializer for the Legislation model.
  """
  class Meta:
    model = Legislation
    fields = '__all__'  # Or specify the fields explicitly


class DepartmentImageSerializer(serializers.ModelSerializer):
  """
  Serializer for the DepartmentImage model.
  """
  class Meta:
    model = DepartmentImage
    fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
  department_images = DepartmentImageSerializer(many=True, read_only=True)
  """
  Serializer for the Department model.
  """
  class Meta:
    model = Department
    fields = '__all__'

class CoreValueItemSerializer(serializers.ModelSerializer):
   class Meta:
      model = CoreValueItem
      fields = '__all__'

class CoreValueSerializer(serializers.ModelSerializer):
   items = CoreValueItemSerializer(many=True, read_only=True)
   class Meta:
      model = CoreValue
      fields = '__all__'

# class LegalOpinionSerializer(serializers.ModelSerializer):
#   """
#   Serializer for the LegalOpinion model.
#   """
#   class Meta:
#     model = LegalOpinion
#     fields = '__all__'


class PublicationSerializer(serializers.ModelSerializer):
  department = serializers.SlugRelatedField(slug_field='name', read_only=True)
  """
  Serializer for the Publication model.
  """
  class Meta:
    model = Publication
    fields = '__all__'


class NewsItemSerializer(serializers.ModelSerializer):
  """
  Serializer for the NewsItem model.
  """
  class Meta:
    model = NewsItem
    fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
  """
  Serializer for the Event model.
  """
  class Meta:
    model = Event
    fields = '__all__'


class HeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Header
        fields = '__all__'

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'

class SpeechesAndPresentationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpeechesAndPresentations
        fields = '__all__'

class NewsLetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsLetter
        fields = '__all__'

# class StatutesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Statutes
#         fields = '__all__'

# class GazetteSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Gazette
#         fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'

class AnnualReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnnualReport
        fields = '__all__'

class MonitoringAndEvaluationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonitoringAndEvaluations
        fields = '__all__'

class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'

# class NoticesAndEventsSlideSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = NoticesAndEventsSlide
#         fields = '__all__'

# class NoticesAndEventsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = NoticesAndEvents
#         fields = '__all__'

class PoliciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Policies
        fields = '__all__'

class StandardOperationProceduresSerializer(serializers.ModelSerializer):
    class Meta:
        model = StandardOperationProcedures
        fields = '__all__'

class FormsAndDocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormsAndDocuments
        fields = '__all__'

# class PrcaticeDirectionsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PrcaticeDirections
#         fields = '__all__'

# class GovernmentGazettesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = GovernmentGazettes
#         fields = '__all__'

class TendersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenders
        fields = '__all__'

# class RegulationsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Regulations
#         fields = '__all__'

class AlbumsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Albums
        fields = '__all__'

class AlbumPicturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumPictures
        fields = '__all__'

class VideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videos
        fields = '__all__'

class OverviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Overview
        fields = '__all__'

class SecretariateStructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecretariateStructure
        fields = '__all__'
        
class DocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documents
        fields = '__all__'