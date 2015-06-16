# -*- coding: utf-8 -*-
"""
.. module:: djstripe.forms
   :synopsis: dj-stripe Forms.

.. moduleauthor:: Daniel Greenfeld (@pydanny)

"""

from django import forms

from .settings import PLAN_CHOICES


class PlanForm(forms.Form):
    plan = forms.ChoiceField(choices=PLAN_CHOICES)
    coupon = forms.CharField(max_length=30, required=False)


class CancelSubscriptionForm(forms.Form):
    pass
