
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='blog_tags',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='blog_types',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='portfolio_tags',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='portfolio_types',
        ),
        migrations.DeleteModel(
            name='TagProfile',
        ),
        migrations.DeleteModel(
            name='TypeProfile',
        ),
    ]
