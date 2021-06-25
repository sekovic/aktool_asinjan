# Generated by Django 3.0.7 on 2020-07-29 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200724_1038'),
    ]

    operations = [
        migrations.AddField(
            model_name='appsettings',
            name='server_hostname',
            field=models.CharField(default='www.asin-jan.com', max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='do_get_my_price_for_asin',
            field=models.BooleanField(default=False, verbose_name='GetMyPricingForASIN'),
        ),
        migrations.AlterField(
            model_name='user',
            name='do_get_product_categories_for_asin',
            field=models.BooleanField(default=False, verbose_name='GetProductCategoriesForASIN'),
        ),
    ]
