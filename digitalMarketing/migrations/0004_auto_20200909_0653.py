# Generated by Django 3.1.1 on 2020-09-09 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('digitalMarketing', '0003_auto_20200909_0604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daservice',
            name='discount',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='digitalMarketing.discount'),
        ),
        migrations.AlterField(
            model_name='daservice',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='discount',
            name='discountPrice',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='dmservice',
            name='discount',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='digitalMarketing.discount'),
        ),
        migrations.AlterField(
            model_name='dmservice',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]