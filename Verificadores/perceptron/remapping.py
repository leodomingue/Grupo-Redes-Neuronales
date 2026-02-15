import numpy as np

def test_01_radius(perceptron):
  radius_test = np.sqrt(np.abs(perceptron.bias / perceptron.weights[0]))
  try:
    assert 4.0 <= radius_test <= 4.2, "Los pesos o bias estan mal"
    return True
  except AssertionError as e:
    print(f"Test radius: {e}")

def test_02_calculated_radius(radius):
  try:
    assert 4.0 <= radius <= 4.2, f"El perceptron se entreno correctamente, pero la formula para encontrar el radio esta mal. tenes {radius} pero debería estar entre 4.0 y 4.2"
    return True
  except AssertionError as e:
    print(f"Test formula radio: {e}")

def test_03_class(perceptron):

  points_inside = np.array([
    [0, 0],      
    [1, 1],      
    [2, 0],      
    [0, 2],      
    [-1, -1],    
    [2, 2],      
  ])
  distances_inside = np.linalg.norm(points_inside, axis=1)

  points_outside = np.array([
    [5, 0],     
    [0, 5],      
    [-5, 0],     
    [0, -5],     
    [4, 4],      
    [3, 4],      
  ])

  distances_outside = np.linalg.norm(points_outside, axis=1)

  points_inside_transformed = (points_inside[:, 0]**2 + points_inside[:, 1]**2).reshape(-1, 1)
  points_outside_transformed = (points_outside[:, 0]**2 + points_outside[:, 1]**2).reshape(-1, 1)

  try:
    predictions_inside = perceptron.predict(points_inside_transformed)
    predictions_outside = perceptron.predict(points_outside_transformed)
    

    correct_inside = np.sum(predictions_inside == 1)  
    correct_outside = np.sum(predictions_outside == -1)  
    
    total_correct = correct_inside + correct_outside
    total_points = len(points_inside) + len(points_outside)
    accuracy_test = total_correct / total_points

    if accuracy_test == 1.0:
      return True
    else:
      print(f"Accuracy insuficiente: {accuracy_test * 100:.2f}%")
      raise AssertionError("Accuracy en puntos de prueba muy baja")

  except Exception as e:
    print(f"Error al predecir - {e}")
    raise


def run_all_test_radius(perceptron, radius):
  print("EJECUTANDO TODOS LOS TESTS")
  results = []
  results.append(test_01_radius(perceptron))
  results.append(test_02_calculated_radius(radius))
  results.append(test_03_class(perceptron))
  all_passed = all(res is True for res in results)
  if all_passed:
    print("Pasaron todos los tests")
    return True
  else:
    print("No pasaron todos los tests")
    return False
