#!/usr/bin/env python3
# encoding: utf8


from exasol_python_test_framework import udf
from abstract_performance_test import AbstractPerformanceTest


class ScalarEmitConsumeTupleOnlyPythonPerformanceTest(AbstractPerformanceTest):

    def setUp(self):
        self.create_schema()
        self.generate_data_linear(500)
        self.query(udf.fixindent('''
                CREATE PYTHON SCALAR SCRIPT CONSUME_TUPLE(
                    intVal DECIMAL(9,0), 
                    longVal DECIMAL(18,0), 
                    bigdecimalVal DECIMAL(36,0), 
                    decimalVal DECIMAL(9,2),
                    doubleVal DOUBLE, 
                    doubleIntVal DOUBLE, 
                    stringVal VARCHAR(100), 
                    booleanVal BOOLEAN, 
                    dateVal DATE, 
                    timestampVal TIMESTAMP) EMITS (count_value INT) AS
                def run(ctx):
                    pass
                '''))
        self.query("commit")
    
    def tearDown(self):
        self.cleanup(self.schema)

    def test_consume_next(self):
        self.run_test(15, 3, 2.0, "SELECT CONSUME_TUPLE(intVal,longVal,bigdecimalVal,decimalVal,doubleVal,doubleIntVal,"
                                  "stringVal,booleanVal,dateVal,timestampVal) FROM T")


if __name__ == '__main__':
    udf.main()
