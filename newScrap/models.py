from django.db import models


class ScrapedData(models.Model):
    """
    A model to store scraped data from websites.
    Each record contains a datetime, website URL, headline text, and link to the article.
    """

    datetime = models.DateTimeField()
    website = models.URLField()
    headline = models.CharField(max_length=255)
    link = models.URLField(default='default')

    def __str__(self):
        """Return the headline text when the model instance is converted to a string."""
        return self.headline
