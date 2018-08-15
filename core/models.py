from django.db import models


class Movie(models.Model):
    RATED_G = 0
    RATED_PG = 1
    RATED_PG_13 = 2
    RATED_R = 3
    NOT_RATED = 4
    RATINGS = (
        (RATED_G, 'G - General Audience'),
        (RATED_PG, 'PG - Parental Guidance'),
        (RATED_PG_13, 'PG-13 - Parents Strongly Cautioned'),
        (RATED_R, 'R - Restricted'),
        (NOT_RATED, 'NR - Not Rated'),
    )

    title = models.CharField(
        max_length=140)
    plot = models.TextField()
    year = models.PositiveIntegerField()
    rating = models.IntegerField(
        choices=RATINGS,
        default=NOT_RATED
    )
    runtime = \
        models.PositiveIntegerField()
    website = models.URLField(blank=True)

    class Meta:
        ordering = ('-year', 'title')

    def __str__(self):
        return '{} ({})'.format(self.title, self.year)


