# -*- coding: utf-8 -*-
"""
Landing page view
"""
from django.views.generic import TemplateView


class LandingView(TemplateView):
    """
    This view renders the propper dashboard
    """
    template_name = "landing.html"
