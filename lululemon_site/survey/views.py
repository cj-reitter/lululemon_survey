from django.shortcuts import render
from django.http import JsonResponse
from .models import SurveyResponse
import json

def survey(request):
    if request.method == 'GET':
        return render(request, 'survey.html')
    
    elif request.method == 'POST':
            try:
                data = json.loads(request.body)

                def clean_text(value):
                    if isinstance(value, str):
                        value = value.strip()
                    return value or None

                age_raw = clean_text(data.get('age'))
                age = int(age_raw) if age_raw else None

                gender = clean_text(data.get('gender'))

                sec1_q4 = data.get('sec1_q4', [])
                if isinstance(sec1_q4, str):
                    sec1_q4 = [sec1_q4]
                elif not isinstance(sec1_q4, list):
                    sec1_q4 = []

                survey_response = SurveyResponse(
                    age=age,
                    gender=gender,
                    sec1_q1=clean_text(data.get('sec1_q1')),
                    sec1_q2=clean_text(data.get('sec1_q2')),
                    sec1_q3=clean_text(data.get('sec1_q3')),
                    sec1_q4=sec1_q4,
                    sec2_q1=clean_text(data.get('sec2_q1')),
                    sec2_q2=clean_text(data.get('sec2_q2')),
                    sec2_q3=clean_text(data.get('sec2_q3')),
                    sec2_q4=clean_text(data.get('sec2_q4')),
                    sec2_q5=clean_text(data.get('sec2_q5')),
                    sec2_q6=clean_text(data.get('sec2_q6')),
                    sec2_q7=clean_text(data.get('sec2_q7')),
                    sec3_q1=clean_text(data.get('sec3_q1')),
                    sec3_q2=clean_text(data.get('sec3_q2')),
                    sec3_q3=clean_text(data.get('sec3_q3')),
                    sec4_q1=clean_text(data.get('sec4_q1')),
                    sec4_q2=clean_text(data.get('sec4_q2'))
                )
                survey_response.save()
                
                return JsonResponse({
                    'success': True,
                    'message': 'Survey response saved successfully.',
                })
            
            except json.JSONDecodeError:
                return JsonResponse({
                    'success': False,
                    'error': 'Invalid JSON data.'
                }, status=400)
            except ValueError:
                return JsonResponse({
                    'success': False,
                    'error': 'Invalid data format.'
                }, status=400)
            except Exception as e:
                return JsonResponse({
                    'success': False,
                    'error': str(e)
                }, status=500)