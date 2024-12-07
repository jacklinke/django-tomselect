# Generated by Django 4.2 on 2023-05-03 09:50

from django.db import migrations


def forwards_func(apps, schema_editor):
    Edition = apps.get_model("app", "Edition")
    Magazine = apps.get_model("app", "Magazine")
    data = [{"name": f"2022-{n}", "year": "2022", "pages": str(n), "pub_num": f"{n+100}"} for n in range(1, 50)]
    data.insert(
        10,
        {
            "name": "VERY LONG NAME THAT IS PROBABLY GOING TO CAUSE SOME PROBLEMS 2022",
            "year": "",
            "pages": "",
            "pub_num": "5000000",
        },
    )
    mag = Magazine.objects.create(name="Test Magazine")
    _other = Magazine.objects.create(name="No Relations")
    for d in data:
        Edition.objects.create(**d, magazine=mag)


def reverse_func(apps, schema_editor):
    Edition = apps.get_model("app", "Edition")
    Magazine = apps.get_model("app", "Magazine")
    Edition.objects.all().delete()
    Magazine.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [migrations.RunPython(forwards_func, reverse_func)]