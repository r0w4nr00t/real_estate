from django.db import models
import uuid
from real_estate.apps.agent.models import Agent

# Create your models here.
class Tour(models.Model):
    url = models.URLField(primary_key=True, unique=True)
    monthly_views = models.PositiveIntegerField()
    daily_views = models.PositiveIntegerField()
    total_views = models.PositiveIntegerField()
    pass

class Property(models.Model):
    """ 
    DB schema for the real estate properties
    Properties can be houses, flats/apartments, stands ...
    """
    Categories = models.TextChoices('Categories', 'FLAT TOWNHOUSE HOUSE COMMERCIAL_BUILDING COTTAGE STAND')
    Provinces = models.TextChoices('Provinces', 'HARARE BULAWAYO MASHONALAND_EAST MATEBELELAND_SOUTH MATEBELELAND_NORTH MIDLANDS MANICALAND')
    
    Status = models.TextChoices('Status', 'ACTIVE SOLD INACTIVE PENDING')
    IncomeModel = models.TextChoices('IncomeModel', 'RENTING SELLING') # name of enum to be changed 
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    addrress_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    province = models.CharField(choices=Provinces.choices, max_length=18)
    zip_code = models.PositiveSmallIntegerField(default=0)
    latitude = models.DecimalField(decimal_places=6, max_digits=12, blank=True)
    longitude = models.DecimalField(decimal_places=6, max_digits=12, blank=True)
    beds = models.PositiveSmallIntegerField()
    bathrooms = models.PositiveSmallIntegerField()
    square_area = models.DecimalField(decimal_places=2, max_digits=20) #square area in square metres
    video = models.URLField()
    primary_image = models.URLField()
    gallery = models.URLField()
    price = models.DecimalField(decimal_places=2, max_digits=20) # price of the property in US Dollars
    owner = models.ForeignKey(
        Agent,
        on_delete=models.CASCADE,
    )
    category = models.CharField(choices=Categories.choices, max_length=19)
    status = models.CharField(choices=Status.choices, max_length=8)
    pool = models.BooleanField(default=False)
    garden = models.BooleanField(default=False)
    rent_or_sale = models.CharField(choices=IncomeModel.choices, max_length=7)
    tour = models.ForeignKey(Tour, on_delete=models.SET_NULL)
    
    def __str__(self):
        full_address = self.get_full_address()
        return f"name: {self.name} location:{full_address}, price:{self.price}, beds:{self.beds}, baths:{self.bathrooms}"
    
    def get_full_address(self):
        return f"{self.addrress_line1}, {self.address_line2}, {self.city}"
    
    class Meta:
        verbose_name_plural = "properties"
        get_latest_by = "created_at" #specifies field to use for latest and earliest. 
                                    # A negative signs says in the reverse order of the attribute specified.
        #ordering = ['created_at'] # default ordering when obtaining a list of objects
    