#!/usr/bin/env python3
# encoding: utf8

import os
import sys

from exasol_python_test_framework import udf
from abstract_python_scalar_emit_consume_emit_very_large import AbstractScalarEmitConsumeEmitVeryLargePythonPerformanceTest


class ScalarEmitConsumeEmitVeryLargePython2PerformanceTest(AbstractScalarEmitConsumeEmitVeryLargePythonPerformanceTest):

    def setUp(self):
        self.setup_test("PYTHON")

    def tearDown(self):
        self.cleanup(self.schema)

    def test_consume_next(self):
        self.execute_consume_next()


if __name__ == '__main__':
    udf.main()
