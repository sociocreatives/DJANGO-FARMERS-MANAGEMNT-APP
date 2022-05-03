# Generated by Django 3.1.4 on 2021-02-08 00:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Audits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('action', models.TextField()),
                ('user', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=10)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Audits',
            },
        ),
        migrations.CreateModel(
            name='Banks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('reg_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Banks',
            },
        ),
        migrations.CreateModel(
            name='Cooperatives',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('growers_code', models.CharField(max_length=20)),
                ('region', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=10)),
                ('reg_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Cooperatives',
            },
        ),
        migrations.CreateModel(
            name='Devices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('imei', models.CharField(max_length=50, unique=True)),
                ('reg_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Devices',
            },
        ),
        migrations.CreateModel(
            name='Factories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('zone', models.CharField(max_length=50)),
                ('reg_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=10)),
                ('cooperative', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kilosahihi.cooperatives')),
            ],
            options={
                'verbose_name_plural': 'Factories/Collection Centres',
            },
        ),
        migrations.CreateModel(
            name='FarmersTransactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('gross_weight', models.CharField(max_length=20)),
                ('tare_weight', models.CharField(max_length=20, null=True)),
                ('number_of_bags', models.CharField(max_length=20, null=True)),
                ('total_amount', models.CharField(max_length=20, null=True)),
                ('amount_deductable', models.CharField(max_length=20, null=True)),
                ('amount_payable', models.CharField(max_length=20, null=True)),
                ('tx_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=10)),
                ('device', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kilosahihi.devices')),
            ],
            options={
                'verbose_name_plural': 'Farmers Transactions',
            },
        ),
        migrations.CreateModel(
            name='FarmInputs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Farm Inputs',
            },
        ),
        migrations.CreateModel(
            name='Produce',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('status', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Produce',
            },
        ),
        migrations.CreateModel(
            name='ProduceVariety',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('status', models.CharField(max_length=10)),
                ('produce', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kilosahihi.produce')),
            ],
            options={
                'verbose_name_plural': 'Produce Variety',
            },
        ),
        migrations.CreateModel(
            name='SmallHolderEstates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('region', models.CharField(max_length=50)),
                ('growers_code', models.CharField(max_length=50)),
                ('geolocation', models.CharField(max_length=50)),
                ('reg_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Small Holder Estates',
            },
        ),
        migrations.CreateModel(
            name='Unions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('reg_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Unions',
            },
        ),
        migrations.CreateModel(
            name='UserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name_plural': 'User Permissions',
            },
        ),
        migrations.CreateModel(
            name='UserRoles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name_plural': 'User Roles',
            },
        ),
        migrations.CreateModel(
            name='UserUnions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('status', models.CharField(max_length=10)),
                ('permission', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kilosahihi.userpermissions')),
                ('role', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kilosahihi.userroles')),
                ('union', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kilosahihi.unions')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'User Unions',
            },
        ),
        migrations.CreateModel(
            name='UserSmallHolderEstates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('status', models.CharField(max_length=10)),
                ('permission', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kilosahihi.userpermissions')),
                ('role', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kilosahihi.userroles')),
                ('smallholderestate', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kilosahihi.smallholderestates')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'User Small Holder Estates',
            },
        ),
        migrations.CreateModel(
            name='UserFieldOfficers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('employee_number', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=10)),
                ('factory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kilosahihi.factories')),
                ('permission', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kilosahihi.userpermissions')),
                ('role', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kilosahihi.userroles')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'User Field Officers',
            },
        ),
        migrations.CreateModel(
            name='UserFarmers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('employee_number', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=10)),
                ('cooperative', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kilosahihi.cooperatives')),
                ('factory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kilosahihi.factories')),
                ('permission', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kilosahihi.userpermissions')),
                ('role', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kilosahihi.userroles')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'User Farmers',
            },
        ),
        migrations.CreateModel(
            name='UserCooperative',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('status', models.CharField(max_length=10)),
                ('cooperative', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kilosahihi.cooperatives')),
                ('permission', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kilosahihi.userpermissions')),
                ('role', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kilosahihi.userroles')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'User Cooperative Societies',
            },
        ),
        migrations.CreateModel(
            name='UserBankAccounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('account', models.CharField(max_length=50, unique=True)),
                ('status', models.CharField(max_length=10)),
                ('bank', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kilosahihi.banks')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Bank Account',
            },
        ),
        migrations.CreateModel(
            name='UserAttributes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('national_id', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=10)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'User Attributes',
            },
        ),
        migrations.CreateModel(
            name='SmallHolderEstateTransactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('delivery', models.CharField(max_length=20)),
                ('tare_weight', models.CharField(max_length=20, null=True)),
                ('number_of_bags', models.CharField(max_length=20, null=True)),
                ('total_amount', models.CharField(max_length=20, null=True)),
                ('amount_deductable', models.CharField(max_length=20, null=True)),
                ('amount_payable', models.CharField(max_length=20, null=True)),
                ('tx_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=10)),
                ('smallholderestate', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kilosahihi.usersmallholderestates')),
                ('variety', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kilosahihi.producevariety')),
            ],
            options={
                'verbose_name_plural': 'Small Holder Estates Transactions',
            },
        ),
        migrations.AddField(
            model_name='smallholderestates',
            name='union',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kilosahihi.unions'),
        ),
        migrations.CreateModel(
            name='SmallHolderEstateInputRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('desc', models.CharField(max_length=50)),
                ('cost_per_unit', models.CharField(max_length=50)),
                ('quantity', models.CharField(max_length=50)),
                ('reason', models.CharField(max_length=50)),
                ('total_amount', models.CharField(max_length=50)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=10)),
                ('inputid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kilosahihi.farminputs')),
                ('smallholderestate', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kilosahihi.usersmallholderestates')),
                ('union', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kilosahihi.unions')),
            ],
            options={
                'verbose_name_plural': 'Farm Input Request',
            },
        ),
        migrations.CreateModel(
            name='SmallHolderEstateIncomeSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.DateTimeField(auto_now_add=True)),
                ('source', models.CharField(max_length=50)),
                ('total_amount', models.CharField(max_length=50)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=10)),
                ('smallholderestate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kilosahihi.usersmallholderestates')),
            ],
            options={
                'verbose_name_plural': 'Small Holder Estate Income Source',
            },
        ),
        migrations.CreateModel(
            name='SmallHolderEstateDebts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('institution', models.CharField(max_length=50)),
                ('total_amount', models.CharField(max_length=50)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=10)),
                ('smallholderestate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kilosahihi.usersmallholderestates')),
            ],
            options={
                'verbose_name_plural': 'Smaller Holder Estate Debts',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('payment_code', models.CharField(max_length=50)),
                ('method', models.CharField(max_length=50)),
                ('payment_status', models.CharField(max_length=50)),
                ('payment_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=10)),
                ('tx_reference', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kilosahihi.farmerstransactions')),
            ],
            options={
                'verbose_name_plural': 'Payment',
            },
        ),
        migrations.CreateModel(
            name='Farms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('acres', models.CharField(max_length=20, unique=True)),
                ('trees', models.CharField(max_length=20, unique=True)),
                ('reg_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=10)),
                ('farmer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kilosahihi.userfarmers')),
            ],
            options={
                'verbose_name_plural': 'Farms',
            },
        ),
        migrations.AddField(
            model_name='farmerstransactions',
            name='farmer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kilosahihi.userfarmers'),
        ),
        migrations.AddField(
            model_name='farmerstransactions',
            name='fieldofficer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kilosahihi.userfieldofficers'),
        ),
        migrations.AddField(
            model_name='farmerstransactions',
            name='variety',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kilosahihi.producevariety'),
        ),
        migrations.CreateModel(
            name='FarmerInputRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('desc', models.CharField(max_length=50)),
                ('cost_per_unit', models.CharField(max_length=50)),
                ('quantity', models.CharField(max_length=50)),
                ('reason', models.CharField(max_length=50)),
                ('total_amount', models.CharField(max_length=50)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=10)),
                ('cooperative', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kilosahihi.cooperatives')),
                ('farmer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kilosahihi.userfarmers')),
                ('inputid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kilosahihi.farminputs')),
            ],
            options={
                'verbose_name_plural': 'Farm Input Request',
            },
        ),
        migrations.CreateModel(
            name='FarmerIncomeSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.DateTimeField(auto_now_add=True)),
                ('source', models.CharField(max_length=50)),
                ('total_amount', models.CharField(max_length=50)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=10)),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kilosahihi.userfarmers')),
            ],
            options={
                'verbose_name_plural': 'Farmer Income Source',
            },
        ),
        migrations.CreateModel(
            name='FarmerDebts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.DateTimeField(auto_now_add=True)),
                ('institution', models.CharField(max_length=50)),
                ('total_amount', models.CharField(max_length=50)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=10)),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kilosahihi.userfarmers')),
            ],
            options={
                'verbose_name_plural': 'Farmer Debts',
            },
        ),
        migrations.AddField(
            model_name='devices',
            name='factory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kilosahihi.factories'),
        ),
        migrations.AddField(
            model_name='cooperatives',
            name='union',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kilosahihi.unions'),
        ),
    ]
