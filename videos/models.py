from django.db import models
from urlparse import urlparse, parse_qs
import gdata.youtube.service as youtube
import re


# Create your models here.

class Email(models.Model):
    message_id   = models.CharField(max_length=20)
    from_address = models.CharField(max_length=100)
    subject      = models.CharField(max_length=100)
    recieved     = models.DateTimeField()
    text_body    = models.TextField()
    html_body    = models.TextField()


    def video_id_find(self, youtube_link):
        """
        Parses the youtube_link in the email object for youtube links
        Taken From: 
        https://stackoverflow.com/questions/4356538/how-can-i-extract-video-id-from-youtubes-link-in-python
        Examples:
        - http://youtu.be/SA2iWivDJiE
        - http://www.youtube.com/watch?v=_oPAwA_Udwc&feature=feedu
        - http://www.youtube.com/embed/SA2iWivDJiE
        - http://www.youtube.com/v/SA2iWivDJiE?version=3&amp;hl=en_US
        """
        query = urlparse(youtube_link)
        if query.hostname == 'youtu.be':
            return query.path[1:]
        if query.hostname in ('www.youtube.com', 'youtube.com'):
            if query.path == '/watch':
                p = parse_qs(query.query)
                return p['v'][0]
            if query.path[:7] == '/embed/':
                return query.path.split('/')[2]
            if query.path[:3] == '/v/':
                return query.path.split('/')[2]
        # fail?
        return None


    def youtube_link_find(self):
        link = re.search("(?P<url>https?://[^\s]+)", self.text_body).group("url")
        print "Found Link: %s" % (link)
        return link


    def populate_data(self):
        self.youtube_link = self.youtube_link_find()
        self.youtube_id = self.video_id_find(self.youtube_link)


class Video(models.Model):
    youtube_id   = models.CharField(max_length=11)
    title        = models.CharField(max_length=200, null=True)
    email        = models.OneToOneField(Email, null=True)
    published    = models.DateTimeField(null=True)
    duration     = models.IntegerField(null=True)
    thumbnail    = models.URLField(max_length=20, null=True)


    def populate_data(self):
        yt_service = youtube.YouTubeService()
        entry = yt_service.GetYouTubeVideoEntry(video_id=self.youtube_id)

        self.title = entry.media.title.text
        self.published = entry.published.text
        self.duration = entry.media.duration.seconds
        self.thumbnail = entry.media.thumbnail[0].url

        try: 
            self.geo_location = entry.geo.location()
        except Exception as e:
            print e

        return self

