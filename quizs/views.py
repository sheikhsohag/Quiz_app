from django.shortcuts import render,redirect
from .models import Question
from .forms import Make_Questions,Choice_Ques_type
from django.core.paginator import Paginator
from accounts.models import UserProfile,User_details
from .globals import lst
from django.utils.text import slugify
from Category.models import Category
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required


# Create your views here.


def create_quiz(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            if request.method == 'POST':
                form = Make_Questions(request.POST)
                if form.is_valid():
                    question = form.cleaned_data['question']
                    option1 = form.cleaned_data['option1']
                    option2 = form.cleaned_data['option2']
                    option3 = form.cleaned_data['option3']
                    option4= form.cleaned_data['option4']
                    answer = form.cleaned_data['answer']
                    category = form.cleaned_data['category']
                    question_slug = slugify(question)
                    ques = Question(question=question, option1=option1, option2=option2, option3=option3, option4=option4, answer=answer, author=request.user,category=category,question_slug=question_slug)
                    ques.save()
                    print(ques)
                    return redirect('home')
            form = Make_Questions() 
            return render(request, 'create_quiz.html', {'form':form})
        return redirect('home')
    return redirect('Login')


def choose_question(request):
    if request.user.is_authenticated:
        form = Choice_Ques_type()
        return render(request, 'choose.html', {'form':form})
    
    
@login_required
def show_quiz(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = Choice_Ques_type(request.POST)  
            if form.is_valid():
                cat = form.cleaned_data['category']
                num = int(form.cleaned_data['choice'])
                quizs = Question.objects.filter(category=cat)
                # print(quizs)
                quizs = quizs[ : num]  
                for q in quizs:
                    lst.append(q.id)
                response = render(request, 'quiz.html', {'questions': quizs})
                response.set_cookie('quesions', quizs)  
                return response
            return redirect('choose_question')

    return redirect('choose_question')

    

def result(request):
    if request.method == 'POST':
        question = Question.objects.filter(pk__in=lst)
        qus_num = len(lst)
        score=0
        wrg=0
        
        
        for q in question:
            quix = request.POST.get(q.question)
            if q.answer == quix:
                score+=1
            else:
                wrg+=1
                
        # user_details = None
        print(score, "  ", wrg)
         
        try:
            user_details = User_details.objects.get(username=request.user)
             
        except User_details.DoesNotExist:
            user_details = User_details(username=request.user)
        
        if qus_num:  
            current_accuracy = (score/qus_num)*100
        else:
            current_accuracy=0
            
        user_details.number_prob_solve += qus_num
        user_details.accurate += score
        user_details.wrong += wrg
        
        if user_details.number_prob_solve:
            user_details.accuracy = (user_details.accurate/user_details.number_prob_solve)*100
        else:
            user_details.accuracy=0
        print(user_details.accurate," ", user_details.number_prob_solve)
            
        user_details.save()
        
        context = {
            
            'cur_num_ques':qus_num,
            'cur_score':score,
            'cur_wrong':wrg,
            'cur_accuracy':current_accuracy,
            'total_problem': user_details.number_prob_solve,
            'total_score':user_details.accurate,
            'total_wrong':user_details.wrong,
            'total_accuracy': user_details.accuracy,
        }   
        lst.clear()       
        return render(request, 'showresult.html', context )
    else:
        return redirect('home')

def ratting(request):
    None
