from django.db import models
from ..login_app.models import Users
# Create your models here.

class QuoteManager(models.Manager):
    def makeQuote(self, postData, user_id):
        errors = []
        if len(postData['quote']) < 10:
            errors.append('Quote must be longer than 10 characters')
        if len(postData['author']) < 3:
            errors.append("Author's name must be longer than 3 characters")
        if len(errors):
            return errors
        user = Users.objects.filter(id=user_id).exclude().get()
        q = Quotes.objects.create(
            quote = postData['quote'],
            author = postData['author'],
            posted_by = user
        )
        return q

    def deleteQuote(self, quote_id):
        quote = Quotes.objects.filter(id=quote_id).exclude().get()
        quote.delete()
        print("quote deleted")

    def addLike(self, postData, user_id):
        q = Quotes.objects.filter(id=postData['like']).exclude().get()
        user = Users.objects.filter(id=user_id).exclude().get()
        liked = user.liked_quotes.all()
        if q in liked:
            pass
        else:
            q.likes.add(user)
        q.save()
class Quotes(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=255)
    likes = models.ManyToManyField(Users, related_name='liked_quotes')
    posted_by = models.ForeignKey(Users, related_name='quotes_posted')
    objects = QuoteManager()
    def __repr__(self):
        return "<Quotes: {} {} {}>".format(self.quote, self.author, self.likes)