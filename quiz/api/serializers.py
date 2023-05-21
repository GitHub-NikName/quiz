from rest_framework import serializers
from rest_framework.validators import UniqueValidator


from questions.models import Question


class QuestionsNum(serializers.Serializer):
    questions_num = serializers.IntegerField()


class QuestionSerializer(serializers.ModelSerializer):
    question_id = serializers.IntegerField(read_only=True)
    id = serializers.IntegerField(
        source='question_id',
        write_only=True,
        validators=[UniqueValidator(queryset=Question.objects.all())]
    )

    def create(self, validated_data):
        return Question.objects.create(**validated_data)

    class Meta:
        model = Question
        fields = '__all__'
