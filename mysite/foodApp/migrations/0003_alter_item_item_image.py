# Generated by Django 4.1.7 on 2023-03-21 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodApp', '0002_item_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://media.istockphoto.com/id/1075374570/vector/coming-soon.jpg?s=612x612&w=0&k=20&c=6W1rSRAoJnxtMSi98mGD7LjiXA3xQMotLn8hJnmXjzI=', max_length=500),
        ),
    ]