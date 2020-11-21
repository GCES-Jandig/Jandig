# Generated by Django 2.2.10 on 2020-11-21 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Artwork2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('patt', models.CharField(default='hiro', max_length=50)),
                ('gif', models.CharField(default='peixe', max_length=50)),
                ('scale', models.CharField(default='1 1', max_length=50)),
                ('position', models.CharField(default='0 0 0', max_length=50)),
                ('rotation', models.CharField(default='270 0 0', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.FileField(upload_to='objects/')),
                ('uploaded_at', models.DateTimeField(auto_now=True)),
                ('author', models.CharField(max_length=60)),
                ('title', models.CharField(default='', max_length=60)),
                ('scale', models.CharField(default='1 1', max_length=50)),
                ('position', models.CharField(default='0 0 0', max_length=50)),
                ('rotation', models.CharField(default='270 0 0', max_length=50)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='objects', to='users.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Marker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.ImageField(upload_to='markers/')),
                ('uploaded_at', models.DateTimeField(auto_now=True)),
                ('author', models.CharField(max_length=60)),
                ('title', models.CharField(default='', max_length=60)),
                ('patt', models.FileField(upload_to='patts/')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Exhibit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.CharField(max_length=50, unique=True)),
                ('creation_date', models.DateTimeField(auto_now=True)),
                ('artworks', models.ManyToManyField(related_name='exhibits', to='core.Artwork')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='exhibits', to='users.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='artwork',
            name='augmented',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Object'),
        ),
        migrations.AddField(
            model_name='artwork',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.Profile'),
        ),
        migrations.AddField(
            model_name='artwork',
            name='marker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Marker'),
        ),
    ]
