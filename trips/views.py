from django import forms
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.forms import ModelForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, FormView

from trips.models import City


class CityList(ListView):
    model = City


class CityCreate(CreateView):
    model = City
    fields = ['location']
    success_url = reverse_lazy('crud:city_cbv_list')


class CityUpdate(UpdateView):
    model = City
    fields = ['location']
    success_url = reverse_lazy('crud:city_cbv_list')


class CityDelete(DeleteView):
    model = City
    success_url = reverse_lazy('crud:city_cbv_list')


class CityView(DetailView):
    model = City


class CityModify(UpdateView):
    class Validate(ModelForm):
        pk = None
        location = forms.CharField()

        class Meta:
            model = City
            fields = ['location']

        def clean(self):
            error_list = []
            data = super(CityModify.Validate, self).clean()
            location = data.get("location")

            if not len(location) > 2:
                error_list += ['city location name is too short,  must be more than 2 characters in length']

            if len(City.objects.filter(~Q(id=self.pk), location=location)) > 0:
                error_list += ['database has this record already']

            if len(error_list) > 0:
                raise ValidationError(error_list)

            return data

    model = City
    template_name = 'trips/city_modify.html'
    form_class = Validate
    success_url = reverse_lazy('crud:city_cbv_list')

    def get(self, request, *args, **kwargs):
        city = get_object_or_404(self.model, pk=self.kwargs['pk'])
        form = self.form_class(instance=city)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        self.form_class.pk = kwargs['pk']
        city = self.model.objects.get(id=kwargs['pk'])
        form = self.form_class(request.POST)

        if form.is_valid():
            city.location = form.data.get('location')
            city.save()
            return HttpResponseRedirect(self.success_url)

        return render(request, self.template_name, {'form': form})


class CityQuery(FormView):
    class Task(ModelForm):
        location = forms.CharField()

        class Meta:
            model = City
            fields = ['location']

    model = City
    template_name = 'trips/city_query.html'
    form_class = Task

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        object_list = self.model.objects.filter(location=form.data.get('location'))
        return render(request, self.template_name, {'form': form, 'object_list': object_list})


class CityFirst(ListView):
    model = City
    template_name = 'trips/city_first.html'
    queryset = model.objects.first()


def city_list(request):
    cities = City.objects.all()
    return render(request, 'trips/city_list.html', {
        'object_list': cities,
    })


def city_create(request):
    class CityForm(ModelForm):
        class Meta:
            model = City
            fields = ['location']

    form = CityForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('crud:city_fbv_list')
    return render(request, 'trips/city_form.html', {'form': form})


def city_update(request, pk):
    class CityForm(ModelForm):
        class Meta:
            model = City
            fields = ['location']

    city = get_object_or_404(City, pk=pk)
    form = CityForm(request.POST or None, instance=city)

    if form.is_valid():
        form.save()
        return redirect('crud:city_fbv_list')
    return render(request, 'trips/city_form.html', {'form': form})


def city_delete(request, pk):
    city = get_object_or_404(City, pk=pk)
    if request.method == 'POST':
        city.delete()
        return redirect('crud:city_fbv_list')
    return render(request, 'trips/city_confirm_delete.html', {'object': city})


def city_view(request, pk):
    city = City.objects.get(pk=pk)
    return render(request, 'trips/city_detail.html', {'object': city})


def city_modify(request, pk):
    class Validate(ModelForm):
        pk = None
        location = forms.CharField()

        class Meta:
            model = City
            fields = ['location']

        def clean(self):
            error_list = []
            data = super(Validate, self).clean()
            location = data.get("location")

            if not len(location) > 2:
                error_list += ['city location name is too short,  must be more than 2 characters in length']

            if len(City.objects.filter(~Q(id=self.pk), location=location)) > 0:
                error_list += ['database has this record already']

            if len(error_list) > 0:
                raise ValidationError(error_list)

            return data

    city = get_object_or_404(City, pk=pk)
    form = Validate(request.POST or None, instance=city)
    form.pk = pk

    if form.is_valid():
        form.save()
        return redirect('crud:city_fbv_list')
    return render(request, 'trips/city_modify.html', {'form': form})


def city_query(request):
    class Task(ModelForm):
        location = forms.CharField()

        class Meta:
            model = City
            fields = ['location']

    form = Task(request.POST or None)

    if form.is_valid():
        object_list = City.objects.filter(location=form.data.get('location'))
        return render(request, 'trips/city_query.html', {'form': form, 'object_list': object_list})

    return render(request, 'trips/city_query.html', {'form': form})


def city_first(request):
    object_list = City.objects.first()
    return render(request, 'trips/city_first.html', {'object_list': object_list})
