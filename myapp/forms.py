from django import forms


class UserFormFields(forms.Form):
    BooleanField = forms.BooleanField()
    NullBooleanField = forms.NullBooleanField()
    CharField = forms.CharField(min_length=2, max_length=20)
    IntegerField = forms.IntegerField(min_value=1, max_value=100)
    DecimalField = forms.DecimalField(min_value=3, max_value=200, decimal_places=2)
    FloatField = forms.FloatField()
    EmailField = forms.EmailField()
    GenericIPAddressField = forms.GenericIPAddressField()
    URLField = forms.URLField()
    FileField = forms.FileField()
    ImageField = forms.ImageField()
    DateField = forms.DateField()
    TimeField = forms.TimeField()
    DateTimeField = forms.DateTimeField()
    DurationField = forms.DurationField()
    ChoiceField = forms.ChoiceField(choices=((1, "Python"), (2, "C++"), (3, "C#")))
    MultipleChoiceField = forms.MultipleChoiceField(choices=((1, "Python"), (2, "C++"), (3, "C#")))


class UserFormData(forms.Form):
    lastname = forms.CharField(min_length=3, max_length=35, label="Фамилия")
    firstname = forms.CharField(min_length=3, max_length=35, label="Имя")
    patronymic = forms.CharField(min_length=3, max_length=35, label="Отчество")
    age = forms.IntegerField(min_value=1, max_value=100, label="Возраст")
    student_group = forms.ChoiceField(choices=((-1, "--Выберите номер своей группы--"), ("У-220", "У-220"),
                                               ("У-221", "У-221"), ("У-222", "У-222"), ("У-223", "У-223"), ("У-224", "У-224"),
                                               ("У-225", "У-225"), ("У-226", "У-226")),
                                    label="Номер группы")
    date_of_birth = forms.DateField(label="Дата рождения")
    programming_language = forms.MultipleChoiceField(choices=(("Python", "Python"), ("C++", "C++"), ("C#", "C#"),
                                                              ("Java", "Java"), ("GOLang", "GOLang")), label="Языки программирования")
    email = forms.EmailField(label="Адрес электронной почты")
