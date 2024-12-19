# Generated by Django 5.0.6 on 2024-11-25 14:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coinname', models.CharField(max_length=100)),
                ('abbreviation', models.CharField(max_length=100)),
                ('logo_url', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NewsWebsite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='BitcoinPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usd', models.FloatField()),
                ('twd', models.FloatField()),
                ('eur', models.FloatField()),
                ('timestamp', models.DateTimeField()),
                ('coin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.coin')),
            ],
        ),
        migrations.CreateModel(
            name='CryptoData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_usd', models.DecimalField(decimal_places=2, max_digits=20)),
                ('price_twd', models.DecimalField(decimal_places=2, max_digits=20)),
                ('price_eur', models.DecimalField(decimal_places=2, max_digits=20)),
                ('market_cap', models.DecimalField(decimal_places=2, max_digits=30)),
                ('volume_24h', models.DecimalField(decimal_places=2, max_digits=30)),
                ('change_24h', models.DecimalField(decimal_places=2, max_digits=5)),
                ('fetched_at', models.DateTimeField()),
                ('coin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='crypto_data', to='main.coin')),
            ],
        ),
        migrations.CreateModel(
            name='NewsArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('url', models.URLField()),
                ('image_url', models.URLField(null=True)),
                ('time', models.DateTimeField()),
                ('website', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.newswebsite')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image', models.ImageField(default='profile_images/default.jpg', null=True, upload_to='profile_images/')),
                ('favorite_coin', models.ManyToManyField(blank=True, to='main.coin')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]