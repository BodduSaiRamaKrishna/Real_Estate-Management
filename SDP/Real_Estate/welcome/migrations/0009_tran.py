# Generated by Django 3.2.3 on 2021-05-18 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0008_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tran',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('add', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('zip', models.CharField(max_length=10)),
                ('card', models.CharField(max_length=30)),
                ('cname', models.CharField(max_length=30)),
                ('cnum', models.CharField(max_length=12)),
                ('expmonth', models.CharField(max_length=2)),
                ('expyear', models.CharField(max_length=4)),
                ('cvv', models.CharField(max_length=3)),
            ],
        ),
    ]
