# Generated by Django 3.1 on 2023-05-16 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cabinet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cabinetName', models.CharField(max_length=255, verbose_name='Кабинет')),
            ],
            options={
                'verbose_name': 'Кабинет',
                'verbose_name_plural': 'Кабинеттер',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseName', models.CharField(max_length=255, verbose_name='Курс')),
                ('slug', models.SlugField(blank=True, editable=False, unique=True)),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курстар',
            },
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dayName', models.CharField(max_length=255, verbose_name='Күн')),
            ],
            options={
                'verbose_name': 'Күн',
                'verbose_name_plural': 'Күндер',
            },
        ),
        migrations.CreateModel(
            name='GroupStudy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupName', models.CharField(max_length=255, verbose_name='Топ атауы')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.course', verbose_name='Курс')),
            ],
            options={
                'verbose_name': 'Топ',
                'verbose_name_plural': 'Топтар',
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('positionName', models.CharField(max_length=255, verbose_name='Ауысым')),
                ('slug', models.SlugField(blank=True, editable=False, unique=True)),
            ],
            options={
                'verbose_name': 'Ауысым',
                'verbose_name_plural': 'Ауысымдар',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjectName', models.CharField(max_length=255, verbose_name='Пән аты')),
            ],
            options={
                'verbose_name': 'Пән',
                'verbose_name_plural': 'Пәндер',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacherName', models.CharField(max_length=255, verbose_name='Мұғалім (Тегі А.)')),
            ],
            options={
                'verbose_name': 'Мұғалім',
                'verbose_name_plural': 'Мұғалімдер',
            },
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('termName', models.CharField(max_length=255, verbose_name='Семестр')),
                ('slug', models.SlugField(blank=True, editable=False, unique=True)),
            ],
            options={
                'verbose_name': 'Семестр',
                'verbose_name_plural': 'Семестрлер',
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lessonTime', models.CharField(max_length=255, verbose_name='Сабақ уақыты')),
                ('cabinet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cabinet', verbose_name='Кабинет')),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.day', verbose_name='Күн')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.groupstudy', verbose_name='Топ')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.subject', verbose_name='Пән')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.teacher', verbose_name='Мұғалім')),
            ],
            options={
                'verbose_name': 'Сабақ кестесі',
                'verbose_name_plural': 'Сабақ кестесі',
            },
        ),
        migrations.AddField(
            model_name='groupstudy',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.position', verbose_name='Ауысым'),
        ),
        migrations.AddField(
            model_name='groupstudy',
            name='term',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.term', verbose_name='Семестр'),
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startDateTime', models.DateTimeField(verbose_name='Басталу күні мен уақыты')),
                ('cabinet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cabinet', verbose_name='Кабинет')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.groupstudy', verbose_name='Топ')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.subject', verbose_name='Пән')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.teacher', verbose_name='Мұғалім')),
            ],
            options={
                'verbose_name': 'Емтихан кестесі',
                'verbose_name_plural': 'Емтихан кестесі',
            },
        ),
    ]
