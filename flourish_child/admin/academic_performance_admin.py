from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple
from ..admin_site import flourish_child_admin
from ..forms import AcademicPerformanceForm
from ..models import AcademicPerformance
from .model_admin_mixins import ChildCrfModelAdminMixin


@admin.register(AcademicPerformance, site=flourish_child_admin)
class AcademicPerformanceAdmin(ChildCrfModelAdminMixin, admin.ModelAdmin):
    form = AcademicPerformanceForm

    fieldsets = (
        (None, {
            'fields': (
                'education_level',
                'education_level_other',
                'mathematics_marks',
                'reading_marks',
                'history_marks',
                'num_days')}
         ), audit_fieldset_tuple)

    radio_fields = {
        'education_level': admin.VERTICAL,
        'mathematics_marks': admin.VERTICAL,
        'reading_marks': admin.VERTICAL,
        'history_marks': admin.VERTICAL,
        'num_days': admin.VERTICAL, }
