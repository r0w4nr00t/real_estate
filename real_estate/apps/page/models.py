from django.db import models
from django.contrib.postgres.fields import ArrayField
from real_estate.apps.agent.models import Agent
import uuid, datetime
from .exceptions import PublishError
from .validators import validate_color
from django.conf import settings
from django.core.exceptions import ValidationError


# Create your models here.
class Page(models.Model):
    Status = models.TextChoices('Status', 'ACTIVE INACTIVE PENDING')
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    agent = models.ForeignKey(
        Agent,
        on_delete=models.CASCADE,
    )
    logo = models.ImageField()
    color = ArrayField(models.IntegerField(), size=3)
    description = models.CharField(max_length=1000)
    cover_photo = models.ImageField(blank=True)
    status = models.CharField(choices=Status.choices, max_length=8)
    is_public = models.BooleanField(default=False)
    monthly_views = models.PositiveIntegerField()
    daily_views = models.PositiveIntegerField()
    total_views = models.PositiveIntegerField()

    class Meta:
        get_latest_by = 'created_at'
        pass
    
    def publish(self):
        if self.status == 'ACTIVE':
            self.is_public = True
        raise PublishError
    
    def set_color(self, r=None, g=None, b=None):
        if not r and g and b:
            r,g,b = settings.DFAULT_PAGE_COLOR # get the default page colors
            self.color = [r,g,b]
            return
        if not validate_color(r,g,b):
           raise ValidationError("Invalid rgb values")
        self.color = [r,g,b]
        pass
    def share_page(self, email):
        ...
    def get_page_url(self):
        return f"pages/{self.id}"
    
    def get_views(self):
        return self.total_views, self.monthly_views, self.daily_views
    
    def add_view(self):
        """ 
        Whenever this page is requested the number of views if increament by 1 accordingly
        """
        now = datetime.date.today()
        if self.updated_at.day == now.day:
            self.daily_views = self.daily_views + 1
        self.daily_views = 1
        
        if self.updated_at.month == now.month:
            self.monthly_views = self.monthly_views + 1 
        self.monthly_views = 1
        
        self.total_views = self.total_views + 1
