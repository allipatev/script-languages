#!/usr/bin/env python3

from exasol_python_test_framework import udf
from exasol_python_test_framework.exatest.testcase import useData
from exasol_python_test_framework.udf.available_python_packages_utils import run_python_package_import_test



class AvailablePython3Packages(udf.TestCase):
    def setUp(self): 
        self.query('create schema available_packages', ignore_errors=True) 

    data = [
            ("from google.cloud import asset",),
            ("from google.cloud import bigquery",),
            ("from google.cloud import bigquery_storage",),
            ("from google.cloud import bigtable",),
            ("from google.cloud.devtools import containeranalysis_v1",),
            ("from google.cloud import datacatalog",),
            ("from google.cloud import datastore",),
            ("from google.cloud import firestore",),
            ("from google.cloud import kms",),
            ("from google.cloud import logging",),
            ("from google.cloud import monitoring",),
#            ("from google.cloud import ndb",), # fails at input
            ("from google.cloud import pubsub",),
            ("from google.cloud import spanner",),
            ("from google.cloud import storage",),
            ("from google.cloud import trace",),
        ]

    @useData(data)
    def test_package_import(self, pkg, fail=False, alternative=None):
        run_python_package_import_test(self, pkg, "PYTHON3", fail, alternative)


if __name__ == '__main__':
    udf.main()
