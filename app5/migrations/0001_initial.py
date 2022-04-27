# Generated by Django 3.2.9 on 2022-01-03 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.BigIntegerField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[['MALE', 'Male'], ['FEMALE', 'Female']], max_length=10)),
                ('adhaar', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='payment',
            fields=[
                ('pid', models.AutoField(primary_key=True, serialize=False)),
                ('pname', models.CharField(max_length=50)),
                ('pemail', models.EmailField(max_length=254)),
                ('pphone', models.BigIntegerField()),
                ('dc', models.IntegerField()),
                ('bank', models.CharField(choices=[['sbi', 'SBI'], ['union', 'UNION']], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='company',
            fields=[
                ('payment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='app5.payment')),
                ('customer_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app5.customer')),
                ('bal', models.IntegerField()),
            ],
            bases=('app5.customer', 'app5.payment'),
        ),
    ]