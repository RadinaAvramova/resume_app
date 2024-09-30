
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20211013_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='testimonials'),
        ),
    ]
