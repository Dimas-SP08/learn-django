from django import forms

class FormField(forms.Form):

    # numeric datatype
    integer_f = forms.IntegerField(required=False)
    decimal_f = forms.DecimalField(required=False)
    float_f = forms.FloatField(required=False)

    #type data string
    char_f = forms.CharField(required=False)
    char_field = forms.CharField(required=False)
    email_field = forms.EmailField()
    slug_field = forms.SlugField()
    regex_field = forms.RegexField(regex=r'(P?<input>)')
    url_field = forms.URLField()
    ipaddress_field = forms.GenericIPAddressField()
    # select input type
    PILIHAN = (
        ('piilhan','Pilihan'),
        ('piilhan1','Pilihan1'),
        ('piilhan2','Pilihan2'),
    )
    choice_field = forms.ChoiceField(choices=PILIHAN)
    multy_choice_field = forms.MultipleChoiceField(choices=PILIHAN)
    typed_choice_field = forms.TypedChoiceField(choices=PILIHAN)
    multy_typed_choice = forms.TypedMultipleChoiceField(choices=PILIHAN)
    null_boolean_field = forms.NullBooleanField()
    # date time type
    date_field = forms.DateField()
    datetime_field = forms.DateTimeField()
    durasi_field = forms.DurationField()
    time_field = forms.TimeField()
    splitdatetime_field = forms.SplitDateTimeField()
    # fiel input type
    file_field = forms.FileField()
    image_field = forms.ImageField()
    # other fields
    boolean_field = forms.BooleanField()
    uuid_field = forms.UUIDField()
    json_field = forms.JSONField()
    file_path_field = forms.FilePathField(path='kontak/', allow_files=True, allow_folders=True)