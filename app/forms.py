from django import forms

#class classroom(forms.Form):
#    class_name = forms.CharField(max_length = 30)
#    class_price = forms.DecimalField(default = 0.00, decimal_places = 2, max_digits = 10)




class StudentForm(forms.Form):
    student_name = forms.CharField(max_length = 30)
    days_attended = forms.IntegerField()
    days_absent = forms.IntegerField()
    current_credit = forms.DecimalField(decimal_places = 2, max_digits = 10)
    student_class = forms.CharField(max_length = 50)

#student_class = forms.ForeignKey(classroom, on_delete = models.CASCADE)
