import numpy as np

def test_02_verify_train(perceptron_lower, perceptron_upper, is_within_bounds):
  try:
    assert hasattr(perceptron_lower, 'weights'), "perceptron_lower no tiene 'weights'"
    assert hasattr(perceptron_upper, 'weights'), "perceptron_upper no tiene 'weights'"
    assert perceptron_lower.weights is not None, "perceptron_lower no está entrenado"
    assert perceptron_upper.weights is not None, "perceptron_upper no está entrenado"
    return True
  except AssertionError as e:
    print(f"Error: {e}")
    raise

def test_03_verify_is_within_bounds(perceptron_lower, perceptron_upper, is_within_bounds):
  x_vals_in = np.array([-5, -2, 0, 2, 5])
  points_on_line = np.column_stack([x_vals_in, 2 * x_vals_in + 1])
  points_slightly_above = np.column_stack([x_vals_in, 2 * x_vals_in + 1 + 0.05])
  points_slightly_below = np.column_stack([x_vals_in, 2 * x_vals_in + 1 - 0.05])
  points_inside_band = np.vstack([points_on_line, points_slightly_above, points_slightly_below])

  try:
    predictions_inside = is_within_bounds(points_inside_band, perceptron_lower, perceptron_upper)
    correct_inside = np.sum(predictions_inside == 1)
    total_inside = len(points_inside_band)
    accuracy_inside = correct_inside / total_inside

    if accuracy_inside == 1.00:
      return True
    else:
      print(f"Accuracy insuficiente para punto dentro del limite: {accuracy_inside * 100:.2f}%")
      return False

  except Exception as e:
    print(f"Error: {e}")
    raise


def test_04_verify_is_outside_bounds(perceptron_lower, perceptron_upper, is_within_bounds):
  x_vals_in = np.array([-5, -2, 0, 2, 5])

  points_far_above = np.column_stack([x_vals_in, 2 * x_vals_in + 1 + 1.0])
  points_far_below = np.column_stack([x_vals_in, 2 * x_vals_in + 1 - 1.0])
  points_medium_above = np.column_stack([x_vals_in, 2 * x_vals_in + 1 + 0.3])
  points_medium_below = np.column_stack([x_vals_in, 2 * x_vals_in + 1 - 0.3])
  points_outside_band = np.vstack([points_far_above, points_far_below, points_medium_above, points_medium_below])

  try:
    predictions_outside = is_within_bounds(points_outside_band, perceptron_lower, perceptron_upper)
    correct_outside = np.sum(predictions_outside == -1)
    total_outside = len(points_outside_band)
    accuracy_outside = correct_outside / total_outside

    if accuracy_outside == 1.00:
      return True
    else:
      print(f"Accuracy insuficiente para puntos fuera del limite: {accuracy_outside * 100:.2f}%")
      return False

  except Exception as e:
    print(f"Error: {e}")
    raise


def run_all_test_within_bounds(perceptron_lower, perceptron_upper, is_within_bounds):
  print("EJECUTANDO TODOS LOS TESTS")
  results = []
  results.append(test_02_verify_train(perceptron_lower, perceptron_upper, is_within_bounds))
  results.append(test_03_verify_is_within_bounds(perceptron_lower, perceptron_upper, is_within_bounds))
  results.append(test_04_verify_is_outside_bounds(perceptron_lower, perceptron_upper, is_within_bounds))
  all_passed = all(res is True for res in results)
  if all_passed:
    print("Todos los tests pasaron correctamente")
    return True
  else:
    print("No pasaron todos los tests")
    return False
