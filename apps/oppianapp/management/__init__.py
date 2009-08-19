'''
Created on 14 August 2009

@author: steve
'''

from django.conf import settings
print settings.INSTALLED_APPS
from django.db.models import signals
from django.utils.translation import ugettext_noop as _
from django.contrib.contenttypes.models import ContentType
from django.template.defaultfilters import slugify


"""
Creates the default oppian data.
"""
if "oppianapp" in settings.INSTALLED_APPS:
    from oppianapp import models as oppianapp_app
    
    def create_initial_oppian_data(app, created_models, verbosity, **kwargs):
        
        if "basic.blog" in settings.INSTALLED_APPS:
            from basic.blog import models as blog
            from basic.blog.admin import SavePost
            import datetime
            
            if verbosity >= 2:
                print "creating oppian blogs:"
                
            title = "Welcome to Oppian"
            blog_image_code = ''
            photos = Photo.objects.filter(photo='images/OppianO-96x82.png')
            if len(photos)==1:
                blog_image_code = '<inline type="media.photo" id="%s" class="small_left" />' % photos[0].id
            body = '%sHello all' % blog_image_code
            
            blogs = blog.Post.objects.filter(title=title)
            if len(blogs)==0:
                post=blog.Post(
                    title=title,
                    body=body,
                    tease=title,
                    slug=slugify(title),
                    status=2, # public
                    allow_comments=True,
                    publish=datetime.datetime.now(),
                    created=datetime.datetime.now())                    
                SavePost(post, True)
                if verbosity >= 2:
                    print '  Adding "%s"' % title
        
    signals.post_syncdb.connect(create_initial_oppian_data, sender=oppianapp_app)
else:
    print "Skipping creation of initial site data as oppian app not found"


"""
Creates the default media - photos.
"""
if "basic.media" in settings.INSTALLED_APPS:
    from basic.inlines import models as media
    from basic.media.models import Photo
    import os, glob

    
    def create_photo(path, leafname, verbosity):
        filename = '%s%s' % (path, leafname)
        photos = Photo.objects.filter(photo=filename)
        if len(photos)==0:
            title = leafname
            description = leafname
            photo = Photo(
                        title=title, 
                        slug=slugify(title), 
                        photo=filename,
                        license="http://creativecommons.org/licenses/by-nc-nd/2.0/",
                        description=description, 
                        tags="logo, oppian")
            photo.save()
            if verbosity >= 2:
                print '  Adding "%s""' % filename
        
    def create_initial_media(app, created_models, verbosity, **kwargs):
        if verbosity >= 2:
            print "creating initial media:"
            
        images_dir = '%s/images' % settings.MEDIA_ROOT
        os.chdir(images_dir)

        # currently only get PNG and JPEG files
        filenames = glob.glob("*.png") + glob.glob("*.jpg")
        for filename in filenames:
            create_photo('images/', filename, verbosity)

    signals.post_syncdb.connect(create_initial_media, sender=media)
else:
    print "Skipping creation of initial inline photos as inline app not found"



"""
Creates the default inline types - photo
"""
if "basic.inlines" in settings.INSTALLED_APPS:
    from basic.inlines import models as inlines
    from basic.media.models import Photo
    
    def create_inline_types(app, created_models, verbosity, **kwargs):
        if verbosity >= 2:
            print "creating inline types:"
        
        photo_content_type = ContentType.objects.get_for_model(Photo)
        types = inlines.InlineType.objects.filter(content_type=photo_content_type)
        if len(types)==0:
            inline_type_photo = inlines.InlineType(title="Photo", content_type=photo_content_type)
            inline_type_photo.save()
            if verbosity >= 2:
                print "  Adding photo"
    
    signals.post_syncdb.connect(create_inline_types, sender=inlines)
else:
    print "Skipping creation of InlineTypes as inline types app not found"



"""
Creates the default Site object.
"""
from django.contrib.sites.models import Site
from django.contrib.sites import models as site_app

def create_default_site(app, created_models, verbosity, **kwargs):
    if Site in created_models:
        # first check for existing site id
        try:
            site = Site.objects.get(id=settings.SITE_ID)
            # delete it if it exists
            site.delete()
        except:
            # site doesn't exist
            pass

        if verbosity >= 2:
            print " Site object"
        s = Site(id=settings.SITE_ID, domain=settings.SITE_DOMAIN, name=settings.SITE_NAME)
        s.save()
    Site.objects.clear_cache()

signals.post_syncdb.connect(create_default_site, sender=site_app)