# Generated by Django 3.1 on 2020-10-02 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='portfolio_Site',
            new_name='portfolio_site',
        ),
    ]
