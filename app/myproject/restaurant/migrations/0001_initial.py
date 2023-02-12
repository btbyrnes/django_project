# Generated by Django 4.1.6 on 2023-02-12 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('no_of_guests', models.SmallIntegerField(default=1)),
                ('booking_date', models.DateTimeField()),
                ('reservation_date', models.DateField()),
                ('reservation_slot', models.SmallIntegerField(default=10)),
            ],
        ),
    ]
