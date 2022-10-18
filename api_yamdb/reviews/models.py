from core.models import PubDateModel
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

CHOICES = (
    ('user', 'Пользователь'),
    ('moderator', 'Модератор'),
    ('admin', 'Администратор'),
)


class User(AbstractUser):
    bio = models.CharField(max_length=250, null=True, blank=True)
    role = models.CharField(max_length=20, default='user', choices=CHOICES)
    confirmation_code = models.CharField(max_length=10, null=True, blank=True)
    email = models.EmailField(unique=True)


class Genre(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Category(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(unique=True, max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Title(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    genre = models.ManyToManyField(
        Genre,
        through='TitleGenreAssign',
        related_name='title'
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True,
        related_name='title'
    )

    @property
    def rating(self):
        reviews = Review.objects.filter(title=self.pk)
        scores = 0
        count = 0
        for review in reviews:
            scores += review.score
            count += 1
        if count == 0:
            return None
        return scores/count

    def __str__(self):
        return self.name[0:15]

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'


class Review(PubDateModel):
    author = models.ForeignKey(
        User,
        verbose_name='review`s author',
        on_delete=models.CASCADE,
        related_name='review'
    )
    text = models.TextField(
        verbose_name='review',
        max_length=100,
        help_text='Напишите ваш отзыв'
    )
    score = models.IntegerField(
        verbose_name='Оценка',
        validators=(
            MinValueValidator(1),
            MaxValueValidator(10))
    )
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    def __str__(self):
        return self.text[0:15]

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        constraints = (
            models.UniqueConstraint(
                fields=('title', 'author',),
                name='unique_title_author'
            ),
        )


class Comment(PubDateModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    text = models.TextField(max_length=500)

    def __str__(self):
        return self.text[0:15]

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class TitleGenreAssign(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('title', 'genre'),)
