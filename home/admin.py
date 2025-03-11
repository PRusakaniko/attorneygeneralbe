from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from .models import *

# Define admin classes for each model
class LegislationAdmin(ImportExportActionModelAdmin):
    pass

class DepartImageAdmin(ImportExportActionModelAdmin):
    list_display = ('id',)

class DepartmentAdmin(ImportExportActionModelAdmin):
    pass

class CoreValueItemAdmin(ImportExportActionModelAdmin):
    pass

class CoreValueAdmin(ImportExportActionModelAdmin):
    pass

class PublicationAdmin(ImportExportActionModelAdmin):
    pass

class NewsItemAdmin(ImportExportActionModelAdmin):
    pass

class EventAdmin(ImportExportActionModelAdmin):
    pass

class HeaderAdmin(ImportExportActionModelAdmin):
    pass

class BannerAdmin(ImportExportActionModelAdmin):
    pass

class SpeechesAndPresentationsAdmin(ImportExportActionModelAdmin):
    pass

class NewsLetterAdmin(ImportExportActionModelAdmin):
    pass

class FeedbackAdmin(ImportExportActionModelAdmin):
    pass

class AnnualReportAdmin(ImportExportActionModelAdmin):
    pass

class MonitoringAndEvaluationsAdmin(ImportExportActionModelAdmin):
    pass

class AboutUsAdmin(ImportExportActionModelAdmin):
    pass

class PoliciesAdmin(ImportExportActionModelAdmin):
    pass

class StandardOperationProceduresAdmin(ImportExportActionModelAdmin):
    pass

class FormsAndDocumentsAdmin(ImportExportActionModelAdmin):
    pass

class AlbumsAdmin(ImportExportActionModelAdmin):
    pass

class AlbumPicturesAdmin(ImportExportActionModelAdmin):
    pass

class VideosAdmin(ImportExportActionModelAdmin):
    pass

class OverviewAdmin(ImportExportActionModelAdmin):
    pass

class SecretariateStructureAdmin(ImportExportActionModelAdmin):
    pass

class DocumentsAdmin(ImportExportActionModelAdmin):
    pass

# Register the models with their respective admin classes
admin.site.register(Legislation, LegislationAdmin)
admin.site.register(DepartmentImage, DepartImageAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(CoreValueItem, CoreValueItemAdmin)
admin.site.register(CoreValue, CoreValueAdmin)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(NewsItem, NewsItemAdmin)
# admin.site.register(Event, EventAdmin)
admin.site.register(Header, HeaderAdmin)
admin.site.register(Banner, BannerAdmin)
admin.site.register(SpeechesAndPresentations, SpeechesAndPresentationsAdmin)
admin.site.register(NewsLetter, NewsLetterAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(AnnualReport, AnnualReportAdmin)
# admin.site.register(MonitoringAndEvaluations, MonitoringAndEvaluationsAdmin)
admin.site.register(AboutUs, AboutUsAdmin)
# admin.site.register(Policies, PoliciesAdmin)
# admin.site.register(StandardOperationProcedures, StandardOperationProceduresAdmin)
# admin.site.register(FormsAndDocuments, FormsAndDocumentsAdmin)
admin.site.register(Albums, AlbumsAdmin)
admin.site.register(AlbumPictures, AlbumPicturesAdmin)
admin.site.register(Videos, VideosAdmin)
admin.site.register(Overview, OverviewAdmin)
admin.site.register(SecretariateStructure, SecretariateStructureAdmin)
admin.site.register(Documents, DocumentsAdmin)
