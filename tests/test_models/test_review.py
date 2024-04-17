#!/usr/bin/python3
""" """

from datetime import datetime
from models import review
import inspect
import models
import pep8
import unittest
from models.base_model import BaseModel
Review = review.Review


class TestReviewDocs(unittest.TestCase):
    """Tests class"""
    @classmethod
    def setUpClass(cls):
        """unit test for review"""
        cls.review_f = inspect.getmembers(Review, inspect.isfunction)

    def test_01_pep8_conformance_review(self):
        """unit test for review"""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_02_pep8_conformance_test_review(self):
        """unit test for review"""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_03_review_module_docstring(self):
        """unit test for review"""
        self.assertIsNot(review.__doc__, None,
                         "review.py needs a docstring")
        self.assertTrue(len(review.__doc__) >= 1,
                        "review.py needs a docstring")

    def test_04_review_func_docstrings(self):
        """unit test for review"""
        for func in self.review_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))

    def test_05_place_id_attr(self):
        """unit test for review"""
        review = Review()
        self.assertTrue(hasattr(review, "place_id"))
        if models.storage_t == 'db':
            self.assertEqual(review.place_id, None)
        else:
            self.assertEqual(review.place_id, "")

    def test_06_user_id_attr(self):
        """unit test for review"""
        review = Review()
        self.assertTrue(hasattr(review, "user_id"))
        if models.storage_t == 'db':
            self.assertEqual(review.user_id, None)
        else:
            self.assertEqual(review.user_id, "")

    def test_07_text_attr(self):
        """unit test for review"""
        review = Review()
        self.assertTrue(hasattr(review, "text"))
        if models.storage_t == 'db':
            self.assertEqual(review.text, None)
        else:
            self.assertEqual(review.text, "")

    def test_08_to_dict_values(self):
        """unit test for review"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        r = Review()
        new_d = r.to_dict()
        self.assertEqual(new_d["__class__"], "Review")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], r.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], r.updated_at.strftime(t_format))

    def test_09_str(self):
        """unit test for review"""
        review = Review()
        string = "[Review] ({}) {}".format(review.id, review.__dict__)
