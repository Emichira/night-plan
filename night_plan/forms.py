# from django import forms
# from django.core.validators import RegexValidator

# class ContactForm(forms.Form):
#     fullname = forms.CharField(label="",
#         widget=forms.TextInput(
#             attrs={
#                 "class": "form-control s-form-v3__input", "placeholder": "* Your full name"
#                 }
#             )
#         )
#     email = forms.EmailField(label="",
#         widget=forms.EmailInput(
#             attrs={
#                 "class": "form-control s-form-v3__input", "placeholder": "* Email"
#                 }
#             )
#         )
#     phone = forms.CharField(label="",
#         widget=forms.TextInput(
#             attrs={
#                 "class": "form-control s-form-v3__input", "placeholder": "* Phone Number"
#                 }
#             )
#         )
#     message =forms.CharField(label="",
#         widget=forms.Textarea(
#             attrs={
#                 "class": "form-control s-form-v3__input", "placeholder": "* Your message"
#                 }
#             )
#         )

#     def clean_email(self):
#         email = self.cleaned_data.get("email")
#         if not "gmail.com" in email:
#             raise forms.ValidationError("Email has to be gmail.com")
#         return email


# class LoginForm(forms.Form):
#     username = forms.CharField(label="",
#         widget=forms.TextInput(
#             attrs={
#                 "class": "form-control s-form-v3__input", "placeholder": "* Your username"
#                 }
#             )
#         )
#     password = forms.CharField(label="",
#         widget=forms.PasswordInput(
#             attrs={
#                 "class": "form-control s-form-v3__input", "placeholder": "* Your password"
#                 }
#             )
#         )

# CHOICES = [('Male'), ('Female'), ('Prefer not to say')]

# class RegisterForm(forms.Form):
#     firstname = forms.CharField(label="",
#         widget=forms.TextInput(
#             attrs={
#                 "class": "form-control s-form-v3__input", "placeholder": "* Your username"
#                 }
#             )
#         )

#     lastname = forms.CharField(label="",
#         widget=forms.TextInput(
#             attrs={
#                 "class": "form-control s-form-v3__input", "placeholder": "* Your username"
#                 }
#             )
#         )

#     email = forms.EmailField(label="",
#         widget=forms.EmailInput(
#             attrs={
#                 "class": "form-control s-form-v3__input", "placeholder": "* Email"
#                 }
#             )
#         )

#     confirm_email = forms.EmailField(label="",
#         widget=forms.EmailInput(
#             attrs={
#                 "class": "form-control s-form-v3__input", "placeholder": "* Email"
#                 }
#             )
#         )

#     dob = forms.DateField(label="",
#         widget=forms.DateInput(
#             attrs={
#                 "class": "form-control s-form-v3__input", "placeholder": "* Email"
#                 }
#             )
#         )

#     Options = [('1', 'Male'), ('2', 'Female'), ('3', 'Prefer not to say')]
#     gender = forms.ChoiceField(label="",
#         widget=forms.Select(
#             attrs={
#                 "class": "btn register-button g-margin-t-30--xs input-with-icon-wrapper mdb-select md-btn colorful-select dropdown-danger form-control s-form-v3__input", "placeholder": "* Gender"
#                 }
#             )
#         )

#     phone = forms.CharField(label="",
#         widget=forms.TextInput(
#             attrs={
#                 "class": "form-control s-form-v3__input", "placeholder": "* Phone Number"
#                 }
#             )
#         )
#     Options = (
#             ('1', 'Nairobi'),
#             ('2', 'Nakuru'),
#         )
#     town = forms.ChoiceField(label="",
#         widget=forms.Select(
#             attrs={
#                 "class": "btn register-button g-margin-t-30--xs input-with-icon-wrapper mdb-select md-btn colorful-select dropdown-danger form-control s-form-v3__input", "placeholder": "* Select your town"
#                 }
#             )
#         )

#     password = forms.CharField(label="",
#         widget=forms.PasswordInput(
#             attrs={
#                 "class": "form-control s-form-v3__input", "placeholder": "* Your password"
#                 }
#             )
#         )

#     confirm_password = forms.CharField(label="",
#         widget=forms.PasswordInput(
#             attrs={
#                 "class": "form-control s-form-v3__input", "placeholder": "* Your password"
#                 }
#             )
#         )

