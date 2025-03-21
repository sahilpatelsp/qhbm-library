# Copyright 2021 The QHBM Library Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Tests for the circuit_model module."""

import cirq
import sympy
import tensorflow as tf
import tensorflow_quantum as tfq

from qhbmlib import circuit_model_utils


def _pystr(x):
  return [str(y) for y in x]


class BitCircuitTest(tf.test.TestCase):
  """Tests the bit_circuit function."""

  def test_bit_circuit(self):
    """Confirms correct bit injector circuit creation."""
    my_qubits = [
        cirq.GridQubit(0, 2),
        cirq.GridQubit(1, 4),
        cirq.GridQubit(2, 2)
    ]
    identifier = "build_bit_test"
    test_circuit = circuit_model_utils.bit_circuit(my_qubits, identifier)
    test_symbols = list(sorted(tfq.util.get_circuit_symbols(test_circuit)))
    expected_symbols = list(
        sympy.symbols(
            "build_bit_test_bit_0 build_bit_test_bit_1 build_bit_test_bit_2"))
    expected_circuit = cirq.Circuit(
        [cirq.X(q)**s for q, s in zip(my_qubits, expected_symbols)])
    self.assertAllEqual(_pystr(test_symbols), _pystr(expected_symbols))
    self.assertEqual(test_circuit, expected_circuit)
