from django import forms
from main.models import Package,Activity,Hotel,Desination


class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = '__all__'


        labels = {
            'cover_image': 'Select Package cover Image',
            'name': 'Select Hotel',
            'description': 'A brief summary of the package',
            'start_date': 'Start Date',
            'end_date': 'End Date',
            'activities': 'Select Activities (Hold Ctrl to select multiple activities)',
            'cruiser_price': 'Land Cruiser Price',
            'van_price': 'Van Price',
            'addons': 'Select Addons (Hold ctrl to select multiple addons)',
        }



        widgets = {
            'start_date': forms.DateInput(attrs={'class': 'form-control','type':'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control','type':'date'}),
            'activities': forms.SelectMultiple(attrs={'class': 'form-select'}),
            'cruiser_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'van_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'addons': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }





class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = '__all__'


        labels = {
            'activity_name': 'Activity name',
            'activity_desc': 'Activity description',
            
        }



        widgets = {
            
            'activity_name': forms.TextInput(attrs={'class': 'form-control'}),
            'activity_desc': forms.Textarea(attrs={'class': 'form-control'}),
        }



class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = '__all__'


        labels = {
            'hotel_image': 'Select Hotel cover Image',
            'name': 'Hotel Name',
            'dest_id': 'Select Destination where the hotel is located',
            'desc': 'Brief description of the hotel',
            
        }



        widgets = {
            
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'dest_id': forms.Select(attrs={'class': 'form-select'}),
            'desc': forms.Textarea(attrs={'class': 'form-control'}),
        }


class DestinationForm(forms.ModelForm):
    class Meta:
        model = Desination
        fields = '__all__'


        labels = {
            'des_name': 'Destination Name',
            'des_image': 'Select destination Image',
            'desc': 'Destination brief description',
            
            
        }



        widgets = {
            
            'des_name': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.Textarea(attrs={'class': 'form-control'}),
        }