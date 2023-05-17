from django.db import models
from pytils.translit import slugify
from datetime import datetime
class Cabinet(models.Model):
    cabinetName = models.CharField("Кабинет", max_length=255)

    def __str__(self):
        return f"{self.cabinetName}"

    class Meta:
        verbose_name = "Кабинет"
        verbose_name_plural = "Кабинеттер"

class Day(models.Model):
    dayName = models.CharField("Күн", max_length=255)

    def __str__(self):
        return f"{self.dayName}"

    class Meta:
        verbose_name = "Күн"
        verbose_name_plural = "Күндер"

class Teacher(models.Model):
    teacherName = models.CharField("Мұғалім (Тегі А.)", max_length=255)

    def __str__(self):
        return f"{self.teacherName}"

    class Meta:
        verbose_name = "Мұғалім"
        verbose_name_plural = "Мұғалімдер"

class Subject(models.Model):
    subjectName = models.CharField("Пән аты", max_length=255)

    def __str__(self):
        return f"{self.subjectName}"

    class Meta:
        verbose_name = "Пән"
        verbose_name_plural = "Пәндер"

class Term(models.Model):
    termName = models.CharField("Семестр", max_length=255)
    slug = models.SlugField(unique=True, editable=False, blank=True)

    def __str__(self):
        return f"{self.termName}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.termName)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Семестр"
        verbose_name_plural = "Семестрлер"
class Position(models.Model):
    positionName = models.CharField("Ауысым", max_length=255)
    slug = models.SlugField(unique=True, editable=False, blank=True)

    def __str__(self):
        return f"{self.positionName}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.positionName)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Ауысым"
        verbose_name_plural = "Ауысымдар"

class Course(models.Model):
    courseName = models.CharField("Курс", max_length=255)
    slug = models.SlugField(unique=True, editable=False, blank=True)

    def __str__(self):
        return f"{self.courseName}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.courseName)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курстар"

class GroupStudy(models.Model):
    groupName = models.CharField("Топ атауы", max_length=255)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, verbose_name="Ауысым")
    term = models.ForeignKey(Term, on_delete=models.CASCADE, verbose_name="Семестр")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс")

    def __str__(self):
        return f"{self.groupName}"

    class Meta:
        verbose_name = "Топ"
        verbose_name_plural = "Топтар"



class Schedule(models.Model):
    group = models.ForeignKey(GroupStudy, on_delete=models.CASCADE, verbose_name="Топ")
    day = models.ForeignKey(Day, on_delete=models.CASCADE, verbose_name="Күн")
    lessonTime = models.CharField("Сабақ уақыты", max_length=255)
    cabinet = models.ForeignKey(Cabinet, on_delete=models.CASCADE, verbose_name="Кабинет")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name="Пән")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name="Мұғалім")

    def __str__(self):
        return f"{self.group.groupName} - {self.lessonTime} - {self.day.dayName}"

    class Meta:
        verbose_name = "Сабақ кестесі"
        verbose_name_plural = "Сабақ кестесі"


class Exam(models.Model):
    group = models.ForeignKey(GroupStudy, on_delete=models.CASCADE, verbose_name="Топ")
    startDateTime = models.DateTimeField("Басталу күні мен уақыты", default=datetime.now)
    cabinet = models.ForeignKey(Cabinet, on_delete=models.CASCADE, verbose_name="Кабинет")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name="Пән")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name="Мұғалім")

    def __str__(self):
        return f"{self.group.groupName} - {self.startDateTime}"

    class Meta:
        verbose_name = "Емтихан кестесі"
        verbose_name_plural = "Емтихан кестесі"