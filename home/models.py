from django.db import models
from django.db.models import Index
from tinymce.models import HTMLField

def upload_to(instance, filename):
    return 'uploads/{filename}'.format(filename=filename)

secretariate_hierarchy = {
    'S1': 'Secretariate 1',
    'S2': 'Secretariate 2',
    'S3': 'Secretariate 3',
    'S4': 'Secretariate 4',
    'S5': 'Secretariate 5',
    'S6': 'Secretariate 6',
    'S7': 'Secretariate 7',
    'S8': 'Secretariate 8',
    'S9': 'Secretariate 9',
    'S10': 'Secretariate 10',
    'S11': 'Secretariate 11',
    'S12': 'Secretariate 12',
    'S13': 'Secretariate 13',
    'S14': 'Secretariate 14',
    'S15': 'Secretariate 15',
}

class Legislation(models.Model):
  """
  Model to store information about legislation.
  """
  title = models.CharField(max_length=255)
  bill_number = models.CharField(max_length=50, unique=True)
  summary = models.TextField()
  status = models.CharField(max_length=50, choices=[
    ('Department', 'Department Progress'),
    ('Ministry', 'Ministry Clarification'),
    ('Drafting', 'Drafting'),
    ('Dispatched', 'Dispacthed to Ministries'),
    ('Cabinet', 'Cabinet/CCL'),    
    ('SubmittedToParliament', 'Submitted to Parliament')    
  ])
  received_date = models.DateField(null=True, blank=True)
  dispatched_date = models.DateField(null=True, blank=True)
  cabinet_date = models.DateField(null=True, blank=True)  
  pres_to_parl_date = models.DateField(null=True, blank=True)  
  department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True, blank=True)
  leg_file = models.FileField(upload_to=upload_to, null=True, blank=True)
  leg_image = models.ImageField(upload_to=upload_to, null=True, blank=True)

  def __str__(self):
    return f"{self.bill_number} - {self.title}"
  
  class Meta:
    indexes = [
        Index(fields=['bill_number']),  # Index frequently queried fields
        Index(fields=['status']),
    ]

class CoreValueItem(models.Model):
    item = models.CharField(max_length=255)

    def __str__(self):
        return self.item
    
    class Meta:
        verbose_name = "core value item"
        verbose_name_plural = "core value items"

class CoreValue(models.Model):
    title = models.CharField(max_length=255)
    items = models.ManyToManyField(CoreValueItem, blank=True)

    def __str__(self):
        return self.title
    

class DepartmentImage(models.Model):
  department_image = models.ImageField(upload_to='course_images/')

class Department(models.Model):
  """
  Model to store information about departments within the AG's office.
  """
  name = models.CharField(max_length=255)
  description = models.TextField(null=True, blank=True)
  contact_email = models.EmailField(null=True, blank=True)
  contact_phone = models.CharField(max_length=20, null=True, blank=True)
  department_images = models.ManyToManyField(DepartmentImage, blank=True)

  def __str__(self):
    return self.name


# class LegalOpinion(models.Model):
#   """
#   Model to store legal opinions issued by the AG's office.
#   """
#   title = models.CharField(max_length=255)
#   date_issued = models.DateField()
#   summary = models.TextField()
#   document = models.FileField(upload_to=upload_to)  # Or URLField
#   department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)


#   def __str__(self):
#     return f"{self.title} ({self.date_issued})"


class Publication(models.Model):
  """
  Model to store publications by the AG's office.
  """
  title = models.CharField(max_length=255)
  date_published = models.DateField(null=True, blank=True)
  summary = models.TextField(null=True, blank=True)
  document = models.FileField(upload_to='publications/')  # Or URLField
  department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
  category = models.CharField(max_length=255, choices=[
    ('Legislation', 'Legislation'),
    ('Legal Opinions', 'Legal Opinions'),
    ('Publications', 'Publications'),
    ('Other', 'Other'),
  ], default='Other', blank=True)

  def __str__(self):
    return f"{self.title} ({self.date_published})"


