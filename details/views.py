from details.forms import EditProfileForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm


def view_details(request):
    args = {'user': request.user}
    return render(request, 'details.html', args)


def edit_details(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/details')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'edit_details.html', args)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            return redirect('/details')
        else:
            return redirect('/details')
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'change_password.html', args)
