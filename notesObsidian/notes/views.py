from django.shortcuts import render
from .models import Note
from .forms import NoteForm, UserRegistrationForm
from django.shortcuts import get_object_or_404 , redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login


# Create your views here.
def index(request):
    return render(request, 'index.html')

def note_list(request):
    notes = Note.objects.all().order_by('-created_at')
    return render(request, 'note_list.html', {'notes': notes})

@login_required
def note_create(request):
    print("notes_create")
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'note_form.html', {'form': form})

@login_required
def note_edit(request, note_id):
    note = get_object_or_404(Note,pk=note_id, user = request.user)
    print("notes_edit")
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES, instance=note)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('note_list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'note_form.html', {'form': form})

@login_required
def note_delete(request, note_id):
    note = get_object_or_404(Note, pk=note_id, user=request.user)
    print("notes_delete")
    if request.method == 'POST':
        note.delete()
        return redirect('note_list')
    return render(request, 'note_confirm_delete.html', {'note': note})


def register(request):
    print("register")
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('note_list')
    else:
        form = UserRegistrationForm()

    return render(request, 'registration/register.html', {'form': form})

