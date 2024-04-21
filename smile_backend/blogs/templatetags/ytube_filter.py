# your_app/templatetags/youtube_filters.py
from django import template

register = template.Library()

@register.filter(name='ytube_embed')
def ytube_embed(link):
    """Extracts the video ID from a YouTube URL and returns the embed link."""
    try:
        video_id = link.split("=")[1]

        return f"https://www.youtube.com/embed/{video_id}?enablejsapi=1&origin=https://yourdomain.com&showinfo=0&iv_load_policy=3&modestbranding=1&theme=light&color=white&rel=0"
                #  https://www.youtube.com/embed/zsB1c4n5FPg?enablejsapi=1&origin=https://yourdomain.com&showinfo=0&iv_load_policy=3&modestbranding=1&theme=light&color=white&rel=0
    except:
        return link
