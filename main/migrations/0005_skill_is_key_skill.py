
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_testimonial_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='is_key_skill',
            field=models.BooleanField(default=False),
        ),
    ]
