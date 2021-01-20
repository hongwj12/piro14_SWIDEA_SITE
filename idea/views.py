from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView,  CreateView, UpdateView
from .models import Idea
from .forms import IdeaForm


# Create your views here.
idea_list = ListView.as_view(model=Idea)
idea_detail = DetailView.as_view(model=Idea)
idea_new = CreateView.as_view(model=Idea, form_class=IdeaForm)
idea_edit = UpdateView.as_view(model=Idea, form_class=IdeaForm)

def idea_delete(request, pk):
    '''
    delete == DELETE
    DB에 저장된 객체를 불러와 삭제하는 뷰
    '''
    idea = get_object_or_404(Idea, pk=pk)

    # 유저가 주소창에에 delete의 url를 직접 쳐서 들어오는 경우를 고려하여 GET처리를 해준다
    if request.method == "GET":
        return redirect('idea:idea_detail', pk)
    elif request.method == "POST":
        idea.delete()
        return redirect('idea:idea_list')
    # GET과 POST의 순서는 이런식으로 바뀌어도 상관없습니다.
    # 단, 사용자가 GET과 POST방식으로만 접근한다는 보장은 없으므로, 이외의 method를 사용 시 오류가 날 수 있습니다.
