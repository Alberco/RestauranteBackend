# Generated by Django 4.1.2 on 2022-10-13 04:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('name_category', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'db_table': 'category',
                'ordering': ['name_category'],
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('name_client', models.CharField(max_length=30)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Customers',
                'db_table': 'client',
                'ordering': ['name_client'],
            },
        ),
        migrations.CreateModel(
            name='TableFood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('name_table_flood', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'TableFlood',
                'verbose_name_plural': 'TableFloods',
                'db_table': 'table_food',
                'ordering': ['name_table_flood'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('name_product', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.category')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'db_table': 'product',
                'ordering': ['name_product'],
            },
        ),
        migrations.CreateModel(
            name='FoodMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('description_food_menu', models.TextField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.client')),
                ('products', models.ManyToManyField(to='orders.product')),
                ('tablefood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.tablefood')),
            ],
            options={
                'verbose_name': 'FoodMenu',
                'verbose_name_plural': 'FoodMenus',
                'db_table': 'food_menu',
            },
        ),
    ]
