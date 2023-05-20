from django.db import models


class Question(models.Model):
    question_id = models.PositiveIntegerField(
        'id вопроса',
        db_index=True,
        unique=True
    )
    question = models.TextField('Текст вопроса')
    answer = models.TextField('Ответ на вопрос')
    created_at = models.DateTimeField('Дата публикации вопроса')

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.question
