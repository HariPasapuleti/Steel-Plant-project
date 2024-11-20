from django.shortcuts import render, redirect, get_object_or_404
from .forms import MachineForm
from .models import Machine
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

@login_required
def machine_add(request):
    # print("working")
    if request.method == 'POST':
        form = MachineForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('machine_list')
    else:
        form = MachineForm()
    return render(request, 'machine/add_machine.html', {'form': form})

@login_required
def machine_list(request):
    machines = Machine.objects.all()

    if request.method == 'POST':
        # Get the machine object by its ID
        machine_id = request.POST.get('machine_id')
        machine = Machine.objects.get(id=machine_id)

        # Get the complaint text from the form submission
        complaint_text = request.POST.get('complaints')

        # Append the new complaint with indexing
        if complaint_text:
            if machine.complaints:
                # Count existing complaints by splitting on newlines
                existing_complaints = machine.complaints.split("\n")
                index = len(existing_complaints) + 1
                machine.complaints += f"\n{index}. {complaint_text}"
            else:
                # First complaint, start with index 1
                machine.complaints = f"1. {complaint_text}"
            machine.save()

        return redirect('machine_list')  # Redirect after successful submission

    return render(request, 'machine/machine_list.html', {'machines': machines})
