from django.db import models
from django.utils import timezone

class Specalty(models.Model):
    name = models.CharField(verbose_name='Название специальности', max_length=255)

    def __unicode__(self):
        return str(self.name)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'специальность'
        verbose_name_plural = 'Специальности'
        ordering = ['name']

class Group(models.Model):
    name = models.CharField(verbose_name='Название группы', max_length=255)
    specalty = models.ForeignKey(Specalty, verbose_name='Специальность')

    def __unicode__(self):
        return str(self.name)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'группу'
        verbose_name_plural = 'Группы'
        ordering = ['name']

class Student(models.Model):
    group = models.ForeignKey(Group, verbose_name='Группа')
    name = models.CharField(verbose_name='ФИО студента', max_length=255)

    def __unicode__(self):
        return str(self.name)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'студента'
        verbose_name_plural = 'Студенты'
        ordering = ['name']

class Teacher(models.Model):
    name = models.CharField(verbose_name='ФИО преподавателя', max_length=255)

    def __unicode__(self):
        return str(self.name)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'преподавателя'
        verbose_name_plural = 'Преподователи'
        ordering = ['name']

class Subject(models.Model):
    teacher = models.ForeignKey(Teacher, verbose_name='Преподаватель')
    name = models.CharField(verbose_name='Название предмета', max_length=255)
    time = models.PositiveIntegerField(verbose_name='Количество часов')

    def __unicode__(self):
        return str(self.name)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'предмет'
        verbose_name_plural = 'Предметы'
        ordering = ['name']

GRADES = (
	(1, 1),
	(2, 2),
	(3, 3),
	(4, 4),
	(5, 5),
)

class Journal(models.Model):
    subject = models.ForeignKey(Subject, verbose_name='Предмет')
    student = models.ForeignKey(Student, verbose_name='Студент')
    teacher = models.ForeignKey(Teacher, verbose_name='Преподаватель')
    attendance = models.BooleanField(verbose_name='Пропуск', default=False)
    grade = models.PositiveIntegerField(verbose_name='Оценка', choices=GRADES)
    timeserver = models.DateTimeField(verbose_name='Дата и время', auto_now_add=True)

    def __unicode__(self):
        return str(self.timeserver)

    def __str__(self):
        return str(self.timeserver)

    class Meta:
        verbose_name = 'запись журнала'
        verbose_name_plural = 'Журнал'
        ordering = ['timeserver']