class NewsItem(models.Model):
  """
  Model for news items and announcements.
  """
  title = models.CharField(max_length=255)
  date_published = models.DateTimeField(auto_now_add=True)
  content = HTMLField()
  news_image = models.ImageField(upload_to=upload_to, null=True, blank=True)
  is_featured = models.BooleanField(default=False)

  def __str__(self):
    return f"{self.title} ({self.date_published})"


class Event(models.Model):
  """
  Model for upcoming events.
  """
  title = models.CharField(max_length=255)
  date = models.DateTimeField()
  location = models.CharField(max_length=255)
  description = models.TextField()
  event_image = models.ImageField(upload_to=upload_to, null=True, blank=True)

  def __str__(self):
    return f"{self.title} ({self.date})"





class Header(models.Model):
    ag_email = models.EmailField()
    ag_phone = models.CharField(max_length=20)
    ag_call_center = models.CharField(max_length=20)
    def __str__(self):
        return self.ag_email

    class Meta:
        verbose_name = "header"
        verbose_name_plural = "headers"

class Banner(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to=upload_to)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'banner'
        verbose_name_plural = 'banners'

class SpeechesAndPresentations(models.Model):
    topic = models.CharField(max_length=350)
    speaker = models.CharField(max_length=150)
    speech_and_presentation_document = models.FileField(upload_to=upload_to)

    def __str__(self):
        return self.topic
    
    class Meta:
        verbose_name = "speech and presentation"
        verbose_name_plural = "speeches and presentations"
    

class NewsLetter(models.Model):
    title = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to=upload_to)
    newsletter_document = models.FileField(upload_to=upload_to)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "newsLetter"
        verbose_name_plural = "newsLetters"

# class Statutes(models.Model):
#     title = models.CharField(max_length=250)
#     file_year = models.DateField()
#     statute_file = models.FileField(upload_to=upload_to)

#     def __str__(self):
#         return self.title
    
#     class Meta:
#         verbose_name = "statute"
#         verbose_name_plural = "statutes"

# class Gazette(models.Model):
#     title = models.CharField(max_length=250)
#     gazette_file = models.FileField(upload_to=upload_to)

#     def __str__(self):
#         return self.title
    
#     class Meta:
#         verbose_name = "gazette"
#         verbose_name_plural = "gazettes"

class Feedback(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    subject = models.CharField(max_length=100, null=True, blank=True)
    message = models.TextField()
    date = models.DateField(auto_now_add=True)
    reviewed = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.name} sent on {self.date}"

    class Meta:
        verbose_name = "feedback"
        verbose_name_plural = "feedbacks"

class AnnualReport(models.Model):
    title = models.CharField(max_length=250)
    cover_image = models.ImageField(upload_to=upload_to)
    annual_report_document = models.FileField(upload_to=upload_to)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "annual report"
        verbose_name_plural = "annual reports"

class MonitoringAndEvaluations(models.Model):
    title = models.CharField(max_length=250)
    monitoring_and_evaluation_document = models.FileField(upload_to=upload_to)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "monitoring and evaluation"
        verbose_name_plural = "monitoring and evaluations"

class AboutUs(models.Model):
    vision = models.TextField()
    mission = models.TextField()
    theme_title = models.CharField(max_length=100)
    theme_description = models.TextField()
    theme_document = models.FileField(upload_to=upload_to)
    strategic_plan_title = models.CharField(max_length=100)
    strategic_plan_document = models.FileField(upload_to=upload_to)

    def __str__(self):
        return self.theme_title
    
    class Meta:
        verbose_name = "about us"
        verbose_name_plural = "about us"

# class NoticesAndEventsSlide(models.Model):
#     title = models.CharField(max_length=250)
#     slide_image = models.ImageField(upload_to=upload_to)

#     def __str__(self):
#         return self.title
    
#     class Meta:
#         verbose_name = "notice and event slide"
#         verbose_name_plural = "notice and event slides"

# class NoticesAndEvents(models.Model):
#     title = models.CharField(max_length=250)
#     notices_and_events = models.FileField(upload_to=upload_to)

#     def __str__(self):
#         return self.title
    
