# Generated by Django 3.0.2 on 2020-03-17 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shopping', '0007_faculty'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(default='', max_length=70)),
                ('phone', models.CharField(default='', max_length=70)),
                ('desc', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='Faculty',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
