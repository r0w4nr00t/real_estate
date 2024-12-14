# Generated by Django 5.1.3 on 2024-12-04 14:15

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('agent', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('addrress_line1', models.CharField(max_length=255)),
                ('address_line2', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('province', models.CharField(choices=[('HARARE', 'Harare'), ('BULAWAYO', 'Bulawayo'), ('MASHONALAND_EAST', 'Mashonaland East'), ('MATEBELELAND_SOUTH', 'Matebeleland South'), ('MATEBELELAND_NORTH', 'Matebeleland North'), ('MIDLANDS', 'Midlands'), ('MANICALAND', 'Manicaland')], max_length=18)),
                ('zip_code', models.PositiveSmallIntegerField(default=0)),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=12)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=12)),
                ('beds', models.PositiveSmallIntegerField()),
                ('bathrooms', models.PositiveSmallIntegerField()),
                ('square_area', models.DecimalField(decimal_places=2, max_digits=20)),
                ('video', models.URLField()),
                ('primary_image', models.URLField()),
                ('gallery', models.URLField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('category', models.CharField(choices=[('FLAT', 'Flat'), ('TOWNHOUSE', 'Townhouse'), ('HOUSE', 'House'), ('COMMERCIAL_BUILDING', 'Commercial Building'), ('COTTAGE', 'Cottage'), ('STAND', 'Stand')], max_length=19)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agent.agent')),
            ],
            options={
                'verbose_name_plural': 'properties',
                'get_latest_by': 'created_at',
            },
        ),
    ]
