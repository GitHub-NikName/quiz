import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import QuestionSerializer, QuestionsNum
from questions.models import Question


URL = 'https://jservice.io/api/random?count='


def get_questions_from_api(num: int) -> list:
    res = requests.get(URL + str(num))
    if res.status_code != 200:
        raise requests.RequestException
    return res.json()


@api_view(['POST'])
def get_question(request):
    last_question = Question.objects.last()
    last_question_serializer = QuestionSerializer(last_question)

    num_serializer = QuestionsNum(data=request.data)
    num_serializer.is_valid(raise_exception=True)
    num = num_serializer.validated_data['questions_num']

    questions = []
    while len(questions) != num:
        data = get_questions_from_api(num - len(questions))
        q_ids = [i['id'] for i in data]
        dub_qs = Question.objects.filter(question_id__in=q_ids).values_list(
            'question_id', flat=True)
        questions += [el for el in data if int(el['id']) not in dub_qs]

    serializer = QuestionSerializer(data=questions, many=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(last_question_serializer.data)
