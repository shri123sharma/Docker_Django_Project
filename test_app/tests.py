import os, sys
import shutil
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.db import models
from django.core.exceptions import ValidationError
from django_todo.settings import BASE_DIR
from .models import Employee


def clean_uploaded_files():
    folder = os.path.join(BASE_DIR,'files/employees')
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)

class TestEmployeeModel(TestCase):
    def setUp(self):
        clean_uploaded_files()
        self.first_name = "Alex"
        self.last_name = "English"
        self.picture_filename = "newplot.png"
        self.cv_filename = "Consumer_Report_consent_1.pdf"
        self.picture_path = os.path.join(BASE_DIR,'test_app/files/employees/alex-english/newplot.png')
        self.cv_path = os.path.join(BASE_DIR ,'test_app/files/employees/alex-english/Consumer_Report_consent_1.pdf')
        
        self.uploaded_picture = SimpleUploadedFile(
            name=self.picture_filename,
            content=open(self.picture_path, "rb").read(),
            content_type="image/png",
        )
        self.uploaded_cv = SimpleUploadedFile(
            name=self.cv_filename,
            content=open(self.cv_path, "rb").read(),
            content_type="application/pdf",
        )

    def tearDown(self):
        clean_uploaded_files()
        pass

    def test_create_without_first_name(self):
        with self.assertRaises(ValidationError):
            employee = Employee(last_name=self.last_name, picture=self.uploaded_picture, cv=self.uploaded_cv)
            employee.save()
    

    def test_create_without_last_name(self):
        with self.assertRaises(ValidationError):
            employee = Employee(first_name=self.first_name, picture=self.uploaded_picture, cv=self.uploaded_cv)
            employee.save()
    

    def test_create_without_picture(self):
        with self.assertRaises(ValidationError):
            employee = Employee(first_name=self.first_name, last_name=self.last_name, cv=self.uploaded_cv)
            employee.save()
            # employee.full_clean()

    def test_create_without_cv(self):
        with self.assertRaises(ValidationError):
            employee = Employee(first_name=self.first_name, last_name=self.last_name, picture=self.uploaded_picture)
            employee.save()

    def test_create_valid_employee_basic_fields(self):
        employee = Employee(
            first_name=self.first_name,
            last_name=self.last_name,
            picture=self.uploaded_picture,
            cv=self.uploaded_cv,
        )
        employee.save()
        
        self.assertIsInstance(employee._meta.get_field('first_name'),models.CharField)
        self.assertIsInstance(employee._meta.get_field('last_name'),models.CharField)

        self.assertEqual(employee.first_name, self.first_name)
        self.assertEqual(employee.last_name, self.last_name)
        
    def test_slug_field(self):
        employee=Employee(
            first_name=self.first_name,
            last_name=self.last_name,
            picture=self.uploaded_picture,
            cv=self.uploaded_cv,
        )
        employee.save()
        self.assertIsInstance(employee._meta.get_field('slug'),models.SlugField)
        
        expected_slug='{}-{}'.format(self.first_name.lower(),self.last_name.lower())
        self.assertEqual(employee.slug,expected_slug)

    

    def test_picture_field(self):
        employee = Employee(
        first_name=self.first_name,
        last_name=self.last_name,
        picture=self.uploaded_picture,
        cv=self.uploaded_cv
        )
        employee.save()
        self.assertIsInstance (employee._meta.get_field('picture'), models.ImageField)
        expected_picture_path='files/employees/{}-{}/{}'.format(
        self.first_name. lower (), self.last_name. lower(), self.picture_filename) 
        self.failUnless (open (employee.picture.path), 'Picture does not exist')
        
        self.assertEqual(
            os.path.normpath (employee.picture.path), os.path.normpath (os.path.join(BASE_DIR, expected_picture_path)))
        
    def test_cv_field(self):
        employee=Employee(
            first_name=self.first_name,
            last_name=self.last_name,
            picture=self.uploaded_picture,
            cv=self.uploaded_cv
        )
        employee.save()
        
        self.assertIsInstance(employee._meta.get_field('cv'),models.FileField)
        expected_picture_path='files/employees/{}-{}/{}'.format(
        self.first_name. lower (), self.last_name. lower(), self.cv_filename)
        self.failUnless (open (employee.cv.path), 'cv does not exist')
        self.assertEqual(
            os.path.normpath(employee.cv.path), os.path.normpath (os.path.join(BASE_DIR, expected_picture_path)))
        
