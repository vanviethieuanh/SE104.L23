# Generated by Django 3.0.4 on 2021-06-28 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.CharField(max_length=24, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=29)),
                ('identify_card_no', models.CharField(max_length=19)),
                ('award_point', models.IntegerField()),
                ('phone_no', models.CharField(max_length=12)),
                ('email_address', models.CharField(max_length=34)),
                ('post_number', models.IntegerField()),
                ('notes', models.CharField(max_length=560)),
            ],
            options={
                'db_table': 'client',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RoomCategories',
            fields=[
                ('id', models.CharField(max_length=24, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=33)),
                ('price', models.IntegerField()),
                ('notes', models.CharField(max_length=568)),
            ],
            options={
                'db_table': 'room_categories',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RoomRentals',
            fields=[
                ('id', models.CharField(max_length=24, primary_key=True, serialize=False)),
                ('create_at', models.DateField()),
                ('start_at', models.DateField()),
                ('check_out_at', models.CharField(max_length=19)),
                ('summary', models.CharField(max_length=487)),
            ],
            options={
                'db_table': 'room_rentals',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.CharField(max_length=24, primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=24)),
                ('status', models.CharField(max_length=24)),
                ('floors', models.IntegerField()),
                ('number', models.IntegerField()),
            ],
            options={
                'db_table': 'rooms',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.CharField(max_length=24, primary_key=True, serialize=False)),
                ('created_at', models.DateField()),
                ('is_canceled', models.CharField(max_length=5)),
                ('quantity', models.IntegerField()),
                ('sub_total', models.IntegerField()),
                ('detail', models.CharField(max_length=557)),
            ],
            options={
                'db_table': 'services',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ServiceTypes',
            fields=[
                ('id', models.CharField(max_length=24, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=568)),
                ('unit_price', models.CharField(max_length=86)),
            ],
            options={
                'db_table': 'service_types',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.CharField(max_length=24, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=34)),
                ('post_number', models.IntegerField()),
                ('email_address', models.CharField(max_length=32)),
                ('phone_no', models.CharField(max_length=12)),
                ('identity_card_no', models.CharField(max_length=19)),
                ('address', models.CharField(max_length=42)),
                ('is_manager', models.CharField(max_length=5)),
            ],
            options={
                'db_table': 'staff',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.CharField(max_length=24, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=36)),
                ('descriptions', models.CharField(max_length=548)),
                ('is_available', models.CharField(max_length=5)),
            ],
            options={
                'db_table': 'status',
                'managed': False,
            },
        ),
    ]
