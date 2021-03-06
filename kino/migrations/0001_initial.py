# Generated by Django 3.1.5 on 2021-03-05 14:08

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.fields.related
import django.utils.timezone
import kino.models.cinema
import kino.models.film
import kino.models.news
import kino.models.shares
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ADS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='images/ads')),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='BackBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='banners/back')),
            ],
        ),
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('description', models.TextField(blank=True, max_length=1000)),
                ('conditions', models.TextField(blank=True, max_length=1000)),
                ('logo', models.ImageField(blank=True, upload_to=kino.models.cinema.upload_cinema_logo)),
                ('preview', models.ImageField(blank=True, upload_to=kino.models.cinema.upload_cinema_preview)),
                ('seo_title', models.CharField(blank=True, max_length=50)),
                ('seo_keywords', models.CharField(blank=True, max_length=100)),
                ('seo_description', models.TextField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CinemaHall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('created_date', models.DateField(default=datetime.datetime.now)),
                ('description', models.TextField(blank=True, max_length=1000)),
                ('scheme', models.ImageField(upload_to='images/scheme')),
                ('preview', models.ImageField(upload_to=kino.models.cinema.upload_cinemahall_preview)),
                ('seo_title', models.CharField(blank=True, max_length=50)),
                ('seo_keywords', models.CharField(blank=True, max_length=100)),
                ('seo_description', models.CharField(blank=True, max_length=100)),
                ('cinema', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='kino.cinema')),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, verbose_name='Name')),
                ('year', models.IntegerField(choices=[(1900, 1900), (1901, 1901), (1902, 1902), (1903, 1903), (1904, 1904), (1905, 1905), (1906, 1906), (1907, 1907), (1908, 1908), (1909, 1909), (1910, 1910), (1911, 1911), (1912, 1912), (1913, 1913), (1914, 1914), (1915, 1915), (1916, 1916), (1917, 1917), (1918, 1918), (1919, 1919), (1920, 1920), (1921, 1921), (1922, 1922), (1923, 1923), (1924, 1924), (1925, 1925), (1926, 1926), (1927, 1927), (1928, 1928), (1929, 1929), (1930, 1930), (1931, 1931), (1932, 1932), (1933, 1933), (1934, 1934), (1935, 1935), (1936, 1936), (1937, 1937), (1938, 1938), (1939, 1939), (1940, 1940), (1941, 1941), (1942, 1942), (1943, 1943), (1944, 1944), (1945, 1945), (1946, 1946), (1947, 1947), (1948, 1948), (1949, 1949), (1950, 1950), (1951, 1951), (1952, 1952), (1953, 1953), (1954, 1954), (1955, 1955), (1956, 1956), (1957, 1957), (1958, 1958), (1959, 1959), (1960, 1960), (1961, 1961), (1962, 1962), (1963, 1963), (1964, 1964), (1965, 1965), (1966, 1966), (1967, 1967), (1968, 1968), (1969, 1969), (1970, 1970), (1971, 1971), (1972, 1972), (1973, 1973), (1974, 1974), (1975, 1975), (1976, 1976), (1977, 1977), (1978, 1978), (1979, 1979), (1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021)], default=2021, verbose_name='Year')),
                ('country', models.CharField(default='', max_length=100)),
                ('director', models.CharField(default='', max_length=65)),
                ('producer', models.CharField(default='', max_length=65)),
                ('music', models.CharField(default='', max_length=65, verbose_name='Music By:')),
                ('scenarist', models.CharField(default='', max_length=65, verbose_name='Written By:')),
                ('genre', models.CharField(max_length=50, null=True)),
                ('description', models.TextField(default='', max_length=1000)),
                ('video', models.URLField(blank=True)),
                ('premiere', models.DateField(default=django.utils.timezone.now)),
                ('preview', models.FileField(upload_to=kino.models.film.upload_film_preview)),
                ('two_dimensions', models.BooleanField(default=False, null=True)),
                ('three_dimensions', models.BooleanField(default=False, null=True)),
                ('imax', models.BooleanField(default=False, null=True)),
                ('duration', models.TimeField(null=True, verbose_name='Duration of film:')),
                ('seo_title', models.CharField(blank=True, max_length=50)),
                ('seo_keywords', models.CharField(blank=True, max_length=100)),
                ('seo_description', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone1', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('phone2', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('seo_text', models.TextField(max_length=500)),
                ('seo_title', models.CharField(blank=True, max_length=50)),
                ('seo_keywords', models.CharField(blank=True, max_length=100)),
                ('seo_description', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('pub_date', models.DateField(default=django.utils.timezone.now)),
                ('description', models.TextField(max_length=1000)),
                ('status', models.CharField(choices=[('ON', 'On'), ('OFF', 'Off')], default=('OFF', 'Off'), max_length=10)),
                ('preview', models.ImageField(null=True, upload_to=kino.models.news.upload_news_preview)),
                ('video', models.URLField(blank=True)),
                ('seo_title', models.CharField(blank=True, max_length=50)),
                ('seo_keywords', models.CharField(blank=True, max_length=100)),
                ('seo_description', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('status', models.BooleanField(default=False)),
                ('preview', models.ImageField(upload_to='images/preview')),
                ('seo_title', models.CharField(blank=True, max_length=50)),
                ('seo_keywords', models.CharField(blank=True, max_length=100)),
                ('seo_description', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Shares',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('pub_date', models.DateField(default=django.utils.timezone.now)),
                ('description', models.TextField(blank=True, max_length=1000)),
                ('status', models.CharField(blank=True, choices=[('ON', 'On'), ('OFF', 'Off')], default=('OFF', 'Off'), max_length=10)),
                ('preview', models.ImageField(upload_to=kino.models.shares.upload_shares_preview)),
                ('video', models.URLField(blank=True)),
                ('seo_title', models.CharField(blank=True, max_length=50)),
                ('seo_keywords', models.CharField(blank=True, max_length=100)),
                ('seo_description', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SharesBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='banners/shares')),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='SliderBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='banners/slider')),
                ('url', models.URLField()),
                ('text', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='VipHallImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='images/vip_hall')),
                ('vip_hall', models.ForeignKey(on_delete=django.db.models.fields.related.ForeignKey, to='kino.page')),
            ],
        ),
        migrations.CreateModel(
            name='SharesImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='images/shares')),
                ('shares', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kino.shares')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.CharField(default=0, max_length=25, null=True, verbose_name='Minimum cost:')),
                ('two_dimensions', models.BooleanField(default=False, null=True)),
                ('three_dimensions', models.BooleanField(default=False, null=True)),
                ('imax', models.BooleanField(default=False, null=True)),
                ('date', models.DateField(default=django.utils.timezone.now, null=True)),
                ('time', models.TimeField(default=django.utils.timezone.now, null=True, verbose_name='Start time:')),
                ('cinemahall', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kino.cinemahall', verbose_name='Hall:')),
                ('film', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kino.film')),
            ],
        ),
        migrations.CreateModel(
            name='NewsImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='images/news')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kino.news')),
            ],
        ),
        migrations.CreateModel(
            name='MobileAppImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='images/mobile_app')),
                ('mobile', models.ForeignKey(on_delete=django.db.models.fields.related.ForeignKey, to='kino.page')),
            ],
        ),
        migrations.CreateModel(
            name='FilmImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='images/film')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kino.film')),
            ],
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(blank=True, max_length=200)),
                ('status', models.BooleanField(default=False)),
                ('coordinates', models.CharField(max_length=100)),
                ('seo_title', models.CharField(blank=True, max_length=50)),
                ('seo_keywords', models.CharField(blank=True, max_length=100)),
                ('seo_description', models.CharField(blank=True, max_length=100)),
                ('cinema', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kino.cinema')),
            ],
        ),
        migrations.CreateModel(
            name='CinemaImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='images/cinema')),
                ('cinema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kino.cinema')),
            ],
        ),
        migrations.CreateModel(
            name='CinemaHallImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='images/cinema_hall')),
                ('cinema_hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kino.cinemahall')),
            ],
        ),
        migrations.CreateModel(
            name='ChildrenRoomImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='images/children_room')),
                ('children_room', models.ForeignKey(on_delete=django.db.models.fields.related.ForeignKey, to='kino.page')),
            ],
        ),
        migrations.CreateModel(
            name='CafeBarImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='images/cafe_bar')),
                ('cafe_bar', models.ForeignKey(on_delete=django.db.models.fields.related.ForeignKey, to='kino.page')),
            ],
        ),
        migrations.CreateModel(
            name='AdvertisingImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='images/advertising')),
                ('advertising', models.ForeignKey(on_delete=django.db.models.fields.related.ForeignKey, to='kino.page')),
            ],
        ),
        migrations.CreateModel(
            name='AboutImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='images/about')),
                ('about', models.ForeignKey(on_delete=django.db.models.fields.related.ForeignKey, to='kino.page')),
            ],
        ),
    ]
