# -*- coding: utf-8 *-*
import datetime

from django.contrib.auth.models import User

from common.utils import render_response


def countdown(request):
    diff = datetime.datetime(2011, 9, 23) - datetime.datetime.today()
    time_left = "0{0}:{1}:{2}:{3}".format(
        diff.days,
        diff.seconds / 60 / 60,
        diff.seconds / 60 - (diff.seconds / 60 / 60 * 60),
        diff.seconds - (diff.seconds / 60 * 60)
    )
    return render_response(request, 'baseCountdown.html',
                                        {'time_left': time_left})


def intro(request):
    """ Intro/Splash screen.
    """
    return render_response(request, 'intro.html')


def features(request):
    """ Features section.
    """
    return render_response(request, 'features.html')


def downloads(request):
    """ Downloads section.
    """
    return render_response(request, 'downloads.html')


def about(request):
    """ About section. All ninja people: devs and packagers
    """
    return render_response(request, 'about.html')


def using(request):
    """ People using Ninja-ide.
    """
    return render_response(request, 'using.html')


def contrib(request):
    """ Contribution section. All info to do so.
    """
    return render_response(request, 'contrib.html')


def updates(request):
    """ Just returns a simple json formatted file telling the
        actual and stable ninja-ide version.
    """
    return render_response(request, 'updates_simple.html')


def user_detail(request, user_name=None):
    """ Returns the user (as 'page_user') info and his/her plugins
        Nothing in case error or no existing user
    """
    context = {}

    try:
        user = User.objects.get(username=user_name)
        context['user_page'] = user
    except Exception, e:
        print e
    else:
        user_plugins = user.plugin_set.all()
        context['plugins'] = user_plugins
        context['user_submitted_plugins'] = user_plugins.exists()

    return render_response(request, 'user_detail.html', context)
