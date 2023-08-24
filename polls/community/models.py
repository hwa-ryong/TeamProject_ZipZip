from django.contrib.auth.models import User

from django.db import models

class Free_Board(models.Model):
    b_title = models.CharField(max_length=100)
    b_content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    b_regdate = models.DateTimeField()
    b_modifydate = models.DateTimeField(null=True, blank=True)
    b_hit = models.IntegerField(default=0)
    b_recommend = models.IntegerField(default=0)

    def __str__(self):
        return str(self.b_title)

class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # 글쓴이
    content = models.TextField()  # 답변내용
    create_date = models.DateTimeField()  # 등록일
    board_type = models.CharField(max_length=10)  # 게시판 타입 (예: 'free', 'review')
    board_id = models.PositiveIntegerField()  # 게시판 아이디 (Free_Board 또는 Review_Board의 pk)

    def __str__(self):
        return self.content