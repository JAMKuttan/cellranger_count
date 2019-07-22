#!/usr/bin/env python3

import pytest
import pandas as pd
from io import StringIO
import os

test_output_path = os.path.dirname(os.path.abspath(__file__)) + \
                    '/../output/'


@pytest.mark.count211
def test_count211_count():
    assert os.path.exists(os.path.join(test_output_path, 'count211', 'sample1_metrics_summary.tsv'))
    assert os.path.exists(os.path.join(test_output_path, 'count211', 'sample1', 'outs'))

@pytest.mark.count302
def test_count302_count():
    assert os.path.exists(os.path.join(test_output_path, 'count302', 'sample1_metrics_summary.tsv'))
    assert os.path.exists(os.path.join(test_output_path, 'count302', 'sample1', 'outs'))