#     class Meta:
#         verbose_name = "notice and event"
#         verbose_name_plural = "notices and events"

class Policies(models.Model):
    title = models.CharField(max_length=250)
    edition = models.CharField(max_length=100)
    policies_document = models.FileField(upload_to=upload_to)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "policy"
        verbose_name_plural = "policies"

class StandardOperationProcedures(models.Model):
    title = models.CharField(max_length=250)
    edition = models.CharField(max_length=100)
    standard_operation_procedure_document = models.FileField(upload_to=upload_to)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "standard operation procedure"
        verbose_name_plural = "standard operation procedures"

class FormsAndDocuments(models.Model):
    topic = models.CharField(max_length=250)
    author = models.CharField(max_length=150)
    publication_date = models.DateField()
    form_and_document_file = models.FileField(upload_to=upload_to)

    def __str__(self):
        return self.topic
    
    class Meta:
        verbose_name = "form and document"
        verbose_name_plural = "forms and documents"

# class PrcaticeDirections(models.Model):
#     title = models.CharField(max_length=250)
#     practice_directions_document = models.FileField(upload_to=upload_to)

#     def __str__(self):
#         return self.title
    
#     class Meta:
#         verbose_name = "practice direction"
#         verbose_name_plural = "practice directions"

# class GovernmentGazettes(models.Model):
#     title = models.CharField(max_length=250)
#     gazette_file = models.FileField(upload_to=upload_to)

#     def __str__(self):
#         return self.title
    
#     class Meta:
#         verbose_name = "government gazette"
#         verbose_name_plural = "government gazettes"

class Tenders(models.Model):
    tender_date = models.DateField()
    title = models.CharField(max_length=250)
    owner = models.CharField(max_length=150)
    tender_file = models.FileField(upload_to=upload_to)

    
    def __str__(self):
        return f"{self.title} ({self.tender_date})"
    
    class Meta:
        verbose_name = "tender"
        verbose_name_plural = "tenders"

# class Regulations(models.Model):
#     title = models.CharField(max_length=250)
#     edition = models.CharField(max_length=100)
#     regulations_document = models.FileField(upload_to=upload_to)

#     def __str__(self):
#         return self.title
    
#     class Meta:
#         verbose_name = "regulation"
#         verbose_name_plural = "regulations"

class Albums(models.Model):
    album_name = models.CharField(max_length=100)

    def __str__(self):
        return self.album_name
    
    class Meta:
        verbose_name = "album"
        verbose_name_plural = "albums"

class AlbumPictures(models.Model):
    album = models.ForeignKey(Albums, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to=upload_to)

    def __str__(self):
        return self.album.album_name
    
    class Meta:
        verbose_name = "album picture"
        verbose_name_plural = "album pictures"

class Videos(models.Model):
    video_name = models.CharField(max_length=100)
    video_link = models.URLField()

    def __str__(self):
        return self.video_name

    class Meta:
        verbose_name = "video"
        verbose_name_plural = "videos"

class Overview(models.Model):
    overview = models.TextField()

    def __str__(self):
        return self.overview
    
    class Meta:
        verbose_name = "overview"
        verbose_name_plural = "overview"

class SecretariateStructure(models.Model):
    hierarchy = models.CharField(max_length=100, choices=secretariate_hierarchy.items())
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to=upload_to)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "attorney general structure"
        verbose_name_plural = "attorney general structure"

class Documents(models.Model):
    title = models.CharField(max_length=250)
    DOCUMENT_TYPE = (
        ('charter', 'Charter'),
        ('constitution', 'Constitution'),
        ('strategicplan', 'StrategicPlan'),
        ('regulations', 'Regulations'),
        ('tenders', 'Tenders'),
    )
    document_type = models.CharField(max_length=100, choices=DOCUMENT_TYPE)
    edition = models.CharField(max_length=100, null=True, blank=True)
    tender_date = models.DateField()
    owner = models.CharField(max_length=250, default="AG")
    document_file = models.FileField(upload_to=upload_to)
        
    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "document"
        verbose_name_plural = "documents"