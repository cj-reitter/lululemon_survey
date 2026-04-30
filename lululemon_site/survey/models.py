from django.db import models

class SurveyResponse(models.Model):
    
    age = models.IntegerField(null=True, blank=True)
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('non-binary', 'Non-binary'),
        ('prefer-not-to-say', 'Prefer not to say'),
        ('other', 'Other'),
    ]
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, null=True, blank=True)
    
    
    sec1_q1 = models.CharField(max_length=30, null=True, blank=True)
    sec1_q2 = models.CharField(max_length=10, null=True, blank=True)
    sec1_q3 = models.CharField(max_length=20, null=True, blank=True)
    sec1_q4 = models.JSONField(default=list, blank=True)

    sec2_q1 = models.CharField(max_length=20, null=True, blank=True)
    sec2_q2 = models.CharField(max_length=20, null=True, blank=True)
    sec2_q3 = models.TextField(null=True, blank=True)
    sec2_q4 = models.CharField(max_length=20, null=True, blank=True)
    sec2_q5 = models.CharField(max_length=20, null=True, blank=True)
    sec2_q6 = models.CharField(max_length=20, null=True, blank=True)
    sec2_q7 = models.CharField(max_length=20, null=True, blank=True)

    sec3_q1 = models.CharField(max_length=20, null=True, blank=True)
    sec3_q2 = models.TextField(null=True, blank=True)
    sec3_q3 = models.CharField(max_length=20, null=True, blank=True)

    sec4_q1 = models.TextField(null=True, blank=True)
    sec4_q2 = models.TextField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Survey Response'
        verbose_name_plural = 'Survey Responses'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Survey Response - {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"