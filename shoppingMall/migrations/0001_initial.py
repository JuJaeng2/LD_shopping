# Generated by Django 4.1.1 on 2023-03-24 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('a_code', models.IntegerField(primary_key=True, serialize=False)),
                ('a_address', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'address',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('ca_code', models.IntegerField(primary_key=True, serialize=False)),
                ('u_id', models.IntegerField()),
                ('c_code', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'cart',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cloth',
            fields=[
                ('c_code', models.IntegerField(primary_key=True, serialize=False)),
                ('c_category', models.CharField(max_length=45)),
                ('c_size', models.CharField(max_length=45)),
                ('c_color', models.CharField(max_length=45)),
                ('c_price', models.IntegerField()),
                ('c_countLeft', models.IntegerField()),
                ('c_countBuy', models.IntegerField()),
                ('c_image', models.ImageField(blank=True, upload_to="shoppingMall/media/", null=True)),
            ],
            options={
                'db_table': 'cloth',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('p_code', models.IntegerField(primary_key=True, serialize=False)),
                ('c_code', models.IntegerField()),
                ('u_id', models.IntegerField()),
            ],
            options={
                'db_table': 'purchase',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('r_code', models.IntegerField(primary_key=True, serialize=False)),
                ('u_id', models.IntegerField()),
                ('r_title', models.CharField(max_length=45)),
                ('r_content', models.CharField(max_length=100)),
                ('r_star', models.IntegerField()),
            ],
            options={
                'db_table': 'review',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('u_id', models.IntegerField(primary_key=True, serialize=False)),
                ('u_pw', models.IntegerField()),
                ('a_code', models.IntegerField()),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
    ]
