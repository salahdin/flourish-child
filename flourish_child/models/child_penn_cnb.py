from django.db import models
from edc_base.model_fields.custom_fields import OtherCharField
from edc_base.model_validators.date import date_not_future
from edc_base.utils import get_utcnow
from edc_constants.choices import YES_NO
from edc_protocol.validators import date_not_before_study_start

from .child_crf_model_mixin import ChildCrfModelMixin
from .list_models import StaffMember
from ..choices import REASONS_PENNCNB_INCOMPLETE, PENNCNB_INVALID, YES_NO_NOT_ASKED


class ChildPennCNB(ChildCrfModelMixin):

    date_deployed = models.DateField(
        verbose_name='Date PennCNB deployed',
        validators=[
            date_not_before_study_start,
            date_not_future],
        default=get_utcnow)

    start_time = models.TimeField(
        verbose_name='Start time of PennCNB')

    stop_time = models.TimeField(
        verbose_name='Stop time of PennCNB')

    staff_assisting = models.ManyToManyField(
        StaffMember,
        verbose_name='Staff member who helped deploy test and monitored')

    completed = models.CharField(
        verbose_name='Was the PennCNB successfully completed?',
        choices=YES_NO,
        max_length=3)

    reason_incomplete = models.CharField(
        verbose_name='If no, please provide reasons',
        choices=REASONS_PENNCNB_INCOMPLETE,
        max_length=50,
        null=True,
        blank=True)

    reason_other = OtherCharField()

    testing_impacted = models.CharField(
        verbose_name='Did any of the following impact the testing session',
        choices=PENNCNB_INVALID,
        max_length=30,
        null=True,
        blank=True)

    impact_other = OtherCharField()

    claim_experience = models.CharField(
        verbose_name='Does the child claim to have experience using a computer?',
        choices=YES_NO_NOT_ASKED,
        max_length=30)

    comments = models.TextField(
        verbose_name=('Please provide any additional comments you would like to add '
                      'about this PennCNB test'),
        max_length=500,
        null=True,
        blank=True)

    class Meta(ChildCrfModelMixin.Meta):
        app_label = 'flourish_child'
        verbose_name = 'Child PennCNB'
        verbose_name_plural = 'Child PennCNB'
